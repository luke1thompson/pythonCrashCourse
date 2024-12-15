current_users = ['Soccerfan98', 'Baphomet', 'strwrSBstwrs', 'bigchungus', 'admin']
current_lower = []
for user in current_users:
    current_lower.append(user.lower())
new_users = ['chigbungus', 'BigChungus', 'mr666', 'dannystan', 'baphoMEt']

for user in new_users:
    if user.lower() in current_lower:
        print('That username is taken; Please choose another.')
    else:
        print('Nice to know SOMEBODY can follow instructions.')
