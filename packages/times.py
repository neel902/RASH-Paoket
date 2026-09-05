from datetime import datetime

dt_object = datetime.now()

formatted_time = dt_object.strftime("%d-%m-%Y %H:%M:%S")
print("Custom format:", formatted_time)
