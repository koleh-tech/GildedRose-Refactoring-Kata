from copy import deepcopy
from gilded_rose import Item, update_normal_item


def test_quality_greater_than_0():
    normal_diff = get_quality_diff(Item("Normal item 1232112", -1, 5))
    conjured_diff = get_quality_diff(Item("Conjured", -1, 5))

    assert normal_diff > 0
    assert conjured_diff > 0
    assert normal_diff == conjured_diff / 2


def test_update_less_than_0():
    normal_item_diff = get_quality_diff(Item("Normal item 1232112", -2, -1))
    conjured_diff = get_quality_diff(Item("Conjured", -2, -1))
    assert normal_item_diff == conjured_diff / 2


def get_quality_diff(input_item: Item):
    output_item = deepcopy(input_item)
    update_normal_item(output_item)
    return input_item.quality - output_item.quality
