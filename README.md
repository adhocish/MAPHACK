# MAPHACK

## What is it?

MapHack is a mobile application that will provide directions from point A to point B using only a phone connection; it does not require **any** access to data/WiFi or pre-downloaded offline maps! MapHack was developed by @[adhocish](https://github.com/adhocish), @[alvinzxu](https://github.com/alvinzxu), and @[YiboDuan](https://github.com/YiboDuan) during the 2015 Genesys Hackathon in Toronto and took first place.

## Demo

Here's a quick [demo](https://www.youtube.com/watch?v=oG2ck1j_Jkk) of the iOS application with WiFi and data turned off.

## How it works

MapHack encodes your inputted source/destination information into DTFM (dual-tone multi-frequency) signals, which are then sent through a phone call to a [Genesys Cloud IVR](http://www.genesys.com/angel/inbound-ivr) (Interactive Voice Response) system. The Cloud IVR system decodes the signal into its original text and hits the MapHack web endpoint with a POST request containing the query data. The MapHack server then uses the Google Maps API to perform the query and returns the step-by-step route information to the Cloud IVR system. The route is then split into separate text messages sent straight to your phone as well as spoken through the ongoing phone call.

MapHack was built using the following technologies:

* Apple iOS
* Genesys Cloud IVR
* Flask web microframework
* DigitalOcean hosting
* Google Maps API
