"""
6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let's call it a glossary.

• Think of five programming words you've learned about in the previous
  chapters. Use these words as the keys in your glossary, and store their
  meanings as values.

• Print each word and its meaning as neatly formatted output. You might
  print the word followed by a colon and then its meaning, or print the word
  on one line and then print its meaning indented on a second line. Use the
  newline character (\n) to insert a blank line between each word-meaning
  pair in your output.
"""


glossary = {
    'variables': 'labels',
    'string': 'series of characters',
    'integers': 'numerical values without fractional part',
    'float': 'numerical values with fractional part',
    'boolean': 'either True or False'
}

print(f"Variables: {glossary['variables']}\n")
print(f"String: {glossary['string']}\n")
print(f"Integers: {glossary['integers']}\n")
print(f"Float: {glossary['float']}\n")
print(f"Boolean: {glossary['boolean']}\n")
