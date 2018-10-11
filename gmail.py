import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("pruthvirajkp150@gmail.com","*123#")
message="Hello"
server.sendmail("pruthvirajkp150@gmail.com","vk9339135@gmail.com",message)
server.quit()