from django.urls import path
from image_upload_app import views

urlpatterns = [
    path("upload", views.test_image_upload.as_view()),
]