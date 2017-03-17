# point
# - n lowercase English letter
# - consonants next to vowel next to consonants
# - not contain 'y'
# - the first letter is vowel or consonant

n = int(input().strip())

vowel = list('aeiou')
consonant = list('bcdfghjklmnpqrstuvwxz')

token = list()

for i in vowel:
    for j in consonant:
        token.append((i, j))


