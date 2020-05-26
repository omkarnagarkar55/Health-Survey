from email.mime.text import MIMEText
import smtplib

def send_email(email, height,average_height,count,bmi):
    from_email="Enter your email here"
    from_password="Enter your password here"
    to_email=email
    condition=''
    
    if(bmi<=18.5):
        condition="Underweight"
    elif(bmi>18.5 and bmi<=24.9):
        condition="Healthy weight"
    elif(bmi>=25 and bmi<=29.9):
        condition="Overweight"
    else:
        condition="Obese"
        

    subject="Height data"
    message="Hey there, your height is <strong>%s</strong>. <br> Average height of all is <strong>%s</strong> and that is calculated out of <strong>%s</strong> people. <br> Your BMI is <strong>%s</strong>. <br> You are <strong>%s</strong>.<br> Thank you!" % (height, average_height, count,bmi,condition)
    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
