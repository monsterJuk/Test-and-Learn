from config import API_KEY, SECRET_KEY
import requests
import time, datetime
import json
import hmac
import hashlib
from pprint import pprint

BASE_URL = 'https://contract.mexc.com/'


def _get_server_time():
    return int(time.time()*1000)


def _sign_v1(sign_params=None):
    if sign_params:
        sign = "%s%s%s" % (API_KEY, _get_server_time(), sign_params)
    else:
        sign = "%s%s" % (API_KEY, _get_server_time())
    sign = hmac.new(SECRET_KEY.encode('utf-8'), sign.encode('utf-8'),
                      hashlib.sha256).hexdigest()
    return sign


def get_history_positions(page_num: int, page_size=None, symbol=None) -> list:
    """get history positions"""
    method = 'GET'
    path = '/api/v1/private/position/list/history_positions'
    url = '{}{}'.format(BASE_URL, path)
    data_original = {
        'page_num': page_num
    }
    if page_size:
        data_original = {"page_size": page_size}
    if symbol:
        data_original = {"symbol": symbol}
    data = '&'.join('{}={}'.format(i, data_original[i]) for i in sorted(data_original))
    sign = _sign_v1(sign_params=data)
    headers = {
        "ApiKey": API_KEY,
        "Request-Time": str(_get_server_time()),
        "Signature": sign,
        "Content-Type": "application/json"
    }
    url = "%s%s%s" % (url, "?", data)
    response = requests.request(method, url, headers=headers).json()

    if response.get('success'):
        return response.get('data')
    else:
        return []


def get_today_positions() -> list:
    currentdate = datetime.datetime.today()
    timestamp_start_day = int(currentdate.replace(hour=0, minute=0, second=0, microsecond=0).timestamp()) * 1000

    all_positions = get_history_positions(page_num=1, page_size=500)
    daily_positions = []

    for position in all_positions:
        if position['updateTime'] >= timestamp_start_day:
            daily_positions.append(position)
        elif position['createTime'] >= timestamp_start_day:
            daily_positions.append(position)

    pprint(len(daily_positions))
    return daily_positions


def count_daily_pnl(daily_positions: list) -> float:
    total_pnl = 0

    for position in daily_positions:
        total_pnl += position['realised']

    return total_pnl


total_pnl = count_daily_pnl(get_today_positions())

print(total_pnl)
pprint(get_today_positions())
