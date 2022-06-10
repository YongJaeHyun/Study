import requests
import os

while 1:
  os.system("clear")
  print("Welcome to IsItDown.py")
  print("Please write a URLs You want to check. (separated by comma)")

  urls_input = input().lower().split(",")
  urls = [url.strip() for url in urls_input]

  for url in urls:
    if url.find("http") == -1:
      url = "http://" + url
    if url.find(".") == -1:
      url = url + ".com"
    try:
      r = requests.get(f"{url}")
      print(f"{url} is Up!")
    except requests.exceptions.ConnectionError:
      print(f"{url} is Down!")
      
  restart_input = ""
  cnt = 0
  while restart_input != "y" and restart_input != "n":
    if cnt >= 1:
      print(f"{restart_input} is not a valid answer")
    restart_input = input("Do You want to start over? y/n ").strip().lower()
    cnt += 1
    
  if restart_input == "n":
    print("------------------------Okay Bye!-------------------------")
    break