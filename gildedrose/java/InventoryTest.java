
package gildedRose;

import static org.junit.Assert.*;

import gildedRose.Inventory;
import gildedRose.Item;

import java.util.Arrays;

import org.junit.Before;
import org.junit.Test;


public class InventoryTest {

    // new Item("+5 Dexterity Vest", 10, 20),
    // new Item("Aged Brie", 2, 0),
    // new Item("Elixir of the Mongoose", 5, 7),
    // new Item("Sulfuras, Hand of Ragnaros", 0, 80),
    // new Item("Backstage passes to a TAFKAL80ETC concert", 15, 20),
    // new Item("Conjured Mana Cake", 3, 6)

    private Inventory inventory = null;

    @Before
    public void setUp() {
    	inventory = new Inventory();
    }
    
    @Test
    public void should_never_changes_quality_of_Sulfuras() throws Exception {
        Item sulfuras = new Item("Sulfuras, Hand of Ragnaros", 0, 80);

        inventory = new Inventory((Item[]) Arrays.asList(new Item("Sulfuras, Hand of Ragnaros", 0, 80)).toArray());

        inventory.updateQuality();

        assertEquals(80, sulfuras.getQuality());
    }

    @Test
    public void should_never_changes_sellIn_of_Sulfuras() throws Exception {
        Item sulfuras = new Item("Sulfuras, Hand of Ragnaros", 0, 80);

        inventory = new Inventory((Item[]) Arrays.asList(sulfuras).toArray());

        inventory.updateQuality();

        assertEquals(0, sulfuras.getSellIn());

    }

    @Test
    public void should_lower_the_sellIn_by_one_for_normal_items() throws Exception {
        Item normalItem = new Item("+5 Dexterity Vest", 10, 20);

        inventory = new Inventory((Item[]) Arrays.asList(normalItem).toArray());

        inventory.updateQuality();

        assertEquals(9, normalItem.getSellIn());
    }

    @Test
    public void should_lower_the_quality_by_one_for_normal_items() throws Exception {
        Item normalItem = new Item("+5 Dexterity Vest", 10, 20);

        inventory = new Inventory((Item[]) Arrays.asList(normalItem).toArray());

        inventory.updateQuality();

        assertEquals(19, normalItem.getQuality());
    }

    @Test
    public void should_not_lower_the_quality_below_zero() throws Exception {
        Item normalItem = new Item("+5 Dexterity Vest", 10, 0);

        inventory = new Inventory((Item[]) Arrays.asList(normalItem).toArray());

        inventory.updateQuality();

        assertEquals(0, normalItem.getQuality());
    }

    @Test
    public void should_lower_the_quality_twice_as_fast_once_the_sell_in_date_has_passed() throws Exception {
        Item normalItem = new Item("+5 Dexterity Vest", -1, 25);

        inventory = new Inventory((Item[]) Arrays.asList(normalItem).toArray());

        inventory.updateQuality();

        assertEquals(23, normalItem.getQuality());
    }

    @Test
    public void should_increase_the_quality_of_aged_brie_as_it_gets_older() throws Exception {
        Item agedBrie = new Item("Aged Brie", 10, 25);

        inventory = new Inventory((Item[]) Arrays.asList(agedBrie).toArray());

        inventory.updateQuality();

        assertEquals(26, agedBrie.getQuality());
    }

    @Test
    public void should_not_increase_the_quality_of_aged_brie_over_50() throws Exception {
        Item agedBrie = new Item("Aged Brie", 10, 50);

        inventory = new Inventory((Item[]) Arrays.asList(agedBrie).toArray());

        inventory.updateQuality();

        assertEquals(50, agedBrie.getQuality());
    }

    @Test
    public void should_lower_backstage_passes_to_zero_quality_once_concert_has_happened() throws Exception {
        Item backStagePass = new Item("Backstage passes to a TAFKAL80ETC concert", -1, 20);

        inventory = new Inventory((Item[]) Arrays.asList(backStagePass).toArray());

        inventory.updateQuality();

        assertEquals(0, backStagePass.getQuality());
    }

    @Test
    public void should_increase_backstage_passes_quality_by_1_when_the_concert_is_more_than_10_days_away() throws Exception {
        Item backStagePass = new Item("Backstage passes to a TAFKAL80ETC concert", 11, 20);

        inventory = new Inventory((Item[]) Arrays.asList(backStagePass).toArray());

        inventory.updateQuality();

        assertEquals(21, backStagePass.getQuality());
    }

    @Test
    public void should_increase_backstage_passes_quality_by_2_when_the_concert_is_10_days_or_less_away() throws Exception {
        Item backStagePass = new Item("Backstage passes to a TAFKAL80ETC concert", 10, 27);

        inventory = new Inventory((Item[]) Arrays.asList(backStagePass).toArray());

        inventory.updateQuality();

        assertEquals(29, backStagePass.getQuality());
    }

    @Test
    public void should_increase_backstage_passes_quality_by_3_when_the_concert_is_5_days_or_less_away() throws Exception {
        Item backStagePass = new Item("Backstage passes to a TAFKAL80ETC concert", 5, 44);

        inventory = new Inventory((Item[]) Arrays.asList(backStagePass).toArray());

        inventory.updateQuality();

        assertEquals(47, backStagePass.getQuality());
    }

    @Test
    public void should_not_increase_backstage_passes_above_a_quality_of_50() throws Exception {
        Item backStagePassMoreThan10DaysAway = new Item("Backstage passes to a TAFKAL80ETC concert", 15, 50);

        Item backStagePass10DaysAway = new Item("Backstage passes to a TAFKAL80ETC concert", 10, 49);
        Item backStagePass5DaysAway = new Item("Backstage passes to a TAFKAL80ETC concert", 5, 48);

        inventory = new Inventory((Item[]) Arrays.asList(backStagePassMoreThan10DaysAway, backStagePass10DaysAway, backStagePass5DaysAway).toArray());

        inventory.updateQuality();

        assertEquals(50, backStagePassMoreThan10DaysAway.getQuality());
        assertEquals(50, backStagePass10DaysAway.getQuality());
        assertEquals(50, backStagePass5DaysAway.getQuality());
    }
}
