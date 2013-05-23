package stringCalculator;
import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

import stringCalculator.StringCalculator;

public class TestStringCalculator {
	StringCalculator kata;
	
	@Before
	public void setUp() throws Exception {
		this.kata = new StringCalculator();
	}

	@Test
	public void test_no_number() {
		int result;
		result = this.kata.add("");
		assertEquals(result, 0);
	}

	@Test
	public void test_one_number() {
		int result;
		result = this.kata.add("1");
		assertEquals(result, 1);
		result = this.kata.add("2");
		assertEquals(result, 2);
	}
	
	@Test
	public void test_two_numbers() {
		int result;
		result = this.kata.add("1,2");
		assertEquals(result, 3);
		result = this.kata.add("2,3");
		assertEquals(result, 5);
	}
	
	@Test
	public void test_many_numbers() {
		int result;
		result = this.kata.add("1,2,3");
		assertEquals(result, 6);
		result = this.kata.add("1,2,3,4");
		assertEquals(result, 10);
	}
	
	@Test
	public void test_new_lines_and_commas() {
		int result;
		result = this.kata.add("1\n2,3");
		assertEquals(result, 6);
	}
	
	@Test
	public void test_specific_delimiters() {
		int result;
		result = this.kata.add("//%\n1\n2%3");
		assertEquals(result, 6);
	}
	
	@Test(expected=Exception.class)
	public void test_no_negative() {
		this.kata.add("1,-2,3");
	}
	
	@Test
	public void test_no_more_than_999() {
		int result;
		result = this.kata.add("1,2,999");
		assertEquals(result, 1002);
		result = this.kata.add("1,2,1000");
		assertEquals(result, 3);
	}
	
	@Test
	public void test_one_custom_delimiter() {
		int result;
		result = this.kata.add("//[**]\n1\n2**3");
		assertEquals(result, 6);
	}

	@Test
	public void test_many_custom_delimiter() {
		int result;
		result = this.kata.add("//[**][%%]\n1%%2**3");
		assertEquals(result, 6);
	}

}
