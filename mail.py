"""Copyright 2014 Tim Dunne

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License."""
import smtplib
import random
# Create a random number to be used as an ID number for each message
id = random.getrandbits(30)
id = str(id)

# Specifying the from and to addresses
fromaddr = 'fromaddress@gmail.com'
toaddrs1  = 'studentmoderators@gmail.com' # To add more emails, se the format ["email1@gmail.com', "email2@gmail.com"] etc
toaddrs2 = 'teachers@gmail.com'
# Create message
print("This will send an email to the moderators of the bullying program.")
name = raw_input("Enter full name: ")
while not name:
    name = raw_input("Please enter full name: ")
year = raw_input("Enter your year: ")
while not year:
    year = raw_input("Please enter your year: ")
year = str(year)
msg = raw_input("Enter your message here in one line, hit enter when finished: ")
message = "#" + id + ": " + msg
msg1 = msg
msg1 += " - "
msg1 += name # Append name and year
msg1 += ", Year "
msg1 += year
message1 = "#" + id + ": " + msg1

# Gmail Login

username = 'account@gmail.com'
password = 'password'

# Sending the mail
try: # attempt to send emails
    # msg 1, no name or year - confidential
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs1, message)
    server.quit()
    
    # msg 2, name and year - sent to teachers
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs2, message1)
    server.quit()

    print("Message sent successfully. Your report will be reviewed as soon as possible.\nIf you require more immediate assistance:")
    print("Kids Help Line - www.kidshelp.com.au or call 1800 55 1800 (free call)\nbeyond blue - www.beyondblue.org.au\nLifeLine - www.lifeline.org.au or call 13 11 14")
except: # Message sending failed for some reason.
    print("Message sending failed. Please check your internet connection and try again.")
    print("Alternatively, if you require more immediate assistance:\nKids Help Line - www.kidshelp.com.au or call 1800 55 1800 (free call)\nbeyond blue - www.beyondblue.org.au\nLifeLine - www.lifeline.org.au or call 13 11 14")
