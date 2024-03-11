import math

def distance_between_structures(structure1, structure2):
    xdist = structure2[0] - structure1[0]
    zdist = structure2[1] - structure1[0]
    d = math.sqrt((xdist * xdist) + (zdist*zdist))
    return d

def distance_from_00(c1):
    d = math.sqrt((c1[0] * c1[0]) + (c1[1] * c1[1]))