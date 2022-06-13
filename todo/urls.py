from django.urls import path
from todo.views import database_list, database_total, database_view, database_mes

urlpatterns = [
    path('', database_list),
    path('total/', database_total),
    path('por_mes/', database_mes),
    # path('<int:pk>/', database_view)
]
