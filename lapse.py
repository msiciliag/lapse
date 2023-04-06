import time 
import os

global n
n = 0

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

def timer(duration):
    act = 0
    while(act < duration):
        mins = int((duration - act)/60)
        secs = (duration - act) - (mins*60)
        #TODO: salen varias g cuando los numeros son mas pequeños que 10 -> remainingg
        print("lapse{}> {} minute(s) and {} second(s) remaining".format(n, mins, secs), end="\r")
        time.sleep(1)
        act+=1

def run():
    global n
    c = "y"
    while(c == "y"):
        print("lapse> duration in mins?")
        duration = int(input())
        n+=1
        timer(duration*60)
        notify("take a breath", "you deserve it :)")
        print("\nlapse{}> continue session y/n?".format(n))
        c = input()

run()
print("lapse> you did {} lapses!".format(n))