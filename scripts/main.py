# script/main.py
import click
import sys
from pathlib import Path
from fetch_btc_data.providers_gmo import BTCProvider

@click.command(
    context_settings=dict(help_option_names=['-h', '--help']),
    help = """
    GMOコインから約定データを取得し、15分足OHLCVを表示します。
    例: python main.py 20250401
    """,
)
@click.argument("yyyymmdd", type=int, metavar = "<yyyymmdd>", required = True)
@click.argument("interval", type = int, metavar = "<interval>")
@click.argument("save_path", type = str, metavar = "<save_path>")

def main(
    yyyymmdd: int,
    interval : int,
    save_path : str):
    # 例: 2025年4月1日のデータを取得
    btc_provider = BTCProvider(interval=interval, save_path=save_path)

    btc_provider.fetch_ohlcv(yyyymmdd)
    print("Download and processing complete.")


if __name__ == "__main__":
    main()