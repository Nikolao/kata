package stringCalculator;


public class StringCalculator {
	String errors = "";
	
	int add(String numbers) {
		if (numbers.isEmpty() == true) {
			return 0;
		}
		return computeSumOfOperators(numbers);
	}

	private Integer computeSumOfOperators(String numbers) {
		String[] operands = getOperandsAsStringsList(numbers);
		resetErrorMessage();
		int ret = 0;
		for (String operand : operands) {
			ret = checkAndAddValue(ret, operand);
		}
		throwExceptionIfErrorMessage();
		return ret;
	}

	private int checkAndAddValue(int sum, String val) {
		int ret = sum;
		int value = Integer.valueOf(val);
		if (value < 0) {
			addErrorMessage("negatives not allowed : " + val);
		}
		else if (value < 1000) {
			ret += value;
		}
		return ret;
	}

	private void resetErrorMessage() {
		errors = "";
	}
	
	private void addErrorMessage(String val) {
		if (!errors.equals("")) {
			errors = errors + "\n";
		}
		errors = errors + val;
	}

	private void throwExceptionIfErrorMessage() {
		if (errors.isEmpty() == false) {
			throw new RuntimeException(errors);
		}
	}

	private String[] getOperandsAsStringsList(String operands) {
		String normalized_numbers = normalizeOperands(operands);
		return normalized_numbers.split("\n");
	}

	private String normalizeOperands(String operands) {
		String[] separators = getCustomSeparatorList(operands);
		String numbers_only = getOperatorsOnly(operands);
		String ret = numbers_only;
		for (String separator : separators) {
			ret = ret.replace(separator, "\n");
		}
		return ret;
	}

	private boolean hasCustomSeparator(String operands) {
		return operands.length() > 2 && operands.substring(0, 2).equals("//");
	}

	private String getOperatorsOnly(String operands) {
		String ret = operands;
		if (hasCustomSeparator(operands)) {
			ret = operands.substring(operands.indexOf("\n")+1);
		}
		return ret;
	}

	private String[] getCustomSeparatorList(String operands) {
		if (!hasCustomSeparator(operands)) {
			return getSingleSeparatorList(",");
		}
		String[] ret;
		String separator = operands.substring(2, operands.indexOf("\n"));
		if (separator.startsWith("[")) {
			separator = separator.substring(1, separator.length()-1);
			ret = separator.split("\\]\\[");
			return ret;
		}
		return getSingleSeparatorList(separator);
	}

	private String[] getSingleSeparatorList(String separator) {
		String[] ret = new String[1];
		ret[0] = separator;
		return ret;
	}
	
}
