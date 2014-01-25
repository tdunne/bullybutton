import smtplib

# Specifying the from and to addresses

fromaddr = 'gmailaddress@gmail.com'
toaddrs  = ['recipient1', 'recipient2'] # Can add more recipients in this form

# Create message
print("This will send an email to the moderators of the bullying program.")
name = raw_input("Enter full name: ")
year = raw_input("Enter your year: ")
year = str(year)
msg = raw_input("Enter your message here in one line, hit enter when finished: ")
msg += " - "
msg += name # Append name and year
msg += ", Year "
msg += year


# Gmail Login

username = 'gmailusername@gmail.com'
password = 'gmailpassword'

# Sending the mail  

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
