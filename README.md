# Laocoon

This script was made for the [Hack@WPI 2020](http://hack.wpi.edu) hackathon.

## Usage
Run exploit.py with python3, enter a port, and connect to it with a reverse shell from the victim's machine.

## Inspiration
During penetration testing, after initial access is gained, privilege escalation must be performed to gain "root" privileges on the system. This can be done using kernel exploits if the Linux kernel is out of date. We decided that it would be a good idea to automate the process of looking for kernel exploits and testing them on a compromised system.

## What it does
There exists an API called searchsploit which allows the user to look up exploits for software. This application parses searchsploit output and hosts the exploits on a web server. The exploits are then downloaded to the victim's machine, are compiled, and are executed. The program then checks if the user ID (uid) is now 0 (root), at which point the program has succeeded.

## How we built it
We used preexisting tools and parsed and combined their functionalities to create one cohesive script that automates the entire process. The program was built with Python 3 and a variety of Bash and Python commands that are sent to the victim's machine.

## Challenges we ran into
The machine that we attacked for testing has lots of outdated software which made it difficult to find ways to execute certain commands on the system. There were many commands that did not exist, or were not new enough to work properly.
We also had lots of problems sending the script to the machine that was responsible for compiling and running the exploits. This python script could not be sent directly through sockets because of it's formatting and we could not use a tool like `wget` to download it from a webserver, so we had to figure out a way to send it in another format.
We first tried encoding the script in base64, but the machine did not have any way to decode it. We found that if we encoded the data in hex, we could decode it using `echo -e | cat`.

## Accomplishments that we're proud of

A working proof-of-concept. 

## What we learned

A lot of problem solving and network programming.

## What's next for Laocoon

- Implement automation for other privilege escalation vectors
- Refine the search for exploits more to reduce runtime
