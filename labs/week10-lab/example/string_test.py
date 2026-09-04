password = input("Insert your password : ")
length = len(password)
words = password.split('@')

if len(words) > 1 and password.count('@') == 1:
    left = words[0].isalnum()
    right = words[1].isalnum()
else:
    left = False;
    right = False;

if length >= 8 and len(words) == 2 and left == True and right == True:
    print("Your password is strong!")
else:
    print("Your password is not strong!")