password = input("Enter your password: ")
password_strength = 0
password_category = {0 :"very bad password",
                     1 :"bad password",    
                     2 :"normal password",
                     3 :"good password",
                     4 :"very good password"}

if len(password) >= 16:
	password_strength += 2
elif len(password) > 8:
	password_strength += 1
if password.isdigit():
	pass
elif password.isalpha():
	pass
elif (not password.isupper() and not password.islower()):
	password_strength += 2
else:
	password_strength += 1

print(password_category[password_strength])