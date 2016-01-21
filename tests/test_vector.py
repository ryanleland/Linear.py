from vector import Vector


def test_float_magnitude():
    v = Vector(-0.221, 7.437)
    assert v.magnitude() == 7.440282924728065

    v = Vector(8.813, -1.331, -6.247)
    assert v.magnitude() == 10.884187567292289

def test_int_dot():
    v1 = Vector(1, 2, -1)
    v2 = Vector(3, 1, 0)

    assert v1.dot(v2) == 5

def test_float_dot():
    v1 = Vector(7.887, 4.138)
    v2 = Vector(-8.802, 6.776)

    assert v1.dot(v2) == -41.382286

    v1 = Vector(-5.955, -4.904, -1.874)
    v2 = Vector(-4.496, -8.755, 7.103)

    assert v1.dot(v2) == 56.397178000000004
