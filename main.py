from config import API_KEY, API_SECRET
from mexc_sdk import Spot

spot = Spot(api_key=API_KEY, api_secret=API_SECRET)

print(spot.ping())
print(spot.time())
<<<<<<< HEAD
print("Goodbye")
=======
print('Hello')
>>>>>>> 15af0aca44a38cf3d28525d448a82e007eee8e38
