import smtplib

email ="mr.sharif.1713@gmail.com"

receiver_email = input ("RECEIVER EMAIL:")

subject = input("SUBJECT: ")

message = input("MESSAGE: ")

text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()

server.login(email,"jbog xxwv vmst bapt")

server.sendmail(email,receiver_email,text)

print(" email has to be sent to"+receiver_email)
