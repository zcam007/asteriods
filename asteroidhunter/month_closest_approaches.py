import calendar, json
import math
from .apiService import *

def month_closest_approaches(date):
  num_days = get_num_days_in_month(date)
  num_intervals = math.ceil(num_days/7)
  intervals = get_intervals(date, num_days, num_intervals)
  results = get_closest_approaches_by_week(date, intervals)
  return json.dumps(results)

def get_closest_approaches_by_week(date, intervals):
  results = {'month': date,'near_earth_objects':{},'asteroid_count': 0}
  for interval in intervals:
    response = feedApi(interval[0], interval[1])
    results['asteroid_count'] += response['element_count']
    for k,v in response['near_earth_objects'].items():
      results['near_earth_objects'][k] = v
  return results 

def get_intervals(date, num_days, num_intervals):
  intervals = []
  for x in range(0, num_intervals):
    start = x * 7 + 1
    end = start + 6 
    # if end is greater than num_days, set end to num_days
    if end > num_days: end = num_days
    start_interval = f'{date}-{str(start).zfill(2)}'
    end_interval = f'{date}-{str(end).zfill(2)}'
    intervals.append([start_interval, end_interval])
  return intervals

def get_num_days_in_month(date):
  datesplit = date.split('-')
  return calendar.monthrange(int(datesplit[0]), int(datesplit[1]))[1]