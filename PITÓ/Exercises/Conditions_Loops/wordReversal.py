word = input("Write the word to reverse: ")

for char in range(len(word)-1,-1,-1): #dont get the -1
    print(word[char],end="")          #and the end=""