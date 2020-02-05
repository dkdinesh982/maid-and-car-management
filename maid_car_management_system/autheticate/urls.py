from rest_framework import routers
from autheticate import views
router=routers.DefaultRouter()
router.register('society-admin',views.RegisterViewSet,basename='register')
router.register('login',views.LoginViewSet,basename='login')
# router.register('logout',views.Logout,basename='logout')

urlpatterns=router.urls