class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        string = list(s.lower())
        mystring = []
        for letter in string:
            if letter == "i":
                mystring.append(1)
            elif letter == "v":
                mystring.append(5)
            elif letter == "x":
                mystring.append(10)
            elif letter == "l":
                mystring.append(50)
            elif letter == "c":
                mystring.append(100)
            elif letter == "d":
                mystring.append(500)
            elif letter == "m":
                mystring.append(1000)
        for j in range(len(mystring) - 1):
            if mystring[j] < mystring[j + 1]:
                total -= mystring[j]
            else:
                total += mystring[j]
        total += mystring[-1]
        return total


sol = Solution()
print(sol.romanToInt("III"))
print(sol.romanToInt("MCMXCIV"))
