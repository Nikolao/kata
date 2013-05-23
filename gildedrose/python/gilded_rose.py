# -*- coding: utf-8 -*-

class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GRItem(Item):
    BASE_SELL_IN_INCREMENT = 1
    BASE_QUALITY_INCREMENT = 1
    MIN_QUALITY = 0
    MAX_QUALITY = 50

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)
        self.sell_in_increment = -GRItem.BASE_SELL_IN_INCREMENT
        self.quality_increment = -GRItem.BASE_QUALITY_INCREMENT

    def update(self):
        self.updateSellIn()
        self.updateQuality()

    def updateSellIn(self):
        self.sell_in += self.sell_in_increment
        if self.hasSellByDatePassed(): self.quality_increment = -2 * GRItem.BASE_QUALITY_INCREMENT

    def updateQuality(self):
        if self.quality < self.MAX_QUALITY: self.quality += self.quality_increment
        if self.quality < self.MIN_QUALITY: self.quality = self.MIN_QUALITY

    def hasSellByDatePassed(self):
        return self.sell_in <= 0


class AgedBrieItem(GRItem):
    def __init__(self, name, sell_in, quality):
        GRItem.__init__(self, name, sell_in, quality)
        self.quality_increment = GRItem.BASE_QUALITY_INCREMENT


class ConjuredItem(GRItem):
    def __init__(self, name, sell_in, quality):
        GRItem.__init__(self, name, sell_in, quality)
        self.quality_increment = -2 * GRItem.BASE_QUALITY_INCREMENT


class SulfurasItem(GRItem):
    def __init__(self, name, sell_in, quality):
        GRItem.__init__(self, name, sell_in, quality)
        self.sell_in_increment = 0
        self.quality_increment = 0


class BackstagePassesItem(GRItem):
    def __init__(self, name, sell_in, quality):
        GRItem.__init__(self, name, sell_in, quality)
        self.quality_increment = GRItem.BASE_QUALITY_INCREMENT

    def updateSellIn(self):
        GRItem.updateSellIn(self)
        if self.hasSellByDatePassed(): self.quality_increment = 0
        elif self.hasLessThan5DaysBeforeSellByDatePass(): self.quality_increment = 3 * GRItem.BASE_QUALITY_INCREMENT
        elif self.hasLessThan10DaysBeforeSellByDatePass(): self.quality_increment = 2 * GRItem.BASE_QUALITY_INCREMENT

    def updateQuality(self):
        GRItem.updateQuality(self)
        if self.hasSellByDatePassed(): self.quality = 0

    def hasLessThan5DaysBeforeSellByDatePass(self):
        return self.sell_in <= 5

    def hasLessThan10DaysBeforeSellByDatePass(self):
        return self.sell_in <= 10


def ItemFactory(name, sell_in, quality):
    if "Brie" in name: return AgedBrieItem(name, sell_in, quality)
    elif "Sulfuras" in name: return SulfurasItem(name, sell_in, quality)
    elif "Conjured" in name: return ConjuredItem(name, sell_in, quality)
    elif "Backstage passes" in name: return BackstagePassesItem(name, sell_in, quality)
    return GRItem(name, sell_in, quality)

