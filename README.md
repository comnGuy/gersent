# GerSent

GerSent is a project that tries to make a relativ good sentiment of a german sentence. Our first approach will be simple techniques like wordlist or interpration to assess the given sentence.

## Getting Started

First you have to install our package.
`pip install gersent`

Now you are able to run a simple sentiment analysis over a german sentence.

```
from gersent import GerSent

ger_senti = GerSent()

print(ger_senti.sentiment('Ich bin ein guter Satz.')
```

## Configurations

# References

Wordlists:

R. Remus, U. Quasthoff & G. Heyer: SentiWS - a Publicly Available German-language Resource for Sentiment Analysis.
In: Proceedings of the 7th International Language Ressources and Evaluation (LREC'10), 2010
