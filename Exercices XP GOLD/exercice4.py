names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
#Ask a user for their name, if their name is in the names list print out the index of the first occurrence of the name.
user_name = input("Please enter your name: ")
if user_name in names:
    index = names.index(user_name)
    print(f"Your name is found at index: {index}")