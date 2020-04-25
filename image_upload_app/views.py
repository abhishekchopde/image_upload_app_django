from django.shortcuts import render
from .serializer import imageUploadSerializer
from django.http import JsonResponse
from rest_framework.views import APIView
# Create your views here.


class test_image_upload(APIView):
    def post(self, request):
        serializer = imageUploadSerializer(data=request.data)
        if serializer.is_valid():
            ret = serializer.save()
            return ret
        return JsonResponse({'ret': serializer.errors}, status=400)
