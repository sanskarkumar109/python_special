import time
from plyer import notification

while True:
    notification.notify(
        title="please drink water",
        message="the national academics of science suggest that you have to drink 4 liters of water a day",
        timeout=10,
    )
    time.sleep(60*60)
