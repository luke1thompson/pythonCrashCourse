alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
    
for number in range(30):
    new_alien = {'color':'green', 'points': 5, 'speed':'fast'}
    aliens.append(new_alien)
    
for alien in aliens[:5]:
    if alien['color'] == 'green':
        alien['color'] = 'poopy brown'
        alien['points'] = 12
        alien['speed'] = 'slow'
    
for alien in aliens[:10]:    
    print(alien)