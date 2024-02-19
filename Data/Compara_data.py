from datetime import datetime
import time

'''
data_to_compare = datetime.strptime("2024-01-30T19:45:00Z", "%Y-%m-%dT%H:%M:%SZ")
timezone = data_to_compare.tzinfo
data_now = datetime.now(timezone)'''


    
data = datetime.strptime('2024-01-31 18:00:00', "%Y-%m-%d %H:%M:%S")
data_convertida = time.mktime(data.timetuple())
print(data_convertida)