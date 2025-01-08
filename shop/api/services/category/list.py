from service_objects.services import Service

from db.models import Category


class ListCategoriesService(Service):


    def process(self):
        return Category.objects.all()

