# from rest_framework import viewsets
# from rest_framework.views import APIView
# from cnab.models import Documentation
# from .serializers import DocumentationSerializer
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from django.http import Http404

#
# class DocumentationViewSet(viewsets.ReadOnlyModelViewSet):
#     serializer_class = DocumentationSerializer
#     queryset = Documentation.objects.all()
#
#
# class DonoViewSet(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def get_object(self, pk):
#         try:
#             return Documentation.objects.get(id=pk)
#         except Documentation.DoesNotExist:
#             raise Http404
#
#
#     def get(self, request, pk, format=None):
#         owner = self.get_object(pk)
#         serializer = DocumentationSerializer(owner)
#         return Response(serializer.data)
#
#
#
# class NameViewSet(APIView):
#     serializer_class = DocumentationSerializer
#     def get_object(self, name):
#         try:
#             return Documentation.objects.filter(dono=name).all()
#         except Documentation.DoesNotExist:
#             raise Http404
#
#
#     def get(self, request, name, format=None):
#         owner = self.get_object(name)
#         serializer = DocumentationSerializer(owner, many=True)
#         return Response(serializer.data)
