
#define URL route for index() view
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

    path('items/', views.MenuView.as_view()),
    path('items/<int:pk>', views.SingleMenuView.as_view()),
    path('api-token-auth/', obtain_auth_token)
    
]
