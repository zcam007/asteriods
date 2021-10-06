import os
from dotenv import load_dotenv
from asteroidhunter.apiService import *
from asteroidhunter.asteroid_closest_approach import *
from asteroidhunter.nearest_misses import *
from asteroidhunter.month_closest_approaches import *
load_dotenv()
# print(os.getenv('API_KEY'))
# print(browseApi())
# print(asteroid_closest_approach(1))
# print(month_closest_approaches('2016-05'))
print(nearest_misses(3))