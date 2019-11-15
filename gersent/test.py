from gersent import GerSent


ger_senti = GerSent()

result = ger_senti.sentiment(
    "Ich nehme dir die Aktion krumm, nicht so negativ sondern positiv!")

print(result)


# import json


# path = './wordlists/de/negativ.txt'

# with open(path, encoding='utf-8') as f:
#     content = f.readlines()
# content = [x.replace('\n', '').split('\t') for x in content]

# positive = {}
# for word in content:
#     score = word[1]
#     positive[word[0].split('|')[0]] = score
#     words = word[2].split(',')
#     for extracted_word in words:
#         if extracted_word is not '':
#             positive[extracted_word] = score


# with open('./wordlists/de/negativ.json', 'w') as fp:
#     json.dump(positive, fp)
