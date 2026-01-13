string = input("Enter a string: ")
result = ""

for i in range(len(string)):
        letter = string[i]
        
        if i == 0:
                result = result + string[i]

        else:
                if string [i] != string[i-1]:
                        result = result + string[i]
print(result)