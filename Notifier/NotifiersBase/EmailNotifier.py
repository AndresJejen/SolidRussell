class EmailNotifier:
    def __init__(self, token):
        self.token = token

    def send_email(self, job):
        email = job.customer.email
        text = "Pet {} washed, message via Email".format(job.pet.name)    ## Es posoble cambiar el mensaje
        validated = self.validate_email(email)
        if validated:
            self._send_protocol_service(email, text)

    def _send_protocol_service(self, email, text):
        print("Sending Email to {0}, Text: {1}".format(email, text))

    def validate_email(self, mobile_phone):
        print("Valid Email", mobile_phone)
        return True
