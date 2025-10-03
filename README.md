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

uv pip install -e .が上手くいかない時の対処法 : 
uv run -p 3.13 python -m pip install -e .
明示的にpipの元となるpythonのバージョンを指定する