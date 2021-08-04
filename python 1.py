#create variables
num=0
a = 1000
b = 10000 
c = 100000
us=0
option=0
#process

print("$ press w for convert number to word")
print("$ press c for convert Lanka rupees to USD")
num=int(input("please Enter the Amount:"))#INPUTS
option=input("Please Enter Your Option:")

if option in 'w':#input any number 0to 100000 to convert to word.
    
    f = { 0:'', 1: 'one',  2:'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine',10 : 'ten',11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',30 : 'thirty', 40 : 'forty', 50 : 'fifty', 
          60 : 'sixty',70 : 'seventy', 80 : 'eighty', 90 : 'ninety',100:'hundred' }#insert dictonary onece,tens,hundreds,thousands.
    if (num>c):
        print("Invalid Input ")
    elif (num==0):
        print("Zero")
    elif (num>0)and(num<20):
        print(">" ,f[num] ,"<") 
    elif (num>=20)and(num<=100):
        if (num%10==0):
            print(">" ,f[num] ,"<")
        else:                                                                                 #once
            print(">" ,f[num//10*10],f[num%10] ,"<")
    elif(num>100)and(num<a):
        if (num%100==0):
            print(">" ,f[num//100],"hundred" ,"<")
        elif (num%100>10) and (num%100<20):
            print(">" ,f[num//100],"hundred",f[num%100] ,"<")
        else:
            if num%100//10==0:                                                                 #selection part
                print(">" ,f[num//100],"hundred",f[num%100%10] ,"<")
            else:   
                print(">" ,f[num//100],"hundred",f[num%100//10*10],f[num%10] ,"<")
    elif(num>=a)and(num<b):
        if num%1000==0:
            print(">" ,f[num//1000],"hundred" ,"<")
        elif (num%a%100>10) and (num%a%100<20):
            print(">" ,f[num//a],"thousand",f[num%a%100] ,"<")
        else:
            if num%a//100==0:
                print(">" ,f[num//a],"thousand",f[num%a%100//10*10],f[num%a%100%10] ,"<")
            else:    
                print(">" ,f[num//a],"thousand",f[num%a//100],"hundred",f[num%a%100//10*10],f[num%a%100%10] ,"<")
    elif(num>=b)and(num<c):
        if num%10000==0:
            print(">" ,f[num//a],"hundred" ,"<")    
        elif (num//a>0) and (num//a<20):   
            print(">" ,f[num//a],"thousand",f[num%a//100],"hundred",f[num%a%100//10*10],f[num%a%100%10] ,"<")
        elif(num%a%100>10)and(num%a%100<20):
            print(">" ,f[num//a//10*10],f[num//a%10],"thousand",f[num%a//100],"hundred",f[num%a%100] ,"<")
        else:
            if num%a//100==0:
                    print(">" ,f[num//a//10*10],f[num//a%10],"thousand",f[num%a%100//10*10],f[num%a%100%10] ,"<")
            else:    
                    print(">" ,f[num//a//10*10],f[num//a%10],"thousand",f[num%a//100],"hundred",f[num%a%100//10*10],f[num%a%100%10] ,"<")
    elif num==100000:
        print('Hundred Thousand')#print 100000
elif option in 'c':
        
        print("Result: USD",round(num/200))#convert usd to Lanla RS

else:
        print(">Invalid Input<")
                




