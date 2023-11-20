import cv2
import os
import string

img=cv2.imread("scrtMsg.jpg")   #file path

msg=input("Enter your secret message:")
password=input("Enter your password:")

d={ }
c={ }    #dictionaries to ascii and pixcel value comparision

for i in range(255):   #max bit range upto ascii value
    d[chr(i)]=i    #converting scrt msg to i.e char to ascii value
    c[i]=chr(i)   #storing charcter values

m=0
n=0
z=0         #rgb

for i in range(len(msg)):
    img[n,m,z]=d[msg[i]]   #each charcter we are storing in image
    n=n+1
    m=m+1
    z=(z+1)%3  #rotating 3 colors for iteration

cv2.imwrite("stegofile.jpg",img)
os.system("start stegofile.jpg")

#decrypt
message=" "

n=0
m=0
z=0

pas=input("Enter your password:")

if password==pas:
    for i in range(len(msg)):
        message=message+c[img[n,m,z]]  #original charcter to message
        n=n+1
        m=m+1
        z=(z+1)%3
    print("Decrypted message",message)
else:
    print("password not valid")