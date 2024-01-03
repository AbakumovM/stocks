from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='about'),
    path('stock/<int:stock_id>/', views.stocks_id),
    path('stock/', views.post_details),
    path('posts/<int:year>', views.posts_list),
    path('country/<str:name_country>', views.shares_in_country, name='country'),
    path('login/', views.login, name='login'),
    path('test/', views.test, name="test"),
]