import smtplib

to = input("enter the email of reciever")
message = input("enter the message:-")
sender_email= input("enter the sender email")
passward = input("enter the passward")

def sendEmail(to,message,sender_email,passward):
    server = smtplib.SMTP('smtp.gmail.cpom',570)
    server.starttls()
    server.login(sender_email,passward)
    server.sendmail(sender_email, to ,message)
    server.close()

sendEmail(to,message,sender_email,passward)
