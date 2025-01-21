from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Machine
from .serializers import MachineSerializer

from rest_framework.decorators import api_view, permission_classes



@api_view(["GET", "POST", "PUT", "DELETE"])
# @permission_classes([IsAuthenticated])  
def machine_api(request, pk=None):
    if request.method == "GET":
        if pk:
            try:
                client = Machine.objects.get(pk=pk)
                serializer = MachineSerializer(client)
                return Response({"data": serializer.data}, status=status.HTTP_200_OK)
            except Machine.DoesNotExist:
                return Response(
                    {"error": "Machine not found"}, status=status.HTTP_404_NOT_FOUND
                )
        else:
            clients = Machine.objects.all()
            serializer = MachineSerializer(clients, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = MachineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Machine created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        print()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        if not pk:
            return Response(
                {"error": "ID is required for update"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            client = Machine.objects.get(pk=pk)
        except Machine.DoesNotExist:
            return Response(
                {"error": "Machine not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = MachineSerializer(
            client, data=request.data, partial=True
        )  # `partial=True` allows partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Machine updated successfully", "data": serializer.data},
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
            client = Machine.objects.get(pk=pk)
        except Machine.DoesNotExist:
            return Response(
                {"error": "Machine not found"}, status=status.HTTP_404_NOT_FOUND
            )

        client.delete()
        return Response(
            {"message": "Machine deleted successfully"}, status=status.HTTP_200_OK
        )



