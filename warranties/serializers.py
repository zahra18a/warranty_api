from rest_framework import serializers
from .models import Product, Warranty

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class WarrantySerializer(serializers.ModelSerializer):
    class Meta:
        model = Warranty
        fields = '__all__'

    def validate(self, data):
        product = data.get('product')
        warranty_code = data.get('warranty_code')

        if Warranty.objects.filter(warranty_code=warranty_code).exists():
            raise serializers.ValidationError("این کد گارانتی قبلاً ثبت شده است.")

        if product.product_code not in warranty_code:
            raise serializers.ValidationError("کد گارانتی با محصول انتخاب‌شده مطابقت ندارد.")

        return data
