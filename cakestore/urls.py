from django.contrib import admin
from django.urls import path
from api.views import get_all_cakes, get_cake, create_cake, update_cake, delete_cake

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cakes/', get_all_cakes, name='get_all_cakes'),
    path('cakes/<int:cake_id>/', get_cake, name='get_cake'),
    path('cakes/create/', create_cake, name='create_cake'),
    path('cakes/<int:cake_id>/update/', update_cake, name='update_cake'),
    path('cakes/<int:cake_id>/delete/', delete_cake, name='delete_cake'),
]
