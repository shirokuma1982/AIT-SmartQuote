class QuoteCalculator:
    """見積金額計算"""

    def calculate(self, rows, exchange_rate=160):

        total_jpy = 0
        total_usd = 0

        for row in rows:

            currency = row.get("請求項目通貨CD", "")
            price = row.get("請求項目単価", "")

            try:
                price = float(price)
            except:
                price = 0

            if currency == "JPY":
                total_jpy += price

            elif currency == "USD":
                total_usd += price

        grand_total = total_jpy + (total_usd * exchange_rate)

        return {
            "jpy": total_jpy,
            "usd": total_usd,
            "exchange_rate": exchange_rate,
            "grand_total": grand_total
        }