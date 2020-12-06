import smtplib
import credentials as cred

port = cred.port
host = cred.host

def send_email(subject, body):
    content = f'From: {cred.sender_name} <{cred.sender_email}>\nTo: {cred.receiver_name} <{cred.receiver_email}>\nSubject: {subject}\n\n{body}'
    with smtplib.SMTP(host, port) as smtp:
        smtp.starttls()
        smtp.login(cred.sender_email, cred.app_pw)
        smtp.sendmail(cred.sender_email, cred.receiver_email, content)