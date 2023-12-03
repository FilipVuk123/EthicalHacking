https://tryhackme.com/room/vulnerabilities101

# Introduction to Vulnerabilities

A vulnerability in cybersecurity is defined as a weakness or flaw in the design, implementation or behaviours of a system or application. An attacker can exploit these weaknesses to gain access to unauthorised information or perform unauthorised actions. 

For example, NIST defines a vulnerability as “weakness in an information system, system security procedures, internal controls, or implementation that could be exploited or triggered by a threat source”.

Vulnerabilities can originate from many factors, including a poor design of an application or an oversight of the intended actions from a user.

# Scoring Vulnerabilities (CVSS & VPR)

Vulnerability management is the process of evaluating, categorising and ultimately remediating threats (vulnerabilities) faced by an organisation.
It is arguably impossible to patch and remedy every single vulnerability in a network or computer system and sometimes a waste of resources.

Vulnerability scoring serves a vital role in vulnerability management and is used to determine the potential risk and impact a vulnerability may have on a network or computer system. For example, the popular Common Vulnerability Scoring System (CVSS) awards points to a vulnerability based upon its features, availability, and reproducibility.



# Vulnerability Databases

1. NVD (National Vulnerability Database)

2. Exploit-DB

## NVD

The National Vulnerability Database is a website that lists all publically categorised vulnerabilities. In cybersecurity, vulnerabilities are classified under “Common Vulnerabilities and Exposures” (Or CVE for short).

These CVEs have the formatting of CVE-YEAR-IDNUMBER. For example, the vulnerability that the famous malware WannaCry used was CVE-2017-0144.


## Exploit-DB

Exploit-DB is a resource that we, as hackers, will find much more helpful during an assessment. Exploit-DB retains exploits for software and applications stored under the name, author and version of the software or application.

We can use Exploit-DB to look for snippets of code (known as Proof of Concepts) that are used to exploit a specific vulnerability.

# An Example of Finding a Vulnerability


For example, in the screenshot below, we can see that the name and version number of this application is “Apache Tomcat 9.0.17”

With this information in hand, let’s use the search filter on Exploit-DB to look for any exploits that may apply to “Apache Tomcat 9.0.17”.

Great! After searching Exploit-DB, there are a total of five exploits that may be useful to us for this specific version of the application. 