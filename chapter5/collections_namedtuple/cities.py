from collections import namedtuple
import json

from coordinates import Coordinate

City = namedtuple('City', ['name', 'country', 'population', 'coordinates'])
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
# print(City._fields)

delhi_data = ('Delhi NCR', 'IN', 21.935, Coordinate(28.613889, 77.208889))

delhi = City._make(delhi_data)


foo = namedtuple('Foo', 'lat lon reference', defaults=['WGS84'])

print(foo(0, 0))
print(foo._field_defaults)
