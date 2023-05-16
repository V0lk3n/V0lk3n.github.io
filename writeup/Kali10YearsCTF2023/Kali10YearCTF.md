---
title: KaliCTF 2023 - 10 Years Anniversary
author: V0lk3n
tags: CTF, KaliCTF, Steganography, Cryptography, CyberSecurity
---

# KaliCTF 2023 - 10 Years Anniversary

![kali_cake2](https://user-images.githubusercontent.com/22322762/230107192-9a3b7077-9d61-429f-8c4e-93d765cc7c3e.png)

![16th_rank](https://user-images.githubusercontent.com/22322762/230107273-40cd4760-921d-49b5-9c79-d4f398962f59.png)

> Written by [V0lk3n](https://twitter.com/V0lk3n)


## Table of Contents

* 1.0 [ARTIC1E.m4v](#ARTIC1E)
* 2.0 [BBS-1995.mov](#BBS-1995)
* 3.0 [BT-adv3rt.mkv](#BT-adv3rt)
* 4.0 [co22upted.flv](#co22upted)
* 5.0 [dia6r4m.mp4](#dia6r4m)
* 6.0 [h45hc4t.avi](#h45hc4t)
* 7.0 [ki5met.mpeg](#ki5met)
* 8.0 [RG8.asf](#RG8)
* 9.0 [S4nt4.jpg](#S4nt4)
* 10.0 [7V-Static.wmv](#7V-Static)

## ARTIC1E.m4v<a name="ARTIC1E"></a>

In this challenge, they give us a picture of an article.

![Challenge](https://user-images.githubusercontent.com/22322762/230107383-fa059211-e371-494f-98cb-b2ca3e3a94b5.png)

At first look the only thing interesting is the coffee stain on the pictures, and on the `T` of `Tenth`.

Then, reading the article we notice some hint at the last part.

![hint](https://user-images.githubusercontent.com/22322762/230107483-7105375a-6f21-47fb-9093-0f4abf5966d2.png)

Of course, it wasnt directly obvious, i jump a lot of analysis, like rotate the article of 10 degree in each way, reverse it, add another copy at top of the original one, but one rotated to 10 degree. And more. A lot more...

So here is what we should be supposed to understand. 

1. We should count every ten letters from the first (highlighted "T" letter by the coffee stain) just to get started.
2. The first sentence of the article is important. (So we should count ten letters from the highlighted T and the first sentence.)
3. While it may not make sense at first (the letter that we will found), rotating that first piece in your mind to view it from different perspectives (ROT Cipher) may eventually to a key breakthrough. (The flag)

So which ROT cipher it is, how many rotations? Well, it's the ten years birthday of Kali Linux, the article said "10th", "ten", "tenth", a lot of time. So ROT10.

Let's try it!

![interesting_part](https://user-images.githubusercontent.com/22322762/230107628-d34c739e-fbeb-4728-b74f-31c3f7c44c0b.png)

We got the letters `Teeayuqdtckji`

Going on Dcode, trying to decode it as ROT10 we fail. Uh oh-oh. But remember, the article said to "Rotate it", so maybe, we should encode it as ROT10 instead?

![rot_encode](https://user-images.githubusercontent.com/22322762/230107703-514a3ea8-ee4a-45b9-952a-a0f072791724.png)

Encrypt it, and Bingo!

![flag](https://user-images.githubusercontent.com/22322762/230107750-73c40cba-2678-42c4-9b6a-16fa98e53827.png)

**Flag : Dookieandmuts**


## BBS-1995.mov<a name="BBS-1995"></a>

We are a strange given text with a nice ARG SOC logo. One line is highlighted which said `USR AT MODEM Commands`.

![Challenge](https://user-images.githubusercontent.com/22322762/230107892-b2fd70bc-9c08-43d0-ae37-f51c41d2b276.png)

Googling about it show us that `AT Command` is used to configure cellular modem. Going on the `USR` support website, we found some documentation.

Source : https://support.usr.com/support/3cxm756/3cxm756-ug/atcoms.htm

Reading at them, i've noticed one similiarity. The `Link Speed`.

Taking the command of each link speed shown in the given challenge, give us those result.

```
&N23 AT&N23 Link Speed - 46666 bps
&N8 AT&N8 Link Speed - 14400 bps
&N15 AT&N15 Link Speed - 31200 bps
&N16 AT&N16 Link Speed - 33600 bps 
&N16 AT&N16 Link Speed - 33600 bps
&N9 AT&N9 Link Speed - 16800 bps  
&N24 AT&N24 Link Speed - 48000 bps
```

Saying those number let me think that each number should correspond to one alphabet letter. So as exemple, the first one `&N23` should be the letter `W`.

Doing this for each connect speed of each users in the challenge return us the flag.

**Flag : WHOPPIX**


## BT-adv3rt.mkv<a name="BT-adv3rt"></a>

We got an Offsec video, carefully listening at it we hear some noises at the end of the video.

https://user-images.githubusercontent.com/22322762/230108129-31cfed6e-b6ab-4107-a8bb-8cfc68ac7f34.mp4

Right click on the video, open it in a new tab to get it's direct link, then use `wget` to download it.

```
$ wget https://10year.kali.org/assets/content/back-commercial/1337x.mp4
```

Once downloaded, open it in `audacity` tool. Then show the spectrogram to reveal the flag.

![flag](https://user-images.githubusercontent.com/22322762/230108057-51ec525c-1724-4725-98ac-1e3061571a82.png)

**Flag : kali4kids**


## co22upted.flv<a name="co22upted"></a>

We see a picture of a kali linux instance, apparently runing `foremost`  and `fdisk` utilities. At top of this screenshot, there is a blinking text.

Select it, copy and past it into a file named "corrupted.txt".

Opening this file, we see the text with a lot of diacritical characters.

Fire up you'r new best friend ChatGPT! And ask him nicely to generate you a python script to remove diacritical characters from that text, and he will do it!

![chatGPT](https://user-images.githubusercontent.com/22322762/230108269-9d860876-1b1c-400b-885a-9ecc2cd91d1b.png)

Save the python script and run it. (I've edited the "input.txt" to "corrupted.txt" to match with my file) 

```python
$ cat uncorrupted.py 
import unicodedata

def remove_diacritical_chars(text):
    """
    Removes diacritical characters from a given text.
    """
    return ''.join(c for c in unicodedata.normalize('NFD', text)
                  if unicodedata.category(c) != 'Mn')

# read text file
with open('corrupted.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# remove diacritical characters from text
text_without_diacritical_chars = remove_diacritical_chars(text)

# write text without diacritical characters to output file
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(text_without_diacritical_chars)
```

```
$ python uncorrupted.py 

$ cat output.txt 

"iVBORw0KGgoAAAANSUhEUgAAAEAAAAAICAYAAABJYvnfAAABhWlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw1AUhU9TRZGKgxWkKGSoThaKijhKFYtgobQVWnUweekfNGlIUlwcBdeCgz+LVQcXZ10dXAVB8AfE1cVJ0UVKvC8ptIjxwuN9nHfP4b37AKFRYarZFQVUzTJS8ZiYza2KPa/wIYQhjCIqMVNPpBcz8Kyve+qmuovwLO++P6tfyZsM8InEc0w3LOIN4plNS+e8TxxkJUkhPieeMOiCxI9cl11+41x0WOCZQSOTmicOEovFDpY7mJUMlXiaOKyoGuULWZcVzluc1UqNte7JXxjIaytprtMaQRxLSCAJETJqKKMCCxHaNVJMpOg85uEPOf4kuWRylcHIsYAqVEiOH/wPfs/WLExNukmBGND9YtsfY0DPLtCs2/b3sW03TwD/M3Cltf3VBjD7SXq9rYWPgIFt4OK6rcl7wOUOMPykS4bkSH5aQqEAvJ/RN+WAwVugb82dW+scpw9Ahma1fAMcHALjRcpe93h3b+fc/u1pze8HygByylYGy2sAAAAGYktHRAD/AP8A/6C9p5MAAAAJcEhZcwAAFiUAABYlAUlSJPAAAAAHdElNRQfnARsQKwQQ1uK0AAADZklEQVRIx9VUXWgcVRT+Vu06rakVmuKcLLZRnKOBlW42jpgI2itaoQ9CH0wanJeOkFX7ELVWX6rENwv1B9EqI0ZWsJrYFwUX20oDxYDxki1Wg6iFjabptnh9aVMkmcbjQ+Yuk20KPvRBDwzMnPvd853zzXcv8B+PQJl8oEz2atY0SpFRigDgGgDoOjJeZikQALAUiKXQCgCl58/VopdOPgwAmkic0LVPr3Bc8jVJ8ef2E74m8TWJJhKJuCwcl24McwtO6C4AgERcckJXNJE0N3P3x2++4XoVkYgnbe73gU1liZiSzz0AOFCGNC1xjHpTZderSFJ7yPLb/a5XEV+TsBQm01y+JhGOh9bvmJ1Zv2N2prHQPTgnTuhKoEy+Z3rfaz3T+zbaoY9t27vfvlu8E7otwjEJx8RSGLJ5iTgLAMJxSTimFF4k4nUJZkIiXgMA0Ts08sBXe99P8kUndMVyWQF8TSIRtwTKUDIApWunB7cx9cpu6RrvecpyJz81vxK2EavD3GKgTPaov/uv4/nAT6zS2LC/f3zxvsELsVHqMlUDZajJYsswH74VmZRIExLxGqPU7XbglPNKAHCb9+Ula1GJWCTiXsu19uVczQndzkY9joWlMMlSKKYdkO4vqZ11vYq4219cXHh189bLBOCwTTRRmNisqom2CseNQivZ90oCpLG+phZfk3xQPFBON2aUKv8bAdK1WAq0ehdVDz62ud+K7ITuhBO67Wl+16uIUWpy1Jsqp90CAG5Il+S9O05uCDfFywa5KXRjTUtqff3cxgFNJN2Dcw3yT4/wmZUuk527ztW6B+c6U01mmgTo9TXJZ990s1GqVSIeSnBZTSQ/5J58FgA+6Wsbs/t8TXKxY74zUCa/kvAScdaKuWHnlh+b1/ufbqu9/cIt61yvUrUCBMpkA2XyFmMFuM4mTtU6bsCdmP8lM1Z/CIge7DucXXVx9i673jeNmb6IJ1q/PV8EgD+Hz6660nF6/MzNCpn6khv8+qgmGpnbfvp869iMkX62sNiv1zOaPhdN9DqOC07dn+nACHDgUWDLF+3Vn95d+/ehWyXG8PLzfg8uoL7nmY8yA8Aj04fmD4ddMQD8Mfzbsp7O/rqtSEtCZQDwsdP6+zavIrmDT1z73Ynrq7iXi/g/RfMFeDXiH7l+vAyGvQbXAAAAAElFTkSuQmCC"
```

Nice! It look like a base64 at first look. I edit the file to remove the additional space at the top, and remove the starting and ending quotes.

Once edited, i use `cat` to read the file, and pipe it through `base64` utilities and decode it to a file.

```
$ cat output.txt 
iVBORw0KGgoAAAANSUhEUgAAAEAAAAAICAYAAABJYvnfAAABhWlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw1AUhU9TRZGKgxWkKGSoThaKijhKFYtgobQVWnUweekfNGlIUlwcBdeCgz+LVQcXZ10dXAVB8AfE1cVJ0UVKvC8ptIjxwuN9nHfP4b37AKFRYarZFQVUzTJS8ZiYza2KPa/wIYQhjCIqMVNPpBcz8Kyve+qmuovwLO++P6tfyZsM8InEc0w3LOIN4plNS+e8TxxkJUkhPieeMOiCxI9cl11+41x0WOCZQSOTmicOEovFDpY7mJUMlXiaOKyoGuULWZcVzluc1UqNte7JXxjIaytprtMaQRxLSCAJETJqKKMCCxHaNVJMpOg85uEPOf4kuWRylcHIsYAqVEiOH/wPfs/WLExNukmBGND9YtsfY0DPLtCs2/b3sW03TwD/M3Cltf3VBjD7SXq9rYWPgIFt4OK6rcl7wOUOMPykS4bkSH5aQqEAvJ/RN+WAwVugb82dW+scpw9Ahma1fAMcHALjRcpe93h3b+fc/u1pze8HygByylYGy2sAAAAGYktHRAD/AP8A/6C9p5MAAAAJcEhZcwAAFiUAABYlAUlSJPAAAAAHdElNRQfnARsQKwQQ1uK0AAADZklEQVRIx9VUXWgcVRT+Vu06rakVmuKcLLZRnKOBlW42jpgI2itaoQ9CH0wanJeOkFX7ELVWX6rENwv1B9EqI0ZWsJrYFwUX20oDxYDxki1Wg6iFjabptnh9aVMkmcbjQ+Yuk20KPvRBDwzMnPvd853zzXcv8B+PQJl8oEz2atY0SpFRigDgGgDoOjJeZikQALAUiKXQCgCl58/VopdOPgwAmkic0LVPr3Bc8jVJ8ef2E74m8TWJJhKJuCwcl24McwtO6C4AgERcckJXNJE0N3P3x2++4XoVkYgnbe73gU1liZiSzz0AOFCGNC1xjHpTZderSFJ7yPLb/a5XEV+TsBQm01y+JhGOh9bvmJ1Zv2N2prHQPTgnTuhKoEy+Z3rfaz3T+zbaoY9t27vfvlu8E7otwjEJx8RSGLJ5iTgLAMJxSTimFF4k4nUJZkIiXgMA0Ts08sBXe99P8kUndMVyWQF8TSIRtwTKUDIApWunB7cx9cpu6RrvecpyJz81vxK2EavD3GKgTPaov/uv4/nAT6zS2LC/f3zxvsELsVHqMlUDZajJYsswH74VmZRIExLxGqPU7XbglPNKAHCb9+Ula1GJWCTiXsu19uVczQndzkY9joWlMMlSKKYdkO4vqZ11vYq4219cXHh189bLBOCwTTRRmNisqom2CseNQivZ90oCpLG+phZfk3xQPFBON2aUKv8bAdK1WAq0ehdVDz62ud+K7ITuhBO67Wl+16uIUWpy1Jsqp90CAG5Il+S9O05uCDfFywa5KXRjTUtqff3cxgFNJN2Dcw3yT4/wmZUuk527ztW6B+c6U01mmgTo9TXJZ990s1GqVSIeSnBZTSQ/5J58FgA+6Wsbs/t8TXKxY74zUCa/kvAScdaKuWHnlh+b1/ufbqu9/cIt61yvUrUCBMpkA2XyFmMFuM4mTtU6bsCdmP8lM1Z/CIge7DucXXVx9i673jeNmb6IJ1q/PV8EgD+Hz6660nF6/MzNCpn6khv8+qgmGpnbfvp869iMkX62sNiv1zOaPhdN9DqOC07dn+nACHDgUWDLF+3Vn95d+/ehWyXG8PLzfg8uoL7nmY8yA8Aj04fmD4ddMQD8Mfzbsp7O/rqtSEtCZQDwsdP6+zavIrmDT1z73Ynrq7iXi/g/RfMFeDXiH7l+vAyGvQbXAAAAAElFTkSuQmCC                                

$ cat output.txt | base64 -d > output.dat
```

Using `file` utilitie, we found out that the decoded base64 is a `PNG`. 

```
$ file output.dat                                                                                                                                                                                                                        
output.dat: PNG image data, 64 x 8, 8-bit/color RGBA, non-interlaced

$ mv output.dat output.png      
```

Open it and we got the flag.

![flag](https://user-images.githubusercontent.com/22322762/230108366-1cdeec14-58f2-4984-a44b-78c5adbf748b.png)

Tricky to read but here it is!

**Flag : WETTROUSERS**


## dia6r4m.mp4<a name="dia6r4m"></a>

On this challenge, we have a diagram. We need to understand it to found the corresponding letter (which will be the flag) at the bottom of the diagram. 

![puzzle](https://user-images.githubusercontent.com/22322762/230175567-7842dd03-da13-4ad2-8c5b-17f95dde9ed3.png)

As we can see, the bottom of the diagram have a symbol for each letter of the flag needed. Also, we already have some letter, but why those letter seem interesting.

Let's try to give a value to each letter, by taking their corresponding numbers.

```
A = 1
B = 2
C = 3
...
```

Next we need to understand each symbols.

```
The blue symbol is a resistor
The orange symbol is a coil
The pink symbol is a AND gate
The green symbol is a potentiometer
The purple symbol is a NOT gate
```

For the following, refere to the picture bellow.

![flag](https://github.com/V0lk3n/V0lk3n.github.io/assets/22322762/e7ab9ede-20a8-4037-8843-48787c14a5b5)

* As E(5) is connected to E(5) with a gray wire, we can assume that connection value is `0`.
* As S(19) is connected to R(18) with a resistor, we can assume that the resistor value is `-1`.
* As S(19) is connected to T(20) with a coil, we can assume that the coil value is `1`.
* As A(1) and D(4) is connected to E(5) through an AND gate, we can assume that the AND gate add those two entry and the value would be `5`.
* As G(7) and B(2) is connected through a potentiometer to E(5), we can assume that the potentiometer substract those two entry and the value would be `5`.
* As `G(7) + 2*resistor` return `5` at the NOT gate, and that exit is V(22), we can assume that the NOT gate value is `17`.

Let's put a value to each symbols again :

```
The blue symbol is a resistor = -1
The orange symbol is a coil = 1
The pink symbol is a AND gate = 5 
The green symbol is a potentiometer = 5
The purple symbol is a NOT gate = 17
```

Now that we got a value for each symbols, we can convert the numbers to their corresponding letters and retrieve the flag.


**Flag : SECURITY**


## h45hc4t.avi<a name="h45hc4t"></a>

On this challenge, we have a `hashcat` command line, where we don't know the hashtype. Also there is a kali linux logo and a strange strings in the border.

![puzzle](https://user-images.githubusercontent.com/22322762/230108600-422c5972-9f8d-4f44-a3b5-02ac657a37a3.png)

Reading in a clock order, and writing those sharp and dot in a file show us something interesting.

```
.######..#.....#.#.....#.######..######..
.#.....#.#.....#.##....#.#.....#.#.....#.
.#.....#.#.....#.#.#...#.#.....#.#.....#.
.######..#.....#.#..#..#.######..######..
.#.......#.....#.#...#.#.#.....#.#.....#.
.#.......#.....#.#....##.#.....#.#.....#.
.#........#####..#.....#.######..######..
.........................................
```

We can see the strings `PUNBB`. A fast google search about it told us more about PunBB.

```
PunBB is a lightweight PHP-based internet discussion board system released under the GNU General Public License.
```

Making another google search with `PunBB hashes`, and we found a GitHub link from an closed issue on `hashcat` asking for the support of `PunBB Hashes`.

![support_punbb_hashes](https://user-images.githubusercontent.com/22322762/230108744-2d5f361a-766d-41dd-99fd-ce5f40544936.png)

Source : https://github.com/hashcat/hashcat/issues/29

Scrolling down, we can the that the support for `PunBB hashes` as been added and the issue closed.

![closed_issue](https://user-images.githubusercontent.com/22322762/230108798-720d6f18-38c0-47d5-956a-e85332dbaa2b.png)

Opening the commit link and we can see the added `hash types` of `PunBB hashes`.

![hashtype](https://user-images.githubusercontent.com/22322762/230108835-f70bc456-3f55-4f14-9775-0062a78e5f3b.png)

```
Added hash-mod 4522 = PunBB
```

So at this step, we have the hash types of PunBB. The dot and sharp string as been decoded. But we have a strange strings at teh end of the picture.

```
EYQOGWCEO
```

Maybe a cipher text that use numbers (4522) to encode?

I've done a google search `Cipher that uses numbers as key`. And after trying few cipher, i've successfully decoded it using `Gronsfeld Cipher`.

Source : https://www.boxentriq.com/code-breaking/gronsfeld-cipher

![flag](https://user-images.githubusercontent.com/22322762/230108908-4dc07ac5-1394-473e-9797-80c854d84e2f.png)

And we got the flag!

**Flag : ATOMCRACK**


## ki5met.mpeg<a name="ki5met"></a>

In this challenge, we see a screenshot of `Kismet` tool.

![puzzle](https://user-images.githubusercontent.com/22322762/230109006-10580536-4afd-4756-80a0-e80274093fc4.png)

First things that we notice, is the strange BSSID `46:72:61:63:74:69:6F:6E:61:74:65:64` which is definitively not a BSSID due to its length.

Seem to be a hexadecimal string. Let's try to convert it to text.

```
$ printf '\x46\x72\x61\x63\x74\x69\x6F\x6E\x61\x74\x65\x64'
Fractionated
```

Nice, but this is not the flag. So it should be a hint. Doing a google search about "Fractionated Cipher" and we found a "Fractionated Morse Cipher".

Now let's try to convert as Morse, the packets bar in the kismet screenshot. Let's assume that each dips separate dot and dashes.

![packet2morse](https://user-images.githubusercontent.com/22322762/230109062-b8fafd57-de33-4b5a-b339-4d891c07303f.png)

```
-.. .... --- .- .--. - -.-. ..-. -.- --.
```

Now let's convert this morse strings to text.

![morse2txt](https://user-images.githubusercontent.com/22322762/230109130-dbfaac07-2391-47c1-8156-6eb62e38000b.png)

Source : http://www.unit-conversion.info/texttools/morse-code/

We get the output `dhoaptcfkg`.

Finally convert this output to text as `Fractionated Morse Cipher`.

![flag](https://user-images.githubusercontent.com/22322762/230109143-c0a50168-124a-4a23-b7ad-96c4717d5b31.png)

Source : https://www.dcode.fr/fractionated-morse

We got the flag!

**Flag : LOVELACE**


## RG8.asf<a name="RG8"></a>

We are given a png with three kali logo and three binary text (Red, Green, Blue)

<img width="504" alt="puzzle" src="https://user-images.githubusercontent.com/22322762/230109239-73022f85-6da6-46af-8829-023ea8045c14.png">

Using `GIMP` separate each colors to get three different pictures.

![separate_colors](https://user-images.githubusercontent.com/22322762/230109309-3220accb-450f-4d7e-80d2-2064ee7aab0b.gif)

First, let's write each binary into a text file for further analysis.

```
Red :

01011000 01001111 01010010 00101100 00100000 01110100 01101000 01100101 01101110 00100000 01001110 01001111 01010100

Green :

00010011 11101000 11000110 11111100 00101101 10110111 11110110 00100110 00001111 11010111 10111110 00101101

Blue :

10000001 01100010 01010101 01110111 10111011 00111000 01100101 10111100 10001000 01000001 00101111 10110101
```

Decoding from binary to text the red part return this sentence :

```
XOR, then NOT
```

As to XOR we should have two input, i assume that we need to XOR the Green with the Blue part to combine them and finally NOT the result.

As exemple, we need to take the first 8bytes of the Green (00010011) and XOR it with the first 8Bytes of the Blue (10000001) to get another 8bytes binary. Do that for the whole Greed with Blue binaries.

Of course, we can do that manually, but we will use online tools to speed up the process.

Let's XOR it through https://xor.pw/

```
Green + Blue XOR :

10010010 10001010 10010011 10001011 10010110 10001111 10010011 10011010 10000111 10010110 10010001 10011000
```

Now with that final result, let's NOT it through https://www.browserling.com/tools/binary-not or manually.

```
XOR binary to NOT :

01101101 01110101 01101100 01110100 01101001 01110000 01101100 01100101 01111000 01101001 01101110 01100111
```

Finally convert the binary to text to retrieve the flag.

![flag](https://user-images.githubusercontent.com/22322762/230109399-909fbee5-71d1-42d9-b23a-fda730f94a8d.png)

**Flag : multiplexing**


## S4nt4.jpg<a name="S4nt4"></a>

We have a `jpg` picture, generally when i find `jpg` pictures in CTF, there is a lot of chance that there is some steganography through `steghide` tool. This was a first "hint" for me.

![santa](https://user-images.githubusercontent.com/22322762/230109759-fa6c9f87-72d0-4e25-adb6-aa19aebb2f65.jpg)

Right click on the picture and save it on my computer to begins an analysis.

Running exiftool return interesting result :

```
$ exiftool santa.jpg                                                                                                                                                                                                                     
ExifTool Version Number         : 12.57
File Name                       : santa.jpg
Directory                       : .
File Size                       : 710 kB
File Modification Date/Time     : 2023:03:22 20:49:33+01:00
File Access Date/Time           : 2023:03:23 09:49:22+01:00
File Inode Change Date/Time     : 2023:03:23 01:00:42+01:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
X Resolution                    : 1
Y Resolution                    : 1
Exif Byte Order                 : Big-endian (Motorola, MM)
Image Description               : INXLU CARROTE (repent)
Resolution Unit                 : None
Artist                          : DANFARMER
Y Cb Cr Positioning             : Centered
Exif Version                    : 0232
Date/Time Original              : 1995:04:05 00:00:00
Create Date                     : 1969:12:28 00:00:00
Components Configuration        : Y, Cb, Cr, -
User Comment                    : SanTas slEiGh (PASSes over the WORlD - ImageDescription)
Flashpix Version                : 0100
Owner Name                      : W1ETSEZWE1TZEVENEMA
GPS Latitude Ref                : North
GPS Longitude Ref               : East
Image Width                     : 3192
Image Height                    : 1900
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 3192x1900
Megapixels                      : 6.1
GPS Latitude                    : 60 deg 10' 21.43" N
GPS Longitude                   : 24 deg 57' 3.83" E
GPS Position                    : 60 deg 10' 21.43" N, 24 deg 57' 3.83" E

```

The  ImageDescription, User Comment and Owner Name seem interesting.

If we took only caps letters at the "User Comment" section, we got "STEG PASSWORD", it seem to hint us that the password for Steghide tool is in the image description.

At first try, it's not the password. Playing with it through an Online scrabble tool, we can see that "INXLU CARROTE" may mean "LINUX CREATOR".

Source : https://www.unscramble.me/

![inxlu](https://user-images.githubusercontent.com/22322762/230109629-64795f29-f196-4205-a090-820591556892.png)

![carrote](https://user-images.githubusercontent.com/22322762/230109644-2a177979-7e30-465d-88fd-70995f0baf9c.png)

The linux creator is `Linus Benedict Torvalds`.

At this step, i'm not sure i'm missing something, but as we only need to find how is formated the password, i've looked at the Owner Name, which seem to be full caps and using the number one as `i`.

Trying "L1NUSBENED1CTTORVALDS" as password for steghide worked and extracted a text file named `steganopayload998568.txt`.

```
$ steghide --extract -sf santa.jpg -p "L1NUSBENED1CTTORVALDS"
```

Read the text file to retrieve the flag.

```
$ cat steganopayload998568.txt                                                                                                                                                                                                           
KALINETHUNTER
```

**Flag : KALINETHUNTER**


## 7V-Static.wmv<a name="7V-Static"></a>

We got a `GIF` that show a TV wich blink static noises. Right click on it, save it as `GIF` file in your desktop.

![puzzle](https://user-images.githubusercontent.com/22322762/230109919-027ed3c4-3bef-481b-9bd6-027251c9a123.gif)

Once downloaded, we will extract all the frames from it using `graphicsmagic`.

First we need to install the tool.

```
$ sudo apt-get install graphicsmagick
```

Then, use it to recover all the frames from the `GIF` file.

```
$ gm convert puzzle.gif -coalesce +adjoin frame%3d.png

$ ls
'frame  0.png'  'frame  1.png'  'frame  2.png'  'frame  3.png'  puzzle.gif
```

Delete the two png with black screen and re-converting the two left `PNG` to one `GIF` with a delay of 1miliseconds and we can see the flag.

```
$ rm 'frame  0.png' 'frame  2.png' 

$ gm convert -delay 1 -loop 0 *.png flag.gif
```

![flag](https://user-images.githubusercontent.com/22322762/230109967-00fae7b1-75ff-4c49-b82c-245fbefc4748.gif)

Another pain to read the flag, so i'm not sure that we found everything on this challenge, but here is the flag.

**Flag : SWORDFISH**

## Author Note 

Thanks to Offsec, ARG SOC, and the Kali Linux team for those awesome puzzle! It was really funny to solve them, meet some great people on the discord. A lot of fun!

Special thanks to :
* RipVanWinkle - Contributor of **ARTIC1E.m4v**
* sawtooth - Contributor of **BBS-1995.mov**
* C45mb0 - Contributor of **BT-adv3rt.mkv** and **7V-Static.wmv**
* Willvoid - Contributor of **co22upted.flv** and **h45hc4t.avi**
* Beamofoldlight - Contributor of **dia6r4m.mp4**
* Sal3m - Contributor of **ki5met.mpeg**
* obafgkm - Contributor of **RG8.asf**
* EizAKme - Contributor of **S4nt4.jpg**

And of course, thanks to my teammate from my new **Godzill'hack** team!
