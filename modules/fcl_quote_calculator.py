class FCLQuoteCalculator:
    """
    OceanQuote AI
    Version 0.4.0
    """

    SIZE_20 = "C02"
    SIZE_40 = "C03"
    SIZE_40HC = "C04"

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

    def calculate(self, rows, exchange_rate=160):

        result = {
            "20FT": {"usd": 0, "jpy": 0},
            "40FT": {"usd": 0, "jpy": 0}
        }

        for row in rows:

            unit = row.get("請求項目単位CD", "")

            if unit == self.SIZE_20:
                target = "20FT"

            elif unit in [self.SIZE_40, self.SIZE_40HC]:
                target = "40FT"

            else:
                continue

            # Ocean Freight
            currency = row.get("請求項目通貨CD", "")

            price = self._to_float(
                row.get("請求項目単価")
            )

            if currency == "USD":
                result[target]["usd"] += price
            else:
                result[target]["jpy"] += price

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
                    result[target]["usd"] += price

                else:
                    result[target]["jpy"] += price

        for size in result:

            result[size]["total"] = (
                result[size]["jpy"]
                + result[size]["usd"] * exchange_rate
            )

        return result