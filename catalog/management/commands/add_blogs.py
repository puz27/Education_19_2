from django.core.management import BaseCommand
from catalog.models import Blog


class Command(BaseCommand):

    def handle(self, *args, **options) -> None:
        """Add information blogs"""

        print("Add information categories.")
        new_categories_list = [
            {
                "name": "INGOLT",
                "description": "In the production of the chair, the most environmentally friendly and durable material for the production of furniture is used - solid pine. Which only gets better with time.The wood is impregnated with wood stain and covered with a transparent acrylic lacquer.",
                "slug": "INGOLT",
                "image": "images/INGOLT.jpg"
            },
            {
                "name": "KANZAS",
                "description": "In the production of the chair, the most environmentally friendly and durable material for the production of furniture is used - solid pine. Which only gets better with time.The wood is impregnated with wood stain and covered with a transparent acrylic lacquer.",
                "slug": "KANZAS",
                "image": "images/KANZAS.jpg",
            },
            ]
        old_blog_list = []
        blog_for_create = []

        # find old data
        get_categories = Blog.objects.all().values('name')
        for data in get_categories:
            old_blog_list.append(data["name"])

        # add new data
        for category in new_categories_list:
            if category["name"] not in old_blog_list:
                blog_for_create.append(
                    Blog(**category)
                    )

        print(f"Add:{blog_for_create}")
        Blog.objects.bulk_create(blog_for_create)
