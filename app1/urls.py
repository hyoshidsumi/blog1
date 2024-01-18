from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.signinView, name='signin'),
    path('home/', views.homeView, name='home'),
    path('signup/', views.signupView, name='signup'),
    path('signout/', views.signoutView, name='signout'),
    # path('create/', views.createView.as_view(), name="create"),
    path('create/', views.create, name="create"),
    path('detail/<int:pk>/', views.detailView, name='detail'),
    path('update/<int:pk>/', views.updateView, name='update'),
    path('delete/<int:pk>/', views.deleteView, name='delete'),
    path('a/', views.a),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
