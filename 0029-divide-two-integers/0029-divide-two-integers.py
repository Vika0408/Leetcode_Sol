class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle overflow case: -2^31 / -1 = 2^31 will overflow, so return 2^31 - 1.
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        # Determine the sign of the result.
        sign = -1 if (dividend > 0) ^ (divisor > 0) else 1
        
        ans = 0
        dvd = abs(dividend)
        dvs = abs(divisor)

        # Perform division using bit manipulation.
        while dvd >= dvs:
            k = 1
            # Double the divisor value until it is less than or equal to the dividend.
            while k * 2 * dvs <= dvd:
                k *= 2
            # Subtract the largest multiple of the divisor from the dividend.
            dvd -= k * dvs
            # Add the corresponding multiple to the answer.
            ans += k

        return sign * ans
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

