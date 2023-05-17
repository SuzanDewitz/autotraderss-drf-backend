from rest_framework import generics
from profiles.models import Profile
from profiles.serializers import ProfileSerializer
from .serializers import ProfileSerializer

class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
