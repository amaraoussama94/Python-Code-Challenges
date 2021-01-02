import re

def is_palindrome (phrase):
    forwards =' '.join(re.findall(r'[a-z]+',phrase.lower()))
    backwords=forwards[::-1]
    return forwards == backwords

print(is_palindrome ('hih'))
                       
