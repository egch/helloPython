class DetectCapital:

    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        if word.isupper() or word.islower():
            return True
        if word[0].isupper() and word[1:].islower():
            return True
        return False


obj = DetectCapital()
string = input("Type ur string: ")
result = obj.detectCapitalUse(string)
print(result)