#Keep asking the user to input the longest sentence they can without the character “A” 
#Each time a user successfully sets a new longest sentence, print a congratulations message.
longest_sentence = ""
while True:
    sentence = input("Please enter the longest sentence you can without the character 'A' or 'a': ")
    if 'A' in sentence or 'a' in sentence:
        print("Your sentence contains the character 'A'. Please try again.")
        continue
    if len(sentence) > len(longest_sentence):
        longest_sentence = sentence
        print("Congratulations! You've set a new longest sentence!")
    else:
        print("Your sentence is not longer than the current longest sentence. Try again.")