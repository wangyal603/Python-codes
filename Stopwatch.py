#Simple stopwatch in python

import time
g=1
s=0
m=0
h=0
t="a"
y=0
while g==1:
  print s,":",m,":",h,t,"m"
  s=s+1
  if s==60:
    s=0
    m=m+1
    if m==60:
      m=0
      h=h+1
      y=y+1
      if h==12:
        h=0
        if y==12:
          t="p"
          if y==24:
            y=0
            t="a"
    
        
  time.sleep(0)
      
