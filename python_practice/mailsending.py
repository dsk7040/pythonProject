import smtplib
import openpyxl
import pandas as pd
import gspread

gc = gspread.service_account("C:\\Users\\Baltech\\Downloads\\deepsheet.json")
wks = gc.open("Automation Use").worksheet("Usermail")
# worksheet = wks.worksheet("Demo")
print(wks)
value = wks.get("B2")
print(value)

object=smtplib.SMTP("smtp.gmail.com",587)

object.starttls()

object.login("dsk7040@gmail.com", "jvdm bnvh ztou kpar")

subject= "Sending mails for Automation testing"
body= "Hello sir I am just try to sending mails " + str(value) + "using automation testing"

message="subject:{}\n\n{}".format(subject, body)

#listofaddress=["testing100web@gmail.com", "testing009web@gmail.com", "testing006web@gmail.com"]

object.sendmail("dsk7040@gmail.com", value, message)
print("Email sent successfuly")

object.quit()
print()