# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
# [assignment] Add your code here
    for n in word:
        if n not in  anagram:
            return False
        else :
            return True




word = input("input word: ").lower().strip()
anagram = input("check anagram: ").lower().strip()


print(find_anagram(word, anagram))
