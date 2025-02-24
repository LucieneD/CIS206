
#Load names into file
with open (r'C:\Users\lucie\OneDrive\Desktop\names.txt', 'r') as file:
    names = {line.strip() for line in file}

#open names file
with open ('notfound.txt', 'a') as not_file:
    while True:
        username = input("Enter a name ")

        if username.lower() == 'exit':
            print ("This program will now exit")
            break
        if username in names:
            print (f"{username} is in the file.")
        else:
            print (f"{username}is not in file. Adding to notfound.txt")
            not_file.write(username + '\n')

