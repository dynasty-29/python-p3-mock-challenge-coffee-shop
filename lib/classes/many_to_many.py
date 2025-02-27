class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters long.")
        if hasattr(self, '_name'):
            raise AttributeError("Coffee name cannot be changed after instantiation.")
        self._name = value

    def orders(self):
        return self._orders

    def customers(self):
        return list(set(order.customer for order in self._orders))

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)


class Customer:
    _all_customers = []

    def __init__(self, name):
        self.name = name
        self._orders = []
        Customer._all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        if len(value) < 1 or len(value) > 15:
            raise ValueError("Name must be between 1 and 15 characters long.")
        self._name = value

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        return order
    
    @classmethod
    def most_aficionado(cls, coffee):
        max_spent = 0
        top_customer = None
        for customer in cls._all_customers:
            total_spent = sum(order.price for order in customer.orders() if order.coffee == coffee)
            if total_spent > max_spent:
                max_spent = total_spent
                top_customer = customer
        return top_customer


class Order:
    all = []  
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        self.customer._orders.append(self) 
        self.coffee._orders.append(self)  
        Order.all.append(self)  

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise ValueError("Price must be a float.")
        if value < 1.0 or value > 10.0:
            raise ValueError("Price must be between 1.0 and 10.0.")
        if hasattr(self, '_price'):
            raise AttributeError("Price cannot be changed after instantiation.")
        self._price = value

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise ValueError("Customer must be of type Customer.")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise ValueError("Coffee must be of type Coffee.")
        self._coffee = value