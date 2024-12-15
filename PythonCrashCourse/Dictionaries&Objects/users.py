unconfirmed_users = ['jim', 'jam', 'jackson', 'jill']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}. Processing data.")
    
    confirmed_users.append(current_user)

print('\nCurrent list of confirmed users:')
print(confirmed_users)