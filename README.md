# GerSent

GerSent is a project that tries to make a relativ good sentiment of a german sentence. Our first approach will be simple techniques like wordlist or interpration to assess the given sentence.

## Getting Started

First you have to install our package.

`pip install gersent`

Now you are able to run a simple sentiment analysis over a german sentence.

```python
from gersent import GerSent

ger_senti = GerSent()

print(ger_senti.sentiment('Ich bin ein guter Satz.')
```

## Configurations

## Examples

Positiv
```python
# Die Äpfel schmecken gut.
{'negative': 0.0, 'positive': 0.3716, 'composite': 0.3716}

# Die Äpfel schmecken gut!
{'negative': 0.0, 'positive': 0.39018, 'composite': 0.39018}

# Die Äpfel schmecken gut!!!
{'negative': 0.0, 'positive': 0.42733999999999994, 'composite': 0.42733999999999994}

# Die Äpfel schmecken sehr gut!
{'negative': 0.0, 'positive': 0.39018, 'composite': 0.39018}
```

Negativ
```python
# Die Äpfel schmecken nicht gut.
{'negative': -0.0, 'positive': -0.3716, 'composite': -0.3716}
```
# References

Wordlists

R. Remus, U. Quasthoff & G. Heyer: SentiWS - a Publicly Available German-language Resource for Sentiment Analysis.
In: Proceedings of the 7th International Language Ressources and Evaluation (LREC'10), 2010
