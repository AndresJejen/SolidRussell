from Models import Customer, Pet


class PetWashJob:
    """
    Clase que implementa el Objeto de Trabajo
    """
    def __init__(self, pet: Pet, customer: Customer, state: str):
        """
        Constructor de la clase Trabajo
        :param pet:
        :param customer:
        :param state:
        """
        self.pet = pet
        self.customer = customer
        self.state = state
