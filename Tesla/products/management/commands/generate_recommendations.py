from django.core.management.base import BaseCommand
from products.models import Product, SearchQuery, RecommendedProduct

class Command(BaseCommand):
    help = 'Generate recommended products based on search queries'

    def handle(self, *args, **kwargs):
        # Your logic to generate recommendations based on search queries goes here
        # For example:
        search_queries = SearchQuery.objects.all()

        for query in search_queries:
            recommended_product = None
            if 'Model' in query.query_text:
                # If the query contains 'Model', recommend the MobileConnector product
                recommended_product = Product.objects.get(name__iexact='MobileConnector')
            elif 'Solar' in query.query_text:
                # If the query contains 'Solar', recommend the PowerWall product
                recommended_product = Product.objects.get(name__iexact='PowerWall')

            if recommended_product:
                # Create RecommendedProduct object and save it to the database
                RecommendedProduct.objects.get_or_create(search_query=query, product=recommended_product)

        self.stdout.write(self.style.SUCCESS('Recommendations generated successfully.'))
