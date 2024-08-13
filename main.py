from  config import API_KEY, API_SECRET
from mexc_sdk import Spot

spot = Spot(api_key=API_KEY, api_secret=API_SECRET)

print(spot.ping())
print(spot.time())
print('Hello')
