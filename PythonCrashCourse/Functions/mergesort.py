def mergesort(dataset):
    # copy = dataset[:]
    recursivemerge(dataset, 0, len(dataset)-1)
    
def recursivemerge(data, start, end):
    print(data, start, end)
    if end - start <= 1:
        if data[end] < data[start]:
            print('swappin')
            temp = data[end]
            data[end] = data[start]
            data[start] = temp
    else:
        middle = (end - start) // 2
        print(f'recursin, first from {start} to {middle}')
        recursivemerge(data, start, middle)
        recursivemerge(data, middle+1, end)
        
data = [9,8,7,6,5,4,3,2,1,0]
mergesort(data)