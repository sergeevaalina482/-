import tkinter as tk
import random
import json

class QuoteGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Quote Generator")
        
        self.quotes = self.load_quotes()  # Загрузка цитат из JSON или использование предопределенного списка
        self.history = []

        self.quote_label = tk.Label(root, text="", wraplength=300)
        self.quote_label.pack(pady=20)

        self.generate_button = tk.Button(root, text="Сгенерировать цитату", command=self.generate_quote)
        self.generate_button.pack(pady=10)

        self.history_label = tk.Label(root, text="История:")
        self.history_label.pack()

        self.history_listbox = tk.Listbox(root, width=50)
        self.history_listbox.pack(pady=10)

        self.author_entry = tk.Entry(root)
        self.author_entry.pack(pady=5)
        self.filter_button = tk.Button(root, text="Фильтровать по автору", command=self.filter_by_author)
        self.filter_button.pack(pady=5)

        self.theme_entry = tk.Entry(root)
        self.theme_entry.pack(pady=5)
        self.theme_filter_button = tk.Button(root, text="Фильтровать по теме", command=self.filter_by_theme)
        self.theme_filter_button.pack(pady=5)

        self.load_history()  # Загрузка истории при старте

    def generate_quote(self):
        quote = random.choice(self.quotes)
        self.quote_label.config(text=f"{quote['text']} - {quote['author']}")
        self.history_listbox.insert(tk.END, f"{quote['text']} - {quote['author']}")
        self.save_history()

    def load_quotes(self):
        try:
            with open("quotes.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return [
                {"text": "Будь собой; все остальные роли уже заняты.", "author": "Оскар Уайльд", "theme": "саморазвитие"},
                {"text": "Жизнь — это то, что происходит, пока вы строите другие планы.", "author": "Джон Леннон", "theme": "жизнь"},
                {"text": "Счастье — это не что иное, как здоровье и плохая память.", "author": "Альберт Швейцер", "theme": "счастье"},
                {"text": "Сложности не могут остановить меня. Каждое препятствие - это возможность научиться чему-то новому.", "author": "Нельсон Мандела", "theme": "мотивация"},
                {"text": "Самый лучший способ предсказать будущее — это создать его.", "author": "Питер Друкер", "theme": "будущее"},
            ]

    def save_history(self):
        with open("history.json", "w") as f:
            history = list(self.history_listbox.get(0, tk.END))
            json.dump(history, f)

    def load_history(self):
        try:
            with open("history.json", "r") as f:
                history = json.load(f)
                for item in history:
                    self.history_listbox.insert(tk.END, item)
        except FileNotFoundError:
            pass

    def filter_by_author(self):
        author = self.author_entry.get().strip()
        self.history_listbox.delete(0, tk.END)
        for quote in self.quotes:
            if author.lower() in quote['author'].lower():
                self.history_listbox.insert(tk.END, f"{quote['text']} - {quote['author']}")

    def filter_by_theme(self):
        theme = self.theme_entry.get().strip()
        self.history_listbox.delete(0, tk.END)
        for quote in self.quotes:
            if theme.lower() in quote['theme'].lower():
                self.history_listbox.insert(tk.END, f"{quote['text']} - {quote['author']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuoteGenerator(root)
    root.mainloop()
