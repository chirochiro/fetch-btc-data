使い方：
uv sync
uv pip install -e .
uv run scripts/main.py yyyymmdd interval save_path

引数 :
yyyymmdd : 取得したい時点
interval : 価格データの頻度
save_path : 保存先パス

注意 : 
intervalは分足で固定
