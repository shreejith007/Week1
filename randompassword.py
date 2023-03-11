import random
letters =['a',"b",'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number =['1','2','3','4','5','6','7','8','9','0']
characters=['!','@','#','$','%','^','&','*','(',')','-','+','=','/','*',':',';','`']
nr_letters=int (input("how many letters would u like to add"))
nr_number=int(input("how many numbers would u like to add"))
nr_characters=int(input("how maany charaters would you like to add"))

password =""
for char in range(1,nr_letters+1):
   random_char = random.choice(letters)
   password += random_char
   
   
for char in range(1,nr_number+1):
   password +=random.choice(number)

for char in range(1,nr_number+1):
  password += random.choice(number)
   
print(password)
   
   