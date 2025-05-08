
import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (-priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        if self.heap:
            priority, count, item = heapq.heappop(self.heap)
            return item
        raise IndexError("Pop from empty priority queue")

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

def heapify(arr, n, i, key):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and key(arr[l]) > key(arr[largest]):
        largest = l
    if r < n and key(arr[r]) > key(arr[largest]):
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, key)

def heap_sort(arr, key=lambda x: x):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, key)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, key)

    return arr[::-1]

class ProductRecommendationSystem:
    def __init__(self, products_db):
        self.products_db = products_db
        self.user_preferences = {}

    def add_user_preference(self, user_id, product_id, rating):
        if user_id not in self.user_preferences:
            self.user_preferences[user_id] = {}
        self.user_preferences[user_id][product_id] = rating

    def calculate_similarity(self, user_id, product):
        if user_id not in self.user_preferences:
            return 0

        user_ratings = self.user_preferences[user_id]
        similarity_score = 0

        for rated_product_id, rating in user_ratings.items():
            rated_product = self.products_db.get_product(rated_product_id)

            if rated_product['category'] == product['category']:
                similarity_score += 0.3 * rating

            price_diff = abs(rated_product['price'] - product['price']) / max(rated_product['price'], product['price'])
            similarity_score += 0.2 * (1 - price_diff) * rating

            if rated_product['brand'] == product['brand']:
                similarity_score += 0.1 * rating

        if len(user_ratings) > 0:
            similarity_score /= len(user_ratings)

        similarity_score += 0.2 * product['average_rating'] + 0.1 * product['popularity']
        return similarity_score

    def recommend_products(self, user_id, n=10, use_heap_sort=False):
        products = []
        for product in self.products_db.get_all_products():
            if user_id in self.user_preferences and product['id'] in self.user_preferences[user_id]:
                continue
            similarity = self.calculate_similarity(user_id, product)
            product['similarity_score'] = similarity
            products.append(product)

        if use_heap_sort:
            sorted_products = heap_sort(products, key=lambda p: p['similarity_score'])
            return sorted_products[:n]
        else:
            pq = PriorityQueue()
            for product in products:
                pq.push(product, product['similarity_score'])
            return [pq.pop() for _ in range(min(n, pq.size()))]
