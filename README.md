# Covid_Vaccine_Finder
In Kerala its very hard to find vaccine, especially for 18+ age catogory(The slots are getting filled within 1 or 2 minutes). So I thought of developing an application for checking the vaccine availability.

This script Checks the availability of vaccine in selected centers(As of now I have added 5 districts, user can select from this.). If an available center is identified, script will send whatsapp message to the selected contacts(User can configure any number of whatsapp groups/names/numbers). 
The user can configure the below things:
  1. Age Group    =>   18+, 40+ and 45+
  2. Vaccine Dose =>   Dose 1 or Dose2
  3. Whatsapp Contact names or groups who needs the message
  4. District names for which you need notification.

The script is compiled into .exe format and uploaded in build folder. So that users can execute the application in a single click. Please note that the user should have the chrome browser version and the chromedriver.exe version same. Version 91.0.4472.77 is used in this project. If you are using another version of chrome, download that version of chromedriver.exe and replace the existing one in the build folder(Build_EXE_Format).
