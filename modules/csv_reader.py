import csv
import os


class CSVReader:
    """見積マスタ(CSV)を読み込むクラス"""

    def __init__(self):
        # プロジェクトルートを取得
        base_dir = os.path.dirname(os.path.dirname(__file__))

        # CSVファイルのパス
        self.csv_path = os.path.join(base_dir, "data", "rate_master.csv")

    def load_data(self):
        """CSVを読み込み、リスト形式で返す"""

        data = []

        with open(self.csv_path, mode="r", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            for row in reader:
                data.append(row)

        return data