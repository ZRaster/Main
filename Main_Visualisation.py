import pptk
import json
import numpy as np

with open('kyiv_counted_points.geojson','r+') as fd:
    data = json.load(fd)

# Collect the polygon coordinates into a list of numpy arrays.
Vs = [np.array(F['geometry']['coordinates'][0]) for F in data['features']]
Hs = [np.array(F['properties']['NUMPOINTS']) for F in data['features']]

#Ws = [np.c_[V[:, 0].tolist(), V[:, 1].tolist()] for V in Vs] - not needed?

#Copy and paste the following function that converts a polygon into a point set.
def sample_polygon(V, H, eps=0.25):
    # samples polygon V s.t. consecutive samples are no greater than eps apart
    # assumes last vertex in V is a duplicate of the first
    M = np.ceil(np.sqrt(np.sum(np.diff(V, axis=0) ** 2, axis = 1)) / eps)
    Q = []
    for (m, v1, v2) in zip(M, V[: -1], V[1:]):
        Q.append(np.vstack([ \
            np.linspace(v1[0], v2[0], m, endpoint = False), \
            np.linspace(v1[1], v2[1], m, endpoint = False),
            np.linspace(H, H, m, endpoint=False)]
        ).T)
    Q = np.vstack(Q)
    return Q

P = np.vstack([sample_polygon(V, H * 3) for V, H in zip(Vs, Hs)])

# P = np.c_[P, np.zeros(len(P))]

P -= np.mean(P, axis=0)[None, :]

v = pptk.viewer(P)
v.attributes(P[:, 2])
v.set(point_size=0.1)
