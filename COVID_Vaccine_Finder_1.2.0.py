# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 10:08:42 2021

@author: soc
"""
from cowin_api import CoWinAPI
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
#from inputimeout import inputimeout, TimeoutOccurred

from cowin_api.constants import Constants

def today() -> str:
    return datetime.now().strftime(Constants.DD_MM_YYYY)



  
# number of elemetns as input
def UserInput():
    n = int(input("Type number of persons/groups you want to send a whatsapp notification and press Enter key: "))
    name_list = []
    # iterating till the range
    print("Type in name of each person/group/number and press enter ")
    for i in range(0, n):
        ele = (input())
        name_list.append(ele)
    
    print("Enter Age Limit. i.e => 18 or 45")
    min_age_limit = int(input())

    print("Enter Dose i.e => 1 or 2")
    Dose = int(input())

    DoseName = f'available_capacity_dose{Dose}'
    print("Find the below details you have entered")
    print(f"\n\
***********************************************************************\n\
***        1.Age limit = {min_age_limit}+                           ***\n\
***        2.Dose Variant = Dose{Dose}                              ***\n\
***        3.Vaccine message will be recieved by => {name_list}    ***\n\
***********************************************************************\n")

    sleep(5)

    print("enter Districts Required for searching\n\
      1 for Kottayam \n\
      2 for Kottayam , Idukki and kollam\n\
      3 for ernakulam \n\
      4 for ernakulam , Kottayam , pathanamthitta, thrissur, Idukki and kollam\n \
      5 for Wayanad and Nilgiri ")
      
    Places = int(input())
    
    return name_list, min_age_limit, DoseName, Places

#name_list1 = ["taj", "Boys", "tripping", "sunni"]
#name_list2 = ["taj"]

#name_list1 = ["9746899624", "minchu"]
#name_list2 = ["9746899624"]



def Vaccine_Finder(Dist, Dates):
    global Vacc_Counter
    Vaccine_Status = False
    Vaccine_data = []
    Vacc_List = []
    Cowin_Link = ["Book your Slot : https://selfregistration.cowin.gov.in/"]
    dictv = {}
    available_centers = cowin.get_availability_by_district(Dist['ID'], date, min_age_limit)

    #print(available_centers)
    for i in available_centers['centers']:
        if(len(i['sessions']) > Dates):
            if(i["sessions"][Dates][DoseName] > 10):
                Vaccine_Status = True
                VaccStatus = [f' Vaccine Available in {Dist["Name"]} for age limit {min_age_limit}...!!!!!!!!!!!!']
                vaccname = i["sessions"][Dates]["vaccine"]
            #print(f'Center name is {i["name"]}')
            #print(f'Number of available Doses is {i["sessions"][0]["available_capacity"]}')
                Vaccine_data += [f' Center name is {i["name"]},  Date = {i["sessions"][Dates]["date"]} ,  Number of available Doses (Dose 1) is {i["sessions"][Dates][DoseName]},   Vaccine name is {vaccname},          Next']
    if Vaccine_Status != True:
        #Vacc_Counter = 0
        print(f'{Dist["Name"]} District : No Vaccine Available ')
        sleep(1)
    elif ((Dist['Vax_Dat']) !=  (Vaccine_data)):
        Vacc_Counter += 1
        Vacc_List += VaccStatus + Vaccine_data + Cowin_Link
        dictv = str(Vacc_List)
        print(f'*{Dist["Name"]} District : Vaccine Available ')
        for i in Address_Array:
            
            sleep(4)
            Wname = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]")
            Wname.send_keys(i)
            Wname.send_keys(Keys.ENTER)
            sleep(2)
            msgbox = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]")
            msgbox.send_keys(dictv)
            msgbox.send_keys(Keys.ENTER)
            Vaccine_Status = False
            
        # if (Vacc_Counter >= 5):
        #     sleep(400)
        # elif (Vacc_Counter >= 3):
        #     sleep(200)
        # elif (Vacc_Counter >= 2):
        #     sleep(100)
        # else:
        Dist['Count'] += 3
        Dist['Vax_Dat'] = Vaccine_data
        Dist['SID'] += 1
        sleep(10)
    else:
        print(f' {Dist["Name"]} District : No New Centers Found')
    #print(f"Vax = {Dist['Vax_Dat']}")


##############################################################################
##############################################################################
#################################### #########################################
################################# START ######################################
#################################### #########################################
##############################################################################

global_count = 0
print("\n\n\n\
              █▀█ █▄█ ▀█▀ █░█ █▀█ █▄░█\n\
              █▀▀ ░█░ ░█░ █▀█ █▄█ █░▀█ \
")

print("\n\
              Welcome...Please Wait.....",end="")
sleep(2)
for i in range(5):
    print(f'{"."}',end="")
    sleep(0.3*i)
print("  \n\n\n\
░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░░ \n\
▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄▄ \n\
▄                                                                    ▄ \n\
▄                                                                    ▄ \n\
▄      █░█ ▄▀█ █▀▀ █▀▀ █ █▄░█ █▀▀   █▀▀ █ █▄░█ █▀▄ █▀▀ █▀█           ▄ \n\
▄      ▀▄▀ █▀█ █▄▄ █▄▄ █ █░▀█ ██▄   █▀░ █ █░▀█ █▄▀ ██▄ █▀▄           ▄ \n\
▄                                                                    ▄ \n\
▄                              ßy                                    ▄ \n\
▄                                                                    ▄ \n\
▄                           Bipul Raj                                ▄ \n\
▄                                                                    ▄ \n\
▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄▄ \n\
░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░░  \n\
")

sleep(4)     

print("\n\
       Please Wait...For your Whatsap Web..",end="")
sleep(2)
for i in range(5):
    print(f'{"."}',end="")
    sleep(0.2*i)
      

Vacc_List = []

Vacc_Counter = 0


driver = webdriver.Chrome('./chromedriver')
#type(browser)
driver.get('https://web.whatsapp.com/')
print("\n\n\n\n")
sleep(15)
print("\n\n Wait ...\n\n\n\n\n")
print(" Retry 1..\n\n\
░░░░░░░Scanning QR Code \n\
░░░░░░░Done!!!!!!!    ")
print("\n\
▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄▄ \n\
░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░░ \n")
print("\n\n\n Login Completed\n\n")
cowin = CoWinAPI()
#states = cowin.get_states()
#print(states)
districts = cowin.get_districts("17")
#print(districts)
#district_id = '306'
Ktym = {"ID":"304", "Name":"Kottayam", "Count" : 0, "Vax_Dat" : [], "SID" : 0}
Kllm = {"ID":"298", "Name":"Kollam", "Count" : 0, "Vax_Dat" : [], "SID" : 0}
Kzkd = {"ID":"305", "Name":"Kozhikode", "Count" : 0, "Vax_Dat" : [], "SID" : 0}
Idki = {"ID":"306", "Name":"Idukki", "Count" : 0, "Vax_Dat" : [], "SID" : 0}
Eklm = {"ID":"307", "Name":"Ernakulam", "Count" : 0, "Vax_Dat" : [], "SID" : 0}
Ptnt = {"ID":"300", "Name":"Pathanamthitta", "Count" : 0, "Vax_Dat" : [], "SID" : 0}
Trsr = {"ID":"303", "Name":"Thrissur", "Count" : 0, "Vax_Dat" : [], "SID" : 0}
Wynd = {"ID":"299", "Name":"Wayanad", "Count" : 0, "Vax_Dat" : [], "SID" : 0}
Nilg = {"ID":"577", "Name":"Nilgiris", "Count" : 0, "Vax_Dat" : [], "SID" : 0}

Kott_Count = 0
Kllm_Count = 0
Kzkd_Count = 0
Eklm_Count = 0
Ptnt_Count = 0

date = today()  # Optional. Takes today's date by default

name_list1 = []
       
input_list = UserInput()

name_list1 = input_list[0]
min_age_limit = input_list[1]
DoseName = input_list[2]
Places = input_list[3]
    
while(1):
    try:
        Address_Array = name_list1
        global_count += 1
        if global_count > 100 :
            Ktym['SID'] = 0
            Kllm['SID'] = 0
            Eklm['SID'] = 0
            Ptnt['SID'] = 0
            Idki['SID'] = 0
            Trsr['SID'] = 0
            Wynd['SID'] = 0
            Nilg['SID'] = 0
            global_count = 0
    
    
        if Ktym['Count'] > 0:        
            Ktym['Count'] -= 1        
        if Kllm['Count'] > 0:        
            Kllm['Count'] -= 1
        if Eklm['Count'] > 0:
            Eklm['Count'] -= 1
        if Ptnt['Count'] > 0:
            Ptnt['Count'] -= 1
        if Idki['Count'] > 0:
            Idki['Count'] -= 1
        if Trsr['Count'] > 0:
            Trsr['Count'] -= 1
        if Wynd['Count'] > 0:
            Wynd['Count'] -= 1
        if Nilg['Count'] > 0:
            Nilg['Count'] -= 1
    
        for S_Id in range(5):
            try:
                print(f'Day-{S_Id + 1}')
    #######################################################################################  
    #######################################################################################
                if Ktym['Count'] < 1 and Ktym['SID'] < 2 and (Places == 1 or Places == 2 or Places == 4):
                    Vaccine_Finder(Ktym,S_Id)
    
                elif(Places == 1 or Places == 2 or Places == 4):
                    print("Kottayam District: Vaccine Status : No New Updates")
    #######################################################################################  
    #######################################################################################              
                if Kllm['Count'] < 1 and Kllm['SID'] < 2 and (Places == 2 or Places == 4):
                    Vaccine_Finder(Kllm,S_Id)
    
                elif(Places == 2 or Places == 4):
                    print("Kollam District: Vaccine Status : No New Updates")
    #######################################################################################  
    #######################################################################################                
                
                if Eklm['Count'] < 1 and Eklm['SID'] < 2 and (Places == 3 or Places == 4):
                    Vaccine_Finder(Eklm,S_Id)
    
                elif(Places == 3 or Places == 4):
                    print("Ernakulam District: Vaccine Status : No New Updates")
    #######################################################################################  
    #######################################################################################                
                
                if Ptnt['Count'] < 1 and Ptnt['SID'] < 2 and (Places == 4):
                    Vaccine_Finder(Ptnt,S_Id)
    
                elif(Places == 4):
                    print("Pathanamthitta District: Vaccine Status : No New Updates")
    #######################################################################################  
    #######################################################################################                
                if Idki['Count'] < 1 and Idki['SID'] < 2 and (Places == 2 or Places == 4):
                    Vaccine_Finder(Idki,S_Id)
                    
                elif(Places == 2 or Places == 4):
                    print("Idukki District: Vaccine Status : No New Updates")
    #######################################################################################  
    #######################################################################################                
                if Trsr['Count'] < 1 and Trsr['SID'] < 2 and (Places == 4):
                    Vaccine_Finder(Trsr,S_Id)
                    
                elif(Places == 4):
                    print("Thrissur District:Vaccine Status : No New Updates")
    #######################################################################################  
    #######################################################################################                
                if Wynd['Count'] < 1 and Wynd['SID'] < 2 and (Places == 5):
                    Vaccine_Finder(Wynd,S_Id)
                    
                elif(Places == 5):
                    print("Wayanad District: Vaccine Status : No New Updates")
    #######################################################################################  
    #######################################################################################                
                if Nilg['Count'] < 1 and Nilg['SID'] < 2 and (Places == 5):
                    Vaccine_Finder(Nilg,S_Id)
                    
                elif(Places == 5):
                    print("Nilgiri District: Vaccine Status : No New Updates")
    #######################################################################################  
    #######################################################################################        
            except:
                print("Try again")
        print("Press ctrl+c For Changing Inputs")
        sleep(5)

    except KeyboardInterrupt:
        print('Hello user you have pressed ctrl-c button.')        
        input_list = UserInput()
        name_list1 = input_list[0]
        min_age_limit = input_list[1]
        DoseName = input_list[2]
        Places = input_list[3]