https://tryhackme.com/room/linuxstrengthtraining

ip = `10.10.234.3`

topson/topson


I will just paste the outputs of history command from the machine...


# Finding your way around linux - overview
# Working with files


cd chatlogs/
grep -iRl 'keyword'
less 2019-10-11 
cd ..
cat ReadMeIfStuck.txt 
find . -name "readME_hint.txt"
cd corperateFiles/RecordsFinances/
cat readME_hint.txt 
ls
cp -- '-MoveMe.txt' moveMeBackup.txt
cat moveMeBackup.txt 
ls
mv -- '-MoveMe.txt' '-march folder'
ls '-march folder'
cd -march\ folder/
cd -- -march\ folder/
ls
./-runME.sh 
cd
find . -name "ReadMeIfStuck.txt"
cat ReadMeIfStuck.txt 
ls
find . -name "additionalHINT"
cat channels/additionalHINT 
find . -name "telephone numbers"
ls corperateFiles/xch/telephone\ numbers/
cat corperateFiles/xch/telephone\ numbers/readME.txt 
find /home/topson/workflows/ -type f -newermt 2016-09-11 ! -newermt 2016-09-13
cat /home/topson/workflows/xft/eBQRhHvx
less /home/topson/workflows/xft/eBQRhHvx





# Hashing - introduction

https://md5hashing.net/hash/md5/5d7845ac6ee7cfffafc5fe5f35cf666d

f9d4049dd6a4dc35d40e5265954b2a46	md4	admin


b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3	sha1	letmein

┌──(kali㉿kali)-[~/Downloads]
└─$ john --format=raw-sha256 --wordlist=ww.mnf hash.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-SHA256 [SHA256 256/256 AVX2 8x])
Warning: poor OpenMP scalability for this hash type, consider --fork=6
Will run 6 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
unacvaolipatnuggi (?)     



# Decoding base64


base64 -d system\ AB/managed/encoded.txt > decodec.txt
less decodec.txt 
find . -name "ent.txt"
cat logs/zhc/ent.txt 


bfddc35c8f9c989545119988f79ccc77	md4	john

# Encryption/Decryption using gpg

find . -name "layer4.txt"
gpg system\ AB/keys/vnmA/layer4.txt 
cat layer4dec.txt 
find . -name "layer3.txt"
gpg oldLogs/2014-02-15/layer3.txt 
cat layer3dec.txt 
find . -name "layer2.txt"
gpg oldLogs/settings/layer2.txt
cat layer2dec.txt 
base64 -d layer2dec.txt layer2decdec.txt
base64 -d layer2dec.txt > layer2decdec.txt
cat layer2decdec.txt 
find . -name "layer1.txt"
gpg logs/zmn/layer1.txt 
cat layer1dec.txt 


# Cracking encrypted gpg files

gpg2john personal.txt.gpg > hash.txt

john --wordlist=data.txt --format-gpg hash.txt

valamanezivonia


gpg personal.txt.gpg (with password valamanezivonia)



# Reading SQL databases

find . -name "employees.sql"
cd serverLx/
mysql -u sarah -p (with password 'password')


mysql> source employees.sql
mysql> show databases;
mysql> use employees;
mysql> show tables;
mysql> describe employees;
mysql> select * from employees where last_name like '%{%}%';



# Final Challenge



