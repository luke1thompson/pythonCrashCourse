mydict = {'green':'nature', 'red':'math', 'blue':'the sky', 'yellow':'the sun'}
mydict['orange'] = 'orange'
mydict[1] = 'me'

for key, value in mydict.items():
    print(f'When I hear "{key}" I think of {value}.')

numdict = {}
for num in range(10):
    numdict[num] = num ** 2

del numdict[3]

for x in range(10):
    print(f"When you square {x} you get: {numdict.get(x, 'I do not know ;( ')}!")
    
for value in numdict.values():
    print(value)