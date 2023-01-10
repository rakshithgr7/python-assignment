#Assuming that we have some email addresses in the "username@companyname.com" format, write a program to  
# print the company name of a given email address. Both user names and company names are composed of letters only

email="rakshith@gmail.com"
domain=email[email.index('@')+1:]
username=email[:email.index('@')]
print(str(domain))
print(str(username))