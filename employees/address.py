from dictionaryMixin import AsDictionaryMixin


class Address(AsDictionaryMixin):
    def __init__(self, street, city, index):
        self.street = street
        self.city = city
        self.index = index

    def __str__(self):
        return self.index + ", " + self.city + ", " + self.street


class AddressBook:

    def __init__(self):
        self._employee_addresses = {
            1: Address('Novaya', 'Moscow', '100200'),
            2: Address('Letnya 30', 'Omsk', '300200'),
            3: Address('Osenya 20', 'Novosibirsk', '234123'),
            4: Address('Springovaya 15', 'Moscow', '111222'),
            5: Address('Staraya 10', 'Moscow', '234221')
        }

    def get_employee_address(self, employee_id):
        address = self._employee_addresses.get(employee_id)
        if not address:
            raise ValueError(employee_id)
        return address