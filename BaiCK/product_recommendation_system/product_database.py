class ProductDatabase:
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, name, category, brand, price, average_rating, popularity):
        self.products[product_id] = {
            'id': product_id,
            'name': name,
            'category': category,
            'brand': brand,
            'price': price,
            'average_rating': average_rating,
            'popularity': popularity
        }

    def get_product(self, product_id):
        return self.products.get(product_id)

    def get_all_products(self):
        return list(self.products.values())

    def load_sample_data(self):
        self.add_product("P001", "Laptop Dell XPS 13", "Laptop", "Dell", 30000000, 4.5, 0.9)
        self.add_product("P002", "iPhone 14", "Smartphone", "Apple", 25000000, 4.7, 0.95)
        self.add_product("P003", "Samsung Galaxy S23", "Smartphone", "Samsung", 23000000, 4.6, 0.92)
        self.add_product("P004", "MacBook Air M2", "Laptop", "Apple", 32000000, 4.8, 0.97)
        self.add_product("P005", "Sony WH-1000XM5", "Tai nghe", "Sony", 9000000, 4.4, 0.85)
        self.add_product("P006", "iPad Pro 2022", "Tablet", "Apple", 28000000, 4.6, 0.91)
        self.add_product("P007", "Kindle Paperwhite", "Tablet", "Amazon", 3500000, 4.3, 0.75)
        self.add_product("P008", "Asus ROG Phone 7", "Smartphone", "Asus", 22000000, 4.2, 0.78)
        self.add_product("P009", "Samsung Galaxy Tab S8", "Tablet", "Samsung", 19000000, 4.5, 0.82)
        self.add_product("P010", "LG Gram 2023", "Laptop", "LG", 27000000, 4.1, 0.7)