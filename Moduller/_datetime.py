import datetime

result = dir(datetime)
print(result)

print("*" * 10)

from datetime import datetime

result = dir(datetime)
print(result)


result = datetime.now()
print(result)

result = datetime.now().year
print(result)


simdi = datetime.now()
result = simdi.year
print(result)


simdi = datetime.now()
result = simdi.month
print(result)

result = datetime.today()
print(result)

result = datetime.ctime(simdi)
print(result)

result = datetime.strftime(simdi, "%Y")
print(result)

result = datetime.strftime(simdi, "%X")
print(result)

result = datetime.strftime(simdi, "%d")
print(result)

result = datetime.strftime(simdi, "%A")
print(result)

result = datetime.strftime(simdi, "%B")
print(result)

result = datetime.strftime(simdi, "%Y %B %A")
print(result)

t = "15 April 2019 hour 10:12:30"
result = datetime.strptime(t, "%d %B %Y hour %H:%M:%S")
print(result)

result = result.year
print(result)

birthday = datetime(1983, 5, 9, 12, 30, 10)
print(birthday)

# Tarih objesi saniye cinsinden gösterilir.
result = datetime.timestamp(birthday)
print(result)

# Saniye bilgisini tarih bilgisine dönüştürür.
result = datetime.fromtimestamp(result)
print(result)

# İki tarih arasındaki fark sonucu timedelta objesi ortaya çıkar. 
result = simdi - birthday
print(result)

result = result.days
print(result)


from datetime import timedelta

result = simdi + timedelta(days=10)
print(result)

result = simdi + timedelta(days=730)
print(result)
