class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_count = Counter(magazine)
        for i in ransomNote:
            if mag_count[i] == 0:
                return False
            else:
                mag_count[i] -= 1
        return True
