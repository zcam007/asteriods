from asteroidhunter import __version__
import unittest, requests, json, os, pytest
from dotenv import load_dotenv
load_dotenv()
from asteroidhunter.asteroid_closest_approach import asteroid_closest_approach


def test_version():
  assert __version__ == '0.1.0'

@pytest.mark.vcr()
def test_asteroid_closest_approach():
  asteroid_json = asteroid_closest_approach(25)
  asteroids = json.loads(asteroid_json)
  for i in range(0, len(asteroids)-1):
    assert asteroids[i]['close_approach_date']
    assert asteroids[i]['close_approach_date_full']
    assert asteroids[i]['epoch_date_close_approach']
    assert asteroids[i]['miss_distance']
    assert asteroids[i]['orbiting_body']
    assert asteroids[i]
    assert type(asteroids[i]) is dict