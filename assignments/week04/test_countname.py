# นับว่ามีสระกี่ตัว (a,e,i,o,u)

# input username Ex. Patcharapon
name = str(input("What is Your name?: "))
# process 
count = 0
for letters in name:
    if letters == 'a' or letters == 'A':
        count += 1
    elif letters == 'e' or letters == 'E':
        count += 1
    elif letters == 'i' or letters == 'I':
        count += 1
    elif letters == 'o' or letters == 'O':
        count += 1
    elif letters == 'u' or letters == 'U':
        count += 1


if letters in ['a' , 'e' , 'i' , 'o' , 'u' , 'A' , 'E' , 'I' , 'O' , 'U']
    count += 1
# output You value is 4 
print(f"Your value in your name is: {count}")