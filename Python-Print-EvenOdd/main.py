lis = []
even = []
odd = []
print("Enter 10 Digits to extract even and odd between them : ")
for i in range(0, 10):
    num = (int(input()))
    lis.append(num)

print("Even numbers is: ")
for num in lis:
    if num % 2 == 0:
        print(num, end=" ")

print("\nOdd numbers is: ")
for num in lis:
    if num == 1 or num % 3 == 0:
        print(num, end=" ")