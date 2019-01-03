# -*- coding=utf-8 -*-

'''
实现一个函数/方法 pattern_match(p, s)

p 含有星号的字符串  a*bb*c，星号代表0-n个前面的字符
    例如 a*b 匹配 b,ab,aaa, 不匹配  ba, baaab

s 是待匹配的字符串

如果匹配，返回true，否则返回 false

'''

def pattern_match(p, s):
    '''
    TODO implementation
    '''
    return True


def test_pattern_match():
    testcase = [
        ('abc', 'abc', True),
        ('a*b', 'aab', True),
        ('a*b', 'b', True),
        ('a*b', 'ba', False),
        ('a*bb*c*', 'aabbcc', True),
        ('a*bb*c', 'aacc', False),
        ('a*b*bc', 'aabc', True),
        ('a*b*bc', 'bbc', True),
    ]
    for p,s,ret in testcase:
        print('p={}, s={}, ret={}, result={}'.format(
            p,s,ret, pattern_match(p,s)))

def main():
    test_pattern_match()

if __name__ == '__main__':
    main()