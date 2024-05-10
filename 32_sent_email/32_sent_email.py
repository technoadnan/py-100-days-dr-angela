import smtplib

my_email = "adpd1000@gmail.com"
password = "gdek vnkh agik zzzt"


# long way 
# connection = smtplib.SMTP("smtp.gmail.com", port=587)
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="expert.technoadnan@gmail.com", msg="Hello there")
# connection.close()

# short way 
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
   connection.starttls()
   connection.login(user=my_email, password=password)
   connection.sendmail(
      from_addr=my_email,
      to_addrs="expert.technoadnan@gmail.com",
      msg="Subject:Hello\n\nThis is the body of my email."
   )