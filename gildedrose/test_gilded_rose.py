# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose, ItemFactory

class GildedRoseTest(unittest.TestCase):

    # All items have a SellIn value which denotes the number of days we have to
    # sell the item
    # All items have a Quality value which denotes how valuable the item is
    # At the end of each day our system lowers both values for every item
    def test_each_day_sell_in_decreases(self):
        items = [ItemFactory("foo", 1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].sell_in)
    def test_each_day_quality_decreases(self):
        items = [ItemFactory("foo", 1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    # Once the sell by date has passed, Quality degrades twice as fast
    def test_quality_decreases_faster_after_date_passed(self):
        items = [ItemFactory("foo", 2, 4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(3, items[0].quality)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(1, items[0].quality)

    # The Quality of an item is never negative
    def test_quality_is_never_negative(self):
        items = [ItemFactory("foo", 3, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertTrue(items[0].quality == 0)
        gilded_rose.update_quality()
        self.assertTrue(items[0].quality == 0)

    # “Aged Brie” actually increases in Quality the older it gets
    def test_aged_brie_increases_in_quality(self):
        items = [ItemFactory(name="Aged Brie", sell_in=2, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(1, items[0].quality)

    # The Quality of an item is never more than 50
    def test_quality_is_never_more_than_50(self):
        items = [ItemFactory(name="Aged Brie", sell_in=2, quality=50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    # “Sulfuras”, being a legendary item, never has to be sold or decreases in
    # Quality
    def test_sulfura_never_has_to_be_sold(self):
        items = [ItemFactory(name="Sulfuras, Hand of Ragnaros", sell_in=5, quality=80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(5, items[0].sell_in)
    def test_sulfura_never_decreases_in_quality(self):
        items = [ItemFactory(name="Sulfuras, Hand of Ragnaros", sell_in=5, quality=80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(80, items[0].quality)

    # “Backstage passes” increases in Quality as it’s SellIn value approaches
    def test_backstage_passes_increases_in_quality(self):
        items = [ItemFactory(name="Backstage passes to a TAFKAL80ETC concert",
                      sell_in=15, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(11, items[0].quality)

    # “Backstage passes” increases in Quality by 2 when there are 10 days or less
    def test_backstage_passes_increases_in_quality_by_2(self):
        items = [ItemFactory(name="Backstage passes to a TAFKAL80ETC concert",
                      sell_in=12, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(11, items[0].sell_in)
        self.assertEquals(11, items[0].quality)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(10, items[0].sell_in)
        self.assertEquals(13, items[0].quality)

    # “Backstage passes” increases in Quality by 3 when there are 5 days or less
    def test_backstage_passes_increases_in_quality_by_3(self):
        items = [ItemFactory(name="Backstage passes to a TAFKAL80ETC concert",
                      sell_in=7, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(6, items[0].sell_in)
        self.assertEquals(12, items[0].quality)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(5, items[0].sell_in)
        self.assertEquals(15, items[0].quality)

    # “Backstage passes” quality drops to 0 after the concert
    def test_backstage_passes_drops_in_quality_after_date(self):
        items = [ItemFactory(name="Backstage passes to a TAFKAL80ETC concert",
                      sell_in=2, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(1, items[0].sell_in)
        self.assertEquals(13, items[0].quality)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].sell_in)
        self.assertEquals(0, items[0].quality)

    # “Conjured” items degrade in Quality twice as fast as normal items
    def test_conjured_items_quality_decreases_by_2(self):
        items = [ItemFactory(name="Conjured Mana Cake", sell_in=3, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(8, items[0].quality)

if __name__ == '__main__':
    unittest.main()
