import json
from .apiService import *


def asteroid_closest_approach(limiter = None):
  asteroids= []
  response = browseApi()
  total_pages = response['page']['total_pages']
  total_pages_to_iterate = limiter if limiter and total_pages > limiter else total_pages
  #loop through all pages
  results = get_all_pages_data(total_pages_to_iterate, asteroids)
  return json.dumps(results) 


def get_all_pages_data(total_pages, asteroids):
  for pageNumber in range(0, total_pages):
    response = browseApi(pageNumber)
    asteroids = get_closest_approached_asteroids(response, asteroids)
  return asteroids


def get_closest_approached_asteroids(data, asteroids):
  for asteroid in data['near_earth_objects']:
    if asteroid['close_approach_data']:
    # sort by closest miss distance
      asteroid['close_approach_data'] = min(asteroid['close_approach_data'], key=lambda data: data['miss_distance']['miles'])
      asteroids.append(asteroid['close_approach_data'])
  return asteroids

