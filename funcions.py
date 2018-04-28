import sys
import time

f = open("passwords","r")
lines = f.readlines()
password1 = lines[0]
password2 = lines[1]
password3 = lines[2]
f.close()

def subprocess(number):
	if number == "1":
		
		member = ['Christian Bunge', 'Max Fernald']
		
		maya = """
                  _____
                 _|[]_|_
               _/_/=|_\_\_
             _/_ /==| _\ _\_
           _/__ /===|_ _\ __\_
         _/_ _ /====| ___\  __\_
       _/ __ _/=====|_ ___\ ___ \_
     _/ ___ _/======| ____ \_  __ \_
     """
     
		print(maya +"\nWelcome to Maya Member Editor. Here are the current members:\n")
		
		for person in member:
			print(person)
			
		print("\nIf you would like to add or remove someone, please ask Christian.")
		
		time.sleep(7.5)
			
	elif number == "2":
		
		subgroups = ["Eamon's Subgroup", "Dylan's Sub-Subgroup"]
		
		sparrow = """      
			        _
                 .'` '`.
              .-", @ `, `.
             '-=;      ;   `.
                 \    :      `-.
                 /    ';        `.
                /      .'         `.
                |     (      `.     `-.._
                 \     \` ` `. \         `-.._
                  `.   ;`-.._ `-`._.-. `-._   `-._
                    `..'     `-.```.  `-._ `-.._.'
                      `--..__..-`--'      `-.,'
                         `._)`/
                          /  /
                         /--(
                      -./,--'`-,
                   ,^--(                     
                   ,--' `-,
		"""
		
		print(sparrow)
		
		print("Welcome to Sparrow Subgroup Veiwer. Here are the current subgroups.\n")
		
		for groups in subgroups:
			print(groups)
			
		print("\nAsk Christian to add new subgroups.")
		
		time.sleep(7.5)
		
	elif number == "3":
		
		f = open("passwords","r")
		lines = f.readlines()
		f.close()
		
		pie = """
        _,..---..,_
    ,-"`    .'.    `"-,
   ((      '.'.'      ))
    `'-.,_   '   _,.-'`
      `\  `'''''`  /`
        `""-----""` """
		
		print(pie)
		
		print("Welcome to Pie Password Veiwer. Here are all the current passwords:\n")
		
		print(password1 + password2 + password3)
		
		print("Ask Christian to add or remove passwords.")
		
		time.sleep(7.5)
		
	elif number == "4"
 
#subprocess("3")
                          
		
		

		

		
	
