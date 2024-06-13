from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Shop
from .serializers import ShopSerializer

class ShopView(APIView):
    def get(self, request):
        shops = Shop.objects.filter(
            (models.Q(category__icontains='Fluorescence') |
             models.Q(category__icontains='Carat') |
             models.Q(category__icontains='Color Grade') |
             models.Q(category__icontains='Cutting Style') |
             models.Q(name__icontains='FLUORESCENCE') |
             models.Q(category__icontains='Round Brilliant') |
             models.Q(subcategory__icontains='CUT PROPORTION') |
             models.Q(subcategory__icontains='CUT GRADE') |
             models.Q(subcategory__icontains='POLISH') |
             models.Q(subcategory__icontains='SYMMETRY') |
             models.Q(subcategory__icontains='THIN-MEDIUM') |
             models.Q(subcategory__icontains='MEDIUM WHITISH BLUE')) &
            models.Q(price__gte=0) & models.Q(price__lte=4.41)
        )
        serializer = ShopSerializer(shops, many=True)
        return Response(serializer.data)