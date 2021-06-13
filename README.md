# Covid_Vaccine_Finder
In Kerala its very hard to find vaccine, especially for 18+ age catogory(The slots are getting filled within 1 or 2 minutes). So I thought of developing an application for checking the vaccine availability.

This script Checks the availability of vaccine in selected centers(As of now I have added 5 districts, user can select from this.). If an available center is identified, script will send whatsapp message to the selected contacts(User can configure any number of whatsapp groups/names/numbers). 
The user can configure the below things:
  1. Age Group    =>   18+, 40+ and 45+
  2. Vaccine Dose =>   Dose 1 or Dose2
  3. Whatsapp Contact names or groups who needs the message
  4. District names for which you need notification.

The script is compiled into .exe format and uploaded in build folder. So that users can execute the application in a single click. Please note that the user should have the chrome browser version and the chromedriver.exe version same. Version 91.0.4472.77 is used in this project. If you are using another version of chrome, download that version of chromedriver.exe and replace the existing one in the build folder(Build_EXE_Format).

LICENSE Information:
LICENSE for the project(Excluding the Third Party Libraries used) is present in the root folder.

Third party modules used and there LICENSE information is given below:
  1. cowin - MIT
  2. time  - MIT
  3. selenium - APACHE
  4. datetime - ZOPE

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


