import json, os, requests

def browseApi(PAGE_NUMBER = 0):
  api_key = os.getenv('API_KEY')
  url = f'https://api.nasa.gov/neo/rest/v1/neo/browse?api_key={api_key}&page={PAGE_NUMBER}'
  return requests.get(url).json()


def feedApi(start_date, end_date):
  api_key = os.getenv('API_KEY')
  url = f'https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={api_key}'
  return requests.get(url).json()