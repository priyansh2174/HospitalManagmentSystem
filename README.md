# hospitalbookingmanagementsystem
The repository contains code for a hospital appointment management system that interacts with Africa's Talking API to seamlessy book Doctor-Patient Appointment thereby improving on Patient's Access to Medical Care, particularly in the rural areas. 

The patient log's into the given hospital's platform and checks the available Doctor Time slots for an appointment, the type of services being offered by that Hospital and the Doctor offering that service.

To book an appointment :
 - The Patient dials a Specified U.S.S.D code e.g *384*743106#, 
 - Selects the service he/she requires.
 - Selects the doctor available to offer an appointment for that given service
 - If the given time is convinient to the patient, the patient selects it.
 - Upon successful completion of the above steps, A message is sent back to the patient's phone number. With it, a booking code is provided. 
    This booking code is used by both the Doctor and the Hospital to verify this Patient's Appointment.
  
# Quick Guide <br />

Below are the steps on how to get the web app up and running

- Clone it: <br />
    git clone https://github.com/john-thuo1/hospitalbookingmanagementsystem.git <br />

- Cd into it: <br />
    cd djangohospitalappointment <br />

- Create a virtual environment
    python3 -m venv venv <br />
     
- Activate venv: <br />
    Mac/Linux: source venv/bin/activate <br />
    Windows: venv\Scripts\activate <br />
    
- Install the requirements <br />
    pip install -r requirements.txt <br />
    
- Create DB <br />
    python manage.py makemigrations <br />
    
- Apply DB Changes <br />
    python manage.py migrate <br />
    
- Create a Ngrok URL: <br />

    Download the ngrok software from their website here, on this page they you will be prompted to sign up to download the application, go ahead and do so. <br />
    Download and start/run the application <br />
    After running the Ngrok application you will see the ngrok terminal window <br />
    Go back to the Ngrok web page where you downloaded the application (the link is displayed above) and navigate to the section labeled “Connect your account” <br />
    Copy the ngrok code provided in the “Connect your account” section onto the Ngrok terminal <br />
    Inside the Ngrok terminal, type the command “ngrok http 8000” <br />
    A ngrok shell window will be displayed, with the name of the newly created ngrok http URL e.g. http://21f3bf1b511a.ngrok.io <br />

    Do not close or quit this ngrok shell <br />

- Configure your Africa’s Talking U.S.S.D. A.P.I.: <br />

Navigate to this URL: you will be required to sign in or sing up if you don’t have an account with Africa’s Talking <br />
While on that page click on the link labeled “create a channel” to create a USSD code <br />
Enter a unique dummy channel e.g. 743106 <br />
Your U.S.S.D. Code is now e.g. *384*743106# <br />

In the callback URL paste the ngrok http URL you created above, after appending “/api/ussd_callback/” at the end of the URL e.g. http://21f3bf1b511a.ngrok.io/api/ussd_callback/ this “/api/ussd_callback/” A.P.I. has already been created in the Django project.

- Click on Create Channel <br />
   Configure the Django Project to use the created ngrok url: <br />
- Open your Django project folder: “djangohospitalappointment” <br />
   Locate a folder with a similar name to your Django project folder, this folder is in the same directory as your “users” app folder
   Inside this folder is a python file labeled “settings.py”

- Open the “settings.py” file and locate the python variable ALLOWED_HOSTS, which is a python list located close to the start of the file

   Inside the ALLOWED_HOSTS list enter the ngrok URL you created as well as the localhost URL, it should resemble something like this: <br />
        ALLOWED_HOSTS =['127.0.0.1','21f3bf1b511a.ngrok.io'] <br />

- Run the server: <br />
   python manage.py runserver <br />

- Navigate to your localhost site <br />
   Follow the instructions on the home page to start using the site
  
  



