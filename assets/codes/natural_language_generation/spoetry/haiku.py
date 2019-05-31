import random

def syllables(word):
    '''takes in string; returns approximate number of syllables in word'''
    syls=0
    
    # count vowels
    previous_vowel=''
    for letter in word:
    
        if letter in 'aeiouy':
            # avoid double-counting dipthongs
            dip=previous_vowel+letter
            
            if previous_vowel=='' or dip=='ao' or dip=='eo' or dip=='ia' or dip=='iu' or dip=='ua' or dip=='ui' or dip=='uo':
                syls+=1
                previous_vowel=letter
        else:
            previous_vowel=''

     # correct for long vowels
    if (word[-1]=='e' or word[-2:]=='es') and syls>1:
        syls-=1
        
    return syls


def sort_by_syl(words):
    '''takes in word list; returns dictionary containing syllable count:word list'''
    syl_dict={}   
    for word in words:
        syls=syllables(word)
        
        if syls in syl_dict:
            syl_dict[syls].append(word)
            
        else:
            syl_dict[syls]=[word]
            
    return syl_dict


def load_words(filename):
    '''returns processed list of words in file'''
    words=[]
    with open(filename) as f:
        line=f.readline()
        while line!='':
            line=line.split()
            words.extend([word.lower().strip(',.?;:!()[]{}') for word in line if word[:-1].isalpha()])        
            line=f.readline()
    return words
    

def haiku_line(syl_dict, syl_needed):
    line=[]
    while syl_needed>0:
        # choose random number of syllables under 7
        syl=1+random.randrange(min(syl_needed,6))
        
        # choose random word with chosen number of syllables
        word=random.choice(syl_dict[syl])
        
        line.append(word)
        syl_needed-=syl

    line[-1]=line[-1]+'\n'

    return ' '.join(line)

def haiku(syl_dict):
    poem=haiku_line(syl_dict, 5)
    poem += haiku_line(syl_dict, 7)
    poem += haiku_line(syl_dict, 5)
    return poem
    
    
words=load_words("emails.txt")
word_dict=sort_by_syl(words)
print haiku(word_dict)[:-1]
