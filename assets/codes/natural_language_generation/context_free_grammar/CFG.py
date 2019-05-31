import random

###### load word bank ######

with open("words.txt") as datafile:
    nouns_s, nouns_p, verbs_trans, verbs_intrans, adjectives, adverbs, prepositions = [line[:-1].split(', ') for line in datafile.readlines() if line[0]!='#']

############################


###### all the nonterminal symbols ######

class Noun:
    def __init__(self, plural):
        self.plural=plural
        
    def replace(self):
        if self.plural:
            return [random.choice(nouns_p)]
        else:
            return [random.choice(nouns_s)]
        
class IntransitiveVerb:
    def __init__(self, plural):
        self.plural=plural
        
    def replace(self):
        verb=random.choice(verbs_intrans)
        if not self.plural:
            # handle different possible pluralizations
            if verb[-1]=='x' or verb[-2:]=='ch' or verb[-2:]=='sh' or verb[-2:]=='th' or verb[-2:]=='ss':
                verb+='es'
            else:
                verb+='s'
        return [verb]
        
class TransitiveVerb:
    def __init__(self, plural):
        self.plural=plural
        
    def replace(self):
        verb=random.choice(verbs_trans)
        if not self.plural:
            # handle different possible pluralizations
            if verb[-1]=='x' or verb[-2:]=='ch' or verb[-2:]=='sh' or verb[-2:]=='th' or verb[-2:]=='ss':
                verb+='es'
            else:
                verb+='s'
        return [verb]
        
class Adjective:
    def replace(self):
        return [random.choice(adjectives)]
        
class Adverb:
    def replace(self):
        return [random.choice(adverbs)]
        
class Preposition:
    def replace(self):
        return [random.choice(prepositions)]


        
class SingularNounPhrase:
    def replace(self):
        return ["the", Adjective(), Noun(False)]
        
class PluralNounPhrase:
    def replace(self):
        return ["the", Noun(True)]
        
class SingularVerbPhrase:
    def replace(self):
        return [IntransitiveVerb(False), Preposition(), PluralNounPhrase()]
        
class PluralVerbPhrase:
    def replace(self):
        return [TransitiveVerb(True), SingularNounPhrase(), Adverb()]


        
class SingularSentence:
    def replace(self):
        return [SingularNounPhrase(), SingularVerbPhrase()]
        
class PluralSentence:
    def replace(self):
        return [PluralNounPhrase(), PluralVerbPhrase()]

##############################


###### actual generator ###### 

def generate_sentence(plural):

    # start symbol
    if plural:
        sentence=[PluralSentence()]
    else:
        sentence=[SingularSentence()]

    # repeatedly apply production rules
    while True:
        newSentence=[]
        for part in sentence:
            if type(part)==str:     # terminal symbol
                newSentence.append(part)
            else:                   # non-terminal symbol
                newSentence.extend(part.replace())        

        # done if all the symbols were terminal
        if newSentence==sentence:
            break
        
        sentence=newSentence

    # concatenate words, capitalize first letter, add punctuation        
    answer = ' '.join(sentence)
    return answer[0].upper() + answer[1:] + '.'


# generate 3 plural and 3 singular sentences 
for i in range(3):
    print generate_sentence(True)
    print generate_sentence(False)
