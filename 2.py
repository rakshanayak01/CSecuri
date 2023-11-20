#exor operation between secrete mss and key for converting msg into a stego object
import cv2
import os
import string

d={ }
c={ }    #dictionaries to ascii and pixcel value comparision

for i in range(255):   #max bit range upto ascii value
    d[chr(i)]=i    #converting scrt msg to i.e char to ascii value
    c[i]=chr(i)   #storing charcter values

x=cv2.imread("scrtMsg.jpg")   #file path

i=x.shape[0]
j=x.shape[1]
print(i,j)

key=input("Enter your secret key:")
text=input("Enter data to hide:")

k1=0
tln=len(text)
z=0     #decides plane
n=0     #decides row
m=0     #decides column

l=len(text)

for i in range(l):
    x[n,m,z]=d[text[i]]^d[key[k1]]   #each charcter we are storing in image
    n=n+1
    m=m+1
    m=(m+1)%3  #rotating 3 colors for iteration
    k1=(k1+1)%len(key)

cv2.imwrite("stegofile.jpg",x)
os.startfile("stegofile.jpg")
print("Data hiding in image completed successfully")

#decrypt
k1=0
tln=len(text)
n=0
m=0

ch=int(input("Enter 1 to extract data from image:"))

if ch==1:
    key1=input("Re enter the key to extract:")
    decrypt=" "

    if key==key1:
        for i in range(l):
            decrypt+=c[x[n,m,z]^d[key[k1]]]  #original charcter to message
            n=n+1
            m=m+1
            m=(m+1)%3
            k1=(k1+1)%len(key)
        print("Encrypted message",decrypt)
    else:
        print("Key doesnt match")
else:
    print("Thank you")