import uuid
from Notifier.NotifiersBase.SMSNotifier import SMSNotifier

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
        """
        Constructor de la clase
        """
        self.persistence = {}
        self.sms_sender = SMSNotifier(token)

    def require_pet_wash(self, pet, customer):
        """
        Recepción de la mascota
        :param pet: Objeto con información de la Mascota
        :param customer: Objeto con información del cliente
        :return: Identificador unico del servicio
        """
        service_id = uuid.uuid4().hex
        self.persistence[service_id] = (pet, customer)      # Tarea 1
        return service_id

    def wash_completed(self, service_id):
        """
        Envio de notificación
        :param service_id: Identificador unico del servicio
        """
        pet, customer = self.persistence[service_id]        # Tarea 2
        self.sms_sender.sendsms(mobile_phone=customer.mobile_phone, text="Pet {} washed".format(pet.name))