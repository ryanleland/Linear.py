from vector import Vector


def test_magnitude():
    v = Vector(-0.221, 7.437)
    assert v.magnitude() == 7.440282924728065

    v = Vector(8.813, -1.331, -6.247)
    assert v.magnitude() == 10.884187567292289

def test_dot():
    v1 = Vector(1, 2, -1)
    v2 = Vector(3, 1, 0)

    assert v1.dot(v2) == 5
