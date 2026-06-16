n = int(input("Enter a number: "))

count = 0
temp = n

while temp > 0:
    count += 1
    temp //= 10

print("Number of digits:", count)
