vowels = ["a", "e", "i", "o", "u"]


def checkForVowels(some_string):
    amountOfVowels = {}
    for i in vowels:
        if i in some_string:
            amountOfVowels[i] = some_string.count(i)
        elif i.upper() in some_string:
            amountOfVowels[i.upper()] = some_string.count(i.upper())
    return amountOfVowels


print(checkForVowels("sOmE string"))
