import json
from .asteroid_closest_approach import asteroid_closest_approach

def nearest_misses(limiter = None):
  asteroids = json.loads(asteroid_closest_approach(limiter))
  sorted_by_distance = sorted(asteroids, key=lambda data: data['miss_distance']['miles'])
  # returning top 10 nearest misses
  return json.dumps(sorted_by_distance[0:10])