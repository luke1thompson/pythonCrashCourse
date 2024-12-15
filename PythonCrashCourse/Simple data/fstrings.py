first = '   Juan  '
last = ' Skadoodle'

fullname = (first.strip() + ' ' + last.strip()).title()
print(fullname)

reason1 = 'pooping in the urinal'
reason2 = 'saying racist things about my dad'
reason3 = 'refusing to wear pants at work'

statement = f'Dear {(first + " " + last).title()}, We regret to inform you that you are fired. \nYour insistence on {reason3} lead directly to this decision. Goodbye'

# print(statement)