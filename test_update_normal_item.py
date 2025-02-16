from copy import deepcopy
from gilded_rose import Item, update_normal_item


def run_update_item(normal_item):
    output_item = deepcopy(normal_item)
    update_normal_item(output_item)
    return output_item


def test_update_conjured_item():
    normal_item = Item("Normal item 1232112", -1, 5)
    normal_item_diff = normal_item.quality - run_update_item(normal_item).quality

    conjured_item = Item("Conjured", -1, 5)
    conjured_item_diff = conjured_item.quality - run_update_item(conjured_item).quality

    assert normal_item_diff == conjured_item_diff / 2


def test_update_conjured_item2():
    normal_item = Item("Normal item 1232112", -2, -1)
    normal_item_diff = normal_item.quality - run_update_item(normal_item).quality

    conjured_item = Item("Conjured", -2, -1)
    conjured_item_diff = conjured_item.quality - run_update_item(conjured_item).quality

    assert normal_item_diff == conjured_item_diff / 2
