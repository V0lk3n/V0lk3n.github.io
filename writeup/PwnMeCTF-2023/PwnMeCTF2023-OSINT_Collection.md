---
title: PwnMeCTF 2023 - OSINT Collection
author: V0lk3n
tags: CTF, PwnMeCTF, OSINT, footprint, google, CyberSecurity
---

# PwnMeCTF 2023 - OSINT Collection

<p align="center">
	<img src="https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/5e970f73-af08-4964-a845-1cf64c3950ad">
	<img src="https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/67a48c63-99b8-4985-8118-a7093adf6773">
</p>

> Written by [V0lk3n](https://twitter.com/V0lk3n)

## Author Note

```
Well, few quick lines to said that i've never explored an OSINT challenge of that quality. 
It is so big and so nice!

I'm really thanksfull to the PwnMeCTF Staff! Thanks for all!

About my Write-Up, while the CTF was runing i was able to flag the 3 first challenge of that collection which contains 5 challenges. 
At the end of the CTF, i've continued it to fully complete it.

Sadly i've been spoiled on discord shortly after the CTF ended, regarding two little thing. 
So this helped me a bit to flag, but ive tried to act like i've never read those spoil.

Thanks again for all! And special thanks to Ganko for the OSINT collection creation! 

I hope you will enjoy my writeup!

- V0lk3n
```



## Table of Contents

* 1.0 [Social Media Goes Brrrr](#SocialMedia)
* 2.0 [Newbie Dev](#NewbieDev)
* 3.0 [French Dream](#FrenchDream)
* 4.0 [Europe](#Europe)
* 5.0 [AmericanDream](#AmericanDream)
* 6.0 [Credits](#Credits)



## Social Media Goes Brrrr<a name="SocialMedia"></a>

Difficulty : **Intro**

Final Value : **50 pts**

Description :

```
[EN] Context explanation: John Droper is a Franco-British individual who leaves an enormous digital footprint. 

(Note: He speaks both English and French, and some information can only be found through one of these languages.) 

First Step : - You have to find one of his main social media 



[FR] Explication du contexte : John Droper est une personne franco-anglaise qui laisse une empreinte numérique énoooooorme. 

(Indication : il parle donc anglais et français, certaines informations ne se trouvent que grâce à une des langues) 

Première étape : - Il faut trouver un de ses réseaux sociaux principaux
```


### Solution 

We only got three informations. The first is his first and last name which is "John Droper". The second is the goal to find his main social media. The third, we know that he is franco-british, he speak both language, and some informations can only be found through one of these.

As we know. Generally, for everyone, the main Social Media would be Facebook, or maybe Twitter or Instagram.

Let's start to search John Droper on facebook.

![1-John_Facebook](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/ef8826fe-bc5d-4329-a18b-fe969ab30bbf)

We notice few profil that match the name, but only one had a Profil Picture which seem too "fake", and in fact, should be our target.

Once our suspect profil opened, we notice three french posts.  It seem to be the right profil, let's have a look to his profil informations.

![2-Facebook_Details](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/96c96a44-0394-4947-bc37-d58186689b18)

Great! We got the flag and a pseudo which is :

```
jdthetraveller
```

Apparently they removed the flag format "PWNME", this is good to unallow us to retrieve it with google dorks like :

```
allintext:"PWNME{"
```

Also, if we attempt to decode the flag from base64, it return us the strings bellow :

```
$ echo "TG9uZyBsaXZlIHRoZSB0cmFpbnMsIGxvbmcgbGl2" | base64 -d
Long live the trains, long liv
```

Which is the beginning of the same sentence from Shakespear found on the John Droper Facebook profil details.

We only need to replace the flag format.

```
FLAG : PWNME{TG9uZyBsaXZlIHRoZSB0cmFpbnMsIGxvbmcgbGl2}
```



## Newbie Dev<a name="NewbieDev"></a>

Difficulty : **Easy**

Final Value : **50 pts**
Description :

```
[EN] For the context of the challenge, please check the introduction challenge's description 

John is a newbie dev, please find informations about this new passion not very developed 



[FR] Pour comprendre le contexte du challenge, regardez la description du challenge d'introduction 

C'est un développeur en herbe, trouvez des infos sur cette passion pas très développée
```

Collected Data :

```
Pseudo : jdthetraveller
Facebook : https://www.facebook.com/profile.php?id=100091409530073
```


### Solution

In this challenge, we know that John is a newbie dev, and we need to find informations about this.

As we seen previously on the facebook profil details (look at the previous picture), he said that he has a website that he doesn't like to give to anyone, and apparently we have enough informations to find it.

Go back to his Facebook profil, looking at his friends show nothing fabulous, excepted that he is friend with "Modération 18-25".

![3-0-Facebook_Friends](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/94e807dd-c5a9-4f10-a520-17ec608b7e1a)

Go to the profil, there is the forum linked.

```
https://www.jeuxvideo.com/forums/0-51-0-1-0-1-0-blabla-18-25-ans.htm
```

A fast reasearch of Author named ```jdthetraveller```, and we found a post.

![3-1-JV_Location](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/493da1a5-efea-4b3d-be4f-da2362e39787)

```
https://www.jeuxvideo.com/forums/42-51-72118292-1-0-1-0-voyage-en-europe.htm
```

![3-2](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/5f66dcc8-6383-4adb-86c5-4a13fe513a43)

Nothing relevant for our challenge at this moment, let's take a look later.

Come back to the Facebook account. Looking at what he published, show three french posts.

![3-Facebook_posts](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/d0c4f697-847d-4006-9555-8f3181528316)

In posting order, the first one said that he finally registered to his new favorite forum, with a train emoji. Also he said that he will talk about its trip there, and we all know his passion for travel.

The second, he's complaining that, even when he is at his home, he cannot access it's favorite bar, because the director of the bar is his ex-girlfriend.

The third and last, said that it's pseudo (jdthetraveller) was available with ```AFNIC```. He took "it" for a while, but as he is travels a lot, he hasn't the time to work on it. Also he is a really bad dev which do a lot of misconfiguration.

As we need to find information about his "dev side". Let's focus on the third post.

Google ```AFNIC``` and we found a company website used to register ```.fr, .re, .pm, .yt, .wf, .tf```domain names.

![4-AFNIC](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/68743fc3-06eb-47b2-aca1-14b55ed257c8)

As we know, John is franco-british and he said that he took his pseudo on it. So we try to guess the domain name ```jdthetraveller.fr```

![5-website](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/e39ebe87-8a2e-4f2d-aaa2-b58d0573600b)

Our guess was exact, we found John Droper website.

Let's start a basic recon.

First, we seen the Twitter, Facebook and Instagram logo. Which mean that he should have an account on those plateform. But the links are not yet included on the website.

Second, we found a part of his email address, which apparently is a "gmail.com" address. Reading the code source return nothing relevant.

Let's do a basic nmap scan focus on port 80 and 443.

```bash
$ nmap -A -p 80,443 jdthetraveller.fr
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-08 16:35 CEST
Nmap scan report for jdthetraveller.fr (13.48.131.55)
Host is up (0.036s latency).
rDNS record for 13.48.131.55: ec2-13-48-131-55.eu-north-1.compute.amazonaws.com

PORT    STATE SERVICE  VERSION
80/tcp  open  http     nginx 1.18.0
|_http-server-header: nginx/1.18.0
|_http-title: Did not follow redirect to https://jdthetraveller.fr/
443/tcp open  ssl/http nginx 1.18.0
| http-git: 
|   13.48.131.55:443/.git/
|     Git repository found!
|     Repository description: Unnamed repository; edit this file 'description' to name the...
|     Remotes:
|_      https://github.com/droperkingjohn/myOwnWebsite.git
| ssl-cert: Subject: commonName=jdthetraveller.fr
| Subject Alternative Name: DNS:jdthetraveller.fr, DNS:www.jdthetraveller.fr
| Not valid before: 2023-04-10T14:15:39
|_Not valid after:  2023-07-09T14:15:38
|_http-title: John Droper's Curriculum
|_http-server-header: nginx/1.18.0
|_ssl-date: TLS randomness does not represent time

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 19.32 seconds
```

We see that the port 80 redirect to port 443. 

A ```.git``` repository is found, with it's corresponding remote repository which also give us a new pseudo ```droperkingjohn```.

```
https://github.com/droperkingjohn/myOwnWebsite.git
```

Go to the remote github repository. We found the source of his website. Also, we can see fourth commits, this should be interesting.

![6-commits](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/ed5b128c-e3a6-4a75-a368-4ec79f6cc544)

In chronological order, the first commit is a License addition.

The second commit is interesting, it show us the old presentation that he was referring to on its website home page.

```html
<body>
	<h1>John Droper's website</h1>
	<br>
	<br>
	<p>I will edit my curriculum later but this is some informations about me :</p> <br>
	<p>- I could be pro with my team but you know... (cruciate ligament rupture...) => https://www.tgb-basket.com/<br>- If you've already met me, you know that I love travelling, this is one of my new favorite forum (i'm not really active but recently I shared informations about my trip in Europe) =>  https://www.forum-train.com/forum/index.php</p>

	<hr style = "border:none;margin-bottom:20%">
	<p class="semiSecret">You can contact me :<br>johndroperdroperjohn@gmail.com<br>(links are not up for the moment sorry...)</p>
	<div class="logosRS">
		<img src="./twitter.png" sizes="30px"/>
		<img src="./facebook.png"/>
		<img src="./instagram.png"/>
    <!-- No copyright but => https://github.com/droperkingjohn -->
	</div>
</body>
```

On this commit we found a lot of informations, let's collect them :

```
His basket team website : 
https://www.tgp-basket.com/

His new favorite train forum (remember the emoji and facebook post) :
https://www.forum-train.com/forum/index.php

The fully revealed gmail address :
johndroperdroperjohn@gmail.com
```

On the third commit, he remove those previously obtained informations.

On the fourth commit, he remove the license and add a comment with the flag.

![7-flag](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/5d3b55aa-512a-4ec1-a744-d9340935b670)

```
FLAG : PWNME{W0w_th15_l00k_l1ke_4n_e4sY_Fl4G}
```



## French Dream<a name="FrenchDream"></a>

Difficulty : **Medium**

Final Value : **185 pts**

Description :

```
[EN] For the context of the challenge, please check the introduction challenge's description Description: 

John is Franco-English but he lives in France and his life is almost entirely available on the internet. 

Find the city where he lives, the username of his current girlfriend and the birth name of his ex. 

The OSINT must remain passive and any interaction is strongly prohibited. No need to get in touch with anyone to solve the challenge. 

Flag Format: PWNME{lille_elonmusk_halliday} 
All lowercase with "_" to separate information. 



[FR] Pour comprendre le contexte du challenge, regardez la description du challenge d'introduction Description : 

John est franco-anglais mais il vit en France et sa vie est presque disponible entièrement sur internet. 

Trouvez la ville où il habite, le username de sa copine actuelle et le nom de naissance de son ex. 

L'OSINT doit rester passif et toute interraction est fortement proscrite. Nulle nécessitée de rentrer en contact avec qui que ce soit pour résoudre le challenge. 

Flag Format : PWNME{lille_elonmusk_halliday} 
Tout en minuscule avec des "_" pour séparer les informations.
```

Collected Data :

```
Pseudo : jdthetraveller
Email : johndroperdroperjohn@gmail.com
Site : https://jdthetraveller.fr
Forum Train : https://www.forum-train.com/forum/index.php
Forum 18-25 : https://www.jeuxvideo.com/forums/42-51-72118292-1-0-1-0-voyage-en-europe.htm
Basket Team : https://www.tgp-basket.com/
GitHub : https://github.com/droperkingjohn
Facebook : https://www.facebook.com/profile.php?id=100091409530073
````


### Solution

Here we know that he live in France, we need to find in which city he live, his girlfriend username and the birth name of her ex girlfriend.

As the website hint us, there should be an Instagram and Twitter account somewhere. Let's investigate the new previously collected data.

I've refered to the ```Ozint``` website. As they are one of the CTF sponsor, i would have a better chance to find the needed tools.

```
https://ozint.eu/
```

First i will focus on the pseudo. Once registered on Ozint, i look at the toolbox under account section.

> Note : You need to be registered to access the toolbox

![8-ozint](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/d3050278-b053-405d-80d1-2b07bb7d88f1)

~Be lazy, be like me...~ I took ```WhatsMyWeb``` tool, because it's the only one Online tools, i alway start by this to get faster research then digg deeper manually or with some script tools if needed.

```
https://whatsmyname.app/
```

I use the tool against the pseudo ```droperkingjohn```, i know that i can put more than one entry. But i prefere to focus item by item.

![9-whatmyweb](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/ccaee0c1-e66d-4132-bc0a-3fb9aa089cf7)

Great! We found it's Twitter account, and apparently, web archive saved something about it.

```
Twitter : https://twitter.com/droperkingjohn
Twitter Wayback : https://web.archive.org/web/2/https://twitter.com/droperkingjohn
```

Going to his twitter account, we found few posts.

In scroll order, the first is a picture of a dog that he was close to adopt while traveling in USA. Seem not relevant for our challenge yet.

The second is a cypher. This part of the challenge is broken, but let's do it anyway.

![11-pigpen](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/6f41257b-1a3c-4e5c-9bd9-465fd4fcbc24)

As this is not my first CTF, i was already aware of this type of cipher, which is ```Pigpen Cipher```. But to identify this one, just google something like "Cipher symbols", and you should found it easily.

Go to dcode and decode the cipher.

```
https://www.dcode.fr/pigpen-cipher
```

![12-pigpen_cracked](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/438afc4c-4cd6-46d9-921b-6466aaa77828)

We got an URL youtube, look any youtube video to get one URL as exemple, and fix it's formating. 
Now there is two things to note. The id will be full caps, and this is wrong. The second is, the url is wrong.

So if we get the correct URL (which is not the case, but it is bellow), we should get this :

```
https://www.youtube.com/watch?v=DQW4W9WGXCQ
```

We need to research it as a google research, and not direct link because we doesn't know which character of the ID are upercase or lowercase.

![13-rickroll](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/5627366f-73f8-4a11-a989-020af702cbe0)

What a sad failed rick roll attempt :(

Let's come back to twitter, the next post after the pigpen cipher, he is saying that he would like to travel, and he is asking for suggestions.

The last post, he said that he love travel, whether united states or europe (his both recent travel), but he really would adopt a dog to follow him. Apparently, he didnt have his wife anymore.

Then in comment of that post, it's a direct message to his wife sying that he love her, but she doesnt like travels as much as his ex girlfriend.

In fact, if there is a direct message on Twitter for his wife, we can deduce that maybe, his wife had a Twitter account. Let's take a look at his followers.

![10-TwitterFriends](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/59eb48f5-b66b-49b1-b24a-3d1a7263dd18)

We found an user called ```Blanche Archambault``` with the username ```BlancheLoveJD```.

![14-Blanche](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/7fe74ea7-44e9-4375-b293-1e643559c2b6)

Great! We found John wife username and get one part of the flag.

```
Pre-Flag : PWNMECTF{?????_blanchelovejd_?????}
```

Now, there is nothing useful on the twitter account for now. So let's try to find his Instagram. Looking at script tools from ```Ozint```. I've selected the tool called ```Blackbird```.

![15-Email](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/5606b926-7294-475e-ab67-ea6a7e19fdf9)

```sh
$ python blackbird.py -u "droperkingjohn"

    ▄▄▄▄    ██▓    ▄▄▄       ▄████▄   ██ ▄█▀ ▄▄▄▄    ██▓ ██▀███  ▓█████▄ 
    ▓█████▄ ▓██▒   ▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█████▄ ▓██▒▓██ ▒ ██▒▒██▀ ██▌
    ▒██▒ ▄██▒██░   ▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒██▒ ▄██▒██▒▓██ ░▄█ ▒░██   █▌
    ▒██░█▀  ▒██░   ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒██░█▀  ░██░▒██▀▀█▄  ░▓█▄   ▌
    ░▓█  ▀█▓░██████▒▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▓█  ▀█▓░██░░██▓ ▒██▒░▒████▓ 
    ░▒▓███▀▒░ ▒░▓  ░▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░▒▓███▀▒░▓  ░ ▒▓ ░▒▓░ ▒▒▓  ▒ 
    ▒░▒   ░ ░ ░ ▒  ░ ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░▒░▒   ░  ▒ ░  ░▒ ░ ▒░ ░ ▒  ▒ 
    ░    ░   ░ ░    ░   ▒   ░        ░ ░░ ░  ░    ░  ▒ ░  ░░   ░  ░ ░  ░ 
    ░          ░  ░     ░  ░░ ░      ░  ░    ░       ░     ░        ░    
        ░                  ░                     ░               ░      

                                        Made with ❤ by p1ngul1n0

[!] Searching 'droperkingjohn' across 582 social networks
[+] - #1 Facebook account found - https://www.facebook.com/droperkingjohn [200 OK]          
[+] - #12 Github account found - https://github.com/droperkingjohn [200 OK]                 
   |--Name:                                                                                 
   |--Nickname:           droperkingjohn                                                    
   |--picture: https://avatars.githubusercontent.com/u/131888528?v=4?s=400                  
[+] - #3 Twitter account found - https://nitter.net/droperkingjohn [200 OK]                 
   |--Name: J*hn Drop*r                                                                     
   |--Member since: 4:34 PM - 30 Apr 2023                                                   
   |--picture: https://nitter.net/pic/pbs.twimg.com%2Fprofile_images%2F1652714074818465793%2FtNg4HM3L.jpg                                                                               
[+] - #16 Twitter Archived account found - http://archive.org/wayback/available?url=https://twitter.com/droperkingjohn [200 OK]                                                         
[+] - #7 Instagram account found - https://www.picuki.com/profile/droperkingjohn [200 OK]   
   |--Name: John Dr*per                                                                     
   |--Bio:             Long live the trains, long live the trains and all the journeys, journeys are the best thing that man has invented.                                              
My Love B. A.                                                                               
   |--Followers: 34                                                                         
   |--Following: 4                                                                          
   |--picture: https://cdn1.picuki.com/hosted-by-instagram/q/0exhNuNYnjBcaS3SYdxKjf8K2fRyWg9SZ60STLepjSVmIR1vLHOapZA0mpCj4yRwKwVlASudYzxk54gqV15XCT14PEPWQbaIRD1U5qSZUejN1Tdi8ZBkkb4xKncXZ3at8cosXAmYdSgIGaYDG7uo+qhT5aGuO1lGpzaSfLVHmHBtv8CbULYo2ZIv7LaCjl+o54Mwd3AYvGglKkAmscnbrSgLUbrzPcMymq90ebQNnppUu76opCu7LmIieDN5MAjHtbrjjeg5tALQOSce1TmqAaw||IhE||qnCKkRM6kK0PqaTkN45vhKl15ObYRDtXD1NKoTB3hr+RnAXEWkqbjUV||7WT2lIOUWccp8aL7JturR||HO||zCUQ4HpWfYZW3sYRvPTDgmIddbhUOsB0LRBH8dd3lrooFXoduP1.jpeg
[+] - #462 Salon24 account found - https://www.salon24.pl/u/droperkingjohn/ [200 OK]
[+] - #312 GitHub account found - https://github.com/droperkingjohn [200 OK]
[+] - #522 Twitter archived profile account found - http://archive.org/wayback/available?url=https://twitter.com/droperkingjohn [200 OK]                                                
[!] Search complete in 20.2 seconds
[!] Results saved to droperkingjohn.json
```

As expected we found an Instagram account through Picuki website, we will come back to this later. For now, let's go on Instagram directly, find our user "droperkingjohn".

```
https://www.instagram.com/droperkingjohn/
```

There is a story, once looking at it we can see a Basketball team, a match about it, a meet up after the match to a bar with a strings with numbers.

![16-InstagramStory](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/217e1a99-4890-4dcc-8bda-3fb8065468a8)

As the number seem to repeat each time themself, and they never exceed four character, i guessed that we should be able to decode it with an old T9 Numpad.

You can help you to decode it through T9, but its easier manually.

```
https://www.dcode.fr/phone-keypad-cipher
```

Once deciphered you get the following sentance :

```
Direction nord, le long de la rivière, premier bar.
```

Which mean :

```
Direction north, along the river, first bar.
```

Now, we know that the Instagram story with the T9 cipher is a meetup to that bar after the match. 

The idea is to locate where happen those basketball matchs, locate them on Google Maps and then, from there, go to the north along the river and the first bar should be our answer.

Remember on facebook, his post complaining about the bar. He said that the director is his ex. So our 2th part of the flag shouldn't be far.

Also, the basketball team website was shared on one of the GitHub commit. Let's take a look.

```
https://www.tgb-basket.com/
```

Once on the site, i've acted like a regular user. So i look how to took a ticket (because generally the ticket would said for which match, where and when). Clicking on "Billetterie" redirect us to the ticket purchase website.

```
https://tgb.ticketchainer.com/
```

I noticed that each match happen at the same location (maybe i was lucky, if it's the case, you should maybe use WayBackMachine to retrieve the match place approximatively at the time of his GitHub commit as example)

Here is the location of the match.

```
Palais des sports du quai de l’Adour
```

![17-MatchPlace](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/ade33733-6feb-4f66-ac67-1fce99723520)

Now let's go on Google Maps locate this place. Then follow the sentance ```Direction north, along the river, first bar```.

![18-GoogleMaps](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/64a048fd-1d14-4b54-bca5-cac8e8d7d9a9)

The bar is ```Bar le landais```.

Now we need to find the director of the bar. So let's google it.

One of the top result is, the website ```PagesJaunes```. Which is, a well known french website of telephone directories. We can find a lot of information such as Address, email, name, organization and more.

![19-PagesJaunes](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/2ea23677-7713-4442-a206-d4b190ede581)

Now go to the site, and look at the contact section.

```
https://www.pagesjaunes.fr/pros/05722827
```

![20-Patronne](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/a1cfeca0-459e-4c2b-9d31-6c7f3dc7018c)

We found the name "Patricia Caussade", a quick look to facebook, and we found a matching person from Tarbes (where the bar come from). Also, she work as "bar trader". 

![21-ExFacebook](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/0543f6a3-e2dd-480c-959d-e1e563b9b386)

```
https://www.facebook.com/patricia.caussade.5
```

Her full name is ```Patricia Caussade Ghestem```.

We got the 2th part of the flag which is ```Ghestem```.

```
Pre-Flag : PWNMECTF{?????_blanchelovejd_ghestem}
```

The last part of the flag will be the city where John live.

Go back to his instagram account. We can see two posts, the first post, had as first picture the united states flag and map. On this one the description is interesting, John is saying that after his trip in the entier world, it was nice to do a barbecue with his friends at home. Also, the post location is set to ```Home Sweet Home```.

![22-InstagramPost1](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/f6013734-99b5-4a23-922f-dc62d78d7cc8)

In fact, we know that, while writing this post John was at home. Looking at the other pictures of the post, we notice two things. There is a purchase ticket, but nothing relevant at first look. 

The second thing is the photoshoped picture with the face of John and Blanche. Blanche seem croped, and then i remembered that once publishing a picture on instagram, the app generally ask to select a zone of the picture to post, then you only see this selected part of the picture.

Now, let's return in our previsouly collected data. And look at the instagram account through the ```Picuki Website```.

```
https://www.picuki.com/profile/droperkingjohn
```

From this site, we are allowed to download the pictures, and also, look the original full size picture.

Look at the ticket and we got the last missing part of our flag!

![23-JohnCityUnreveleadTicket](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/c42c5043-d4ec-4933-8976-12f971877440)

```
Flag : PWNMECTF{lannemezan_blanchelovejd_ghestem}
```



## Europe<a name="Europe"></a>

Difficulty : **Medium**

Final Value : **315 pts**

Description :

```
[EN] For the context of the challenge, please check the introduction challenge's description

Description: John loves adventure and travel can you give me the 3 cities he visited during his trip to Europe.  

Flag Format: PWNME{city1_city2_city3} 
Cities in lower case and in alphabetical order and separated by a "_".  



[FR] Pour comprendre le contexte du challenge, regardez la description du challenge d'introduction  

Description : John aime l'aventure et le voyage pouvez vous me donner les 3 villes qu'il a visité lors de son voyage en Europe.  

Flag Format : PWNME{ville1_ville2_ville3} 
Les villes en miniscules et par ordre alphabétique et séparées par un "_".
```

Collected Data :

```
Pseudo : jdthetraveller
Pseudo2 : droperkingjohn
Wife Pseudo : BlancheLoveJD
Wife Name : Blanche Archambault
Wife Twitter : https://twitter.com/BlancheLoveJD
Ex Name : Patricia Caussade Ghestem
Ex Facebook : https://www.facebook.com/patricia.caussade.5
Email : johndroperdroperjohn@gmail.com
Site : https://jdthetraveller.fr
Forum Train : https://www.forum-train.com/forum/index.php
Forum 18-25 : https://www.jeuxvideo.com/forums/42-51-72118292-1-0-1-0-voyage-en-europe.htm
Basket Team : https://www.tgp-basket.com/
GitHub : https://github.com/droperkingjohn
Facebook : https://www.facebook.com/profile.php?id=100091409530073
Twitter : https://twitter.com/droperkingjohn
Twitter Wayback : https://web.archive.org/web/2/https://twitter.com/droperkingjohn
Instagram : https://www.instagram.com/droperkingjohn/
Picuki Instagram : https://www.picuki.com/profile/droperkingjohn
```


### Solution

On this challenge, we need to find the name of the three city that John visited during his trip in Europe.

First, we will look at the second instagram post that we havn't seen yet.

![24-InstagramPost2](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/27752176-b224-4aca-9c46-bdefee13fd65)

We can see a Austria flag picture with a description of John saying that he needed to use his bank ticket, otherwise he cannot eat. He is disapointed because he loved it and in fact, he want to track it. 

Two days later, he made another comment saying that, it's been 24 days he used the bank ticket and he don't have any news. This mean he used the bank ticket the 10 April 2023, based on the comment date.

The other picture is a part of the bank ticket, where we can read the Serial Number and seen that it's a 10 euro ticket.

Come back to picuki website on the John instagram account, and download the bank ticket picture.

```
https://www.picuki.com/profile/droperkingjohn
```

![25-DownloadedEuroNote](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/67310053-4b26-4dcd-aa02-a5fbea9e3199)

Once downloaded, do a google research with it using Google Lens (on smartphone, or at the right of the google search bar, click on the camera to upload it).

![26-GoogleImage](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/e9aeef19-f635-4a43-a2c2-13dfac6c214e)

Next we use the text research function, we select the serial number. And we found a match.

![27-BillLocation](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/f015556a-65c0-4458-a6c4-6c30ae416abc)

Following it redirect us to EBay.

```
https://www.ebay.fr/itm/275429255605
```

![28-FullBankNote](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/7dfd45c1-a4f0-4090-98f2-b7d3b288913a)

Here we got the full picture of both side of the bank note! Nice we can now proceed to the tracking. On google, searching ```Euro Tracker```we found a site that allow you to register your ticket based on your location. This purpose as for goal that, the more user who get this ticket on hand, register it based on where they get it. By this way, with the time, we can track where the specified ticket has traveled.

```
https://en.eurobilltracker.com/
```

Register to the website, and then connect to it. Create a new note and enter the informations. We already now the value (10 euros), we know the Serial Number.
And now, as we got the other side of the ticket through Ebay, on a 10 euros ticket, if we zoom on the star (According eurobilltracker website) we can find the printer code.

![29-PrinterCode](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/867ee440-4ddf-4231-b595-0243685798e9)

![30-EuroTracker](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/e6d0bc64-76f3-4326-9829-099e999ce43d)

Once the note registered, we are listed with every users that also registered this bank note and from where.

![31-Scoreboard](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/a028d3a9-5c39-462b-a344-dd87a0b1fc2b)

Scrolling down, since reaching the first person to register this note, we found ```Jdthetraveller```, that registered his bank note the 10th April 2023 from the city ```Gols (7122)```from ```Austria```. The country and date match with the instagram post and comment.

![32-Gols](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/5f381d69-5144-4eb3-b8bc-8081d5511d5f)

We got our first city for the flag!

```
Pre-Flag : PWNMECTF{?gols?} < Can be the first or last part too.
```

We already seen two others sources of his trip in Europe. The ```Jeux Video 18-25 Forum``` and the ```Train Forum```.

Let's start on the ```Jeux Video 18-25 Forum```

```
https://www.jeuxvideo.com/forums/42-51-72118292-1-0-1-0-voyage-en-europe.htm
```

![3-2](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/3061eabc-8264-4237-8920-5414ec95d5b6)

Here John is saying that he is new to the site and one of his friend told him that the 18-25 community can help him.

He said that he need to find another friend that send to him three messages really strange, which are "investisseur", "utopique", "ligamenteux". He know that his friend is mysterious but he is lost. He think that maybe lose this friend should be more easier than solve the case.

Then later he said that he found the solution, and now he can now join him.

Reading at it, its like his friend try to give him a challenge and apparently, as he can join him once resolving the case, the answer should be a city or location. But the only things that we got is the three words.

Do a google research about ```Three Words Cipher```, and we found a website named```What3Words``` which use three words to convert them back to GPS Coordinates.

But as there is a lot of clone / alternative, use this one bellow to avoid problem :

```
https://what3words.com/
```

Use the three given words to convert them to the city.

![33-what3web](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/88fcd44a-a474-4a1b-b03c-0555bab14177)

We got our 2th flag part which is ```Kaunas``` city!

```
Pre-Flag : PWNMECT{?_gols_?kaunas?} < Alway not sure of the flag order
```

Now let's have a look to the last Europe source that we have, the ```Train forum```.

```
https://www.forum-train.com/forum/index.php
```

Once on the home page, we look on the "Présentation" topic.

![34-TrainForum](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/ab3c8546-ba63-43d9-8249-e0afb0625d19)

We notice directly one subject because there is a big emoji green on it. Also, the username of his User is ```jdthetraveler```, note that there is a typo on this one, a ```L``` is missing. I guess this is, once again, to unallow us to find him through Google Dorks.

Open it, and we found two post and one answer not relevant from someone.

![35-TrainForumPost](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/fd0b5cbe-5627-4c90-ba89-747f001f37e0)

The first post, John said he is fan of travel since long time. He recently did a travel in Europe and a part of this travel was in train. After going to Central Europe, he decided to go on Eastern Europe. He left from Bratislava and travel for an average of 10h58. Also he ask for suggestions about some place to visit in United States.

Then we got the not relevant answer. Followed by another answer from John, saying that he forgot to said that he doesnt got the time to visit Bratislava unlike the other cities of his trip in Europe.

So Bratislava is not a city of our flag. But with thoses informations, the idea is to locate each train which left Bratislava and made a travel with an average of 10h58 to reech it's destination, which should be our last city.

To do this, i used ```direkt.bahn.guru```  (you can find it hosted and on GitHub).

```
Site : https://direkt.bahn.guru/

GitHub : https://github.com/juliuste/direkt.bahn.guru
```

Once on the website, select the city ```Bratislava hl.st.``` as it's the first result for Bratislava.

On the filter, be sure to select ```All Trains```. And search a travel with an average time of 10h58.

![36-TrainCityAverageTime](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/9aed0f77-5248-4926-9681-10faa170db21)

Great! We found the city ```Terespol``` with an average time of 10h58.

We got the full flag!

```
Flag : PWNME{gols_kaunas_terespol}
```



## American Dream<a name="AmericanDream"></a>

Difficulty : **Hardcoor**

Final Value : **361 pts**

Description :

```
[EN] For the context of the challenge, please check the introduction challenge's description  

Description: John has wonderful memories of his trip to the United States but he lost his memory on certain points, with all the information you have on him, you can help him, can't you?  

Give me the city of the assembly plant of the car he rented. The email service used by the company where he saw the dog of his dreams. The price (in dollars rounded up) of what he bought when he went to the bar that was robbed on 01/15/2023.        

Flag Format: PWNME{miami_sendinblue_2600} 
All lowercase with "_" to separate information.  



[FR] Pour comprendre le contexte du challenge, regardez la description du challenge d'introduction  

Description : John a de merveilleux souvenirs de son voyage aux États-Unis mais il a perdu la mémoire sur certains points, avec toutes les informations que vous avez sur lui, vous pouvez l'aider n'est-ce pas ?  

Donnez moi la ville de l'usine de montage de la voiture qu'il a loué. Le service de mail utilisé par l'entreprise où il a vu le chien de ses rêves. Le prix (en dollars arrondi à l'unité) de ce qu'il a acheté lorsqu'il est allé au bar qui a subit un vol le 15/01/2023.        

Flag Format : PWNME{miami_sendinblue_2600} 
Tout en minuscule avec des "_" pour séparer les informations.
```

Collected Data :

```
Pseudo : jdthetraveller
Pseudo2 : droperkingjohn
Wife Pseudo : BlancheLoveJD
Wife Name : Blanche Archambault
Wife Twitter : https://twitter.com/BlancheLoveJD
Ex Name : Patricia Caussade Ghestem
Ex Facebook : https://www.facebook.com/patricia.caussade.5
Email : johndroperdroperjohn@gmail.com
Site : https://jdthetraveller.fr
Forum Train : https://www.forum-train.com/forum/index.php
Forum 18-25 : https://www.jeuxvideo.com/forums/42-51-72118292-1-0-1-0-voyage-en-europe.htm
Basket Team : https://www.tgp-basket.com/
GitHub : https://github.com/droperkingjohn
Facebook : https://www.facebook.com/profile.php?id=100091409530073
Twitter : https://twitter.com/droperkingjohn
Twitter Wayback : https://web.archive.org/web/2/https://twitter.com/droperkingjohn
Instagram : https://www.instagram.com/droperkingjohn/
Picuki Instagram : https://www.picuki.com/profile/droperkingjohn
```


### Solution

For this last challenge, we need to find the city of the assembly plant of the rented car. The email service used by the company where he saw the dog. And finally the price of what he bought when he went to the bar that was robbed on 01/15/2023

As we dont get any informations about the car and the bar, we will look at the dog first that we discovered on John twitter profil.

![37-dog_twitter](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/36c72f78-6ec6-48a1-b564-c8d680b93668)

Download the picture, and load it on Google Lense. We doesnt find any visual matches, but if we click on "Find Images Sources", we can find the website where you can adopt the dog called ```Zookie```.

```
https://www.dognkittycity.org/pets/18106340-zookie.html
```
![38-dog](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/14412b81-c304-4787-8ae2-8f872116196a)

![39-dog_website](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/0114fc71-c610-4aac-a312-e34fe704bd2c)

Now that we got the company website, we can look at the dns. For this i used another Online tools by Google.

```
https://toolbox.googleapps.com/apps/dig/#MX/
```

If we look at MX records, we can think that the email server is ```Google.com``` or ```GoogleMail.com```

![40-emailrabbit](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/b65a07ce-cd64-4597-ba94-e5fed137db2b)

But this is wrong, if you look carefully at the whole dig report, specifically at the TXT records, you notice the value bellow :

```
"v=spf1 include:4abd214d3b.alatus.eoidentity.com ~all"
```

![41-email_correct](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/97525fd3-e054-4e7c-8712-196b64fa1f9f)

A quick access at ```eoidentity.com``` and we discover an home page with an "Hello message" to the right email server which is ```EmailOctopus```.

![42-EmailOctopus](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/b5429f7c-ca2a-440a-ad25-7d567beb7ff6)

We got the first part of our flag!

```
Pre-Flag : PWNME{?????_emailoctopus_?????}
```

Now, we didnt get any information to look for the car or bar. But there is one collected data that i've intentionally left aside, to avoid to get too much informations to look later and get a cleaner Write-Up.

So let's enumerate the email address of John. Of course, if you work on the challenges without reading the writeup, you basically should already seen this information.

```
johndroperdroperjohn@gmail.com
```

Once again, we go look the toolbox of ```Ozint``` at the "Email" category.

![43-OzintEmail](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/98bd27f1-c582-4410-a258-e39a44415145)

Selecting the tool ```epeios```, and enumerating John email address return one interesting result.

```
https://epieos.com/
```

```
https://calendar.google.com/calendar/u/0/embed?src=johndroperdroperjohn@gmail.com&pli=1
```

![44-JohnMailEnum](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/6ba6b308-9b8b-4dc4-b209-38faaca4cfcc)

We found his Google Calendar. The WayBack url for the google plus doesnt work. Also we get some data hidden, the website ask you to register for reveal them, i did it for fun but there is nothing relevant so far.

![45-JohnMailFull](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/cb047d0b-fa57-43c4-9da3-6c43f60fcfb6)

Now on the Google Calendar, we look at the past few month to see if there is something about his trip. And we found few notes in january, containing some bar where John has been and what he bought there. We also know that those bar was in Texas. Let's collect thoses informations :

```
Date :
jeudi, 12 janv. 2023

Lieu:
The Royal Pour Bar and Grill, 9909 Garland Rd, Dallas, TX 75218, États-Unis 

Description :
3 Brisket Grilled Cheese 
1 Royal Dogs

====================================

Date :
lundi, 16 janv. 2023

Lieu :
The Cottage Lounge, 3006 W Northwest Hwy, Dallas, TX 75220, États-Unis 

Description : 
1french fries 
1 texas burger

====================================

Date :
mercredi, 18 janv. 2023

Lieu :
the Skellig, 2409 N Henderson Ave, Dallas, TX 75206, États-Unis

Description: 
2 Soft Baked Pretzel 
1 Grilled chicken

====================================

Date:
lundi, 23 janv. 2023

Lieu:
Monkey Bar, 77 Highland Park Village, Dallas, TX 75205, États-Unis

Description :
7 Cocktails of the Day

====================================

Date :
mardi, 24 janv. 2023

Lieu:
The Hard Shake Bar, 211 S Akard St, Dallas, TX 75202, États-Unis

Description:
2 Supurrito 
1 Swipe Right
```

![46-GoogleCalendar](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/1fef6f92-d2a3-439b-9cbe-0ce6bc8950f5)

We note that each bar is located at Dallas in Texas, but apparently, there is nothing for the 01/15/2023. So thats not enough to get this part of the flag. 

The desciption of the challenge said that the concerned bar was robbed the 01/15/2023. So we should try to find something about this incident.

The idea is to find crime records about the incident, and find one of the bar address found on the Google Calendar that match the roberry of the 01/15/2023.

Make a quick google research about "Dallas Crime Records" and i find a Dallas Police website.

![47-DallasPolice](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/cdd3f266-897d-4eb2-812f-a9b6be5d838e)

```
https://dallaspolice.net/resources/Pages/Crime-reports.aspx
```

While looking at it, it look like a ressources cheat sheet. And at the bottom of the result, i'v found an "Interactive Crime Map" which seem to be what we need.

![48-CrimeMap](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/abf6d838-0671-4b5e-80bd-95554b19ce1c)

```
https://communitycrimemap.com/?agency=Dallas,%20TX
```

Once redirected to the site, we change the filter and select "All events" (to be sure that we will not miss something). Then we change the date range from 01/15/23 to 01/15/23, and finally we but a buffer of 500ft and we tick the box saying "Only display events within buffer", this will avoid to get a big range of incident and limit the area closest to the bar.

![49-FilterCrime](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/810cdf4c-8d95-4e8e-8719-c01c95a6aacf)

Now because of this ticked box, be sure to write (or copy past) exactly the same address of the bar, and check them one by one.

Once trying the address of ```the Skellig``` bar, we found a match! I put the satellite view and zoom on it.

![50-CrimeBar](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/0a103493-ac4b-41c9-be84-6eca9e715753)

Now, to be fully sure of our answer to avoid to get a wrong flag. I open google map, and search the same address, then zoom at the same location.

![51-CoorectLocation](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/72e2fa8f-4ae5-4a00-a906-d68b298baa26)

We got the confirmation that John go to ```the Skellig``` bar the 01/15/2023.

Going to the Skellig bar website, we can find the menu. We can guess that John take the same order than the one he took on the Google Calendar :

```
Date :
mercredi, 18 janv. 2023

Lieu :
the Skellig, 2409 N Henderson Ave, Dallas, TX 75206, États-Unis

Description : 
2 Soft Baked Pretzel 
1 Grilled chicken
```

But at the time of the CTF, the displayed price have changed. We need to use Wayback machine and load the date closest to the 01/15/2023.

![52-WaybackBar](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/d1301398-f54a-49e2-afce-d9515163ee81)

```
Direct Link to correct food menu page :
https://web.archive.org/web/20230205150920/https://www.theskelligdallas.com/food-menu
```

![53-baritem1](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/d677634a-c4d9-4049-a08a-69541efd7537)

![54-baritem2](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/8f9b0a40-34b9-49a2-a949-5680e31d26ab)

We found the same item that John bought the 01/18/2023, let's calculate the total amount.

```
2 Soft Baked Pretzel = $5 x2 = $10
+
1 Grilled chicken = $11
=
$21
```

We got the 2th part of the flag!

```
PreFlag : PWNMECTF{?????_emailoctopus_21}
```

Now we need to find some information about the car. Just like the email address that i left aside, there is another data collected that we didnt looked at yet. 

The WayBack url of the Twitter account. Once again, you should already seen this information when you looked at the Twitter account for the first time, to find if there is difference of both version. 

```
https://web.archive.org/web/2/https://twitter.com/droperkingjohn
```

Looking at it, we found few deleted posts that come after the dog post (so the newest posts of the profil has been deleted).

![55-TwitterWebArchive](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/8dab9359-8c93-4849-aa9a-69c5d44f370f)

We can see a thread about his trip at USA. He said he love "this" country, and one state especially that he visited lately. He said also, that he rodeoed for the first time at night and he visited a nice place about space, where he learned that the earth isn't flat.

With this information and our previous flag part, we can know that he talk about Texas. The rodeo hint on that way, and if we google something like "Dallas well known space place", we find the "Space Center Houston" located at :

```
https://spacecenter.org/

## 1601 E NASA Pkwy, Houston, TX 77058
```

Which can confirm our guess.

Come back to the web archived twitter, and in the next post, John said that he rented a car giving the string ```MLD8331```. He said that the car is from 2013. 

And finally he said that the next time, he may be visiting the last next bigger states of United states. This finally confirm our guess, because the second bigger states is Texas (just google something like "rate state by size").

So now we got few informations about that car. The string look like a plate number and we know that the car is from 2013 and few other less important informations.

For this step i've used a loooot of website about "plate lookup", and i only found one which work.

```
https://www.lookupaplate.com/
```

Note that you can find it also by simply researching ```MLD8331 TX```. 

Enter the plate number ```MLD8331``` and select the state ```Texas```.

![56-lookup_plate](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/332b259e-086f-4037-b033-e45fa0b35f71)

![57-Plate_Information](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/5f3933e5-e31a-4a23-81ed-bbb4302d956d)

We successfully identified the plate. Now look into the detailed specifications. And under general we found the Plant City value ```HWASUNG```.

![58-Plate_City](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/d52be36e-1a00-4103-a9b0-91ce307597eb)

We got our final flag part!

```
Flag : PWNMECTF{hwasung_emailoctopus_21}
```

Final Collected Data (doesn't contain everything, like all city or bar) :

```
Pseudo : jdthetraveller
Pseudo2 : droperkingjohn
Wife Pseudo : BlancheLoveJD
Wife Name : Blanche Archambault
Wife Twitter : https://twitter.com/BlancheLoveJD
Ex Name : Patricia Caussade Ghestem
Ex Facebook : https://www.facebook.com/patricia.caussade.5
Not adopted Dog name : Zookie
Email : johndroperdroperjohn@gmail.com
Site : https://jdthetraveller.fr
Forum Train : https://www.forum-train.com/forum/index.php
Forum 18-25 : https://www.jeuxvideo.com/forums/42-51-72118292-1-0-1-0-voyage-en-europe.htm
Basket Team : https://www.tgp-basket.com/
GitHub : https://github.com/droperkingjohn
Facebook : https://www.facebook.com/profile.php?id=100091409530073
Twitter : https://twitter.com/droperkingjohn
Twitter Wayback : https://web.archive.org/web/2/https://twitter.com/droperkingjohn
Instagram : https://www.instagram.com/droperkingjohn/
Picuki Instagram : https://www.picuki.com/profile/droperkingjohn
Pet Adoptions Site : https://www.dognkittycity.org/pets/18106340-zookie.html
Google Calendar : https://calendar.google.com/calendar/u/0/embed?src=johndroperdroperjohn@gmail.com&pli=1
```



## Credits<a name="Credits"></a>

Special thanks to :

* **[PwnMeCTF](https://twitter.com/ecole2600)** - for the CTF!
* **[Ecole 2600](https://twitter.com/pwnmectf)** - who made it possible!
* **[Ganko](https://twitter.com/G4nk0)** - for creating this AWESOME OSINT challenge category!

And of course... 

**Thanks to my newest team [Godzillhack!](https://godzillhack.com)**

![scoreboard1](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/b356e857-3a53-40d0-afa3-8198f13d74e8)




