from asteroidhunter import __version__
import unittest, requests, json, os, pytest
from dotenv import load_dotenv
load_dotenv()
from asteroidhunter.nearest_misses import nearest_misses

def test_version():
  assert __version__ == '0.1.0'

@pytest.mark.vcr()
def test_nearest_misses():
  asteroids_json = nearest_misses(50)
  asteroids = json.loads(asteroids_json)
  d0 = asteroids[0]['miss_distance']['miles']
  d1 = asteroids[1]['miss_distance']['miles']
  d2 = asteroids[2]['miss_distance']['miles']
  d3 = asteroids[3]['miss_distance']['miles']
  d4 = asteroids[4]['miss_distance']['miles']
  d5 = asteroids[5]['miss_distance']['miles']
  d5 = asteroids[5]['miss_distance']['miles']
  d6 = asteroids[6]['miss_distance']['miles']
  d7 = asteroids[7]['miss_distance']['miles']
  d8 = asteroids[8]['miss_distance']['miles']
  d9 = asteroids[9]['miss_distance']['miles']

  assert len(asteroids) == 10
  assert d0 < d1
  assert d1 < d2
  assert d2 < d3
  assert d3 < d4
  assert d4 < d5
  assert d5 < d6
  assert d6 < d7
  assert d7 < d8
  assert d8 < d9

  for i in range (0, 10):
    assert asteroids[i]['close_approach_date']
    assert asteroids[i]['close_approach_date_full']
    assert asteroids[i]['epoch_date_close_approach']
    assert asteroids[i]['miss_distance']
    assert asteroids[i]['orbiting_body']
    assert asteroids[i]
    assert type(asteroids[i]) is dict