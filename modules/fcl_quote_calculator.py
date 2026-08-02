class FCLQuoteCalculator:
    """
    AIT SmartQuote
    Version 0.4.1
    """

    def _to_float(self, value):

        if value is None:
            return 0

        value = str(value).replace(",", "").strip()

        if value == "":
            return 0

        try:
            return float(value)
        except:
            return 0

    def _add_row(self, result, row, exchange_rate):

        currency = row.get("請求項目通貨CD", "")

        price = self._to_float(
            row.get("請求項目単価")
        )

        if currency == "USD":
            result["usd"] += price
        else:
            result["jpy"] += price

        # Charge1～20
        for i in range(1, 21):

            currency = row.get(
                f"Charge通貨単位CD{i}",
                ""
            )

            price = self._to_float(
                row.get(f"Charge単価{i}")
            )

            if currency == "USD":
                result["usd"] += price
            else:
                result["jpy"] += price

    def calculate(
        self,
        quote,
        exchange_rate=160
    ):

        result = {
            "20FT": {
                "usd": 0,
                "jpy": 0
            },
            "40FT": {
                "usd": 0,
                "jpy": 0
            }
        }

        # 20FT
        for row in quote["20FT"]:
            self._add_row(
                result["20FT"],
                row,
                exchange_rate
            )

        # 40FT
        for row in quote["40FT"]:
            self._add_row(
                result["40FT"],
                row,
                exchange_rate
            )

        # 40HCは40FTへ加算
        for row in quote["40HC"]:
            self._add_row(
                result["40FT"],
                row,
                exchange_rate
            )

        # BL料金を両方へ加算
        for row in quote["BL"]:

            self._add_row(
                result["20FT"],
                row,
                exchange_rate
            )

            self._add_row(
                result["40FT"],
                row,
                exchange_rate
            )

        for size in result:

            result[size]["total"] = (
                result[size]["jpy"]
                + result[size]["usd"] * exchange_rate
            )

        return result