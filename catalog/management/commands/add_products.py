import django.db.utils
from django.core.management import BaseCommand
from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options) -> None:
        """Add information items"""

        print("Add information items.")
        new_items_list = [
            {
                "name": "KALLAX",
                "description": "Hang it on the wall or stand it on the floor – the KALLAX series adapts to your needs. Smooth surfaces and rounded corners give a quality feel and you can personalise the unit with inserts and boxes.",
                "image": "images/KALLAX.jpg",
                "category_id": 100,
                "price": 1000,
                "slug": "KALLAX"
            },
            {
                "name": "FLARRA",
                "description": "In this mini chest of drawers you can store small things like desk accessories, hair clips and jewellery. Perfect to put on a desk or chest of drawers – and can be folded flat if you want to stash it away.",
                "image": "images/FLARRA.jpg",
                "category_id": 100,
                "price": 1000,
                "slug": "FLARRA"
            },
            {
                "name": "TJABBA",
                "description": "This magazine file happily takes care of everything from newspapers and bills to the children's first drawings. It is also simple to move if you want to reorganise the bookcase.",
                "image": "images/TJABBA.jpg",
                "category_id": 100,
                "price": 1500,
                "slug": "TJABBA"
            },
            {
                "name": "NAMMARO",
                "description": "Create a comfy living room feel outdoors with NÄMMARÖ series. With everything you need for chill moments,long dinners and cheerful summer parties, no matter if you have a balcony, terrace or garden.",
                "image": "images/NAMMARO.jpg",
                "category_id": 100,
                "price": 1200,
                "slug": "NAMMARO"
            },
            {
                "name": "KOLBJORN",
                "description": "Perfect to have on the balcony for plant pots and garden tools, in the hallway for shoes or in the bathroom to keep shampoos and towels organised. May be completed with KOLBJÖRN shelving unit on top.",
                "image": "images/KOLBJORN.jpg",
                "category_id": 100,
                "price": 1900,
                "slug": "KOLBJORN"
            },
            {
                "name": "TORDH",
                "description": "This low TORDH shelving unit has room for plant pots and tools. Perfect on a small terrace or balcony – and complete with more units when you like. Made of acacia and matches ÄPPLARÖ outdoor furniture.",
                "image": "images/TORDH.jpg",
                "category_id": 100,
                "price": 1900,
                "slug": "TORDH"
                },
            {
                "name": "HYLLIS",
                "description": "Practical storage solution in galvanised steel for small spaces indoors or outdoors. Just as suitable on the balcony as in the hallway, kitchen or bathroom. Sturdy, lightweight and approved for wet areas.",
                "image": "images/HYLLIS.jpg",
                "category_id": 100,
                "price": 1900,
                "slug": "HYLLIS",

            },
            {
                "name": "FLAMSIG",
                "description": "Treat yourself to the luxury of this simple white dinnerware – easy to use and suitable for any occasion. Set a stylish table for everyday meals or add personal accessories for a dinner party.",
                "image": "images/FLAMSIG.jpg",
                "category_id": 101,
                "price": 5000,
                "slug": "FLAMSIG"
            },
            {
                "name": "GLADELIG",
                "description": "The beautiful sandy-glazed surface turns every meal into pure joy. Decorate your table with clean classic shapes and a strong crafted look. A timeless feel with a unique and decorative design.",
                "image": "images/GLADELIG.jpg",
                "category_id": 101,
                "price": 3000,
                "slug": "GLADELIG"
            },
            {
                "name": "VARDAGEN",
                "description": "Life’s a party, but most days are pretty ordinary. Make the most of them by serving up good food on this simple,timeless dinnerware. Like it? There’s a whole series with the same name.",
                "image": "images/VARDAGEN.jpg",
                "category_id": 101,
                "price": 3100,
                "slug": "VARDAGEN",
            },
            {
                "name": "JAKOBSBYN",
                "description": "This lampshade in glass is mouth blown by a skilled craftsperson and therefore unique.",
                "image": "images/JAKOBSBYN.jpg",
                "category_id": 102,
                "price": 3100,
                "slug": "JAKOBSBYN",
            },
            {
                "name": "LUFTMASSA",
                "description": "Create your own personalised pendant or floor lamp by combining the lampshade with your choice of cord set or lamp base.",
                "image": "images/LUFTMASSA.jpg",
                "category_id": 102,
                "price": 1400,
                "slug": "LUFTMASSA"
            },
            {
                "name": "VRENSTED",
                "description": "This rug will serve its purpose wherever you like. Made from easy-care polypropylene that can handle wear and tear both outdoors and indoors. It’s reversible so you can switch the look every now and then.",
                "image": "images/VRENSTED.jpg",
                "category_id": 103,
                "price": 1100,
                "slug": "VRENSTED"
            }
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
