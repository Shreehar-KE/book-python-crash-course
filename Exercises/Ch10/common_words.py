from pathlib import Path


def count_word(fileName, word):
    try:
        path = Path('project_gutenberg/'+fileName)
    except FileNotFoundError:
        print(f"{fileName} is not found...!")
    else:
        contents = path.read_text().lower()
        count = contents.count(word)
        return count


texts = ['PrideAndPrejudice.txt', 'SherlockHolmes.txt', 'RomeoAndJuliet.txt']

for text in texts:
    count = count_word(text, 'the ')
    print(f"The total count of the word 'the' in {text} is {count}.")
