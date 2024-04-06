


class Card:
    def __init__(self, request):
        self.session = request.session

    def add(self, product, product_count):
        product_id = str(product.id)
        product_count = int(product_count)
       
