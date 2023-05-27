from django.core.management import BaseCommand
from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options) -> None:
        """Add information categories"""

        print("Add information categories.")
        new_categories_list = [
            {"id": 100, "name": "furniture", "description": "furniture"},
            {"id": 101, "name": "kitchenware", "description": "kitchenware"},
            {"id": 102, "name": "lighting", "description": "lighting"},
            {"id": 103, "name": "textiles", "description": "textiles"}
            ]
        old_categories_list = []
        categories_for_create = []

        # find old data
        get_categories = Category.objects.all().values('name')
        for data in get_categories:
            old_categories_list.append(data["name"])

        # add new data
        for category in new_categories_list:
            if category["name"] not in old_categories_list:
                categories_for_create.append(
                    Category(**category)
                    )

        print(f"Add:{categories_for_create}")
        Category.objects.bulk_create(categories_for_create)
