from service_objects.services import Service

from db.models import Product


class ProductsListService(Service):

    def process(self):
        return self.get_list_products

    @property
    def get_list_products(self):
        return Product.objects.all().order_by('id')
