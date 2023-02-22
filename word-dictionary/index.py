from PyDictionary import PyDictionary

dictionary = PyDictionary()

word = input("Write a word to find in Dictionary: ")

def main(word):
    print(dictionary.meaning(word))

main(word)