#! /usr/bin/python
import json
import re

class Directions:

  def __init__(self, leg):
    self.__leg = leg

  def formatter(self, field, is_text=True):
    if is_text:
      return self.__leg[field]['text']
    else:
      return self.__leg[field]['value']

  def distance(self):
    return self.formatter('distance')

  def duration(self):
    return self.formatter('duration')

  def format_step(self,s):
    steps = s['html_instructions'] + " for " + s['distance']['text']
    p = re.compile(r'<.*?>')
    return p.sub('', steps)

  def steps(self):
    return map(self.format_step, self.__leg['steps'])


f = open('maps.json','r')
parsed_json = json.load(f)

result = None
if parsed_json['status'] == 'OK':
  trip = parsed_json['routes'][0]['legs'][0] ## first leg of first route
  d = Directions(trip)
  result = d.steps()
else:
  if 'error_message' in parsed_json:
    print parsed_json['error_message']

print result

