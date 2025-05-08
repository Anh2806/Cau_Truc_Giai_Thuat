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
        self.add_product("P011", "Huawei MatePad 11.5",      "Tablet",      "Huawei",  12500000, 4.2, 0.74)
        self.add_product("P012", "Google Pixel 8 Pro",        "Smartphone",  "Google",  26500000, 4.7, 0.93)
        self.add_product("P013", "Lenovo Legion 5 Pro",       "Laptop",      "Lenovo",  34000000, 4.6, 0.88)
        self.add_product("P014", "Bose QuietComfort Ultra",   "Tai nghe",    "Bose",     8500000, 4.5, 0.81)
        self.add_product("P015", "Apple Watch Series 9",      "Wearable",    "Apple",    11500000, 4.8, 0.96)
        self.add_product("P016", "Dell Alienware AW3423DWF",  "Monitor",     "Dell",    23500000, 4.9, 0.83)
        self.add_product("P017", "Canon EOS R8 Body",         "Camera",      "Canon",   38500000, 4.4, 0.67)
        self.add_product("P018", "Asus ZenBook 14 OLED",      "Laptop",      "Asus",    29500000, 4.3, 0.79)
        self.add_product("P019", "Samsung Galaxy Buds3 Pro",  "Tai nghe",    "Samsung",  4500000, 4.2, 0.72)
        self.add_product("P020", "Kindle Scribe 64 GB",       "Tablet",      "Amazon",   9500000, 4.1, 0.69)
        self.add_product("P021", "Razer Blade 16 RTX 4090",   "Laptop",      "Razer",   89900000, 4.7, 0.55)
        self.add_product("P022", "DJI Mini 4 Pro Fly More",   "Drone",       "DJI",     23800000, 4.6, 0.76)
        self.add_product("P023", "Sony α6700 Kit 16‑50mm",    "Camera",      "Sony",    32900000, 4.5, 0.71)
        self.add_product("P024", "Xbox Series X 2 TB",        "Console",     "Microsoft",15900000,4.8, 0.84)
        self.add_product("P025", "NVIDIA GeForce RTX 4080 S", "GPU",         "NVIDIA",  39900000, 4.9, 0.62)
