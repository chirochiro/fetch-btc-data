import requests
import pandas as pd
import numpy as np
from io import BytesIO
from datetime import datetime, timedelta

def get_ohlcv_15min(yyyymmdd: int) -> pd.DataFrame:
    """
    指定した日付のBTC取引履歴を取得し、15分間隔のOHLCVデータをDataFrameで返す。
    date_str: 'YYYYMMDD' 形式の日付文字列 (例: '20250401')
    """
    # 1. データURLの組み立て（年、月ディレクトリとファイル名）
    base_url = "https://api.coin.z.com/data/trades/BTC_JPY"
    date_str = str(yyyymmdd)               # '20250401'
    year  = date_str[0:4]                 # '2025'
    month = date_str[4:6]                 # '04'

    # 組み立てたURL例: https://api.coin.z.com/data/trades/BTC/2025/4/20250401_BTC.csv.gz
    data_url = f"{base_url}/{year}/{month}/{date_str}_BTC_JPY.csv.gz"
    
    # 2. .gzファイルのダウンロードとメモリ上への読み込み
    response = requests.get(data_url)
    response.raise_for_status()  # HTTPエラーの場合は例外を発生させる
    # ダウンロードしたバイナリデータをBytesIOに載せ、pandasで読み込む（gzip圧縮を自動解凍）
    csv_buffer = BytesIO(response.content)
    df = pd.read_csv(csv_buffer, compression='gzip')
    
    # timestamp列をdatetime型に変換
    df['datetime'] = pd.to_datetime(df['timestamp'])

    
    # 4. 15分間隔（900秒）でデータをグルーピングしてOHLCVを算出
    # datetimeを15分単位に丸め（切り捨て）して interval 列を作成
    df['interval'] = df['datetime'].dt.floor('15min')
    # intervalごとに価格と数量を集計
    grouped = df.groupby('interval')
    ohlcv = pd.DataFrame({
        'Open':   grouped['price'].first(),
        'High':   grouped['price'].max(),
        'Low':    grouped['price'].min(),
        'Close':  grouped['price'].last(),
        'Volume': grouped['size'].sum()
    })
    
    # 5. 結果のデータフレームを返す（インデックスが各15分区間の開始時刻）
    return ohlcv
