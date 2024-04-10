# QUESTION. 회문 순열
# 주어진 문자열이 회문(palindrome)의 순열인지 아닌지 확인하는 함수를 작성하라.
# 회문이란 앞으로 읽으나 뒤로 읽으나 같은 단어 혹은 구절을 의미하며,
# 순열이란 문자열을 재배치하는 것을 뜻한다. 


# my solution
from collections import Counter

def pelindrome(string):
    char_cnt = Counter()
    char_len = 0
    for s in string:
        if s == ' ':
            continue
        char_len += 1
        
        if char_cnt[s] == 0:
          char_cnt[s] += 1
        else:
          char_cnt[s] -= 1

    total = sum(char_cnt.values())

    if char_len%2 == 0:
        if total != 0:
            return False
    else:
        if total != 1:
            return False
    return True


# ANSWER
# 짝수 길이 문자열 : 홀수들 + 홀수
# 홀수 길이 문자열 : 짝수들 + 홀수
# 홀수 개인 문자가 1개 이상일 수 없다.
def pal_perm(phrase):
    '''function checks if a string is a permutation of a palindrome or not'''
    table = [0 for _ in range(ord('z') - ord('a') + 1)]
    countodd = 0
    for c in phrase:
        x = char_number(c)
        if x != -1:
            table[x] += 1
            if table[x] % 2:
                countodd += 1
            else:
                countodd -= 1

    return countodd <= 1

def char_number(c):
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')
    val = ord(c)

    if a <= val <= z:
        return val - a
    elif A <= val <= Z:
        return val - A
    return -1
