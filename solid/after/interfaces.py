from abc import ABC, abstractmethod


# Abstract interfaces for each dependency
class IDatabase(ABC):
    @abstractmethod
    def save_order(self, order):
        pass


class IPaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, order):
        pass


class IEmailService(ABC):
    @abstractmethod
    def send_confirmation(self, order):
        pass

    @abstractmethod
    def send_failure(self, order):
        pass
