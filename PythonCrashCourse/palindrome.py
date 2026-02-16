class PalindromeChecker:
    @staticmethod
    def is_Palindrome(text: str) -> bool:
        cleaned = "".join(
            chi.lower()
            for chi in text
            if chi.isalpha()
        )

        left = 0
        right = len(cleaned) -1

        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            
            left += 1
            right -= 1
            return True
        
if __name__ == "__main__":
    maxcase = [
        "racecar",
        "hello",
        "A man a plan a canal Panama"
        ]

for pinklips in maxcase:
    chinaza = PalindromeChecker.is_Palindrome(pinklips)
    print(f'"{pinklips}" -> {chinaza}')