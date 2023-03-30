# %%
from datetime import datetime
from pytz import timezone
import pytz

print (pytz.all_timezones)
print(datetime.now(timezone('Asia/Tokyo')))
print(datetime.now(timezone('Europe/Madrid')))
