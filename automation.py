import time 
import plyer
from plyer import notification 


title = 'Today'
message = 'Aadithya check your G-Mail'

notification.notify(
        title= title,
        message= message,
        app_icon = None,
        timeout= 10,
        toast=False
)