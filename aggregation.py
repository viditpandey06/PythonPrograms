class Address:
    def __init__(self, door_number, street_name, city, state, postal_code):
        self.door_number = door_number
        self.street_name = street_name
        self.city = city
        self.state = state
        self.postal_code = postal_code

    def display_address(self):
        print(f"Address: {self.door_number}, {self.street_name}, {self.city}, {self.state}, {self.postal_code}")


class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address  # Aggregation - Customer has an Address

    def update_details(self, name=None, email=None, address=None):
        if name:
            self.name = name
        if email:
            self.email = email
        if address:
            self.address = address

    def view_details(self):
        print(f"Customer Name: {self.name}")
        print(f"Email: {self.email}")
        self.address.display_address()  # Display associated Address information



customer_address = Address("123", "Main Street", "Cityville", "State", "12345")
customer = Customer("John Doe", "john@example.com", customer_address)
print("Initial Customer Details:")
customer.view_details()
print()


customer.update_details(name="Jane Smith", email="jane@example.com")
new_address = Address("456", "Broadway", "Townsville", "State", "67890")
customer.update_details(address=new_address)

print("Updated Customer Details:")
customer.view_details()
