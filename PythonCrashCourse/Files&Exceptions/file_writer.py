from pathlib import Path
 
path = Path('programming.txt')
content = (
    'You really think someone would do that?\n'
    'Just go on the internet and tell lies?\n'
    '-No fucking way.'
    )
path.write_text(content)
with path.open('a') as f:
    f.write("This text will be appended. Don't forget \n")
    
path.open('a').write("Here's a good concise way to write it")