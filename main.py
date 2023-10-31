class Book:
    def __init__(self, book_title, total_pages, readed_to_page):
        self.title = book_title
        self.total_pages = total_pages
        self.readed_to_page = readed_to_page

    def reader_percent(self):
        if int(self.total_pages) != 0:
            readed_percent = (int(self.readed_to_page) * 100) / int(self.total_pages)
            return readed_percent


class Library:
    def __init__(self):
        self.books = []

    def add_new_book(self, book):
        if isinstance(book, Book) and (book.total_pages >= book.readed_to_page):
            self.books.append(book)

    def delete_book(self, book_title):
        for book in self.books:
            if book_title == book.title:
                self.books.remove(book)
                print("Книга була видалена успішно!")
                return
        else:
            print("Надана книга не є елементом бібліотеки, або не є об'єктом класу Book")

    def update_book_information(self, book_title, readed_to_page):
        for book in self.books:
            if book_title == book.title:
                book.readed_to_page = readed_to_page

    def display_books_info(self, display_books_info):
        if display_books_info is True:
            for book in reversed(list(self.books)):
                print("Назва книги - " + book.title)
                print("Відсоток прочитаних сторінок - " + str(round(book.reader_percent(), 2)) + "%\n")
        else:
            print("Дякуємо, ваші книги було успішно збережено!")


library = Library()


def add_book():
    book_title = input("Введіть назву книги, яку хочете додати: ")
    total_book_pages = input("Введіть кількість сторінок у цій книзі: ")
    readed_to_page = input("Введіть сторінку, до якої ви дочитали: ")
    if not total_book_pages.isdigit() or not readed_to_page.isdigit() or int(total_book_pages) < int(readed_to_page):
        print("Некоректні данні сторінок! Введіть книгу з коректними данними ще раз!")
    else:
        display_books = input("Чи бажаєте ви переглянути бібліотеку? (Так/Ні): ")
        want_to_add_book = Book(book_title, total_book_pages, readed_to_page)
        library.add_new_book(want_to_add_book)
        if display_books.lower() == "так":
            library.display_books_info(True)
        else:
            library.display_books_info(False)


while True:
    if len(library.books) > 0:
        while True:
            continue_or_stop = input("Чи бажаєте ви продовжити працювати у програмі? (Так/Ні): ")
            if continue_or_stop.lower() == "ні":
                break
            add_delete_or_update_book = input("Введіть 'Додати', для запису книги у бібліотеку, 'Видалити' задля видалення книги з бібліотеки, та 'Оновити' задля оновлення кількості сторінок: ")
            if add_delete_or_update_book.lower() == "додати":
                while True:
                    add_book()
                    add_that_one_book = input("Чи бажаєте ви ввести ще книгу? (Так/Ні): ")
                    if add_that_one_book.lower() == "ні":
                        break
            if add_delete_or_update_book.lower() == "видалити":
                while True:
                    display_books = input("Чи бажаєте ви переглянути бібліотеку? (Так/Ні): ")
                    if display_books.lower() == "так":
                        library.display_books_info(True)
                    book_title = input("Введіть назву книги, яку хочете видалити: ")
                    delete_book_attention = input("Ви дійсно хочете видалити цю книгу? (Так/Ні): ")
                    if delete_book_attention.lower() == "так":
                        library.delete_book(book_title)
                        display_books = input("Чи бажаєте ви переглянути бібліотеку? (Так/Ні): ")
                        if display_books.lower() == "так":
                            library.display_books_info(True)
                    else:
                        break
                    if len(library.books) > 0:
                        delete_that_one_book_attention = input("Чи ви хочете видалити, ще одну книгу? (Так/Ні): ")
                        if delete_that_one_book_attention.lower() == "ні":
                            break
                    else:
                        break
            if add_delete_or_update_book.lower() == 'оновити':
                while True:
                    display_books = input("Чи бажаєте ви переглянути бібліотеку? (Так/Ні): ")
                    if display_books.lower() == "так":
                        library.display_books_info(True)
                    book_title = input("Введіть назву книги, яку хочете оновити: ")
                    new_readed_to_page_info = input("Введіть нові значення прочитаних сторінок: ")
                    update_book_attention = input("Ви дійсно хочете оновити цю книгу? (Так/Ні): ")
                    if update_book_attention.lower() == "так":
                        library.update_book_information(book_title, new_readed_to_page_info)
                        display_books = input("Чи бажаєте ви переглянути бібліотеку? (Так/Ні): ")
                        if display_books.lower() == "так":
                            library.display_books_info(True)
                    else:
                        break
    else:
        add_book()
    stop_app = input("Зупинити виконання програми? (Так/Ні): ")
    if stop_app.lower() == "так":
        break
