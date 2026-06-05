from janitor.janitor import calculate_cost


def test_calculate_cost_basic():
    volumes = [{"Size": 8}, {"Size": 10}]
    assert calculate_cost(volumes) == round((8 + 10) * 0.08, 2)
