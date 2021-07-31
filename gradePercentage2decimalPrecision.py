from typing import Text


def grade(subject,name):

    if subject >= 90 :
        txt = "{:.2f}".format(subject)
        print("harold has S grade " + name + " and his percentage is ",txt)
    elif subject >= 80 :
        txt = "{:.2f}".format(subject)
        print("harold has A grade " + name + " and his percentage is ",txt)
    elif subject >= 70 :
        txt = "{:.2f}".format(subject)
        print("harold has B grade " + name + " and his percentage is ",txt)
    elif subject >= 60 :
        txt = "{:.2f}".format(subject)
        print("harold has C grade " + name + " and his percentage is ",txt)
    elif subject >= 40 :
        txt = "{:.2f}".format(subject)
        print("harold has D grade " + name + " and his percentage is ",txt)
    elif subject < 40 :
        txt = "{:.2f}".format(subject)
        print("harold has E grade " + name + " and his percentage is ",txt)

for i in range(0,1):
    phy=float(input("Enter the Marks for Physics"))
    chem=float(input("Enter the Marks for Chemistry"))
    bio=float(input("Enter the Marks for Biology"))
    math=float(input("Enter the Marks for Maths"))
    comp=float(input("Enter the Marks for Computer"))
phy_p = phy % 100
chem_p = chem % 100
bio_p = bio % 100
math_p = math % 100
comp_p = comp % 100
s1 = "Physics"
s2 = "Chemistry"
s3 = "Biology"
s4 = "Maths"
s5 = "Computer"
grade(phy_p,s1)
grade(chem_p,s2)
grade(bio_p,s3)
grade(math_p,s4)
grade(comp_p,s5)

