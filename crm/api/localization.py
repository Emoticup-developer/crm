from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Localization
from .serializers import LocalizationSerializer

from rest_framework.decorators import api_view, permission_classes



@api_view(["GET", "POST", "PUT", "DELETE"])
# @permission_classes([IsAuthenticated])  
def localization_api(request, pk=None):
    if request.method == "GET":
        if pk:
            try:
                client = Localization.objects.get(pk=pk)
                serializer = LocalizationSerializer(client)
                return Response({"data": serializer.data}, status=status.HTTP_200_OK)
            except Localization.DoesNotExist:
                return Response(
                    {"error": "Localization not found"}, status=status.HTTP_404_NOT_FOUND
                )
        else:
            clients = Localization.objects.all()
            serializer = LocalizationSerializer(clients, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = LocalizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Localization created successfully", "data": serializer.data},
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
            client = Localization.objects.get(pk=pk)
        except Localization.DoesNotExist:
            return Response(
                {"error": "Localization not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = LocalizationSerializer(
            client, data=request.data, partial=True
        )  # `partial=True` allows partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Localization updated successfully", "data": serializer.data},
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
            client = Localization.objects.get(pk=pk)
        except Localization.DoesNotExist:
            return Response(
                {"error": "Localization not found"}, status=status.HTTP_404_NOT_FOUND
            )

        client.delete()
        return Response(
            {"message": "Localization deleted successfully"}, status=status.HTTP_200_OK
        )



