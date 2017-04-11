def solution(word):
    vowel_set = 'aeiouy'
    is_beautiful = True
    for i in range(len(word) - 1):
        if word[i] == word[i + 1] or (word[i] in vowel_set and
                                      word[i + 1] in vowel_set):
            is_beautiful = False
    return is_beautiful


word = input().strip()
print('Yes' if solution(word) else 'No')
