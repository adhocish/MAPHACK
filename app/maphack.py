from app import app
from flask import jsonify, request

import json
import urllib2

GMAPS_API_ARG = "json?"
GMAPS_API_SEP = "&"
GMAPS_API_KEY = "AIzaSyCs0TSnD82gNm4EMg0GfVL2MU8Pag9_fFg"
GMAPS_API_ENDPOINT = "https://maps.googleapis.com/maps/api/directions/"
GMAPS_API_FIELDS = [
    "origin",
    "destination",
    # "key",
    # "mode",
    # "waypoints",
    # "alternatives",
    # "avoid",
    # "language",
    # "units",
    # "region",
    # "departure_time",
    # "arrival_time",
    # "transit_mode",
    # "transit_route_preferences"
]

def get_maps_url(args):
    # base URL
    url = GMAPS_API_ENDPOINT + GMAPS_API_ARG

    # append Maps parameters
    for field in GMAPS_API_FIELDS:
        url += field + "=" + args[field] + GMAPS_API_SEP

    # append API key
    url += "key=" + GMAPS_API_KEY

    return url

@app.route("/maphack/api/", methods=["POST"])
def directions():
    # Retrieve form data
    try:
        params = {}
        # Iterate over accepted fields
        for field in GMAPS_API_FIELDS:
            params[field] = request.form[field]
    except Exception as e:
        print e
        return jsonify({'result':'400'}) # bad request

    # Generate Maps API URL with input parameters
    requestURL = get_maps_url(params)

    # Visit Maps API URL and read response
    response = urllib2.urlopen(requestURL).read()

    # TODO: parse Google Maps json response

    return response