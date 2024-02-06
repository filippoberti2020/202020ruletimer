from win10toast import ToastNotifier
import time

toaster = ToastNotifier()
while True:
    toaster.show_toast("Time to rest your eyes", "Look 20 feet away for 20 seconds", duration=20)
    time.sleep(60*20)  # 20 minutes
