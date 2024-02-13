from datetime import datetime
c = datetime.now()
ctime = c.strftime('%H : %M : %S')
print(ctime)