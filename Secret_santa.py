from random import shuffle

Santa =['Pradhyumna',
'Krithika',
'Apoorva',
'Akshay',
'Azhar',
'Shiva',
'Sukesh',
'Sree',
'Abhishek',
'Anusha',
'Nick',
'Rahman',
'Lakshmi',
'Nikita',
'Shahab',
'Karthikeya',
'Krishna Chaitanya',
'Padmaja',
'Raghav',
'Karan Shah',
'Khushboo',
'A S K Chaitanya Reddy',
'Yamini',
'Kishore',
'Veena',
'Madhu',
'Santosh',
'Varun']
#print(len(Santa))
Flag= 0
Santee=Santa.copy()
shuffle(Santa)
shuffle(Santee)
length = len(Santa)
'''while(Flag!=length):
    for i in range(0,length):
        if(Santa[i]!=Santee[i]):
            Flag= Flag+1
        else:
            shuffle(Santa)
            Flag=0
            i=0'''
          
#if(Flag==28):
for x in range(0,length):
    print("{}-{}".format(Santa[x],Santee[x]))