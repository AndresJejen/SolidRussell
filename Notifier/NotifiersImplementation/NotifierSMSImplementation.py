from Notifier.INotifier import INotifier
#from Notifier.NotifiersBase.SMSNotifier import SMSNotifier

from ..NotifiersBase import EmailNotifier, SMSNotifier


class NotifierSMSImplementation(INotifier):

    def __init__(self, *args, **kwargs):
        self.notifier = SMSNotifier(kwargs['token'])

    def notify(self, *args, **kwargs):
        job = kwargs['job']
        self.notifier.send_sms(job)


