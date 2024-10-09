import smtplib

server = smtplib.SMTP('smtp.gmail.com',535)

server.starttls()

server.login('gmail.com','password')

server.sendmail('sender', 'noreply@gmail.com','Mail sent from demo')

print('Mail sent')