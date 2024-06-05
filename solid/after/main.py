from factory import DependencyFactory
from interfaces import IDatabase, IEmailService, IPaymentProcessor


# High-level OrderProcessor class
class OrderProcessor:
    def __init__(
        self,
        db: IDatabase,
        payment_processor: IPaymentProcessor,
        email_service: IEmailService,
    ):
        # Injecting dependencies, reducing coupling and improving testability
        self.db = db
        self.payment_processor = payment_processor
        self.email_service = email_service

    def process_order(self, order):
        self.db.save_order(order)
        if self.payment_processor.process_payment(order):
            self.email_service.send_confirmation(order)
        else:
            self.email_service.send_failure(order)


if __name__ == "__main__":
    db = DependencyFactory.create_database()
    payment_processor = DependencyFactory.create_payment_processor()
    email_service = DependencyFactory.create_email_service()

    # Injecting dependencies into OrderProcessor
    order_processor = OrderProcessor(db, payment_processor, email_service)
    order = {}
    order_processor.process_order(order)
