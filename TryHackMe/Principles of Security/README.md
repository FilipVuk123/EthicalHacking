https://tryhackme.com/room/principlesofsecurity


# Intro

The following room is going to outline some of the fundamental principles of information security. The frameworks used to protect data and systems to the elements of what exactly makes data secure.

The measures, frameworks and protocols discussed throughout this room all play a small part in "Defence in Depth."

# The CIA Triad

## Confidentiality

This element is the protection of data from unauthorized access and misuse. Organisations will always have some form of sensitive data stored on their systems. To provide confidentiality is to protect this data from parties that it is not intended for.

There are many real-world examples for this, for example, employee records and accounting documents will be considered sensitive. Confidentiality will be provided in the sense that only HR administrators will access employee records, where vetting and tight access controls are in place. Accounting records are less valuable (and therefore less sensitive), so not as stringent access controls would be in place for these documents. Or, for example, governments using a sensitivity classification rating system (top-secret, classified, unclassified)


## Integrity

The CIA triad element of integrity is the condition where information is kept accurate and consistent unless authorized changes are made. It is possible for the information to change because of careless access and use, errors in the information system, or unauthorized access and use. In the CIA triad, integrity is maintained when the information remains unchanged during storage, transmission, and usage not involving modification to the information. Steps must be taken to ensure data cannot be altered by unauthorised people (for example, in a breach of confidentiality).


Many defences to ensure integrity can be put in place. Access control and rigorous authentication can help prevent authorized users from making unauthorized changes. Hash verifications and digital signatures can help ensure that transactions are authentic and that files have not been modified or corrupted.


## Availability

In order for data to be useful, it must be available and accessible by the user.

The main concern in the CIA triad is that the information should be available when authorised users need to access it.

Availability is very often a key benchmark for an organisation. For example, having 99.99% uptime on their websites or systems (this is laid out in Service Level Agreements). When a system is unavailable, it often results in damage to an organisations reputation and loss of finances. Availability is achieved through a combination of many elements, including:


Having reliable and well-tested hardware for their information technology servers (i.e. reputable servers)
Having redundant technology and services in the case of failure of the primary
Implementing well-versed security protocols to protect technology and services from attack


### Q1. What element of the CIA triad ensures that data cannot be altered by unauthorised people?
integrity

### Q2. What element of the CIA triad ensures that data is available?
availability

### Q3. What element of the CIA triad ensures that data is only accessed by authorised people?
confidentiality


# Principles of Privileges

Two key concepts are used to assign and manage the access rights of individuals, two key concepts are used: Privileged Identity Management (PIM) and Privileged Access Management (or PAM for short).

Initially, these two concepts can seem to overlap; however, they are different from one another. PIM is used to translate a user's role within an organisation into an access role on a system. Whereas PAM is the management of the privileges a system's access role has, amongst other things.



### Q1. What does the acronym "PIM" stand for?
Privileged Identity Management

### Q2. What does the acronym "PAM" stand for?
Privileged Access Management

### Q3. If you wanted to manage the privileges a system access role had, what methodology would you use?
PAM

### Q4. If you wanted to create a system role that is based on a users role/responsibilities with an organisation, what methodology is this?
PIM


# Security Models Continued
Let's explore some popular and effective security models used to achieve the three elements of the CIA triad.

## The Bell-La Padula Model

The Bell-La Padula Model is used to achieve confidentiality. This model has a few assumptions, such as an organisation's hierarchical structure it is used in, where everyone's responsibilities/roles are well-defined.

The model works by granting access to pieces of data (called objects) on a strictly need to know basis. This model uses the rule "no write down, no read up".

## Biba Model

The Biba model is arguably the equivalent of the Bell-La Padula model but for the integrity of the CIA triad.

This model applies the rule to objects (data) and subjects (users) that can be summarised as "no write up, no read down". This rule means that subjects can create or write content to objects at or below their level but can only read the contents of objects above the subject's level.


### Q1. What is the name of the model that uses the rule "can't read up, can read down"?
The Bell-LaPadula Model

### Q2. What is the name of the model that uses the rule "can read up, can't read down"?
The Biba Model

### Q3. If you were a military, what security model would you use?
The Bell-LaPadula Model

### Q4. If you were a software developer, what security model would the company perhaps use?
The Biba Model



# Threat Modelling & Incident Response

Threat modelling is the process of reviewing, improving, and testing the security protocols in place in an organisation's information technology infrastructure and services.

The threat modelling process is very similar to a risk assessment made in workplaces for employees and customers. The principles all return to:

- Preparation
- Identification
- Mitigations
- Review


It is, however, a complex process that needs constant review and discussion with a dedicated team. An effective threat model includes:

- Threat intelligence
- Asset identification
- Mitigation capabilities
- Risk assessment


To help with this, there are frameworks such as STRIDE (Spoofing identity, Tampering with data, Repudiation threats, Information disclosure, Denial of Service and Elevation of privileges) and PASTA (Process for Attack Simulation and Threat Analysis) infosec never tasted so good!


A breach of security is known as an incident. And despite all rigorous threat models and secure system designs, incidents do happen. Actions taken to resolve and remediate the threat are known as Incident Response (IR) and are a whole career path in cybersecurity.


An incident is responded to by a Computer Security Incident Response Team (CSIRT) which is prearranged group of employees with technical knowledge about the systems and/or current incident. 

### Q. What model outlines "Spoofing"?
STRIDE

### Q. What does the acronym "IR" stand for?
Incident Response

### Q. You are tasked with adding some measures to an application to improve the integrity of data, what STRIDE principle is this?
Tampering

### Q. An attacker has penetrated your organisation's security and stolen data. It is your task to return the organisation to business as usual. What incident response stage is this? 
Recovery
