from rest_framework import generics, permissions, filters
from autotraders_drf_backend.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Autotrader
from .serializers import AutotraderSerializer


class AutotraderList(generics.ListCreateAPIView):
    """
    List autotrader posts and create post for logged in users.
    Perform_create method ties a post to the logged in user.
    """

    serializer_class = AutotraderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Autotrader.objects.all()

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'saved__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'title',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AutotraderDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Detailed view of a autotrader posting.
    Update or delete a posting for owner of the post.
    """
    serializer_class = AutotraderSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Autotrader.objects.all()        