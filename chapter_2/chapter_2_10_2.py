from array import array

octets = array('B', range(6))
m1 = memoryview(octets)
print()