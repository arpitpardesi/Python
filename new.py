import os
import firebase as fb
firebase=fb.FirebaseApplication("https://attendence-33dad.firebaseio.com/")
a=os.getcwd()
if os.path.exists(a+"\\firebase.txt"):
    file1=open(a+"\\firebase.txt",'w')
    fb.put("User/","1",str(file1))
    file1.write("")