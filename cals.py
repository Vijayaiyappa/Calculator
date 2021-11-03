'''
Author:  v-star
Date:  8-6-2019
course: python

Function: calculator
Description:  calculates the given number by user

eg: input 

2+(2+3)+(2+(2*2)-1)

what's new ?
well it excepts Round brackets just copy and paste  the example in input 
'''
import sys
d=0
val = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
opp = ("*", "+", "-", "/", 0, 0, 0, 0, 0, 0)
brackets=[]
pos1=0
pos2=0
try:
    userin = input("enter the value\n")
    # it will not except empty string
    if  userin == "":
        raise IndexError
except IndexError:
    print("please input a value")
userin = f"{userin}+()"
d=0
brackets=[]
end=0
countb=0
counte=0
while "(" and ")" in userin :
    if "(" and ")" in userin :

        #stores the index of round brackets in brackets variable
        for i2 in range(len(userin)):
            if userin[i2] in ["(", ")"]:
                brackets.append(i2)
    
    for i4 in range(len(brackets)):# countb and counte will store the count of opening round brackets and closing   round brackets
        if userin[brackets[i4]] in ["("] and d==0:
            countb=countb+1
        elif d==0:
            counte=counte+1


    try: # checks for the equality of opening and closing round brackets
        if countb!=counte:
            raise Exception
    except Exception:
        print("invalid input")
        sys.exit(1)


    f=0
    f2=0
    n3=0
    # it will format the string
    if len(brackets) == 2:
         userin=userin[:-3]# removing extra  +() when brackets length is 2 eg:2+3+() will be formatted into 2+3
         userin =f"({userin})"# adding extra round brackets at the begging and end of userin because to avoid the error in line 66
         user = userin[1:len(userin)-1]
         f2 = 1
         n3=1
    #checks whether userin index 0 equal to ( and userin index 1 is equal to )
    if userin[brackets[0]] == "(" and userin[brackets[ 1]] == ")" and f2==0:
        user = userin[(brackets[0] + 1):brackets[1]]
        f2=1
    # checks whether userin index 0 equal to ( and userin index 1 is equal to (
    elif userin[brackets[0]] == "(" and userin[brackets[1]] == "(":# handele
        for i in range(len(brackets)):
            # it is used to terminate the loop when ths condition satisfy  the if statement
            if userin[brackets[i]] == "(" and userin[brackets[i - 1]] == ")" and i - 1 != -1 :
                end = i - 1
                break
        store1 = brackets[0:end + 1] # stores begging and end of (( and ))
        a = ((len(store1)) / 2)# finding the midpoint store1
        a = int(a)
        user = userin[max(store1[:a]) + 1:min(store1[a:])]
        f=1

    user = f"{user}+0"
    res2 = []
    res1 = []
    oop = []
    p2 = 0
    integer = 0
    oppr = ""

    def add(value, ans):
        return ans + value

    def sub(value, ans):
        return ans - value

    def mult(value, ans):
        return ans*value

    def div(value, ans):
        return ans / value

    for i in range(len(user)):
        if user[i] in opp:# checking user input operators in  opp
            oppr = user[i]
            res2.append(integer)
            oop.append(oppr)
            res1.clear()

        elif user[i] in val:# checking user input number in  val
            res1.append(user[i])
            integer = "".join(res1)
            integer = int(integer)

    p3 = 0
    for n2 in range(len(oop) - 1):
        # if the index res2[0] ie p3 is equal to zero  then this will execute
        if p3 == 0:
            p3 = p3 + 2

            if oop[n2] == "*":
                d = res2[0] * res2[1]

            elif oop[n2] == "-":
                d = res2[0] - res2[1]

            elif oop[n2] == "+":
                d = res2[0] + res2[1]

            elif oop[n2] == "/":
                d = res2[0] / res2[1]

        else:

            if oop[n2] == "+":
                v = res2[p3]
                d = add(v, d)
                p3 = p3 + 1 #incrementing by 1 so we can iterate through the list res2 ,ie v=res2[p3]


            elif oop[n2] == "/":
                v = res2[p3]
                d = div(v, d)
                p3 = p3 + 1


            elif oop[n2] == "*":
                v = res2[p3]
                d = mult(v, d)
                p3 = p3 + 1

            elif oop[n2] == "-":
                v = res2[p3]
                d = sub(v, d)
                p3 = p3 + 1


    if n3 != 1: # in the line 56 when  that statement is true  n3 will be initialized to 1
        print(userin[:-3]) # removing extra round brackets at the end of the index
    else:
        print(userin)

    if f == 1: # if the userin is in has double round brackets ,ie (( this will be executed
        d = str(d)
        userin = f"{userin[:(max(store1[:a]))]}{d}{userin[(min(store1[a:]) + 1):]}"
        store1.clear()

    if f2==1: # if the userin is in has 1 opening round  brackets and 1 closing round brackets this will be  executed,ie ()
        d=str(d)
        if brackets[0] != 0: # this will be  not executed when userin is in this form num1 num2 num_n +() eg:23+()
            userin = f"{userin[:brackets[0]]}{d}{userin[brackets[1] + 1:]}"
        else:
            userin=f"{d}{userin[brackets[1]+1:]}"
    brackets.clear()

print(d)
