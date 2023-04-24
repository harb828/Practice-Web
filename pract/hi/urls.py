from django.urls import path
from . import views
"""

Path(hi/name, function call to open, name to reference call)
So in this case, it would be http://ip.hi/harv
In other words, we are routing it!

Traceback to the views.py, what if there was a thousand of names? Would I create a thousand functions as well? NO!
Turns out, we can just use one function and it will just greet anyone. eg. http://ip.hi/bern will show Hi Bern.

"""

urlpatterns = [
    path("", views.index, name ="index"),
    path("<str:name>", views.greet, name = "greet")
    # path("harv", views.harv, name = "harv") 
]