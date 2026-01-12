#Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
my_name = "Adnane"
while True:
    user_name = input("What is ur name? ")
    if user_name == my_name:
       print(" Fin a 3chi4i " + user_name) 
       break
else:
        print("You are not " + my_name + ", try again.") 
    