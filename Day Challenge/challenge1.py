number = input("Enter a number: ")
length = input("Enter the desired length: ")
multiples = []

for i in range(1, int(length) + 1):
        multiples.append(int(number) * i)
print(multiples)

