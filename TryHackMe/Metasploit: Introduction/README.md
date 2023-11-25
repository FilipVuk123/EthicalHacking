https://tryhackme.com/room/metasploitintro


# Intro

Metasploit is the most widely used exploitation framework. Metasploit is a powerful tool that can support all phases of a penetration testing engagement, from information gathering to post-exploitation.


The Metasploit Framework is a set of tools that allow information gathering, scanning, exploitation, exploit development, post-exploitation, and more. While the primary usage of the Metasploit Framework focuses on the penetration testing domain, it is also useful for vulnerability research and exploit development.


The Metasploit Framework is a set of tools that allow information gathering, scanning, exploitation, exploit development, post-exploitation, and more. While the primary usage of the Metasploit Framework focuses on the penetration testing domain, it is also useful for vulnerability research and exploit development.


# Main Components of Metasploit
Before diving into modules, it would be helpful to clarify a few recurring concepts: vulnerability, exploit, and payload.

- Exploit: A piece of code that uses a vulnerability present on the target system.
- Vulnerability: A design, coding, or logic flaw affecting the target system. The exploitation of a vulnerability can result in disclosing confidential information or allowing the attacker to execute code on the target system.
- Payload: An exploit will take advantage of a vulnerability. However, if we want the exploit to have the result we want (gaining access to the target system, read confidential information, etc.), we need to use a payload. Payloads are the code that will run on the target system.


You will see four different directories under payloads: adapters, singles, stagers and stages.

- Adapters: An adapter wraps single payloads to convert them into different formats. For example, a normal single payload can be wrapped inside a Powershell adapter, which will make a single powershell command that will execute the payload.
- Singles: Self-contained payloads (add user, launch notepad.exe, etc.) that do not need to download an additional component to run.
- Stagers: Responsible for setting up a connection channel between Metasploit and the target system. Useful when working with staged payloads. “Staged payloads” will first upload a stager on the target system then download the rest of the payload (stage). This provides some advantages as the initial size of the payload will be relatively small compared to the full payload sent at once.
- Stages: Downloaded by the stager. This will allow you to use larger sized payloads.


### Q1. What is the name of the code taking advantage of a flaw on the target system?
Exploit

### Q2. What is the name of the code that runs on the target system to achieve the attacker's goal?
Payload

### Q3. What are self-contained payloads called?
Singles

### Q4. Is "windows/x64/pingback_reverse_tcp" among singles or staged payload?
Singles


# Msfconsole


### Q1 How would you search for a module related to Apache?
search apache

### Q2. Who provided the auxiliary/scanner/ssh/ssh_login module?
todb

# Working with modules

commands: use, show options, set, search, unset, unset all, setg, unsetg, back, run/exploit, check sessions 

### Q1. How would you set the LPORT value to 6666?
set LPORT 6666

### Q2. How would you set the global value for RHOSTS  to 10.10.19.23 ?
setg RHOSTS 10.10.19.23

### Q3. What command would you use to clear a set payload?
unset PAYLOAD

### Q4. What command do you use to proceed with the exploitation phase?
exploit




