class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        result = []

        if (numerator < 0) != (denominator < 0):
            result.append("-")

        numerator = abs(numerator)
        denominator = abs(denominator)

        integer_part = numerator // denominator
        result.append(str(integer_part))

        remainder = numerator % denominator
        if remainder == 0:
            return "".join(result)

        result.append(".")  

        seen = {}  
        while remainder != 0:
            if remainder in seen:
                start = seen[remainder]
                result.insert(start, "(")
                result.append(")")
                break

            seen[remainder] = len(result)
            remainder *= 10
            digit = remainder // denominator
            result.append(str(digit))
            remainder %= denominator

        return "".join(result)