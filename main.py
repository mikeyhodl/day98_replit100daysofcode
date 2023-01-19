import schedule, time, os, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

password = os.environ['mailPassword']
username = os.environ['mailUsername']


def sendMail():
  email = "Don't forget to take a break!"
  server = "mail.lancolatech.co.ke"
  port = 465
  s = smtplib.SMTP(host=server, port=port)
  s.starttls()
  s.login(username, password)

  msg = MIMEMultipart()
  msg['To'] = "mike@mikeowino.com"
  msg['From'] = username
  msg['Subject'] = "Take a BREAK"
  msg.attach(MIMEText(email, 'html'))

  s.send_message(msg)
  del msg


def printMe():
  print("⏰ Sending Reminder")
  sendMail()  # Moved the subroutine into printMe which is already scheduled


schedule.every(1).hours.do(printMe)  # Changed the interval to every 1 hour

while True:
  schedule.run_pending()
  time.sleep(1)
