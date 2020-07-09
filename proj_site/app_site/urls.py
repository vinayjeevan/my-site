from django.urls import path
from .views import signup,user_login,Agent_details
urlpatterns = [
    path('user_login/',user_login, name="user_login"),
    path('signup/',signup, name="signup"),
    path('Agent_details/',Agent_details, name="Agent_details"),
]

