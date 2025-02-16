from copy import deepcopy
from gilded_rose import Item, update_normal_item


def test_update_conjured_item():
    # args: ('foo', -1, 51) => 'foo, -2, 49'
    normal_item = Item("Normal item 1232112", -1, 5)
    output_item = deepcopy(normal_item)
    update_normal_item(output_item)
    normal_item_diff = normal_item.quality - output_item.quality

    normal_item = Item("Conjured", -1, 5)
    output_item = deepcopy(normal_item)
    update_normal_item(output_item)
    conjured_item_diff = normal_item.quality - output_item.quality

    assert normal_item_diff == conjured_item_diff / 2
