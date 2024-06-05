class OrderProcessor:
    def __init__(self):
        # Directly creating dependencies, tightly coupling this class to specific implementations
        pass

    def process_order(self, order):
        # High-level module directly depends on low-level modules
        self.save_order(order)
        if self.process_payment(order):
            self.send_confirmation(order)
        else:
            self.send_failure(order)

    def save_order(self, order):
        print("Order saved to database")

    def process_payment(self, order):
        print("Processing payment")
        return True

    def send_confirmation(self, order):
        print("Sending order confirmation email")

    def send_failure(self, order):
        print("Sending payment failure email")