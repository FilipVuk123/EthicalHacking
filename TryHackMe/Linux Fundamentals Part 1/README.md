https://tryhackme.com/room/linuxfundamentalspart1

# A Bit of Background on Linux

The name "Linux" is actually an umbrella term for multiple OS's that are based on UNIX (another operating system). Thanks to UNIX being open-source, variants of Linux comes in all shapes and sizes - suited best for what the system is being used for.

For example, Ubuntu & Debian are some of the more commonplace distributions of Linux because it is so extensible. I.e. you can run Ubuntu as a server (such as websites & web applications) or as a fully-fledged desktop. For this series, we're going to be using Ubuntu.

### Q. Research: What year was the first release of a Linux operating system?
1991


# Interacting With Your First Linux Machine (In-Browser)



# Running Your First few Commands


### Q. If we wanted to output the text "TryHackMe", what would our command be?
echo TryHackMe

### Q. What is the username of who you're logged in as on your deployed Linux machine?
tryhackme


# Interacting With the Filesystem!

### Q. On the Linux machine that you deploy, how many folders are there?
4

### Q. Which directory contains a file? 
folder4

### Q. What is the contents of this file?
Hello World

### Q. Use the cd command to navigate to this file and find out the new current working directory. What is the path?
/home/tryhackme/folder4


# Searching for Files



# An Introduction to Shell Operators


### Q. If we wanted to run a command in the background, what operator would we want to use?
&

### Q. If I wanted to replace the contents of a file named "passwords" with the word "password123", what would my command be?
echo password123 > passwords

### Q. Now if I wanted to add "tryhackme" to this file named "passwords" but also keep "passwords123", what would my command be
echo tryhackme >> passwords


# Conclusions & Summaries


