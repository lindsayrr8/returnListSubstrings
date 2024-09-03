
# This program creates a function that
# returns a list of all substrings in a string.



# Function that gets permutations of substrings.
def substrings(s):
    
    # An empty string/no substrings.
    allSubstrings = []

    # Generates substrings starting with first character.
    for i in range(len(s)):
        substring = ""
        for n in range(i + 1):
            substring += s[n]
        allSubstrings.append(substring)

    # Generates substrings for the string without the first character.
    for i in range(1, len(s)):
        substring = ""
        for n in range(i, len(s)):
            substring += s[n]
        allSubstrings.append(substring)

    return allSubstrings



# Function that takes user input to evaluate a string's substrings.
def getUserInput():
    
    inputString = input("Please input a word: ")
    # Creates variable to store result of user input evaluated by substrings function.
    result = substrings(inputString)
    print(result)


getUserInput()
