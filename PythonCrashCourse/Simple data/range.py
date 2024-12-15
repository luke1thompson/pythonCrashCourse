squares = []

for num in range(1,11):
    squares.append(num*num)
    
squares2 = [num**2 for num in range(1,6)]

# print(squares)
# print(squares2)

million = [num for num in range(1000000)]
# print(f"The min is {min(million)}, the max is {max(million)}, and the sum is {sum(million)}.")

cubes = [num**3 for num in range(1,11)]
cubes.reverse()
print(cubes)

maxcubes = sorted(cubes)[-3:]
print(maxcubes)