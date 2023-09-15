class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        volume = length * width * height
        index = int(length >= 10**4 or height >= 10**4 or width >= 10**4 or volume >= 10**9) + 2*(mass >= 100)
        return ("Neither", "Bulky", "Heavy", "Both")[index]