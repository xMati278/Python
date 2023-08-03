class Manager:
    def __init__(self):
        self.orders = {"karty": 15}

    def add_order(self, item, amount):
        if item in self.orders.keys():
            self.orders[item] += amount
        else:
            self.orders[item] = amount
        print(self.orders)

    def sell(self, id_to_sell):
        self.orders[id_to_sell] -= 1
        print(self.orders)


class Order:
    def __init__(self, order_id, name, price):
        self.id = order_id
        self.name = name
        self.price = price


def main():
    manager = Manager()
    manager.add_order("karty", 3)
    manager.add_order("klocki", 15)
    manager.sell("karty")


if __name__ == "__main__":
    main()
    