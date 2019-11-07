char = input('Enter a character between a and z ( or A and Z): ')
def isVowel(char):
    return char.lower() in 'aeiou'
print("\n"+str(char) + " is a vowel: " + str(isVowel(char)))