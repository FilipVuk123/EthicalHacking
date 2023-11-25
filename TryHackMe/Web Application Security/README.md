https://tryhackme.com/room/introwebapplicationsecurity


# Intro

The idea of a web application is that it is a program running on a remote server. A server refers to a computer system running continuously to “serve” the clients.

Consider an online shopping application. The web application will read the data about the products and their details from a database server. A database is used to store information in an organized way. Examples include information about products, customers, and invoices. A database server is responsible for many functions, including reading, searching, and writing to the database.

Many companies offer bug bounty programs. A bug bounty program allows the company to offer a reward for anyone who discovers a security vulnerability (weakness) in the company’s systems. The main condition is that the found vulnerability is within the bug bounty scope and rules. Among many others, Google, Microsoft, and Facebook have bug bounty programs. Discovering a bug can earn you from a few hundred USD to tens of thousands of USD, depending on the severity of the vulnerability, i.e., the weakness you discovered.

### Q1. What do you need to access a web application?
Browser


# Web Application Security Risks

There are a few main categories of common attacks against web applications. Consider the following steps and related attacks.

- Log in at the website: The attacker can try to discover the password by trying many words. The attacker would use a long list of passwords with an automated tool to test them against the login page.
- Search for the product: The attacker can attempt to breach the system by adding specific characters and codes to the search term. The attacker’s objective is for the target system to return data it should not or execute a program it should not.
- Provide payment details: The attacker would check if the payment details are sent in cleartext or using weak encryption


## Identification and Authentication Failure
Identification refers to the ability to identify a user uniquely. In contrast, authentication refers to the ability to prove that the user is whom they claim to be. The online shop must confirm the user’s identity and authenticate them before they can use the system. However, this step is prone to different types of weaknesses. Example weaknesses include:

- Allowing the attacker to use brute force, i.e., try many passwords, usually using automated tools, to find valid login credentials.
- Allowing the user to choose a weak password. A weak password is usually easy to guess.
- Storing the users’ passwords in plain text. If the attacker manages to read the file containing the passwords, we don’t want them to be able to learn the stored password.

## Injection
An injection attack refers to a vulnerability in the web application where the user can insert malicious code as part of their input. One cause of this vulnerability is the lack of proper validation and sanitization of the user’s input.

## Cryptographic Failures
This category refers to the failures related to cryptography. Cryptography focuses on the processes of encryption and decryption of data. Encryption scrambles cleartext into ciphertext, which should be gibberish to anyone who does not have the secret key to decrypt it. In other words, encryption ensures that no one can read the data without knowing the secret key. Decryption converts the ciphertext back into the original cleartext using the secret key. Examples of cryptographic failures include

- Sending sensitive data in clear text, for example, using HTTP instead of HTTPS.
- Relying on a weak cryptographic algorithm. 
- Using default or weak keys for cryptographic functions. 


### Q1. You discovered that the login page allows an unlimited number of login attempts without trying to slow down the user or lock the account. What is the category of this security risk?
Identification and Authentication Failure


### Q2. You noticed that the username and password are sent in cleartext without encryption. What is the category of this security risk?
Cryptographic Failures


# Practical Example of Web Application Security



### Q1. Check the other users to discover which user account was used to make the malicious changes and revert them. After reverting the changes, what is the flag that you have received?
https://inventory-management.thm/activity?user_id=9 -> revert everything -> get the flag



