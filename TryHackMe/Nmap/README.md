https://tryhackme.com/room/furthernmap




# Introduction

When it comes to hacking, knowledge is power. The more knowledge you have about a target system or network, the more options you have available. This makes it imperative that proper enumeration is carried out before any exploitation attempts are made.


Say we have been given an IP (or multiple IP addresses) to perform a security audit on. Before we do anything else, we need to get an idea of the “landscape” we are attacking. What this means is that we need to establish which services are running on the targets. For example, perhaps one of them is running a webserver, and another is acting as a Windows Active Directory Domain Controller. The first stage in establishing this “map” of the landscape is something called port scanning. When a computer runs a network service, it opens a networking construct called a “port” to receive the connection.  Ports are necessary for making multiple network requests or having multiple services available. 

If we do not know which of these ports a server has open, then we do not have a hope of successfully attacking the target; thus, it is crucial that we begin any attack with a port scan. This can be accomplished in a variety of ways – usually using a tool called nmap, which is the focus of this room. Nmap can be used to perform many different kinds of port scan – the most common of these will be introduced in upcoming tasks; however, the basic theory is this: nmap will connect to each port of the target in turn. Depending on how the port responds, it can be determined as being open, closed, or filtered (usually by a firewall). Once we know which ports are open, we can then look at enumerating which services are running on each port – either manually, or more commonly using nmap.

### Q.What networking constructs are used to direct traffic to the right application on a server?
Ports

### Q.How many of these are available on any network-enabled computer?
65535

### Q.[Research] How many of these are considered "well-known"? (These are the "standard" numbers mentioned in the task)
1024




# Nmap Switches


### Q. What is the first switch listed in the help menu for a 'Syn Scan' (more on this later!)?
-sS

### Q. Which switch would you use for a "UDP scan"?
-sU

### Q. If you wanted to detect which operating system the target is running on, which switch would you use?
-O

### Q. Nmap provides a switch to detect the version of the services running on the target. What is this switch?
-sV

### Q. The default output provided by nmap often does not provide enough information for a pentester. How would you increase the verbosity?
-v

### Q. Verbosity level one is good, but verbosity level two is better! How would you set the verbosity level to two? (Note: it's highly advisable to always use at least this option)
-vv

### We should always save the output of our scans -- this means that we only need to run the scan once (reducing network traffic and thus chance of detection), and gives us a reference to use when writing reports for clients.

### Q. What switch would you use to save the nmap results in three major formats?

-oA
### Q. What switch would you use to save the nmap results in a "normal" format?

-oN
### Q. A very useful output format: how would you save results in a "grepable" format?

-oG
### Sometimes the results we're getting just aren't enough. If we don't care about how loud we are, we can enable "aggressive" mode. This is a shorthand switch that activates service detection, operating system detection, a traceroute and common script scanning.

### Q. How would you activate this setting?

-A
### Q. Nmap offers five levels of "timing" template. These are essentially used to increase the speed your scan runs at. Be careful though: higher speeds are noisier, and can incur errors!

### Q. How would you set the timing template to level 5?

-T5
### Q. We can also choose which port(s) to scan.

### Q. How would you tell nmap to only scan port 80?

-p 80
### Q. How would you tell nmap to scan ports 1000-1500?

-p 1000-1500
### A very useful option that should not be ignored:

### Q. How would you tell nmap to scan all ports?

-p-
### Q. How would you activate a script from the nmap scripting library (lots more on this later!)?

--script
### Q. How would you activate all of the scripts in the "vuln" category?

--script=vuln



# Scan Types Overview

When port scanning with Nmap, there are three basic scan types. These are:

- TCP Connect Scans (-sT)
- SYN "Half-open" Scans (-sS)
- UDP Scans (-sU)
Additionally there are several less common port scan types, some of which we will also cover (albeit in less detail). These are:

- TCP Null Scans (-sN)
- TCP FIN Scans (-sF)
- TCP Xmas Scans (-sX)



# Scan Types TCP Connect Scans

To understand TCP Connect scans (-sT), it's important that you're comfortable with the TCP three-way handshake.

For example, if a port is closed, RFC 9293 states that:

"... If the connection does not exist (CLOSED), then a reset is sent in response to any incoming segment except another reset. A SYN segment that does not match an existing connection is rejected by this means."

In other words, if Nmap sends a TCP request with the SYN flag set to a closed port, the target server will respond with a TCP packet with the RST (Reset) flag set. By this response, Nmap can establish that the port is closed.

If, however, the request is sent to an open port, the target will respond with a TCP packet with the SYN/ACK flags set. Nmap then marks this port as being open (and completes the handshake by sending back a TCP packet with ACK set).

This is all well and good, however, there is a third possibility.

What if the port is open, but hidden behind a firewall?

Many firewalls are configured to simply drop incoming packets. Nmap sends a TCP SYN request, and receives nothing back.

This can make it extremely difficult (if not impossible) to get an accurate reading of the target(s).

# Scan Types SYN Scans

As with TCP scans, SYN scans (-sS) are used to scan the TCP port-range of a target or targets; however, the two scan types work slightly differently. SYN scans are sometimes referred to as "Half-open" scans, or "Stealth" scans.

Where TCP scans perform a full three-way handshake with the target, SYN scans sends back a RST TCP packet after receiving a SYN/ACK from the server (this prevents the server from repeatedly trying to make the request).

This has a variety of advantages for us as hackers:

- It can be used to bypass older Intrusion Detection systems as they are looking out for a full three way handshake.
- SYN scans are often not logged by applications listening on open ports, as standard practice is to log a connection once it's been fully established. 
- Without having to bother about completing (and disconnecting from) a three-way handshake for every port, SYN scans are significantly faster than a standard TCP Connect scan.

