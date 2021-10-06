from asteroidhunter import __version__
import unittest, requests, json, os, pytest
from dotenv import load_dotenv
load_dotenv()
from asteroidhunter.apiService import *
import pytest

def test_version():
    assert __version__ == '0.1.0'
    
@pytest.mark.vcr()
def test1():
    key = os.getenv('API_KEY')
    url = f'https://api.nasa.gov/neo/rest/v1/neo/browse?api_key={key}&page=1'
    res = requests.get(url).json()
    keys = list(res)
    assert keys == ['links', 'page', 'near_earth_objects']

@pytest.mark.vcr()
def test_browse_api():
  res = browseApi(1)
  keys = list(res)
  assert keys == ['links', 'page', 'near_earth_objects']

@pytest.mark.vcr()
def test_feed_api():
  start_date = '2018-04-15'
  end_date = '2018-04-22'
  res = feedApi(start_date, end_date)
  keys = list(res)
  assert keys == ['links', 'element_count', 'near_earth_objects']