class SMSNotifier:
    def __init__(self, token):
        self.token = token

    def sendsms(self, mobile_phone, text):
        validated = self.validate_mobile(mobile_phone)
        if validated:
            self._send_protocol_service(mobile_phone, text)

    def send_sms(self, job):
        number = job.customer.mobile_phone
        text = "Pet {} washed".format(job.pet.name)    ## Es posoble cambiar el mensaje
        validated = self.validate_mobile(number)
        if validated:
            self._send_protocol_service(number, text)

    def _send_protocol_service(self, mobile_phone, text):
        print("Sending SMS to {0}, Text: {1}".format(mobile_phone, text))

    def validate_mobile(self, mobile_phone):
        print("Valid Number", mobile_phone)
        return True
