from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category_list = [
            {'name': 'vegies'},
            {'name': 'meat'},
        ]
        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )
        Category.objects.bulk_create(category_for_create)



        product_list = [
            {'name': 'Artichoke', 'description': 'healthy replacement for chips', 'category': category_for_create[0],
             'price_for_1': '11'},
            {'name': 'Asparagus', 'description': 'healthy replacement for chips', 'category': category_for_create[0],
             'price_for_1': '12'},
            {'name': 'Aubergene', 'description': 'healthy replacement for chips', 'category':  category_for_create[0],
             'price_for_1': '13'},
            {'name': 'Avocado', 'description': 'healthy replacement for chips', 'category':  category_for_create[0], 'price_for_1': '14'},
        ]
        products_for_create = []

        for product_item in product_list:
            products_for_create.append(
                Product(**product_item)
            )

        Product.objects.bulk_create(products_for_create)
