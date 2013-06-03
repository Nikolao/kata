#

class StringCalculator():
    MAX_VALUE = 1000
    SEPARATOR = ","
    def add(self, _string):
        if _string == "": return 0
        ret = 0
        normalized_string = self.normalizeString(_string)
        numbers = normalized_string.split(StringCalculator.SEPARATOR)
        errors = ""
        for nn in numbers:
            if nn[0] == "-":
                if errors != "":
                    errors += "\n"
                errors += "negative numbers not allowed : " + nn
                continue
            val = int(nn)
            if val < StringCalculator.MAX_VALUE:
                ret += val
        if errors != "":
            raise Exception(errors)
        return ret

    def normalizeString(self, _string):
        delimiters = None
        if _string[:2] == "//":
            delimiter, _string  = _string[2:].split("\n", 1)
            if "[" in delimiter:
                delimiters = delimiter[1:-1].split("][")
            else:
                delimiters = [delimiter, ]
        _string = _string.replace("\n", StringCalculator.SEPARATOR)
        if delimiters:
            for delimiter in  delimiters:
                _string = _string.replace(delimiter, StringCalculator.SEPARATOR)
        return _string

#
