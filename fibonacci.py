def fib(index):
    print([0, 1, 1, 2, 3, 5, 8, 13, 21])
    print(' 0, 1, 2, 3, 4, 5, 6, 7,  8')
    arr = [0,1]
    for i in range(2, index+1):
        next = arr[i-2] + arr[i-1]
        arr.append(next)
    print(arr[index])

fib(7)