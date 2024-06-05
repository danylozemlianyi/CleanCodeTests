from impl import (Database, EmailService, IDatabase, IEmailService,
                  IPaymentProcessor, PaymentProcessor)


# Factory for creating dependencies
class DependencyFactory:
    @staticmethod
    def create_database() -> IDatabase:
        # Factory method to create Database instance
        return Database()

    @staticmethod
    def create_payment_processor() -> IPaymentProcessor:
        # Factory method to create PaymentProcessor instance
        return PaymentProcessor()

    @staticmethod
    def create_email_service() -> IEmailService:
        # Factory method to create EmailService instance
        return EmailService()
