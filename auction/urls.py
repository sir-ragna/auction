from django.urls import path, include


from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('register', views.register, name="register"),
    path('', views.index, name="index"),
    path('listing', views.create_listing, name="create_listing"),
    path('listing/<int:id>', views.show_listing, name="show_listing"),
]