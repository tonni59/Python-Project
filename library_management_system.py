import tkinter as tk
from tkinter import messagebox, ttk

# Main application class
class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("800x500")
        self.root.config(bg="#F5F5F5")

        # Data store
        self.books = []

        # Title Label
        title = tk.Label(self.root, text="Library Management System", font=("Helvetica", 24, "bold"), bg="#4CAF50", fg="white")
        title.pack(side="top", fill="x")

        # Frames
        self.manage_frame = tk.Frame(self.root, bd=5, relief="ridge", bg="#4CAF50")
        self.manage_frame.place(x=20, y=70, width=350, height=400)

        self.display_frame = tk.Frame(self.root, bd=5, relief="ridge", bg="#4CAF50")
        self.display_frame.place(x=400, y=70, width=380, height=400)

        # Manage Frame Widgets
        self.lbl_title = tk.Label(self.manage_frame, text="Book Title", font=("Helvetica", 12), bg="#4CAF50", fg="white")
        self.lbl_title.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        self.txt_title = tk.Entry(self.manage_frame, font=("Helvetica", 12), bd=3, relief="groove")
        self.txt_title.grid(row=0, column=1, pady=10, padx=10, sticky="w")

        self.lbl_author = tk.Label(self.manage_frame, text="Author", font=("Helvetica", 12), bg="#4CAF50", fg="white")
        self.lbl_author.grid(row=1, column=0, pady=10, padx=10, sticky="w")

        self.txt_author = tk.Entry(self.manage_frame, font=("Helvetica", 12), bd=3, relief="groove")
        self.txt_author.grid(row=1, column=1, pady=10, padx=10, sticky="w")

        self.lbl_year = tk.Label(self.manage_frame, text="Year", font=("Helvetica", 12), bg="#4CAF50", fg="white")
        self.lbl_year.grid(row=2, column=0, pady=10, padx=10, sticky="w")

        self.txt_year = tk.Entry(self.manage_frame, font=("Helvetica", 12), bd=3, relief="groove")
        self.txt_year.grid(row=2, column=1, pady=10, padx=10, sticky="w")

        self.lbl_isbn = tk.Label(self.manage_frame, text="ISBN", font=("Helvetica", 12), bg="#4CAF50", fg="white")
        self.lbl_isbn.grid(row=3, column=0, pady=10, padx=10, sticky="w")

        self.txt_isbn = tk.Entry(self.manage_frame, font=("Helvetica", 12), bd=3, relief="groove")
        self.txt_isbn.grid(row=3, column=1, pady=10, padx=10, sticky="w")

        # Buttons
        self.btn_add = tk.Button(self.manage_frame, text="Add Book", font=("Helvetica", 12, "bold"), bg="#2196F3", fg="white", command=self.add_book)
        self.btn_add.grid(row=4, column=0, pady=20, padx=10, sticky="w")

        self.btn_delete = tk.Button(self.manage_frame, text="Delete Book", font=("Helvetica", 12, "bold"), bg="#F44336", fg="white", command=self.delete_book)
        self.btn_delete.grid(row=4, column=1, pady=20, padx=10, sticky="w")

        self.btn_clear = tk.Button(self.manage_frame, text="Clear", font=("Helvetica", 12, "bold"), bg="#FFC107", fg="black", command=self.clear_fields)
        self.btn_clear.grid(row=5, column=0, pady=10, padx=10, sticky="w")

        self.btn_exit = tk.Button(self.manage_frame, text="Exit", font=("Helvetica", 12, "bold"), bg="#9E9E9E", fg="white", command=self.root.quit)
        self.btn_exit.grid(row=5, column=1, pady=10, padx=10, sticky="w")

        # Display Frame Widgets
        self.book_table = ttk.Treeview(self.display_frame, columns=("Title", "Author", "Year", "ISBN"), show="headings")
        self.book_table.heading("Title", text="Title")
        self.book_table.heading("Author", text="Author")
        self.book_table.heading("Year", text="Year")
        self.book_table.heading("ISBN", text="ISBN")
        self.book_table.column("Title", width=100)
        self.book_table.column("Author", width=100)
        self.book_table.column("Year", width=50)
        self.book_table.column("ISBN", width=80)
        self.book_table.pack(fill="both", expand=True)

    def add_book(self):
        title = self.txt_title.get()
        author = self.txt_author.get()
        year = self.txt_year.get()
        isbn = self.txt_isbn.get()

        if title and author and year and isbn:
            self.books.append({"Title": title, "Author": author, "Year": year, "ISBN": isbn})
            self.update_table()
            self.clear_fields()
            messagebox.showinfo("Success", "Book added successfully!")
        else:
            messagebox.showerror("Error", "All fields are required!")

    def delete_book(self):
        selected_item = self.book_table.selection()
        if selected_item:
            item = self.book_table.item(selected_item)
            title = item["values"][0]
            self.books = [book for book in self.books if book["Title"] != title]
            self.update_table()
            messagebox.showinfo("Success", "Book deleted successfully!")
        else:
            messagebox.showerror("Error", "No book selected!")

    def update_table(self):
        for row in self.book_table.get_children():
            self.book_table.delete(row)
        for book in self.books:
            self.book_table.insert("", "end", values=(book["Title"], book["Author"], book["Year"], book["ISBN"]))

    def clear_fields(self):
        self.txt_title.delete(0, "end")
        self.txt_author.delete(0, "end")
        self.txt_year.delete(0, "end")
        self.txt_isbn.delete(0, "end")


# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagementSystem(root)
    root.mainloop()
