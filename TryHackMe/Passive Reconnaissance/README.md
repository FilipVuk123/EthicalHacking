https://tryhackme.com/room/passiverecon


# Intro

In this room, after we define passive reconnaissance and active reconnaissance, we focus on essential tools related to passive reconnaissance. We will learn three command-line tools:

- whois to query WHOIS servers
- nslookup to query DNS servers
- dig to query DNS servers

We use whois to query WHOIS records, while we use nslookup and dig to query DNS database records. These are all publicly available records and hence do not alert the target.

We will also learn the usage of two online services:

- DNSDumpster
- Shodan.io

These two online services allow us to collect information about our target without directly connecting to it.




# Passive vs Active Recon
Reconnaissance (recon) can be defined as a preliminary survey to gather information about a target. It is the first step in The Unified Kill Chain to gain an initial foothold on a system. We divide reconnaissance into:

- Passive Reconnaissance
- Active Reconnaissance

In passive reconnaissance, you rely on publicly available knowledge. It is the knowledge that you can access from publicly available resources without directly engaging with the target. 

Passive reconnaissance activities include many activities, for instance:

- Looking up DNS records of a domain from a public DNS server.
- Checking job ads related to the target website.
- Reading news articles about the target company.


Active reconnaissance, on the other hand, cannot be achieved so discreetly. It requires direct engagement with the target.

Examples of active reconnaissance activities include:

- Connecting to one of the company servers such as HTTP, FTP, and SMTP.
- Calling the company in an attempt to get information (social engineering).
- Entering company premises pretending to be a repairman.


### Q1. You visit the Facebook page of the target company, hoping to get some of their employee names. What kind of reconnaissance activity is this? (A for active, P for passive)
P


### Q2. You ping the IP address of the company webserver to check if ICMP traffic is blocked. What kind of reconnaissance activity is this? (A for active, P for passive)
A

### Q3. You happen to meet the IT administrator of the target company at a party. You try to use social engineering to get more information about their systems and network infrastructure. What kind of reconnaissance activity is this? (A for active, P for passive)
A


# Whois

WHOIS is a request and response protocol that follows the RFC 3912 specification. A WHOIS server listens on TCP port 43 for incoming requests. The domain registrar is responsible for maintaining the WHOIS records for the domain names it is leasing. The WHOIS server replies with various information related to the domain requested. Of particular interest, we can learn:

- Registrar: Via which registrar was the domain name registered?
- Contact info of registrant: Name, organization, address, phone, among other things. (unless made hidden via a privacy service)
- Creation, update, and expiration dates: When was the domain name first registered? When was it last updated? And when does it need to be renewed?
- Name Server: Which server to ask to resolve the domain name?

usage: whois tryhackme.com


### Q1. When was TryHackMe.com registered?
20180705

### Q2. What is the registrar of TryHackMe.com?
namecheap.com

### Q3. Which company is TryHackMe.com using for name servers?
cloudflare.com



# nslookup and dig
Find the IP address of a domain name using nslookup, which stands for Name Server Look Up.

usage: nslookup [-option] [name | -] [server]
 

For more advanced DNS queries and additional functionality, you can use dig, the acronym for “Domain Information Groper,” if you are curious. Let’s use dig to look up the MX records and compare them to nslookup. We can use dig DOMAIN_NAME, but to specify the record type, we would use dig DOMAIN_NAME TYPE.

usage: dig @server name type


### Q1. Check the TXT records of thmlabs.com. What is the flag there?
dig  thmlabs.com TXT -> copy the flag

# DNSDumpster

https://dnsdumpster.com/

### Q1. Lookup tryhackme.com on DNSDumpster. What is one interesting subdomain that you would discover in addition to www and blog?
remote

# Shodan.io
https://www.shodan.io/


### Q1. According to Shodan.io, what is the 2nd country in the world in terms of the number of publicly accessible Apache servers?
Germany

### Q2. Based on Shodan.io, what is the 3rd most common port used for Apache?
8080

### Q3. Based on Shodan.io, what is the 3rd most common port used for nginx?
5001

# Tools used: dig, nslookup, whois, shodan, dnsdumpster