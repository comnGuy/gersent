from gersent import GerSent


ger_senti = GerSent()

print('Positiv')
positive_sentence_list = [
    'Die Äpfel schmecken gut.',
    'Die Äpfel schmecken gut!',
    'Die Äpfel schmecken gut!!!',
    'Die Äpfel schmecken sehr gut!',
]
for sentence in positive_sentence_list:
    print(sentence)
    print(ger_senti.sentiment(sentence))
    print()

print('Negativ')
negative_sentence_list = [
    'Die Äpfel schmecken nicht gut.',
    'Ich nehme dir die Aktion krumm, nicht so negativ sondern positiv!',
]
for sentence in negative_sentence_list:
    print(sentence)
    print(ger_senti.sentiment(sentence))
    print()
