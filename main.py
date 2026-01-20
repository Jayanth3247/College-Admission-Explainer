import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import GoogleGenerativeAI
import os
    # Use a pipeline as a high-level helper



def send_email(name,mailid,course,marks):

    system_instruction = f""" You are a helpful assistant in a college, your goal is to give guidance 
    to the student who filled a form. Your guidance should invlove, suggesting a course best suitable
    for the student based on the marks scored in 12th std. You should also give the information about 
    the course fee. 

    Available Courses: [Btech IT - only for candidates who scored more than 450, fees is Rs. 120000/year
                        Be CSE - only for candidates who scored more than 400, fees is Rs. 120000/year
                        Btech AI - only for candidates who scored more than 480, fees is Rs. 150000/year
                        Be Civil - For canidates who scored more than 300, fees is Rs. 80000/year]
    
    
    The following is the student's information to whom you should address
    Name: {name}
    Course Interested: {course}
    12th marks: {marks}

    Based on the above data, give the student guidance that can directly be emailed. Be polite while handling rejections. 
    Do not exceed 200 words. No preamble. 

"""

    # pipe = pipeline("text-generation", model="LiquidAI/LFM2.5-1.2B-Instruct")
    # messages = [
    #     {"role": "user", "content": system_instruction},
    # ]
    # content = pipe(messages)

    model = GoogleGenerativeAI(model = 'gemini-flash-latest', api_key = 'AIzaSyC431S64MDxUTghjah63mE4U7H1tWqp0Yc')
    content = model.invoke(system_instruction)

    mail = EmailMessage() #Dictionary
    mail['from'] = 'thuli.edu@gmail.com'
    mail['to'] = mailid
    mail['subject'] = "Greetings from Jayanth's College"

    mail.set_content(content)


    sender = 'thuli.edu@gmail.com'
    app_password = os.environ['APP_PASSWORD']

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
        server.login(sender, app_password)
        server.send_message(mail)
        print(f"Email sent to {mail['to']} successfully.  ")

#send_email('Jayanth','jayanth.ofcl@gmail.com','AI',380)