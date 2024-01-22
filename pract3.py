import random 
lenght=int(input('enter the password length')) 
i=1
password='' 
a='abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()' 
while i<=lenght: 
    password=password+random.choice(a)  
    i=i+1 
print('password is: ',password) 
