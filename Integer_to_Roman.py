class Solution:
    def intToRoman(self, num: int) -> str:
        one = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        ten = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hundred = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thousand = ["", "M", "MM", "MMM"]
        return thousand[num//1000] + hundred[(num%1000)//100] + ten[(num%100)//10] + one[num%10]
