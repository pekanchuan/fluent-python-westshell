from collections import namedtuple

Coordinate = namedtuple('Coordinate', 'lat lon')
moscow = Coordinate(55.765, 37.617)

print(moscow)
