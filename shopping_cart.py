l=1100
l=l*1
lg=((13/100)*1500)
l=l+lg
u=900
u=u*4
ug=((7/100)*900);
u=u+ug
c=200
c=c*3
cg=((28/100)*200);
c=c+cg
h=100
h=h*2
hg=((0/100)*100);
h=h+hg
print("the gst for leather wallet is",lg)
print("the gst for umbrella is",ug)
print("the gst for cigarette is",cg)
print("the gst for honey is",hg)
max1=max(lg,ug,cg,hg)
print("the max gst paid is",max1)
if(max1==lg):
    print("the max gst paid for the item is leather")
elif(max1==ug):
    print("the max gst paid is for umbrella")
elif(max1==cg):
    print("the max gst paid is for cigaretee")
elif(max1==hg):
    print("the max gst paid is for honey")
sum=l+c+u+h
print("the total amount to be paid to shopkepper is",sum)

