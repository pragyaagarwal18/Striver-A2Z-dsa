n = int(input("Enter a number: "))

original = n
digits = len(str(n))
total = 0

temp = n

while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp = temp // 10

if total == original:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