There are, however, a couple of disadvantages to SYN scans, namely:

- They require sudo permissions[1] in order to work correctly in Linux. This is because SYN scans require the ability to create raw packets (as opposed to the full TCP handshake), which is a privilege only the root user has by default.
- Unstable services are sometimes brought down by SYN scans, which could prove problematic if a client has provided a production environment for the test.



# Scan Types UDP Scans

Unlike TCP, UDP connections are stateless. This means that, rather than initiating a connection with a back-and-forth "handshake", UDP connections rely on sending packets to a target port and essentially hoping that they make it. This makes UDP superb for connections which rely on speed over quality (e.g. video sharing), but the lack of acknowledgement makes UDP significantly more difficult (and much slower) to scan. The switch for an Nmap UDP scan is (-sU)


# Scan Types NULL, FIN and Xmas

As the name suggests, NULL scans (-sN) are when the TCP request is sent with no flags set at all. As per the RFC, the target host should respond with a RST if the port is closed.


FIN scans (-sF) work in an almost identical fashion; however, instead of sending a completely empty packet, a request is sent with the FIN flag (usually used to gracefully close an active connection). Once again, Nmap expects a RST if the port is closed.


As with the other two scans in this class, Xmas scans (-sX) send a malformed TCP packet and expects a RST response for closed ports. It's referred to as an xmas scan as the flags that it sets (PSH, URG and FIN) give it the appearance of a blinking christmas tree when viewed as a packet capture in Wireshark.

The expected response for open ports with these scans is also identical, and is very similar to that of a UDP scan. If the port is open then there is no response to the malformed packet. Unfortunately (as with open UDP ports), that is also an expected behaviour if the port is protected by a firewall, so NULL, FIN and Xmas scans will only ever identify ports as being open|filtered, closed, or filtered. If a port is identified as filtered with one of these scans then it is usually because the target has responded with an ICMP unreachable packet.


That said, the goal here is, of course, firewall evasion. Many firewalls are configured to drop incoming TCP packets to blocked ports which have the SYN flag set (thus blocking new connection initiation requests). By sending requests which do not contain the SYN flag, we effectively bypass this kind of firewall.

# Scan Types ICMP Network Scanning

To perform a ping sweep, we use the -sn switch in conjunction with IP ranges which can be specified with either a hypen (-) or CIDR notation. i.e. we could scan the 192.168.0.x network using:

- nmap -sn 192.168.0.1-254
or

- nmap -sn 192.168.0.0/24


The -sn switch tells Nmap not to scan any ports -- forcing it to rely primarily on ICMP echo packets (or ARP requests on a local network, if run with sudo or directly as the root user) to identify targets. In addition to the ICMP echo requests, the -sn switch will also cause nmap to send a TCP SYN packet to port 443 of the target, as well as a TCP ACK (or TCP SYN if not run as root) packet to port 80 of the target.


# NSE Scripts Overview

The Nmap Scripting Engine (NSE) is an incredibly powerful addition to Nmap, extending its functionality quite considerably. NSE Scripts are written in the Lua programming language, and can be used to do a variety of things: from scanning for vulnerabilities, to automating exploits for them. The NSE is particularly useful for reconnaisance, however, it is well worth bearing in mind how extensive the script library is.


There are many categories available. Some useful categories include:

- safe:- Won't affect the target
- intrusive:- Not safe: likely to affect the target
- vuln:- Scan for vulnerabilities
- exploit:- Attempt to exploit a vulnerability
- auth:- Attempt to bypass authentication for running services (e.g. Log into an FTP server anonymously)
- brute:- Attempt to bruteforce credentials for running services
- discovery:- Attempt to query running services for further information about the network (e.g. query an SNMP server).

# NSE Scripts Working with the NSE

In Task 3 we looked very briefly at the --script switch for activating NSE scripts from the vuln category using --script=vuln

Multiple scripts can be run simultaneously in this fashion by separating them by a comma. For example: --script=smb-enum-users,smb-enum-shares







# NSE Scripts Searching for Scripts




# Firewall Evasion

So, we need a way to get around this configuration. Fortunately Nmap provides an option for this: -Pn, which tells Nmap to not bother pinging the host before scanning it. 


The following switches are of particular note:

1. -f:- Used to fragment the packets (i.e. split them into smaller pieces) making it less likely that the packets will be detected by a firewall or IDS.
2. An alternative to -f, but providing more control over the size of the packets: --mtu <number>, accepts a maximum transmission unit size to use for the packets sent. This must be a multiple of 8.
3. --scan-delay <time>ms:- used to add a delay between packets sent. This is very useful if the network is unstable, but also for evading any time-based firewall/IDS triggers which may be in place.
4. --badsum:- this is used to generate in invalid checksum for packets. Any real TCP/IP stack would drop this packet, however, firewalls may potentially respond automatically, without bothering to check the checksum of the packet. As such, this switch can be used to determine the presence of a firewall/IDS.

# Practical


### Q. Does the target (MACHINE_IP)respond to ICMP (ping) requests (Y/N)?
N

### Q. Perform an Xmas scan on the first 999 ports of the target -- how many ports are shown to be open or filtered?
999

### Q. There is a reason given for this -- what is it?
Note: The answer will be in your scan results. Think carefully about which switches to use -- and read the hint before asking for help!

No Response

### Q. Perform a TCP SYN scan on the first 5000 ports of the target -- how many ports are shown to be open?
5

### Q. Deploy the ftp-anon script against the box. Can Nmap login successfully to the FTP server on port 21? (Y/N)
Y

