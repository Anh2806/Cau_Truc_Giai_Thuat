import tkinter as tk
from product_database import ProductDatabase
from recommendation_system import ProductRecommendationSystem
from ui import ProductRecommendationUI

def main():
    db = ProductDatabase()
    db.load_sample_data()

    recommendation_system = ProductRecommendationSystem(db)

    root = tk.Tk()
    app = ProductRecommendationUI(root, recommendation_system)
    root.mainloop()

if __name__ == "__main__":
    main()