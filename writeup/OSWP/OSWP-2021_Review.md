# OSWP - 2021 Review

# Table of Contents

* 1.0 [Introduction](#Introduction)
  * 1.1 [Why this review?](#why)
  * 1.2 [Why I took the WiFu course?](#whywifu)
* 2.0 [WiFu Course](#course)
  * 2.1 [Purchasing](#purchase)
  * 2.2 [Material used](#material)
  * 2.3 [Setup tips](#setuptips)
  * 2.4 [The Course](#thecourse)
  * 2.5 [Course Overview](#overview)
* 3.0 [OSWP Examination](#oswp)
  * 3.1 [Preparation](#preparation)
  * 3.2 [Exam](#exam)
* 4.0 [Conclusion](#conclusion)
* 5.0 [Bonus - Gift](#gift)


# Introduction<a name="Introduction"></a>

## Why this review?<a name="why"></a>

As a lot think that the OSWP and WiFu course are outdated and I don't, and also we dont find a lot of OSWP review, I decided to make one.

## Why I took the WiFu course?<a name="whywifu"></a>

I see that many think that the WiFu course is outdated and that it's useless to take it. Additionnaly, Offensive Security are currently updating their courses and adding news one. Maybe they will update the WiFu course? So why I took it?

Well, I was bored at home and want to learn something new by doing an Offensive Security course. As I'm already OSCP certified, and I didn't have 1299$ for a course, I was thinking to take the OSWP which cost only 450$.

If they update the course, I can purchase the updated material and pratice again, as the lab is an "Home Lab" and not an online lab, so the impact will be minor. If it was an Online lab, as OSCP, in addition of purchasing the updated material, I need to buy lab time to see and pratice on the newest machines, at this time the update has a major impact for me.

That's why I took the course.


# WiFu Course<a name="course"></a>

## Purchasing<a name="purchase"></a>

Once I purchased the course (13/02/2021), 1h30 later I received the mail with the material, so the 120 days delay to take the examination start since you buy the course and had received your course material.

## Material used<a name="material"></a>

* Router 1 : Netgear DG834GT
* Router 2 : D-Link Wireless N 150 Home Router (DIR-601)

* Wireless card 1 : Alfa AWUS036NHA 
* Wireless card 2 : Alfa ASWU036NH

* Target 1 : Samsung Galaxy S9
* Target 2 : OnePlus 7pro with NetHunter
* Target 3 : Laptop with Windows XP

* Attacker : Windows 10 Host with Back Track 5 on VmWare

## Setup tips<a name="setuptips"></a>

To setup your router, you only need to connect it with the alimentation. Then connect an ethernet cable from the router to your laptop the time to configure the router, then remove it. You don't need to connect them to ADSL, if your target are connected to the WiFi but they didn't have internet access, this is not a problem and it will not impact on your lab exercices.

If you can't connect your victim client to the router (it happened to me for WEP authentication), try another client, or try to change the key from 64 to 128 bytes.

## The Course<a name="thecourse"></a>

For the course, personally I opted to focus the PDF,  taking some notes and doing the home lab exercices, then watching the videos.

it was... a bad... idea. 

The PDF and videos has the same content with minor change, if you do it like me, you will watch the 4h of videos like a movie and it will be so boring... (SPOILER : he die at the end of the movie). You should read one module of the pdf and see related videos, and of course, take notes. Maybe you don't will read those notes through your course, but trust me, it can be really useful when you want to read it few months later to refresh your memory.

## Course Overview<a name="overview"></a>

The course is really well explained, the first part is a bit boring as they said, BUT this part is really interesting too!

I really liked the home lab exercices, it's really interesting to see the impact of each attacks against the targets, it was really fun!

As I was really frustrated to not find a fix to this problem, here is an advice :

When you lead a bypass shared key authentication, if you got a Broken SKA message like me : You can try to change the client target or try to manually connect the client to the router while you are capturing with airodump-ng. If the problem continue, I don't really have an answer, I've done a lot of research, a lot has the same problem, but no one find why this problem happen. Maybe it's the router.

The end of the course was a bit, shortcuted, that was a bit sad, but they explained the necessary things.

Yes, it's a lot WEP focused, so you can think that it's outdated, but it don't!

Why the course isn't outdated at my eyes ? Because we can see that it's a fundamental course which teach the base. You can't lead advanced things without knowing the base. And thats why this course is really good, it's not just "Cracking Wifi", but a lot of wireless knowledge to gain.

If the course need an update, it's because it use BackTrack 5 which is really outdated, and because the course contain some typos but that not a real problem. I think that the course is pretty good in this state, maybe it can be more good that Offensive Security create a new course to lead the OSWP to the next level, as OSEP does with OSCP.

Wait and see!

# OSWP Examination<a name="oswp"></a>

## Preparation<a name="preparation"></a>

To prepare myself for examination, i used my 4 last days for masteries all the attack methode learned. To do that, I'v created a private GitHub repository where I redacted all the attacks summary. Then I praticed in my home lab since I understood how work each attacks and how to lead them perfectly.

The day before the examination, I was thinking in which environment I will take the examination and how I will take screenshots / notes depending of it.

I opted for my Windows 10 host on my laptop, using the Windows Terminal, with the screen capture tool already instaled (win+maj+s) and CherryTree for my notes.

## Exam<a name="exam"></a>

2 hours before my examination, I prepared my environment, opening four Windows Terminal, creating a directory where to stock my screenshot and my notes, and starting to creates notes in CherryTree. Double check that my laptop is connected to the sector, that I'm connected to the right wireless and that I have an Ethernet Cable not far of me in case of emergency.

Examination started at 18:00, I received the mail with the SSH credentials, once connected to the BackTrack's host in my four terminal windows, I started the examination.

If you have completed the course and lab exercices, and that you understand how and why those attacks work and when use them, the examination is really easy. If you understand it, you can't fail it. I completed each stage without any errors such as Broken SKA or others.

It took me 32 minutes to take down the three targets, taking the notes and screenshots.

Then I redacted the Report using the Offensive Security Examination Report provided, it took me 2h51 to redact it, send it, and receive the confirmation e-mail that my documentation has been send.

The next day (24h30 later), I receiveid an e-mail by Offensive Security saying that I passed with success the examination and that I am OSWP certified!

# Conclusion<a name="conclusion"></a>

In conclusion, I really appreciated this course which teach the fundamental of the wireless network. It's not only Wifi Cracking content. It's outdated in termes of OS used and PDF quality, otherwise it teach the base, "the must know", it's not because WEP is pratically not used that mean it doesn't, and never, has existed. But in fact, you can't do advanced things without base and this course is perfect as first step and to gain knowledge in wireless network area and boost you penetration testing skills!

The examination was really easy once you had completed the course and understand perfectly each attacks. As the examination is only wifi cracking related, It's sad that it's not more challenging, something such as intercept traffic, and find a bank account connection in the packet capture. But it was really a fun rush anyway. And maybe that will be added if they updated the course, or into a new one wireless related, who know? :)

So Did I recommend the course?

Yes a lot! But if you want to wait for an update before taking it, do it, that's a choice in your hand!

# Bonus - Gift<a name="gift"></a>

As I've a little bit modified the examination report template provided by Offensive Security, I've created my own templated based on how I redacted mine examination report. I created two version such as Offensive Security, one for Microsoft Words users, and one for Libre Office and Open Office users.

What change with my template compared at the Offensive Security one?

- Added Reconnaissance step
- Added Lab Informations summary 

You can find both of them on my GitHub or by clicking <a href="https://github.com/V0lk3n/OSWP-Report-Template">here</a>.

<a href="https://twitter.com/v0lk3n">V0lk3n</a>
