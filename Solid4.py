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
from Models import PetWashJob
from Respository.RepositoriesBase import MemoryRepository
from Notifier.INotifier import INotifier


class PetWash:
    """
    PetWash Class
    Objeto principal del proceso, de recepción, lavado y retorno de mascota
    """
    def __init__(self, repository: MemoryRepository, notifier: INotifier):
        """
        Constructor de la clase
        :param repository:
        :param notifier:
        """
        self.repository = repository
        self.notifier = notifier

    def require_pet_wash(self, job: PetWashJob):
        """
        Recepción de la mascota
        :param job:
        :return: Identificador unico del servicio
        """
        identifier = self.repository.put(job)
        return identifier

    def wash_completed(self, service_id):
        """
        Envio de notificación
        :param service_id: Identificador unico del servicio
        """
        pet_wash_job = self.repository.update_state(service_id, 'Wash completed')
        self.notifier.notify(job=pet_wash_job)

    def services_by_customer(self, customer):
        return self.repository.find_by_customer(customer)
