import re


def word_count(s):
    words_cache = {}
    s = re.compile(r'[]":;,.+=/\\|[{}()*^&-]').sub('', s.lower()).split()
    for word in s:
        if word not in words_cache:
            words_cache[word] = 1
        else:
            words_cache[word] += 1
    return words_cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
