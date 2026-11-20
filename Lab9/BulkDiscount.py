from DiscountStrategy import DiscountStrategy


class BulkDiscount(DiscountStrategy):
    """Takes a fixed amount off totals at or above a threshold.
    BulkDiscount(200, 20) = 20 off any total of 200 or more."""

    def __init__(self, threshold: float, amount: float):
        if threshold < 0 or amount < 0:
            raise ValueError("Threshold and amount cannot be negative.")
        self.__threshold: float = threshold
        self.__amount: float = amount

    def apply(self, total: float) -> float:
        return total - self.__amount if total >= self.__threshold else total
