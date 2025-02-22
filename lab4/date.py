
import datetime
#1
fivedays = datetime.date.today() - datetime.timedelta(5)
print(fivedays)


#2
today = datetime.date.today()
yesterday = today - datetime.timedelta(1)
tommorow = today + datetime.timedelta(1)


#3
x = datetime.datetime.now()
print(x.strftime("%f"))

