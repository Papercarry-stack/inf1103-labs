from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    """Strategy interface: every discount turns an order total into a new total."""

    @abstractmethod
    def apply(self, total: float) -> float:
        pass
