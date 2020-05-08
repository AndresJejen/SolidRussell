from Models.IActor import IActor


class Pet(IActor):
    def __init__(self, *args, **kwargs):
        """
        Implementa la Mascota
        :param args:
        :param kwargs:
        """

        self.name = kwargs['name']
        self.type = kwargs['type']

    def get_info(self):
        """
        Retorna la información de la mascota
        :return: Objeto con la información de la mascota
        """
        info = {
            'name': self.name,
            'type': self.type
        }
        return info
