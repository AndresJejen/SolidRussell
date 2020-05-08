class IActor:

    def __init__(self, *args, **kwargs):
        self.name = kwargs['name']

    def get_info(self):
        """
        Retorna la información del Actor
        :return:
        """
        raise Exception("NotImplementedException")
