import smtplib
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart

pengirim = 'daffakik129@gmail.com' #Pengirim
penerima = 'lala@gmail.com' #Penerima
msg = MIMEText("HAlo selamat siang apa kabar kamu disana") #Isi
msg['Subject'] = 'Menanyakan kabar padamu' #Subject
msg['From'] = pengirim
msg['To'] = penerima

msg = MIMEMultipart()
msg.attach(MIMEText(file("test.txt").read()))

pwd = 'ApaPasswordMu' #Password
s = smtplib.SMTP_SSL()
s.connect('smtp.gmail.com', 465)
s.login(pengirim, pwd)
s.sendmail(pengirim, penerima, msg.as_string())
s.quit()