from app import app
from flask import jsonify, request

# import json
import urllib2
from parse import get_steps

GMAPS_API_ARG = "json?"
GMAPS_API_SEP = "&"
GMAPS_API_KEY = "AIzaSyCs0TSnD82gNm4EMg0GfVL2MU8Pag9_fFg"
GMAPS_API_TRANSPORTATION_MODE = "walking"
GMAPS_API_ENDPOINT = "https://maps.googleapis.com/maps/api/directions/"

GMAPS_PARAMETERS = {
    "origin" : "",
    "destination" : "",
    "key" : GMAPS_API_KEY,
    "mode" : GMAPS_API_TRANSPORTATION_MODE,
    # "waypoints" : "",
    # "alternatives" : "",
    # "avoid" : "",
    # "language" : "",
    # "units" : "",
    # "region" : "",
    # "departure_time" : "",
    # "arrival_time" : "",
    # "transit_mode" : "",
    # "transit_route_preferences : """
}

def get_maps_url(args):
    # base URL
    url = GMAPS_API_ENDPOINT + GMAPS_API_ARG

    # append Maps parameters
    for field in GMAPS_PARAMETERS:
        url += field + "=" + args[field] + GMAPS_API_SEP

    return url

@app.route("/maphack/api/", methods=["POST"])
def get_directions():
    # Retrieve form data
    try:
        # Iterate over accepted fields
        for key in GMAPS_PARAMETERS:
            if GMAPS_PARAMETERS[key] == "":
                GMAPS_PARAMETERS[key] = request.form[key]
    except Exception as e:
        print e
        return jsonify({'result':'400'}) # bad request

    # Generate Maps API URL with input parameters
    requestURL = get_maps_url(GMAPS_PARAMETERS)

    # Visit Maps API URL and read response
    response = urllib2.urlopen(requestURL).read()

    # Parse Google Maps json response
    steps = get_steps(response)

    return jsonify({'result':steps})