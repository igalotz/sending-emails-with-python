from settings import SENDER_EMAIL, SENDER_PASSWORD
import smtplib

email='malpimozg@gmail.com'
msg = 'kocham programowac {}'.format('bardzo')

smtp = smtplib.SMTP('smtp.gmail.com', 587)  #conection to email server
smtp.ehlo()
smtp.starttls()
smtp.ehlo()
smtp.login(SENDER_EMAIL, SENDER_PASSWORD)




smtp.sendmail(SENDER_EMAIL,email,msg,)
smtp.quit()

#Zezwalaj na mniej bezpieczne aplikacje: WŁĄCZONE