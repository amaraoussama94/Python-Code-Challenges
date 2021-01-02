import re #extract indiv word
from collections import Counter # for counting uniq items

def count_words(path):
    with open(path,encoding='utf-8')as file :
        all_words = re.findall(r"[0-9a-zA-Z']+",file.read())
        all_words=[ord.upper() for ord in all_words]
        print('\n Total words:',len(all_words))
        
        word_counts=Counter()#counter obj
        for word in all_words:
            word_counts[word]+=1  #dictionnery

        print('\n Top 20 words :')
        for word in word_counts.most_common(20):
            print(word[0],'\t',word[1])
        
count_words('test.txt')
