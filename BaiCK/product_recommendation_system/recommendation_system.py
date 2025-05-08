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
    
    def peek(self):
        if self.heap:
            priority, count, item = self.heap[0]
            return item
        raise IndexError("Peek from empty priority queue")
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def size(self):
        return len(self.heap)

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

    def recommend_products(self, user_id, n=10):
        pq = PriorityQueue()

        for product in self.products_db.get_all_products():
            if user_id in self.user_preferences and product['id'] in self.user_preferences[user_id]:
                continue

            similarity = self.calculate_similarity(user_id, product)
            product['similarity_score'] = similarity
            pq.push(product, similarity)

        recommendations = []
        for _ in range(min(n, pq.size())):
            recommendations.append(pq.pop())

        return recommendations