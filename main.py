
# First we need to import spacy 
import spacy 

import  MysqlQueries.getTokenForQuestion
import MysqlQueries.getFirstLevelData
# Creating blank language object then 
# tokenizing words of the sentence 
nlp = spacy.load("en_core_web_sm")
doc = nlp("what is phone of nischal ?") 
verbs = []
auxillaryVerbs = []
adjectives = []
pronouns = []
punctuations = []
nouns = []
sconj = []
propn = []

alltokens = []
def switchTokens(token):
    if token.pos_ == "VERB":
        verbs.append(token)
    elif token.pos_ == "AUX":
        auxillaryVerbs.append(token)
    elif token.pos_ == "ADJ":
        adjectives.append(token)
    elif token.pos_ == "PRON":
        pronouns.append(token)
    elif token.pos_ == "PUNCT":
        punctuations.append(token)
    elif token.pos_ == "NOUN":
        nouns.append(token)
    elif token.pos_ == "SCONJ":
        sconj.append(token)
    elif token.pos_ == "PROPN":
        propn.append(token)

for token in doc:
    switchTokens(token)
    print(token.pos_)

for val in adjectives:
    alltokens.append(MysqlQueries.getTokenForQuestion.getToken(val.text))
# for val in nouns:
#     print(val)
#     alltokens.append(MysqlQueries.getTokenForQuestion.getToken(val.text))

for val in alltokens:
    if len(nouns) > 0:

        vals = MysqlQueries.getFirstLevelData.getFirstLevelData(val, nouns[0].text)
        print(vals)
    
for val in nouns:
    alltokens.append(MysqlQueries.getTokenForQuestion.getToken(val.text))
    # for val in nouns:
    #     print(val)
    #     alltokens.append(MysqlQueries.getTokenForQuestion.getToken(val.text))

for val in alltokens:
    if len(adjectives) > 0:

        vals = MysqlQueries.getFirstLevelData.getFirstLevelData(val, adjectives[0].text)
        print(vals)


# print("verbs : ") 
# print(verbs) 
# print("\n")
# print("auxillary verbs : " )
# print(auxillaryVerbs)
# print("\n")
# print("adjectives : "  )
# print(adjectives)
# print("\n")
# print("pronouns : "  )
# print(pronouns)
# print("\n")
# print("noun : ")
# print(nouns)
# print("\n")
# print("punctuations : ")
# print(punctuations)
# print("\n")
# print("subordinating conjunction : ")
# print(sconj)
# print("\n")
# print("Proper noun : ")
# print(propn)
# print("\n")

# print("Freeschema Tokens : ")
# print(alltokens)
# print("\n")