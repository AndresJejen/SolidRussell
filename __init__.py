# Process
from Solid1 import PetWash as PetWash1
from Solid2 import PetWash as PetWash2
from Solid3 import PetWash as PetWash3
from Solid4 import PetWash as PetWash4


# Models
from Models.Customer import Customer
from Models.Pet import Pet
from Models.PetWashJob import PetWashJob

# Auxiliar Tools
from Notifier.NotifiersBase.SMSNotifier import SMSNotifier
from Respository.RepositoriesBase.MemoryRepository import MemoryRepository
from Notifier.NotifiersImplementation.NotifierSMSImplementation import NotifierSMSImplementation
from Notifier.NotifiersImplementation.NotifierEmailImplementation import NotifierEmailImplementation


def main():
    """
    Ejecuta el Programa Principal
    :return:
    """
    ## Sin Solid
    # Procesador = PetWash1(1234)

    ## Responsabilidad Unica
    # Procesador = PetWash2(1234)

    ## mas Inversión de las dependencias
    #repository = MemoryRepository()
    #notifier = SMSNotifier(1234)
    #Procesador = PetWash3(repository, notifier)

    ## mas Open Close
    repository = MemoryRepository()
    #notifier = NotifierSMSImplementation(token=12345)
    notifier = NotifierEmailImplementation(token=12345)
    Procesador = PetWash4(repository, notifier)

    # Procesador = PetWash5(1234)   # mas Liskov
    # Procesador = PetWash6(1234)   # mas -----
    continuar = True

    while continuar:

        # input
        cliente = input("Ingrese El nombre de cliente: ")
        mascota = input("Ingrese El nombre de la Mascota: ")
        mascota_type = input("Ingrese El tipo de Mascota: ")
        cliente_num = input("Ingrese El número de Contacto: ")
        cliente_email = input("Ingrese un correo electronico de Contacto: ")

        customer = Customer(name=cliente, mobile_phone=cliente_num, email=cliente_email)
        pet = Pet(name=mascota, type=mascota_type)
        print("Customer Info", customer.get_info())
        print("Pet Info", pet.get_info())

        #jobIdentifier = Procesador.require_pet_wash(pet, customer) # Para Solid1 and Solid 2

        job = PetWashJob(pet, customer, 'new job')  # Para Inversión de dependencias, open_close
        jobIdentifier = Procesador.require_pet_wash(job)

        variable: str = 23
        print(variable, type(variable))

        Procesador.wash_completed(jobIdentifier)

        continuar = False


if __name__ == "__main__":
    main()
