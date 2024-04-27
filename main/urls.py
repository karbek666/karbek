from django.urls import path


from .views import ProductAPIView, UserRegisterationView, CommentAPIView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('product/', ProductAPIView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(),  name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', UserRegisterationView.as_view()),
    path('Comment/', CommentAPIView.as_view()),


]
