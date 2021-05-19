import time
from datetime import datetime

while True:
	now = datetime.now()
	result = now.strftime("%H:%M:%S")
	print(result, end="", flush=True)
	print("\r", end="", flush=True)
	time.sleep(1)
