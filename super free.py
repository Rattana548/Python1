add = float(input("Enter amount : "))
rate = float(input("Enter rate : "))
year = int(input("Enter year : "))

addamount = add * (1 + rate/100 ) ** year
print ("Total :",round(addamount,2),"\n")



addamount1 = add * (1+ rate/100) ** 1
print ("One Year : " , round(addamount1,2) , "\n")
addamount1 = add * (1+ rate/100) ** 2
print ("Two Year : " , round(addamount1,2) , "\n")
addamount1 = add * (1+ rate/100) ** 3
print ("Three Year : " , round(addamount1,2) , "\n")
addamount1 = add * (1+ rate/100) ** 4
print ("Four Year : " , round(addamount1,2) , "\n")
addamount1 = add * (1+ rate/100) ** 5
print ("Five Year : " , round(addamount1,2) , "\n")
addamount1 = add * (1+ rate/100) ** 6
print ("Six Year : " , round(addamount1,2) , "\n")
addamount1 = add * (1+ rate/100) ** 7
print ("Seven Year : " , round(addamount1,2) , "\n")
addamount1 = add * (1+ rate/100) ** 8
print ("Eight Year : " , round(addamount1,2) , "\n")
addamount1 = add * (1+ rate/100) ** 9
print ("Nine Year : " , round(addamount1,2) , "\n")
addamount1 = add * (1+ rate/100) ** 10
print ("Ten Year : " , round(addamount1,2) , "\n")
