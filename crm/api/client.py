from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Client
from .serializers import ClientSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes



@api_view(["GET", "POST", "PUT", "DELETE"])
# @permission_classes([IsAuthenticated])  
def client_api(request, pk=None):
    if request.method == "GET":
        if pk:
            try:
                client = Client.objects.get(pk=pk)
                serializer = ClientSerializer(client)
                return Response({"data": serializer.data}, status=status.HTTP_200_OK)
            except Client.DoesNotExist:
                return Response(
                    {"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND
                )
        else:
            clients = Client.objects.all()
            serializer = ClientSerializer(clients, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.create_user(
                username=request.data.get("username"),
                password=request.data.get("password"),
                email=request.data.get("email")
            )
            user.save(),
            return Response(
                {"message": "Client created successfully", "data": serializer.data},
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
            client = Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            return Response(
                {"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = ClientSerializer(
            client, data=request.data, partial=True
        )  # `partial=True` allows partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Client updated successfully", "data": serializer.data},
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
            client = Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            return Response(
                {"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND
            )

        client.delete()
        return Response(
            {"message": "Client deleted successfully"}, status=status.HTTP_200_OK
        )




@api_view(["POST"])
def reset_password(request, pk):
    try:
        client = Client.objects.get(id=pk)
        print(client.username)
        user = User.objects.get(username = client.username)
        new_password = request.data.get("new_password")
        if new_password:
            user.set_password(new_password)
            user.save()
            return Response({"message": "Password reset successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "New password is required"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as ex:
        return Response({"error": f"Client not found {ex}"}, status=status.HTTP_404_NOT_FOUND)