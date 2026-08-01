"""
OceanQuote AI
データ辞書

CSVの列名を一元管理する。
CSVのレイアウトが変更された場合は、このファイルのみ修正する。
"""

# ==========================================
# 基本情報
# ==========================================

SHIPPER = "荷主名"
BILL_TO = "請求先正式名"

POL = "発地名"
POD = "着地名"

CARRIER = "Carrier名"
ROUTE = "Route名"

TRANSPORT = "運送形態名"

START_DATE = "契約期間開始日"
END_DATE = "契約期間終了日"

REMARK = "備考"


# ==========================================
# Charge
# ==========================================

CHARGE_NAME_PREFIX = "Charge名"
CHARGE_RATE_PREFIX = "Charge単価"
CHARGE_UNIT_PREFIX = "Charge単位名"
CHARGE_CURRENCY_PREFIX = "Charge通貨単位名"