https://tryhackme.com/room/linuxmodules


# du

du is a command in linux (short for disk usage) which helps you identify what files/directories are consuming how much space. If you run a simple du command in terminal...

# Grep, Egrep, Fgrep

The official documentation says, The grep filter searches a file for a particular pattern of characters, and displays all lines that contain that pattern. The pattern that is searched in the file is referred to as the regular expression

egrep and fgrep are no different from grep(other than 2 flags that can be used with grep to function as both). In simple words, egrep matches the regular expressions in a string, and fgrep searches for a fixed string inside text. Now grep can do both their jobs by using -E and -F flag, respectively.

In other terms, grep -E functions same as egrepand grep -F functions same as fgrep.

# Did someone said STROPS?

String Manipulations (STRing OPerationS)

For strops, we have the following tools that I always keep in my arsenal and you should too:

- tr
- awk
- sed
- xargs
Other commands to be familiar with:

- sort
- uniq


# tr

Translate command(tr) can help you in number of ways, ranging from changing character cases in a string to replacing characters in a string. It's awesome at it's usage. Plus, it's the easiest command and a must know module for quick operations on strings.

Syntax: tr [flags] [source]/[find]/[select] [destination]/[replace]/[change]



# awk
This is the most-est powerful tool in my arsenal, I can't think of any other command that can do something and not awk.

Awk is a scripting language used for manipulating data and generating reports.The awk command programming language requires no compiling, and allows the user to use variables, numeric functions, string functions, and logical operators.

Syntax: awk [flags] [select pattern/find(sort)/commands] [input file]

# sed

sed(Stream EDitor) is a tool that can perform a number of string operations. Listing a few, could be: FIND AND REPLACE, searching, insertion, deletion.

Syntax: sed [flags] [pattern/script] [input file]


# xargs

xargs, a very simple command to use when it comes to make passed string a command's argument, technically, positional argument. The official documentation says, xargs is a command line tool used to build and execute command from the standard input. 




# sort and uniq

sort command, as the name suggests sorts the lines alphabetically and numerically, automatically. All you got to do is pipe the stdin into sort command.

Unique command filters the output (from either a file or stdin) to remove any duplicates

# cURL

cURL(stands for crawl URL; It outputs the data of a URLs webpage in a raw format). Another amazing command to perform activities that you can do with your browser, in just a terminal way. You can't download cat pictures from a direct google search and right clicking > save the image. But with a little grepping and pattern matching iframes, that can be possible too. 



# wget

You definitely have known the command line way of downloading stuff with wget(web-get) command, and thus this is gonna be a quick guide to that tool.

Syntax: wget protocol://url.com/

# xxd

xxd, which is well known for hexdumps or even the reverse. This command is not very vast to explore, but still knowing this command thoroughly will help you handling hex strings and hex digits. Whether you're playing ctfs, or bypassing JWT with automation, xxd can do it all. This command can take input from a file or the input can be passed through piping or redirection.



# Other modules

- gpg command

Sidenote: GPG(Gnu Privacy Guard) and PGP(Pretty Good Privacy) are 2 different types of encryption. PGP is based on RSA encryption, whereas GPG(open-source) is a re-write of PGP and by default uses AES encryption.

- tar command

Whether if it is a gzip archive or a bzip archive, encrypting and decrypting can be easily done by this tool. Do check out the man page for tar man tar. 

- id/pwd/uname commands

Let's not forget the legends that we deploy on the battlefield after getting init shell access on a machine.

- ps/kill commands

List processes, and kill processes with PID. To know more about ps command you can find some help here.

- base64 command

Why go to online sites when you can decode base32 and base64 at your own terminal.

