from abc import ABC, abstractmethod

class PaymentMethod(ABC):

    @abstractmethod
    def biaya_admin(self, jumlah: float) -> float: 
        pass