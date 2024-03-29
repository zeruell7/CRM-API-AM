from django.urls import path
from .views import CostumerView,UserView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'costumers', CostumerView, basename='costumer_list')
urlpatterns = router.urls

urlpatterns = [
    path('costumer/',CostumerView.as_view({'get': 'list'}), name = 'costumer_list'),
    path('costumer/<int:pk>/',CostumerView.as_view({'get':'retrieve','put':'update','delete':'destroy'}), name = 'costumer'),
    path('user/',UserView.as_view({'get': 'list'}), name = 'user_list'),
    path('user/<int:pk>/',UserView.as_view({'get':'retrieve','put':'update','delete':'destroy'}), name = 'user')
]