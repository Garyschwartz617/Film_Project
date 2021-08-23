from django.urls import path, include
from . import views
 

urlpatterns = [
    path('signup', views.UserCreationView.as_view(), name='register'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('profile/<int:id>',views.profileID, name = 'profile'),
    path('', include('django.contrib.auth.urls'))
]