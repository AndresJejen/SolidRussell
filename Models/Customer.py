from Models.IActor import IActor


class Customer(IActor):
    def __init__(self, *args, **kwargs):
        """
        Implementa el Cliente
        :param args:
        :param kwargs:
        """

        self.name = kwargs['name']
        self.mobile_phone = kwargs['mobile_phone']
        self.email = kwargs['email']

    def get_info(self):
        """
        Retorna la información del Cliente
        :return: Objeto con la información del cliente
        """
        info = {
            'name': self.name,
            'mobile_phone': self.mobile_phone,
            'email': self.email
        }
        return info
