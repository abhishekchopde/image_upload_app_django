from rest_framework import serializers
import hashlib
from functools import partial
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import JsonResponse
from rest_framework import status
import logging
logger = logging.getLogger(__name__)
from .models import Images


def hash_image(file, block_size=65536):
    # Utility function to hash images
    hasher = hashlib.md5()
    for buf in iter(partial(file.read, block_size), b''):
        hasher.update(buf)

    return hasher.hexdigest()


# hash block size is of 1 KB
def hash_data(data, block_size = 1024):
    hasher = hashlib.md5()
    for i in range(5):
        buf = data[i*block_size:(i+1)*block_size]
        hasher.update(buf)
    return hasher.hexdigest()

class uploadedImagesSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Images.objects.create(**validated_data)

    class Meta:
        model = Images
        fields = ('imageHash', 'imageType', 'uploadedBy')


class imageUploadSerializer(serializers.Serializer):
    # use_url gives file url, i.e. MEDIA_URL + filename
    image = serializers.FileField(max_length=None, allow_empty_file=False)
    uploadedBy = serializers.CharField(max_length=20, allow_blank=False)
    def create(self, validated_data):
        image = validated_data.get('image')
        uploadedBy = validated_data.get('uploadedBy')
        image_exist = False
        image_hash = hash_image(image)
        image_extn = image.name.split(".")[-1]
        data = {
            'imageHash': image_hash,
            'imageType': image_extn,
            'uploadedBy': uploadedBy
        }

        # generating a serializer
        try:
            image_obj = Images.objects.filter(imageHash=image_hash)[0]
            data['uploadedBy'] = image_obj.uploadedBy
            data['imageType'] = image_obj.imageType
            image_serializer = uploadedImagesSerializer(instance=image_obj, data=data)
            image_exist = True
        except Exception as e:
            image_serializer = uploadedImagesSerializer(data=data)

        # saving the data in db
        if image_serializer.is_valid():
            image_serializer.save()
        else:
            return JsonResponse({"invalid data": image_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        # saving the image in media
        if not image_exist:
            image.seek(0)
            image.name = image_hash + '.' + image_extn
            try:
                path = default_storage.save(str(image), ContentFile(image.read()))
            except Exception as e:
                logger.exception("error saving videos")
                return JsonResponse({"internal error ": "videos upload failed"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return JsonResponse({"hashe": image_hash}, status=status.HTTP_201_CREATED)