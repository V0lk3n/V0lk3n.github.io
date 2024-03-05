---
title: ByuCTF 2023 - WriteUp
author: V0lk3n
tags: CTF, Osu!CTF, Cryptography, OSINT, Forensics, CyberSecurity
---

# Osu!CTF 2024 - WriteUp

## Scoreboard

<p align="center">
	<img src="assets/img/osu_ctf_2024_scoreboard.png">
</p>

<p align="center">
	<img src="assets/img/osu_ctf_2024_position.png">
</p>

> There was a total of 984 teams playing that CTF

## Solved Challenges

<p align="center">
	<img src="assets/img/osu_ctf_2024_solves.png">
</p>

> Written by [V0lk3n](https://twitter.com/V0lk3n)

## Author Notes 

```
At the time to register on this event on CTFTime, i had no clue of what Osu!Game was, and i was thinking that this CTF would be a normal CTF with a category focused on that game.

I was thinking that it could be funny, but honnestly, the CTF was much more focusing on the game than i would think. This impacted a lot my fun on the CTF at a point to think that it was only made to bring new player to the game....

But, there was few cool challenge anyway. Here is my writeup for few of my solve on the CTF that i found cool enough to make writeup about them.

- V0lk3n
```

## Table of Contents
  
* [**Cryptography**](#Cryptography)
	* [base 727](#base727)
	* [ROSSAU](#rossau)<br/><br/>
* [**Forensics**](#Forensics)
	* [Nathan on Osu!](#Nathan-on-osu) 
	* [Volatile Map](#Volatile-Map)<br/><br/> 
* [**OSINT**](#OSINT)
	* [When You See It](#wysi)<br/><br/>  
* [**Credits**](#Credits)


## Cryptography<a name="Cryptography"></a>

### base 727<a name="base727"></a>

Value : **104 points**

Solves : **566 Solves**

Author : **quin**, **ChatGPT**

Challenge :

<p align="center">
	<img src="assets/img/Cryptography/base727/osu_ctf_2024_crypto_base727.png">
</p>

Attachments : **out.txt**, **727.py**

### Solution

As the challenge show, Quitec used ChatGPT to create a program that encodes any strings in base 727. And the challenge give us the encoded base 727 strings and the generated program.

If ChatGPT created the challenge, why losing my time to decipher it manually? 

So i've asked ChatGPT too!

My first attempt was to directly send him the base727 strings and ask him to decode it, but he answered with a big theory on how to proceed. Too much time to solve a ChatGPT generated challenge.

<p align="center">
	<img src="assets/img/Cryptography/base727/1-Submit_Hash_to_ChatGPT.png">
</p>

So my next attempt, i've submited the code to encode strings in base727, and asked him to redecode the strings. 

<p align="center">
	<img src="assets/img/Cryptography/base727/2-Submit_the_code_to_ChatGPT.png">
</p>

ChatGPT answered him by providing to me the script to decode the base727 strings.

<p align="center">
	<img src="assets/img/Cryptography/base727/3-ChatGpt_final_answer.png">
</p>

Here is the code :

```python
import binascii

def decode_base_727(encoded_string):
    base = 727
    decoded_value = 0

    for char in encoded_string:
        decoded_value = decoded_value * base + ord(char)

    decoded_string = ""
    while decoded_value > 0:
        decoded_string = chr(decoded_value % 256) + decoded_string
        decoded_value //= 256

    return decoded_string

encoded_hex = "06c3abc49dc4b443ca9d65c8b0c386c4b0c99fc798c2bdc5bccb94c68c37c296ca9ac29ac790c4af7bc585c59d"
encoded_string = binascii.unhexlify(encoded_hex).decode()

decoded_string = decode_base_727(encoded_string)
print(decoded_string)

```

Save the code and run it, and we got the flag.

<p align="center">
	<img src="assets/img/Cryptography/base727/4-Flag.png">
</p>

**Flag : osu{wysiwysiwysiywsywiwywsi}**


### ROSSAU<a name="rossau"></a>

Value : **105 points**

Solves : **451 Solves**

Author : **BrokenAppendix**

Challenge :

<p align="center">
	<img src="assets/img/Cryptography/ROSSAU/osu_ctf_2024_crypto_ROSSAU.png">
</p>

```bash
n = 5912718291679762008847883587848216166109

e = 876603837240112836821145245971528442417
```

### Solution

For this challenge, i used the tool **RsaCtfTool**. This tool seem outdated today, you will encounter error installing the requirements with pip, but if you should be fine with a bit of google, and following carefully the installations steps noted in the readme of RsaCtfTool.

The idea was to generate the public key using the "n" and "e" numbers. Then we generate the private key using the public key. If that work, we should be able to dump the parameters used in the private key, and in fact, retrieve the private key exponent.

Let's start by generate the public key.

```bash
$ cd RsaCtfTool

$ python3 RsaCtfTool.py --createpub -n 5912718291679762008847883587848216166109 -e 876603837240112836821145245971528442417 > key.pub

$ cat key.pub  
-----BEGIN PUBLIC KEY-----
MDowDQYJKoZIhvcNAQEBBQADKQAwJgIREWA8Hv5C5OVALDhKvIeivt0CEQKTe8IJ
DBMb9Lq+6AUQNmIx
-----END PUBLIC KEY-----
```

Now with our public key, let's try to retrieve the private key.

```bash
$ python3 RsaCtfTool.py --publickey key.pub --private

['key.pub']

[*] Testing key key.pub.
attack initialized...
attack initialized...
[*] Performing rapid7primes attack on key.pub.
[+] loading prime list file data/ea229f977fb51000.pkl.bz2...
loading pickle data/ea229f977fb51000.pkl.bz2...
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 61174/61174 [00:00<00:00, 2339713.61it/s]
[+] loading prime list file data/fbcc4333b5f183fc.pkl.bz2...
loading pickle data/fbcc4333b5f183fc.pkl.bz2...
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 21048/21048 [00:00<00:00, 2245782.51it/s]
[+] Time elapsed: 0.2732 sec.
[*] Performing smallq attack on key.pub.
[+] Time elapsed: 0.3354 sec.
[*] Performing nonRSA attack on key.pub.
[+] Time elapsed: 0.0013 sec.
[*] Performing system_primes_gcd attack on key.pub.
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 7007/7007 [00:00<00:00, 1189520.71it/s]
[+] Time elapsed: 0.0283 sec.
[*] Performing factordb attack on key.pub.
[*] Attack success with factordb method !
[+] Total time elapsed min,max,avg: 0.0013/0.3354/0.1596 sec.

Results for key.pub:

Private key :
-----BEGIN RSA PRIVATE KEY-----
MFkCAQACERFgPB7+QuTlQCw4SryHor7dAhECk3vCCQwTG/S6vugFEDZiMQIDAeZN
AgkDO7s2uaxgmMsCCQVfvwELk5qZ9wIDAeZNAgMB5k0CCQHoTdErRuByvg==
-----END RSA PRIVATE KEY-----
```

Perfect, we got the private key! Save it to a file, then dump the parameters used in this private key.

```bash
$ echo "-----BEGIN RSA PRIVATE KEY-----
MFkCAQACERFgPB7+QuTlQCw4SryHor7dAhECk3vCCQwTG/S6vugFEDZiMQIDAeZN
AgkDO7s2uaxgmMsCCQVfvwELk5qZ9wIDAeZNAgMB5k0CCQHoTdErRuByvg==
-----END RSA PRIVATE KEY-----" > key.priv

$ cat key.priv
-----BEGIN RSA PRIVATE KEY-----
MFkCAQACERFgPB7+QuTlQCw4SryHor7dAhECk3vCCQwTG/S6vugFEDZiMQIDAeZN
AgkDO7s2uaxgmMsCCQVfvwELk5qZ9wIDAeZNAgMB5k0CCQHoTdErRuByvg==
-----END RSA PRIVATE KEY-----

$ python3 RsaCtfTool.py --dumpkey --key key.priv
private argument is not set, the private key will not be displayed, even if recovered.
None
n: 5912718291679762008847883587848216166109
e: 876603837240112836821145245971528442417
d: 124493
p: 59644326261100157131
q: 99132954671935298039
```

It worked! We dumped the parameters used in the private key and found the private key exponent which is the `d` numbers `124493`.

Now let's try to find the osu user id which match with that number.

The link to find user is `https://osu.ppy.sh/users/<id>`, to find this simply google something like "osu game users". Replace the id with the correct value.

https://osu.ppy.sh/users/124493

<p align="center">
	<img src="assets/img/Cryptography/ROSSAU/flag.png">
</p>

Is username `chocomint` is the flag, put it in the flag format and this is it!

**Flag : osu{chocomint}**

## Forensics<a name="Forensics"></a>

### Nathan on Osu!<a name="Nathan-on-osu"></a>

Value : **117 points**

Solves : **162 Solves**

Author : **sahuang**, **hollow**

Challenge :

<p align="center">
	<img src="assets/img/Forensics/Nathan-On-Osu/osu_ctf_2024_forensics_nathan-on-osu.png">
</p>

Attachments : **nathan_on_osu.zip**

### Solution

Reading at the challenge description, i directly was thining about <a href="https://en.wikipedia.org/wiki/ACropalypse">aCropalypse vulnerability</a>. Here is another great source to understand how aCropalypse vulnerablity work : https://news.sophos.com/en-us/2023/03/22/windows-11-also-vulnerable-to-acropalypse-image-data-leakage/

To solve this challenge, i used a cool tool found on github called <a href="https://github.com/frankthetank-music/Acropalypse-Multi-Tool">Acropalypse Multi Tool</a>, made by <a href="">frankthetank-music</a>.

Git clone the tool, install the dependencies and run it.

```bash
$ pip3 install -r requirements.txt              

$ python3 gui.py
```

Once the gui tool opened, we got two options, one to detect potentials files which can be vulnearble to aCropalypse. And the second option to restore the uncroped picture.

<p align="center">
	<img src="assets/img/Forensics/Nathan-On-Osu/1-Run_acropalypse_tool.png">
</p>

Let's run the detection option to see if our picture are listed as potentially vulnerable.

<p align="center">
	<img src="assets/img/Forensics/Nathan-On-Osu/2-Detection.png">
</p>

Seem that the picture may be vulnerable. Now let's try to recover it, but first let's get the picture metadata using exiftool.

```bash
$ exiftool nathan_on_osu.png
ExifTool Version Number         : 12.76
File Name                       : nathan_on_osu.png
Directory                       : .
File Size                       : 919 kB
File Modification Date/Time     : 2024:02:20 12:14:52+01:00
File Access Date/Time           : 2024:03:04 21:05:50+01:00
File Inode Change Date/Time     : 2024:03:04 21:05:50+01:00
File Permissions                : -rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 1047
Image Height                    : 246
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
SRGB Rendering                  : Perceptual
Gamma                           : 2.2
Pixels Per Unit X               : 3779
Pixels Per Unit Y               : 3779
Pixel Units                     : meters
Warning                         : [minor] Trailer data after PNG IEND chunk
Image Size                      : 1047x246
Megapixels                      : 0.258
```

Here few thing to notice :

- The actual image size is 1047x246. This help us to guess what was the original size.
- The warning suggest data after the IEND chunk. Which match with aCropalypse vulnerability.
- The color type is set to RGB with Alpha

Using strings (or any hex editor) confirm that there is two IEND chunk on the picture, and also we can look for the Color type which seem more a RGB color model with gamma correction than RGB with Alpha as said exiftool.

```bash
$ strings nathan_on_osu.png
IHDR
sRGB
gAMA
...

$ strings nathan_on_osu.png | grep IEND
IEND
IEND

```

Let's recover the original picture.

With all those information we can restore the original picture by using the `Restoring Tool` option, selecting the picture and setting the tool to `Custom RGB` and guessing the Width/Height to 1920x1080 which is generally the most used resolution and helped with the cropped picture size. Finally click on `Acropalypse Now`.

<p align="center">
	<img src="assets/img/Forensics/Nathan-On-Osu/3-restoring_tool.png">
</p>

Great! Save the uncroped picture, open it and look at the flag!

<p align="center">
	<img src="assets/img/Forensics/Nathan-On-Osu/resconstructed.png">
</p>


**Flag : osu{cr0pp3d_Future_Candy<3}**

### Volatile Map<a name="Volatile-Map"></a>

Value : **139 points**

Solves : **76 Solves**

Author : **hollow**

Challenge :

<p align="center">
	<img src="assets/img/Forensics/Volatile-Map/osu_ctf_2024_forensics_volatile-map.png">
</p>

Attachments : **https://drive.google.com/file/d/1OpRth-9oVwICNyOa2MiCgH24tsI6CDr6/view?usp=sharing**

### Solution

Because this is a Forensics challenge, that the attachements is a memory dump, and finally the name of the challenge. I was thinking to use `Volatility` tool to solve this challenge.

First let's download and setup volatility3.

```bash
$ git clone https://github.com/volatilityfoundation/volatility3.git

$ cd volatility3

$ pip3 install -r requirements.txt
```

I would start to use `imageinfo` parameter, to see to which profil the memory dump belong to. But i wasn't lucky and the parameter didnt worked on this dump.

So i used file command to see if it could tell me someting and i was right.

```bash
$ file memory.dmp
memory.dmp: MS Windows 64bit crash dump, version 15.19041, 2 processors, DumpType (0x1), 1048576 pages
```

We know that the memory was dump on a Windows 64bit version 15.19041, generally, i use profile with volatility2 and this was the first time i used volatility3 and get some troubles loading profile as you can see. But apparently, it wasn't needed for our challenge.

```bash
$ python3 vol.py -f ../memory.dmp --profile=Winx64_19041 windows.pstree
Volatility 3 Framework 2.7.0
...
volatility: error: unrecognized arguments: --profile=Winx64_19041
```

So my next step was to enumerate the running process, using `windows.pslist` parameter.

I noticed that there was a notepad.exe running, and this is generally really interesting while doing Forensics challenge.

```bash
python3 vol.py -f ../memory.dmp windows.pslist
...
7928    2272    notepad.exe     0xca8604d4d340  3       -       1       True    2024-03-01 13:42:17.000000      N/A     Disabled
```

At the time of solving, i was going to dump the notepad process then read the dumped file helping myself with some grep, like this.

```bash
$ python3 vol.py -f ../memory.dmp -o dump/ windows.memmap --pid 7928 --dump
...

$ strings dump/pid.7928.dmp | grep osu{.*                                  
"C:\Windows\System32\notepad.exe" C:\Users\Administrator\AppData\Local\osu!\Songs\beatmap-638448119315467561-ambient-relaxing-music-for-you-15969\osu{ - 686964655f6e (sahuang) [X3NlZWVlZWVlZWVla30=].osu
osu{ - 686964655f6e (sahuang) [X3NlZWVlZWVlZWVla30=].osu
```

But while writing this writeup, i figured a more easily way was using `pstree`, as the flag content was the name of the file opened with notepad and not the content in that file, but of course, theire should be a tons of method to retrieve the flag, such as listing the files on the memory dump.

```bash
$ python3 vol.py -f ../memory.dmp windows.pstree | grep notepad.exe                         
**** 7928  100.02272    notepad.exe     0xca8604d4d340  3       -       1       True    2024-03-01 13:42:17.000000      N/A     \Device\HarddiskVolume3\Windows\SysWOW64\notepad.exe    "C:\Windows\System32\notepad.exe" C:\Users\Administrator\AppData\Local\osu!\Songs\beatmap-638448119315467561-ambient-relaxing-music-for-you-15969\osu{ - 686964655f6e (sahuang) [X3NlZWVlZWVlZWVla30=].osu C:\Windows\SysWOW64\notepad.exe
```

Great so apparently we found the flag, because the file name is `osu{ - 686964655f6e (sahuang) [X3NlZWVlZWVlZWVla30=].osu` but of course, now we need to do some decode. Apparently there is two encoded strings, the first one seem to be in hexadecimal format, and the second seem to be a base64.

Let's use echo and pipe it to xxd to decode the hex strings, then use echo and pipe it to base64 to decode the base64 strings. Or use CyberChef with the "Magic" operations (in case if you aren't sure of which hash it is).

```bash
$ echo "68 69 64 65 5f 6e" | xxd -r -p   
hide_n

$ echo "X3NlZWVlZWVlZWVla30=" | base64 -d
_seeeeeeeeeek}
```

**Flag : osu{hide_n_seeeeeeeeeek}**

### Sad Solution

Well, i really hope that the intended solution was using Volatility tool due to the challenge name... But...

```bash
$ strings memory.dmp| grep osu{.* 
osu{ - 686964655f6e (sahuang) [X3NlZWVlZWVlZWVla30=].osu.lnk
```

And again, use echo and pipe it to  xxd and base64 to decode the flag. Or use cyberchef with "Magic" operations.

```bash
$ echo "68 69 64 65 5f 6e" | xxd -r -p   
hide_n

$ echo "X3NlZWVlZWVlZWVla30=" | base64 -d
_seeeeeeeeeek}
```

**Flag : osu{hide_n_seeeeeeeeeek}**

## OSINT<a name="OSINT"></a>

### When You See It<a name="wysi"></a>

Value : **188 points**

Solves : **35 Solves**

Author : **sahuang**

Challenge :

<p align="center">
	<img src="assets/img/OSINT/When-You-See-It/osu_ctf_2024_osint_when-you-see-it.png">
</p>

Attachments : **challenge.zip**

### Solution

Downloading the attachments and extracting its content, we got a GIF, with the hand of someone pointing his computer.

As the challenge description said, the flag is in 3 part. And also the person on the GIF should be important for the beginning (of the challenge?).

So let's start from there, i splitted the GIF into frame, using online tools such as <a href="https://ezgif.com/split">EZgif</a> or with the terminal using `convert`from `imagemagick`.

```bash
$ convert challenge.gif -coalesce +adjoin splitted%3d.png 

$ ls
 challenge.gif     'splitted  3.png'  'splitted  8.png'  'splitted 13.png'  'splitted 18.png'  'splitted 23.png'  'splitted 28.png'  'splitted 33.png'  'splitted 38.png'  'splitted 43.png'  'splitted 48.png'
 challenge.zip     'splitted  4.png'  'splitted  9.png'  'splitted 14.png'  'splitted 19.png'  'splitted 24.png'  'splitted 29.png'  'splitted 34.png'  'splitted 39.png'  'splitted 44.png'  'splitted 49.png'
'splitted  0.png'  'splitted  5.png'  'splitted 10.png'  'splitted 15.png'  'splitted 20.png'  'splitted 25.png'  'splitted 30.png'  'splitted 35.png'  'splitted 40.png'  'splitted 45.png'
'splitted  1.png'  'splitted  6.png'  'splitted 11.png'  'splitted 16.png'  'splitted 21.png'  'splitted 26.png'  'splitted 31.png'  'splitted 36.png'  'splitted 41.png'  'splitted 46.png'
'splitted  2.png'  'splitted  7.png'  'splitted 12.png'  'splitted 17.png'  'splitted 22.png'  'splitted 27.png'  'splitted 32.png'  'splitted 37.png'  'splitted 42.png'  'splitted 47.png'
```

From then, i pick one of frame which had the more content in it, and used Google Image to reverse search the picture.

I took the `splitted 40.png` picture which is the one bellow.

<p align="center">
	<img src="assets/img/OSINT/When-You-See-It/splitted-40.png">
</p>

And we found a result that seem match our challenge, a youtube video :

<p align="center">
	<img src="assets/img/OSINT/When-You-See-It/1-Reverse_Search.png">
</p>

Video link : https://www.youtube.com/watch?v=_bAcERFKyB0

But apparently, it wasn't the good video (yep, i got the right one at first attempt when solving but not this time, not the good frame i guess).

So go back to the google image, and i pressed under the video "see exact matches".

From there i check every result, and we can see the correct video :

<p align="center">
	<img src="assets/img/OSINT/When-You-See-It/2-Reverse_Search_correct.png">
</p>

Video link : https://www.youtube.com/watch?v=iy5aJLdZXzA

From there look at the tittle, the person on the GIF should be `Will Stetson` or `Aireu`.

Great, we got the first needed information. Now go back to our GIF. And let's start few staganography stuff.

First i used strings on the file to see if we can see something.

```bash
$ strings challenge.gif
...
secret/UT
.bux
secret/confidentialUT
secret/secret.wavUT
.bux
```

And at the end of the file, it seem that there is something inside as intended.

I extract the content using `binwalk` or `foremost`.

```bash
$ binwalk -e challenge.gif

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             GIF image data, version "89a", 498 x 373
3410748       0x340B3C        Zip archive data, at least v1.0 to extract, name: secret/
3410813       0x340B7D        Zip archive data, encrypted at least v2.0 to extract, compressed size: 201, uncompressed size: 230, name: secret/confidential
3411107       0x340CA3        Zip archive data, encrypted at least v2.0 to extract, compressed size: 2821, uncompressed size: 317388, name: secret/secret.wav
3414272       0x341900        End of Zip archive, footer length: 22
```

Great, the content is extracted! But as we can see, the `secret` folder with the files `confidential` and `secret.wav` is compressed into a encrypted zip archive.

So here, the person name on the GIF should be the password.

Let's try some password such as `WillStetson`,  `Aireu`, `will`, etc...

And we successfully uncompress the zip archive using the password `Aireu`.

```bash
$ unzip 340B3C.zip 
Archive:  340B3C.zip
   creating: secret/
[340B3C.zip] secret/confidential password: 
  inflating: secret/confidential     
  inflating: secret/secret.wav 
```

Let's see the extracted files type.

```bash
$ file *           
confidential: ASCII text
secret.wav:   RIFF (little-endian) data, WAVE audio, Microsoft PCM, 8 bit, mono 11050 Hz
```

Read the `confidential` content which seem to be a txt file.

```bash
$ cat confidential 
HIGHLY CONFIDENTIAL

<REDACTED>
I have stored extremely important files here and in another place.

Find it at "osu_game_/[0-9]+/".

As a reward, here is the first part of the flag: `osu{@nd_`

Yours,

Team Osu!Gaming
</REDACTED>
```

Great! We got our first part of the flag!

**Flag part1 : osu{@and_**

As the text file said, there is important files stored in another place, and we can find them at `osu_game_/[0-9+/`. So now, we need to find which numbers to put instead of the regex strings.

Listening at the `secret.wav` audio files, it seem to be a morse code. For this step i used an online tool which can decode morse from audio to ASCII.

Morse Audio Online Decoder : https://morsecode.world/international/decoder/audio-decoder-adaptive.html

<p align="center">
	<img src="assets/img/OSINT/When-You-See-It/3-Morse_decoded.png">
</p>

Great! Here is the strings :

```bash
4E7A49334E7A4933
```

But as the Regex said, the content should be only numbers. So its should be an hexadecimal strings to decode.

Let's try to decode it use `echo`and pipe it to `xxd`. Or use online tool or whatever.

```bash
$ echo "4E7A49334E7A4933" | xxd -r -p
NzI3NzI3
```

Great! But once again, seem not our strings, and this time it seem to be a base64. Let's decode it using `echo` and pipe it to `base64` or whatever way.

```bash
$ echo "NzI3NzI3" | base64 -d  
727727
```

Finally! We got our numbers. So we should found the others stored files somewhere at `osu_game_727727`. 

I tried to google this, but no luck. But as it's an OSINT challenge...... okey i assume that i got an hint from support for here hehe, i was looking too far, thinkin it was a path to the osu website, or ctf plateform, because i was looking for "stored files". For me the `confidential` note was not well written for this step.

Well, we need to look for a social media account! So i started from twitter, and search for an user called `osu_game_727727`. And i found it!

Twitter URL : https://twitter.com/osu_game_727727

<p align="center">
	<img src="assets/img/OSINT/When-You-See-It/4-Twitter_flag_part2.png">
</p>

And we got the second part of our flag which is the account name!

**Flag Part2 : wh3n_y0u_fuxx1n_**

Great! Now we see directly a strange strings as first post. So i put it under CyberChef using `magic` operations. And i got a Youtube URL.

Video Link : https://youtu.be/-ailwY-o7NM

<p align="center">
	<img src="assets/img/OSINT/When-You-See-It/5-Strings2ytb.png">
</p>

Browsing the youtube URL and.....

<p align="center">
	<img src="assets/img/OSINT/When-You-See-It/6-RickRoll.png">
</p>

Shit, get Rick Rolled. You got me.

Let's go back to the twitter account. Looking at the post, we can see a comment with another hashes. Which seem to be an hexadecimal strings again.

<p align="center">
	<img src="assets/img/OSINT/When-You-See-It/7-real_hash.png">
</p>


Once again decode it using `echo` and pipe it to `xxd`.

```bash
$ echo "68747470733a2f2f6f73752e7070792e73682f626561746d6170736574732f353639393836236f73752f31323038323435" | xxd -r -p
https://osu.ppy.sh/beatmapsets/569986#osu/1208245 
```

Great, we got an url, let's browse it.

<p align="center">
	<img src="assets/img/OSINT/When-You-See-It/8-click-click.png">
</p>

God... They really LOVE trolling! Time for clicking then!

<p align="center">
	<img src="assets/img/OSINT/When-You-See-It/9-click-part1.png">
</p>

Note that when i read to "start from the bottom", i was like, naaah ENOUGH TROLLING, im pretty sure that it will be on the three next click!

<p align="center">
	<img src="assets/img/OSINT/When-You-See-It/10-click-part2.png">
</p>
<p align="center">
	<img src="assets/img/OSINT/When-You-See-It/11-click-part3.png">
</p>
<p align="center">
	<img src="assets/img/OSINT/When-You-See-It/12-click-part4.png">
</p>
<p align="center">
	<img src="assets/img/OSINT/When-You-See-It/13-click-part-flag.png">
</p>

On... the... three next click? Are you sure? We finally... Got our third and last part of the flag!

**Flag Part3 : cL1ck3d_nd_c_1T!!!}**

**Flag : osu{@and_wh3n_y0u_fuxx1n_cL1ck3d_nd_c_1T!!!}**


## Credits<a name="Credits"></a>

Special thanks to :

- Ishra! <3 This was his first CTF, but as an Osu! player, he helped us a lot on this one! Thanks for all!
- Thanks to my team mate : R0stM, Sam and Rom1 who tried their best on this with the short time that they had while this CTF was running!

And of course... 

**Thanks to all my team [Godzillhack!](https://godzillhack.com)**
