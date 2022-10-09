from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductCreateAPIView.as_view()),
    path('<int:pk>/update', views.ProductUpdateAPIView.as_view()),
    path('<int:pk>/delete', views.ProductDeleteAPIView.as_view()),
    path('products/', views.product_alt_view, name="product_alt_view"),
    path('list/', views.ProductMixinView.as_view()),
    path('<int:pk>', views.ProductDetailAPIView.as_view())
]