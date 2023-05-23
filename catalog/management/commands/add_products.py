import django.db.utils
from django.core.management import BaseCommand
from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Add information items.")
        new_items_list = [
            {"name": "Cat", "description": "Little cat.", "image": "images/cat.png", "category_id": 101, "price": 111},
            {"name": "Dog", "description": "Little dog.", "image": "images/dog.png", "category_id": 101, "price": 222},
            {"name": "TV-SET", "description": "Samsung.", "image": "images/TV.png", "category_id": 100, "price": 10000},
            {"name": "Gibson", "description": "Best guitar!", "image": "images/gibson.png", "category_id": 104, "price": 5000},
            {"name": "Fender", "description": "Best guitar!", "image": "images/fender.png", "category_id": 104, "price": 7000},
            {"name": "ESP", "description": "Best guitar!", "image": "images/ESP.png", "category_id": 104, "price": 4000},
            ]
        old_items_list = []
        items_for_create = []

        # find old data
        get_items = Product.objects.all().values('name')
        for data in get_items:
            old_items_list.append(data["name"])

        # add new data
        for category in new_items_list:
            if category["name"] not in old_items_list:
                items_for_create.append(
                    Product(**category)
                    )

        try:
            Product.objects.bulk_create(items_for_create)
            print(f"Add:{items_for_create}")
        except django.db.utils.IntegrityError as er:
            print(f"Check keys!\n{er}")
