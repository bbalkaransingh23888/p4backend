from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.exceptions import (
    ValidationError, PermissionDenied
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from p4_app.p4_api.models import Category, Game
from p4_app.p4_api.serializers import CategorySerializer, GameSerializer


# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    # The user must be logged in to create a category
    permission_classes = (IsAuthenticated,)

    # convert the data back and forth
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all().filter(owner=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        # check if the category already exists for current user
        category = Category.objects.filter(
            name=request.data.get('name'),
            owner=request.user
        )

        if category:
            msg = 'Category with that name already exists'
            raise ValidationError(msg)
        return super().create(request)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def destroy(self, request, *args, **kwargs):
        category = Category.objects.get(pk=self.kwargs["pk"])
        if not request.user == category.owner:
            raise PermissionDenied("You cannot destroy me. I shall destroy you for your outrage, plebeian!")
        return super().destroy(self, request, *args, **kwargs)


class CategoryGames(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = GameSerializer

    def get_queryset(self):
        if self.kwargs.get("category_pk"):
            category = Category.objects.get(pk=self.kwargs["category_pk"])
            queryset = Game.objects.filter(
                owner=self.request.user,
                category=category
            )
            return queryset

    def perform_create(self, serializer):
        serializer.save()


class SingleCategoryGame(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = GameSerializer

    def get_queryset(self):
        # localhost:8000/categories/category_pk<1>/games/pk<1>/
        if self.kwargs.get("category_pk") and self.kwargs.get("pk"):
            category = Category.objects.get(pk=self.kwargs["category_pk"])
            queryset = Game.objects.filter(
                pk=self.kwargs["pk"],
                owner=self.request.user,
                category=category
            )
            return queryset


class GameViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = GameSerializer

    def get_queryset(self):
        queryset = Game.objects.all().filter(owner=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            raise PermissionDenied(
                "Only users logged into their accounts can create games"
            )
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def destroy(self, request, *args, **kwargs):
        game = Game.objects.get(pk=self.kwargs["pk"])
        if not request.user == game.owner:
            raise PermissionDenied(
                "How dare you attempt to destroy me. I shall erase you from existence!"
            )
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        game = Game.objects.get(pk=self.kwargs["pk"])
        if not request.user == game.owner:
            raise PermissionDenied(
                "You have no permission to edit this game"
            )
        return super().update(request, *args, **kwargs)
