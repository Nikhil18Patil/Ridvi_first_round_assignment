from django.shortcuts import render

# myapp/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer

class InvoiceAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            invoice = get_object_or_404(Invoice, pk=pk)
            serializer = InvoiceSerializer(invoice)
        else:
            invoices = Invoice.objects.all()
            serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)

    def post(self, request):
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        invoice = get_object_or_404(Invoice, pk=pk)
        serializer = InvoiceSerializer(invoice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        invoice = get_object_or_404(Invoice, pk=pk)
        invoice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
