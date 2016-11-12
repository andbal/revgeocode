#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
NAME:           rev_geocode
AUTHOR(s):      Andrea Balotti - balotti.and@gmail.com
DATE:           10 Nov 2016
DESCRIPTION:    Given a CSV with pair of coordinates (decimal long/lat), return
                a file with coordinates and address of the points using reverse
                geocode from GEOPY library.
NOTE:           1) install GEOPY with PIP if not installed
                2) input CSV have NO header and contains coordinates pair in
                   long/lat format (in this order, separated with comma and
                   one pair for line)
GEOCODER LIST:  GoogleV3
                Nominatim
                Bing

COPYRIGHT (c) 2016 - ANDREA BALOTTI
"""

import os, csv
from geopy.geocoders import GoogleV3

# path to file
file_in="/home/andrea/src/github/revgeocode/input_coord/random_pnt.csv"
file_out=os.path.join(os.path.dirname(file_in),"out_address.csv")

# declare variables
geolocator = GoogleV3()
out = []

# open output file for writing
with open(file_out,"w") as fo:
    writer = csv.writer(fo, delimiter=',')
    writer.writerow(['long','lat','address'])
    
    # read input file and reverse geocoding
    with open(file_in,"r") as fi:
        reader = csv.reader(fi, delimiter=',')
        for line in reader:
            ### Coordinates string MUST be long/lat, and NOT lat/long !!!
            location = geolocator.reverse(line,exactly_one=True)
            out = [line[0],line[1],location.address] # out as: long,lat,address
            
            # write result in output file
            writer.writerow(out)
        print("Processing complete!")
