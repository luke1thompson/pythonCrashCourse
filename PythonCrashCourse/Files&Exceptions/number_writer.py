from pathlib import Path
import json

username = input('Please enter a username: ')

path = Path('numbers.json')
contents = json.dumps(username.title())
path.write_text(contents)