from django.urls import path


from .views import BbListCreate

urlpatterns=[
    path('api/bb/', BbListCreate.as_view()),
]
