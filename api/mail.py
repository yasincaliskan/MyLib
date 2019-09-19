import smtplib

content = "Bu otomatik gönderilmiş bir e-postadır."
mail = smtplib.SMTP("smtp.gmail.com",587)
mail.ehlo()
mail.starttls()

mail.login("yaskocaliskan26@gmail.com","password")
mail.send("yaskocaliskan26@gmail.com","yasin.caliskan@dpu.edu.tr",content)