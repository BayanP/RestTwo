from rest_framework import viewsets, permissions, status
from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category
from rest_framework.response import Response


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [
        permissions.AllowAny,                             # разрешение на все запросы
        # permissions.IsAuthenticated,                    #разрешение после авторизации
        # permissions.IsAdminUser,                        # разрешение только администраторам
        # permissions.IsAuthenticatedOrReadOnly,          #разрешение на чтение без администраторов
    ]
    def destroy(self, request, *args, **kwargs):     #встроенная функция
        instance = self.get_object()                        #instance- пустой экземпляр
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [
        permissions.AllowAny,                             # разрешение на все запросы
        # permissions.IsAuthenticated,                    #разрешение после авторизации
        # permissions.IsAdminUser,                        # разрешение только администраторам
        # permissions.IsAuthenticatedOrReadOnly,          #разрешение на чтение без администраторов
    ]
    def destroy(self, request, *args, **kwargs):     #встроенная функция
        instance = self.get_object()                        #instance- пустой экземпляр 
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)