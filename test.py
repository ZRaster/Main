import pptk
import json
import numpy as np

with open('kyiv_counted_points.geojson','r+') as fd:
    data = json.load(fd)


#Collect the polygon coordinates into a list of numpy arrays.
Vs = [np.array(F['geometry']['coordinates'][0]) for F in data['features']]

Hs = [np.array(F['properties']['NUMPOINTS']) for F in data['features']]

Ws = np.hstack(([Vs],[Hs]))

print(Ws)

#Collect the NUMPOINTS into a list of numpy arrays.
#Hs = [np.array(H['properties']['NUMPOINTS']) for H in data['features']]
#print(Hs)

#Convert the points into UTM coordinates (District of Columbia’s UTM zone is 18)
#Ws = [np.c_[V[:, 0].tolist(), V[:, 1].tolist()] for V in Vs]

#transform numpoints into vertical list
#HsV = np.vstack(Hs)

#Copy and paste the following function that converts a polygon into a point set.
