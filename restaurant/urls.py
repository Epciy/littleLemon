from .import views
from django.urls import path,include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'bookings/tables', views.BookingView)


urlpatterns = [
    path("home",views.home,name="home"),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),


    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', views.BookingView.as_view({'get': 'list'})),
    #path('bookings/', views.BookingView.as_view({'get':'list',','delete':'destroy'}),name='bookings'),
    path('message/', views.msg),
    path('api-token-auth', obtain_auth_token),
]
