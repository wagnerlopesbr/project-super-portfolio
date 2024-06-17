from rest_framework import viewsets
from projects.models import Profile, Project
from projects.serializers import ProfileSerializer, ProjectSerializer
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        context = {"profile": instance}
        if request.method == "GET":
            return render(request, "profile_detail.html", context)
        return super().retrieve(request, *args, **kwargs)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
