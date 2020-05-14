from Models.PetWashJob import PetWashJob
from Notifier.NotifiersBase.SMSNotifier import SMSNotifier
from Respository.RepositoriesBase.MemoryRepository import MemoryRepository


# Ejemplo
# En este fichero podemos encontrar una implementación eficáz
# del proceso operacional para una empresa que se dedica al
# aseo de mascotas
#
# Proceso:
#   1. Los clientes llevan su mascota y la empresa registra el ingreso
#   2. La empresa ejecuta el trabajo de lavado
#   3. Cuando la mascota está lista, la empresa contacta al cliente por mensaje de texto
#       para informarle que ya puede retirar a su mascota.


class PetWash:
    """
    PetWash Class
    Objeto principal del proceso, de recepción, lavado y retorno de mascota
    """
    def __init__(self, token):
        self.repository = MemoryRepository()  # Dependencia Implicita
        self.notifier = SMSNotifier(token)    # Dependencia Implicita

    def require_pet_wash(self, pet, customer):
        """
        Recibe la mascota, genera el proceso de lavado y almacena el trabajo
        :param pet: Objeto con información de la mascota
        :param customer: Cliente
        :return: Objeto del trabajo
        """
        job = PetWashJob(pet, customer, 'new job')
        return self.repository.put(job)

    def wash_completed(self, service_id):
        """
        Proceso de lavado terminado
        :param service_id: Identificador unico del proceso
        """
        pet_wash_job = self.repository.update_state(service_id, 'Wash completed')
        self.notifier.send_sms(pet_wash_job)

    def services_by_customer(self, customer):
        """
        Busca todos los trabajos realizados antes a un usuario
        :param customer: Objeto con información del cliente
        :return: Lista de trabajos de un cliente
        """
        return self.repository.find_by_customer(customer)
