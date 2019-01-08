from django.urls import path, include
from . import views

myapp = 'shopapp'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('login/', views.signin, name='login'),
    path('logout/', views.signout, name='logout'),
    path('signup/', views.signup, name='signup'),
    #path('<int:dept_id>/', views.aisle_list, name='aisle_list'),
    #path('item/<int:ais_id>/', views.product_list, name='product_list'),
    path('chart_list/', views.chart_list, name='chart_list'),
    path('vip_reorder_page/', views.chart_page, name='chart_page'),
    path('vip_reorder/', views.get_data, name='vip_reorder'),
    path('vip_aisle_page/', views.vip_aisle_page, name='vip_aisle_page'),
    path('vip_aisle/', views.get_aisle, name='vip_aisle'),
    path('order_dow_page/', views.order_dow_page, name='order_dow_page'),
    path('order_dow/', views.get_dow, name='order_dow'),
    path('aisle/<int:a>/', views.detail_middle, name='detail_middle'),
    path('aisle/<int:a>/<int:aisle_id>/', views.detail_middle_five, name='detail_middle_five'),
]