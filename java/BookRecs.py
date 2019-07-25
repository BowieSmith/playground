# Customer: ("name", (purchase tuples))
# Purchase: ("type", "name")

if __name__ == "__main__":
    customers = [
            ("Bob", (
                ("book", "SICP"),
                ("book", "CLRS"),
                ("car", "Soul"))),
            ("Sara", (
                ("car", "Kia"),
                ("book", "OTR"))),
            ("Mike", (
                ("book", "CLRS"),
                ("bike", "XRS"),
                ("book", "SICP")))]

    print("\nCustomer List:")
    for customer in customers:
        print(customer)

    print("\nPurchases List:")
    purchase_lists = [customer[1] for customer in customers]
    purchases = [purchase for sublist in purchase_lists for purchase in sublist]
    for purchase in purchases:
        print(purchase)

    print("\nBook Purchases List:")
    book_purchases = [purchase for purchase in purchases if purchase[0] == "book"]
    for book_purchase in book_purchases:
        print(book_purchase)

    print("\nBook Purchase Counts:")
    book_purchase_counts = {}
    for book_purchase in book_purchases:
        if book_purchase in book_purchase_counts:
            book_purchase_counts[book_purchase] += 1
        else:
            book_purchase_counts[book_purchase] = 1
    print(book_purchase_counts)

    print("\nOrdered Book Purchases (Descending order by purchase count)")
    ordered_book_purchases = sorted(book_purchase_counts.items(), key=lambda item: item[1], reverse=True)
    print(ordered_book_purchases)
