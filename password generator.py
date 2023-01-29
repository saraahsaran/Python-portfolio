import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
total=int(input("Enter total characters you need to create passsword:"))
letter_ip=int(input("How many letters u want:"))
number_ip=int(input("How many numbers u want:"))
symbols_ip=int(input("How many symbols u want:"))
Total_string=" "
if total==(letter_ip+number_ip+symbols_ip):
  for count in range(1,total+1):
    if (count<letter_ip+1):
       Total_string=Total_string+random.choice(letters)
    if(count<number_ip+1):
       Total_string=Total_string+random.choice(numbers)
    if(count<symbols_ip+1):
       Total_string=Total_string+random.choice(symbols)
  print(f"Your password is {Total_string}")
else:   
  print("Mismatch of inputs")      
