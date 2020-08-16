from datetime import datetime

br1 = 1 / 2.43
print(br1)

print(format(br1, '0.4f'))

print("1 BRL = {rate:0.2f} USD".format(rate=br1))

print(format(42, 'b'))

print(format(2/3, '.1%'))


now = datetime.now()

print(format(now, '%H:%M:%S'))

print("It's now {:%I:%M %p}".format(now))
