import smtplib
#enable smtp in your email
sender_email = 'xxxxxxxxxx@gmail.com'
sender_password ='xxxxxxxxxxxxxxxxx'

def send_email(recever_email , subject , body):
    message ='Subject : {}\n\n{}'.format(subject, body)
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
        server.login(sender_email , sender_password )
        server.sendmail(sender_email , recever_email ,message)
    print("send email ")


recever_email='xxxxxxxxxxx@gmail.com'
subject='Test'
body='hi this is test code'

send_email (recever_email , subject , body)
