from interfaces import IDatabase, IEmailService, IPaymentProcessor


# Concrete implementations of the interfaces
class Database(IDatabase):
    def save_order(self, order):
        print("Order saved to database")


class PaymentProcessor(IPaymentProcessor):
    def process_payment(self, order):
        print("Processing payment")
        return True


class EmailService(IEmailService):
    def send_confirmation(self, order):
        print("Sending order confirmation email")

    def send_failure(self, order):
        print("Sending payment failure email")
