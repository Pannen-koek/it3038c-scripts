import os
import platform

#Stores the currently logged in user
user = os.getlogin()

#Gets Information on the OS
currentOS = platform.system()


print ('This computer is running', currentOS)
print ('The current User is', user)