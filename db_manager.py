import csv
from Modelo_parcial.src.models.book import Book
from Modelo_parcial.src.models.purchase_order import PurchaseOrder


def load_books():
    books = []
    with open('Modelo_parcial/src/db/books.csv', 'r') as books_file:
        rows = csv.DictReader(books_file)

        for row in rows:
            books.append(
                Book(
                    row['ISBN'],
                    row['title'],
                    row['author'],
                    row['price'],
                    row['published'],
                    row['language'],
                    row['number_pages'],
                    row['press'],
                    row['ranking']
                )
            )

        return books





def save_purchase_order(purchase):

    with open('Modelo_parcial/src/db/purchase_order.csv', 'a') as purchase_file:
        header = ['purchase_date', 'ISBN', 'user_id', 'full_address']

        writer = csv.DictWriter(purchase_file, fieldnames=header)

        if purchase_file.tell() == 0:
            writer.writeheader()

        writer.writerow(purchase)


def load_purchase_orders():
    orders = []
    with open('Modelo_parcial/src/db/purchase_order.csv', 'r') as orders_file:
        rows = csv.DictReader(orders_file)

        for row in rows:
            orders.append(
                PurchaseOrder(
                    row['purchase_date'],
                    row['ISBN'],
                    row['user_id'],
                    row['full_address'],

                )
            )

        return orders