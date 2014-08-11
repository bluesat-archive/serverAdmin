#!/user/bin/python3

# newBSuser.py
# v1.0.0
# based on newBSuser.sh v2.1.0
# REQUIRES:
#     newBSuser-email.pl
#     newBSuser-sql.exp
#     newBSuser-ssh.exp
#
# Script to create a new user for BLUEsat Unix system, set
# random password (generated internally) for Unix system, add
# user to 'team' group, ssh into orion as the user to sync Samba
# and set https password then email a notification to the
# user's external email (BCCing ss@bluesat for
# confirmation)
#
# Optionally sets up email forwarding to entered email address.
#
# Also tries to remove web password from the newmembers auth file
# for the requested username
#
# Gets data from user input (interactive) for entry into SQL
# database and creation of a new user account.

import string
import getpass
import os
import os.path

######################
# ROOT CHECK
# If not run as root (or sudo'd) exit
ROOTUID = 0
if not os.getuid() == ROOTUID:
   print("This script has to be run by root (or a sudoer)\nExiting due to lack of awesome")
   exit()


# Function set
def validEmail(emailToCheck):
   # if only [a-zA-Z0-9_.\- then true
   for char in emailToCheck:
      if char not in string.ascii_letters+string.digits+"@_.\\":
         return False
   # fell through, all characters valid email character
   return True

def validNumeric(numericToCheck):
   for char in numericToCheck:
      if char not in string.digits:
         return False
   # fell through, all characters valid numeric
   return True

def validAlphabetic(alphabeticToCheck):
   for char in alphabeticToCheck:
      if char not in string.ascii_letters+' ':
         return False
   # fell through, all characters valid alphabetic
   return True

def validAlphaNumeric(alphaNumericToCheck):
   for char in alphaNumericToCheck:
      if char not in string.ascii_letters+string.digits:
         return False
   # fell through, all characters valid numeric
   return True


####################
# Main program
# NEW USER INFO
# Full Name
fullName=input("Enter full name (a-z, A-Z):")
while not validAlphabetic(fullName):
   print("Your name must not be null and may only contain alphabetic\ncharacters and spaces")
   fullName=input("Enter full name (a-z, A-Z):")

# Student ID
studentID=input("Enter student ID Number (0-9 - Don't include the 'z'):")
while not validNumeric(studentID):
   print("Your student number must not be null and may only\ncontain numbers")
   studentID=input("Enter student ID Number (0-9 - Don't include the 'z'):")

# External Email
email=input("Enter an email addresss (account instrutions will be sent)\nto this address:")
while not validEmail(email):
   print("""Your email address has been rejected by the script\n 
         email=input("Enter an email addresss 
         (account instrutions will be sent)\n
         to this address:") 
         If {inputEmail} is correct, inform the admin of the 
         error""".format(inputEmail=email))

# Mobile Number
mobileNumber=input("Enter a mobile number")
while not validNumeric(mobileNumber):
   print("""Your mobile number must not be nulla nd may only\n
      contain numbers""")
   mobileNumber=input("Enter a mobile number")

# Github username
gitHubUserName=input("Enter your github username")
while not validAlphaNumeric(gitHubUserName):
   gitHubUserName=input("Enter your github username")
   #if not valid
   ##

#Skype
skypeUserName=input("Enter a skype username (optional)")
if skypeUserName=="":
   print("No skype username entered")


# Information Check
verifiedDetails = False
print("""The following data has been entered\n
      Name:\t\t\t{fullname}\n
      Student ID:\t\t\t{fullname}\n
      Email Address:\t\t\t{emailAddress}\n
      Mobile:\t\t\t{mobileNumber}\n
      Github:\t\t\t{githubUser}\n
      Skype:\t\t\t{skypeUser}""".format(
         fullname=fullname, emailAddress=email, mobileNumber=mobileNumber, githubUser=githubUserName, skypeUser=skypeUserName))
while not verifiedDetails:
   detailsVerifiedAnswer = input("Is this information correct? [y/n]:")
   if (detailsVerifiedAnswer == "y" or detailsVerifiedAnswer == "yes"):
      verifiedDetails = True
      print("Details verified, Continuing")
   elif (detailsVerifiedAnswer == "n" or detailsVerifiedAnswer == "no"):
      print("Details rejected\nStat the script again...\nAborting now ")
      exit()
   else:
      print("invalid choice, answer yes or no")

# NEW aCCOUNT DETAILS
# Desired Username
desiredUserName=input("Enter desired username (a-z - Will be tolower'd")
while not validAlphabetical(desiredUserName) or :
   desiredUserName=input("Enter desired username (a-z - Will be tolower'd")
   # checking the home directory on server for desired username doesn't already exist
   if not os.path.exists("/home/{userName}".format(userName=disiredUserName)):
      print("This user name is free")
   else:
      print("The user name:{userName} is taken".format(userName=desiredUserName))
      desiredUserName=""
      continue

      
# Desired Password
print("""READ THIS!\n
You are about to enter a password into an unsecure script.\n
If you have issues with this, leave this field
blank and a random password will be generated and sent
to you via email.\n"""
desiredPassword = getpass.getpass("Enter a password")
if desiredPassword="":
   print("""Generating a random password. 
   You will receive the password\n
   via email""")
   # produce random password
else:
print("Enter again to verify:")
   
# Email Forwarding
while:
   emailForwardingChoice=input("Whould you like to set up email forwarding [y/n]?")


#################################### 
# CREATE ACCOUNT
# Run user creation after check that user does not eist again

os.system("sudo adduser --disabled-login --quiet {name}".format(name=desiredUserName))
os.system("sudo aduser {name} team".format(name=desiredUserName))
os.system("sudo echo {name}:{password} | chpasswd".format(name=desiredUserName , password=desiredPassword)
os.system("echo {name}@bluesat.unsw.edu.au | sudo var/lib/mailman/bin/ad_members -r - -w y -a n team".format(name=desiredUserName))
os.system("/usr/bin/htpasswd -D /etc/apache2/auth/newmembers {name}".format(name=desiredUserName))
os.system("/usr/bin/htpasswd -bm /etc/apache2/auth/members {name} {password}".format(name=desiredUserName , password=desiredPassword ))

# Crate email forwarding file
# CHECK THIS WILL WORK CORRECTLY
if forwarding:
   os.system("echo \# Exim Filter > /home/{name}/.forward".format(name=desiredUserName))
   #os.system("echo ")
   os.system("echo unseen deliver {email} >> /home/{name}/.forward".format(email= , name=desiredUserName)
   os.system("chown {name}:{name} /home/{name}/.forward".format(name=desiredUserName))

# SSH  in to enable accoutn
os.system("""/root/bin/newBSuser-ssh.exp {password} pegasus {userName} "id -u" """.format(userName=desiredUserName, password=desiredPassword))

####################
# SEND EMAIL
# Send accoutn creation email to user's external and new internal email
print("Sending Account Creation Email for {user}".format(user=desiredUserName))
os.system(" sudo /root/bin/newBSuser-sql.exp {fullname} {userName} {mobile} {studentID} {github} {skype}".format(fullname=fullname, userName=desiredUserName, mobile=mobileNumber, studentID=studentID, github=githubUserName, skype=skypeUserName))

print("User Information Saved\nAccount Creation Complete")
exit()

      
   
