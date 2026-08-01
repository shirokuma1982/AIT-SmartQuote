from flask import Flask, render_template, request

from modules.csv_reader import CSVReader
from modules.search_engine import SearchEngine
from modules.quote_calculator import QuoteCalculator

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():

    # CSV読込
    reader = CSVReader()
    data = reader.load_data()

    # 検索条件
    shipper = request.args.get("shipper", "").strip()

    # 為替（デフォルト160）
    exchange_rate = float(
        request.args.get("exchange_rate", "160")
    )

    results = []
    quote = None

    if shipper:

        engine = SearchEngine()

        results = engine.search(
            data=data,
            shipper=shipper
        )

        calculator = QuoteCalculator()

        quote = calculator.calculate(
            rows=results,
            exchange_rate=exchange_rate
        )

        print("=" * 60)
        print(f"検索条件：{shipper}")
        print(f"検索結果：{len(results)} 件")
        print(f"JPY合計：{quote['jpy']:,.0f}")
        print(f"USD合計：{quote['usd']:,.2f}")
        print(f"総額：{quote['grand_total']:,.0f}")
        print("=" * 60)

    return render_template(
        "index.html",
        results=results,
        quote=quote,
        exchange_rate=exchange_rate
    )


if __name__ == "__main__":
    app.run(debug=True)