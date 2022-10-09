from django.http import JsonResponse
# *important
from django.forms.models import model_to_dict
# ----end---

from rest_framework.response import Response
from rest_framework.decorators import api_view


from products.serializers import ProductSerializer
from products.models import Product




# Create your views here.
def api_home2(request, *args, **kwargs):

    model_data = Product.objects.all().order_by("?").first()
    data = {}

# First approach here
    # if model_data:
    #     data['id'] = model_data.id
    #     data['title'] = model_data.title
    #     data['content'] = model_data.content
    #     data['price'] = model_data.price
    # first approach ends here

    # Preferred approach here
    if model_data:
        data = model_to_dict(model_data, fields=('id', 'price', 'title'))
    return JsonResponse(data)


# convert api_home view to a rest_framework view

@api_view(['GET'])
def api_home1(request, *args, **kwargs):
    instance = Product.objects.all().order_by('?').first()
    data = {}

    if instance:
        data = ProductSerializer(instance).data
        print(data)
    return Response(data)


@api_view(['POST'])
def api_home(request, *args, **kwargs):

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        data = serializer.data
        return Response(data)
