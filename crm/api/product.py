from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes



@api_view(["GET", "POST", "PUT", "DELETE"])
# @permission_classes([IsAuthenticated])  
def product_api(request, pk=None):
    if request.method == "GET":
        if pk:
            try:
                client = Product.objects.get(pk=pk)
                serializer = ProductSerializer(client)
                return Response({"data": serializer.data}, status=status.HTTP_200_OK)
            except Product.DoesNotExist:
                return Response(
                    {"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND
                )
        else:
            clients = Product.objects.all()
            serializer = ProductSerializer(clients, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Product created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        if not pk:
            return Response(
                {"error": "ID is required for update"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            client = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(
                {"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = ProductSerializer(
            client, data=request.data, partial=True
        )  # `partial=True` allows partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Product updated successfully", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        # Delete an existing client
        if not pk:
            return Response(
                {"error": "ID is required for delete"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            client = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(
                {"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND
            )

        client.delete()
        return Response(
            {"message": "Product deleted successfully"}, status=status.HTTP_200_OK
        )



