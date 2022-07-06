
class PurchaseOrder:

    def __init__(self, purchase_date, ISBN, user_id, full_address) -> None:
        self.purchase_date = purchase_date
        self.ISBN = ISBN
        self.user_id = user_id
        self.full_address = full_address

    def serialize(self):
        return {'purchase_date': self.purchase_date,
                'ISBN': self.ISBN,
                'user_id': self.user_id,
                'full_address': self.full_address
                }