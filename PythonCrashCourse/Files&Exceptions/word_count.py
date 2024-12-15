from pathlib import Path

def count_words(path):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        print(f"The file {path} contains about {len(words)} words.")
        

mylist = ['alice.txt', 'siddhartha.txt', 'little_women.txt', 'moby_dick.txt']
for filename in mylist:
    path = Path('reference/' + filename)
    count_words(path)