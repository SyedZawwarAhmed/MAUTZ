import nltk
import string
from nltk.parse.generate import generate

sampleString = 'ye car123,apple11,house101;'

# grammar = nltk.CFG.fromstring("""
#     S -> NP VP
#     VP -> V NP | V NP PP
#     PP -> P NP
#     V -> "saw" | "ate" | "walked"
#     NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
#     Det -> "a" | "an" | "the" | "my"
#     N -> "man" | "dog" | "cat" | "telescope" | "park"
#     P -> "in" | "on" | "by" | "with" 
# """)

# Define the CFG
# grammar = nltk.CFG.fromstring("""
#     S -> 'ye' id new ';'
#     new -> ',' id new | empty
#     id -> LETTER (LETTER | DIGIT)* | empty
#     LETTER -> '[a-zA-Z]'
#     DIGIT -> '[0-9]'
#     empty ->
# """)

letters = string.ascii_lowercase
formatted_letters = "|".join([f"'{letter}'" for letter in letters])
# print(formatted_letters)

formatted_digits = "|".join([f"'{i}'" for i in range(10)])

grammar = nltk.CFG.fromstring(f"""
    S -> 'ye' ID ';'
    ID -> LETTERS
    LETTER -> {formatted_letters} LETTER | {formatted_letters}
    DIGIT -> {formatted_digits}
    empty -> 
""")


# Generate sentences from the CFG
# for sentence in generate(grammar):
#     print(sentence)


parser = nltk.parse.EarleyChartParser(grammar)
sentence = 'ye abcaz ;'

try:
    parsed_trees = list(parser.parse(sentence.split()))
    print("The sentence is valid in the grammar.")
except Exception as error:
    print(error)