loop=0
while(loop<100):
  loop-=1
  file=open("LOGS/filename"+str(loop)+".txt",w)
  file.write("\n Duplicate file")
  file.close()
