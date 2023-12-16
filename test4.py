data=[0, 1, 5, 2, 4, 3, 6]

print(data[-6]) # output 1

print(data[1:-2]) # output [1, 5, 2, 4]

print(data[4::-2]) # moving backward [4, 5, 0]

print(data[-7:-3]) # output [0, 1, 5, 2]

print(data[-3:-7]) # output []

print(data[-3:-7:-1]) # output [4, 2, 5, 1]

print(data[-8]) # out of range