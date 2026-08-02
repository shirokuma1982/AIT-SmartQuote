class QuoteBuilder:
    """
    CSVの請求項目を見積単位へ整理するクラス
    """

    OCEAN_FREIGHT = "2000"

    SIZE_LCL = "C01"
    SIZE_20 = "C02"
    SIZE_40 = "C03"
    SIZE_40HC = "C04"

    UNIT_BL = "14"

    def build(self, rows):

        quote = {
            "20FT": [],
            "40FT": [],
            "40HC": [],
            "LCL": [],
            "BL": []
        }

        for row in rows:

            charge_cd = row.get("請求項目CD", "")
            unit_cd = row.get("請求項目単位CD", "")
            charge_unit = row.get("Charge単位CD1", "")

            # Ocean Freight
            if charge_cd == self.OCEAN_FREIGHT:

                if unit_cd == self.SIZE_20:
                    quote["20FT"].append(row)

                elif unit_cd == self.SIZE_40:
                    quote["40FT"].append(row)

                elif unit_cd == self.SIZE_40HC:
                    quote["40HC"].append(row)

                elif unit_cd == self.SIZE_LCL:
                    quote["LCL"].append(row)

            # BL単位
            elif charge_unit == self.UNIT_BL:

                quote["BL"].append(row)

        return quote