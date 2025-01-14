## Usual BoilerPlate code for a data intensive class
class Product:
    # Definitions
    def __init__(self, name: str, price: float, quantity: int = 0):
        self._name = name
        self._price = price
        self._quantity = quantity
        
    def __repr__(self):
        return (
            f"Product(name={self._name!r}, price={self._price}, quantity={self._quantity})"
        )
    
    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        
        return (
            self._name == other._name and
            self._price == other._price and
            self._quantity == self._quantity
        )
    
    ## Implementation
    def total_cost(self) -> float:
        return self._price * self._quantity

## All the above "Definitions" code can be auto generated using the dataclass decorator as given below

from dataclasses import dataclass

@dataclass
class Stationary:
    name: str
    price: float
    quantity: int = 0

    def total_cost(self) -> float:
        return self.price * self.quantity

s1 = Stationary('Pencil', 1.45, 100)
s2 = Stationary('Eraser', 0.99, 50)
s3 = Stationary('Ruler', 4.49, 300)
s4 = Stationary('Pencil', 1.45, 100)

print(s1)
print(s1.total_cost())
print(s1 == s4)
print(s2 == s3)

