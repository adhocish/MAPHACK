#! /usr/bin/python
import json
import re

FOR_ACTIONS = [
    "Continue",
    "Head",
]

IN_ACTIONS = [
    "Destination"
]

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
        # Grammar
        sep = " in "
        for action in FOR_ACTIONS:
            if action in s['html_instructions']:
                sep = " for "
        for action in IN_ACTIONS:
            if action in s['html_instructions']:
                sep = " in "

        step = s['html_instructions'] + sep + s['distance']['text']

        # Replace HTML tags
        p = re.compile(r'<div style.*?>')
        step = p.sub('. ', step)
        p = re.compile(r'<.*?>')
        step = p.sub('', step)

        return step
        
    def steps(self):
        return map(self.format_step, self.__leg['steps'])

def get_steps(mapsJson):
    parsed_json = json.loads(mapsJson)
    result = None

    if parsed_json['status'] == 'OK':
        trip = parsed_json['routes'][0]['legs'][0] ## first leg of first route
        d = Directions(trip)
        return d.steps()
    elif parsed_json['status'] == 'ZERO_RESULTS':
        return 'No available routes.'
    elif parsed_json['status'] == 'NOT_FOUND':
        return 'Location not found.'
    elif parsed_json['status'] == "REQUEST_DENIED":
        return parsed_json['error_message']
    else:
        if 'error_message' in parsed_json:
            return parsed_json['error_message']

    return result