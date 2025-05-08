import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox

class ProductRecommendationUI:
    def __init__(self, master, recommendation_system):
        self.master = master
        self.recommendation_system = recommendation_system

        master.title("Hệ thống đề xuất sản phẩm")
        master.geometry("800x600")

        self.tab_control = ttk.Notebook(master)

        self.recommend_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.recommend_tab, text="Đề xuất sản phẩm")

        self.rate_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.rate_tab, text="Xem và đánh giá sản phẩm")

        self.tab_control.pack(expand=1, fill="both")

        self.setup_recommend_tab()
        self.setup_rate_tab()

    def setup_recommend_tab(self):
        user_frame = ttk.LabelFrame(self.recommend_tab, text="Thông tin người dùng")
        user_frame.pack(fill="x", padx=10, pady=10)

        ttk.Label(user_frame, text="ID người dùng:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.user_id_entry = ttk.Entry(user_frame)
        self.user_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(user_frame, text="Số lượng đề xuất:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.num_recommendations_entry = ttk.Entry(user_frame)
        self.num_recommendations_entry.insert(0, "10")
        self.num_recommendations_entry.grid(row=0, column=3, padx=5, pady=5, sticky="w")

        recommend_button = ttk.Button(user_frame, text="Nhận đề xuất", command=self.get_recommendations)
        recommend_button.grid(row=0, column=4, padx=5, pady=5, sticky="w")

        self.recommendation_frame = ttk.LabelFrame(self.recommend_tab, text="Sản phẩm đề xuất")
        self.recommendation_frame.pack(fill="both", expand=True, padx=10, pady=10)

        columns = ("id", "name", "category", "brand", "price", "rating", "similarity")
        self.recommendation_tree = ttk.Treeview(self.recommendation_frame, columns=columns, show="headings")

        for col in columns:
            self.recommendation_tree.heading(col, text=col.capitalize())
            self.recommendation_tree.column(col, width=100)

        scrollbar = ttk.Scrollbar(self.recommendation_frame, orient="vertical", command=self.recommendation_tree.yview)
        self.recommendation_tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.recommendation_tree.pack(fill="both", expand=True)

    def setup_rate_tab(self):
        self.products_frame = ttk.LabelFrame(self.rate_tab, text="Danh sách sản phẩm")
        self.products_frame.pack(fill="both", expand=True, padx=10, pady=10)

        columns = ("id", "name", "category", "brand", "price", "rating")
        self.products_tree = ttk.Treeview(self.products_frame, columns=columns, show="headings")

        for col in columns:
            self.products_tree.heading(col, text=col.capitalize())
            self.products_tree.column(col, width=100)

        scrollbar = ttk.Scrollbar(self.products_frame, orient="vertical", command=self.products_tree.yview)
        self.products_tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.products_tree.pack(fill="both", expand=True)

        self.products_tree.bind("<Double-1>", self.show_product_rating_dialog)
        self.load_products()

    def load_products(self):
        for item in self.products_tree.get_children():
            self.products_tree.delete(item)

        for product in self.recommendation_system.products_db.get_all_products():
            self.products_tree.insert("", "end", values=(
                product['id'],
                product['name'],
                product['category'],
                product['brand'],
                f"{product['price']}đ",
                f"{product['average_rating']:.1f}"
            ))

    def get_recommendations(self):
        try:
            user_id = self.user_id_entry.get()
            if not user_id:
                messagebox.showerror("Lỗi", "Vui lòng nhập ID người dùng")
                return

            n = int(self.num_recommendations_entry.get())
            if n <= 0:
                messagebox.showerror("Lỗi", "Số lượng đề xuất phải lớn hơn 0")
                return

            for item in self.recommendation_tree.get_children():
                self.recommendation_tree.delete(item)

            recommendations = self.recommendation_system.recommend_products(user_id, n)

            for product in recommendations:
                self.recommendation_tree.insert("", "end", values=(
                    product['id'],
                    product['name'],
                    product['category'],
                    product['brand'],
                    f"{product['price']}đ",
                    f"{product['average_rating']:.1f}",
                    f"{product['similarity_score']:.2f}"
                ))
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def show_product_rating_dialog(self, event):
        item = self.products_tree.selection()[0]
        product_id = self.products_tree.item(item, "values")[0]
        product_name = self.products_tree.item(item, "values")[1]

        dialog = tk.Toplevel(self.master)
        dialog.title(f"Đánh giá sản phẩm: {product_name}")
        dialog.geometry("400x200")
        dialog.transient(self.master)
        dialog.grab_set()

        ttk.Label(dialog, text="ID người dùng:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        user_id_entry = ttk.Entry(dialog)
        user_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(dialog, text="Đánh giá (1-5):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        rating_var = tk.StringVar()
        rating_combobox = ttk.Combobox(dialog, textvariable=rating_var, values=["1", "2", "3", "4", "5"])
        rating_combobox.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        def submit_rating():
            try:
                user_id = user_id_entry.get()
                if not user_id:
                    messagebox.showerror("Lỗi", "Vui lòng nhập ID người dùng")
                    return

                rating = float(rating_var.get())
                if rating < 1 or rating > 5:
                    messagebox.showerror("Lỗi", "Đánh giá phải từ 1 đến 5")
                    return

                self.recommendation_system.add_user_preference(user_id, product_id, rating)
                messagebox.showinfo("Thành công", "Đã thêm đánh giá thành công!")
                dialog.destroy()

            except Exception as e:
                messagebox.showerror("Lỗi", str(e))

        submit_button = ttk.Button(dialog, text="Gửi đánh giá", command=submit_rating)
        submit_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)