def bubblesort(dataset):
    for x in range(1, len(dataset)):
        while x > 0:
            if dataset[x] < dataset[x-1]:
                swap(dataset, x, x-1)
                x -= 1
            else:
                break
            
def insertionsort(dataset, printflag):
    if printflag:
        print(dataset)
    for index in range(len(dataset)):
        minindex = index
        for x in range(index+1, len(dataset)):
            if dataset[x] < dataset[minindex]:
                minindex = x
        if index < minindex:
            swap(dataset, index, minindex)
            print(f"swapping index {index} and {minindex}.")
    if printflag:
        print(dataset)       

def findminindex(dataset, start, end):
    minindex = start
    for x in range(start+1, end):
        if dataset[x] < dataset[minindex]:
            minindex = x
    return minindex
        
def swap(data, x, y):
    temp = data[x]
    data[x] = data[y]
    data[y] = temp
    
numbers1 = [5, 4, 3, 2, 1]
numbers2 = [7, 4, 3, 1, 6, 5, 2]
numbers3 = [3,1,5,4,26,11,6,9,31,44,2,57,53,44,99,10,12,7]

insertionsort(numbers3, True)
