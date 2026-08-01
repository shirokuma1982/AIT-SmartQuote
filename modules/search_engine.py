from modules.data_dictionary import (
    SHIPPER,
    POL,
    POD,
    CARRIER,
    TRANSPORT
)


class SearchEngine:
    """見積検索エンジン"""

    def search(
        self,
        data,
        shipper="",
        pol="",
        pod="",
        carrier="",
        transport=""
    ):

        results = []

        for row in data:

            if shipper:
                if shipper.lower() not in row[SHIPPER].lower():
                    continue

            if pol:
                if pol.lower() not in row[POL].lower():
                    continue

            if pod:
                if pod.lower() not in row[POD].lower():
                    continue

            if carrier:
                if carrier.lower() not in row[CARRIER].lower():
                    continue

            if transport:
                if transport.lower() not in row[TRANSPORT].lower():
                    continue

            results.append(row)

        return results