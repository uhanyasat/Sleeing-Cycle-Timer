# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 10:44:38 2021

@author: Sathish
"""


from datetime import datetime, timedelta  


# datetime object containing current date and time
now = datetime.now()
#print("now =", now)
# dd/mm/YY H:M:S
dt_string = now.strftime("%H:%M:%S")
print( dt_string)	
#Small Description about the code
print('Hello User!.The current time is :',dt_string)
print('------------------------------------------------')
print('------------------------------------------------')
print('You have five sleeping life cycle every day!')
print('------------------------------------------------')
print('------------------------------------------------')
print('''select mode to know about life cycles:
         1--To know about Wake up time
         2--To know about start of sleep time
      ''')


def sleep_cycle(start_time,i):
    
        updated_time = start_time + timedelta(minutes=105)
        print("Starting Time cycle {0} for Sleep:".format(i),now.strftime("%H:%M:%S") )
        print('You are having 15 minutes bonus time for preparation to get deep sleep!')
        print("Wake up time:",updated_time.strftime("%H:%M:%S") )
        
        return updated_time
   
def sleep_cycle2(wake_time,i):     
         updated_time = wake_time - timedelta(minutes=105)
         start_time = updated_time.strftime("%H:%M:%S")
         print("Starting Time cycle {0} for Sleep:".format(i))
         #print("Starting Time for Sleep:",S_T.strftime("%H:%M:%S") )
         print('You are having 15 minutes bonus time for preparation to get deep sleep!')
         print("Starting Time for Sleep:",start_time )
         return start_time
         
    
Refreshing_time=15# initialzing the refreshing time
Sleeping_life_cycle_time=90   #initializing the sleeping time
mode=int(input())
if mode==1:
    print('Enter 1 for current time to sleep or Enter 2 for specific time to sleep ')
    S_time=int(input())#prompt the user to get mode of time
    if S_time==1:
        start_time=datetime.now()
        for i in range (1,6):
            start_time=sleep_cycle(start_time,i)
            
    elif S_time==2:
        print('Enter the time in format H:M:S:')
        S_H=str(input('Time:'))#prompt the user to get starting time of sleep
        format = "%H:%M:%S" 
        S_T=datetime.strptime(S_H,format)
        start_time=S_T
        for i in range (1,6):
            start_time=sleep_cycle(start_time,i)
        
    else:
        print('Invalid option')
elif mode==2:#To know about wakeup time
     print('Enter the wake up time in format H:M:S:')
     W_H=str(input('Time:'))
     format = "%H:%M:%S" 
     W_T=datetime.strptime(W_H,format)
     i=5
     while i<=5:
         
         updated_time = W_T - timedelta(minutes=105)
         start_time = updated_time.strftime("%H:%M:%S")
         print("Starting Time cycle {0} for Sleep:".format(i))
         print('You are having 15 minutes bonus time for preparation to get deep sleep!')
         print("Starting Time for Sleep:",start_time )
         
         i-=1
         W_T=updated_time
         if i==0:
             break