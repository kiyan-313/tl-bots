from datetime import datetime
import pytz

tz = pytz.timezone('America/Los_Angeles')

x=datetime.now(tz)
print(x)