import sys
import time
from funcions import *

logo = """
               /`_>
              / /
              |/
          ____|    __
         |    \.-``  )
         |---``\  _.'
      .-`'---``_.'
     (__...--``     
"""

print(logo)

admincheck = input("Please enter your admin password(Case Sensitive)> ")

if admincheck == password1 or password2 or password3:

	print("\nWelcome to Max's Mafia Terminal, my name is Enigma. How may I assist you?")

	while True:

		print("""
		1)View members
		2)Veiw Sub-Divisions
		3)Veiw Passwords
		4)Update(Have to have Git installed)
		5)Quit
		""")

		affimativenum = str([1, 2, 3, 4, 5])

		mainpromt = input("ENIGMA> ")

		if mainpromt in affimativenum:
			subprocess(mainpromt)
		else:
			print("That is not a valid operation")
			
else:
	sys.exit()

