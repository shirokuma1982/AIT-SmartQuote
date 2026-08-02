from flask import Flask, render_template, request

from modules.csv_reader import CSVReader
from modules.search_engine import SearchEngine
from modules.quote_builder import QuoteBuilder
from modules.fcl_quote_calculator import FCLQuoteCalculator
from modules.data_dictionary import SHIPPER

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():

    # CSV読込
    reader = CSVReader()
    data = reader.load_data()

    # 検索条件
    shipper = request.args.get("shipper", "").strip()

    # 為替
    try:
        exchange_rate = float(request.args.get("exchange_rate", "160"))
        if exchange_rate <= 0:
            raise ValueError
    except (TypeError, ValueError):
        exchange_rate = 160.0

    results = []
    quote = None
    quote_info = None

    if shipper:

        # 検索
        engine = SearchEngine()

        results = engine.search(
            data=data,
            shipper=shipper
        )

        # 見積単位へ整理
        builder = QuoteBuilder()

        grouped_quote = builder.build(results)

        # FCL試算
        calculator = FCLQuoteCalculator()

        quote = calculator.calculate(
            grouped_quote,
            exchange_rate
        )

        if results:
            first_result = results[0]
            quote_info = {
                "shipper": first_result.get(SHIPPER, ""),
                "pol": first_result.get("PlaceofReceiptCD", ""),
                "pod": first_result.get("PlaceofDeliveryCD", ""),
                "carrier": first_result.get("CarrierCD", "")
            }

        print("=" * 60)
        print(f"検索条件：{shipper}")
        print(f"検索件数：{len(results)}")

        print()

        print("20FT")
        print(quote["20FT"])

        print()

        print("40FT")
        print(quote["40FT"])

        print("=" * 60)

    return render_template(
        "index.html",
        results=results,
        quote=quote,
        quote_info=quote_info,
        shipper=shipper,
        exchange_rate=exchange_rate
    )


if __name__ == "__main__":
    app.run(debug=True)
