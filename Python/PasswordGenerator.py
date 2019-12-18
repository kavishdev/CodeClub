import random   

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=`~\|;:,./<>?'


length = input('Password length?')
length = int(length)
if     (length >= 21):
    print("It's to lengthy.")
    print("please try again....")
    length = input('Password length?')
    length = int(length)
else:
    pass 
no = input('Number of passwords')
no = int(no)
for p in range(no):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print (password)