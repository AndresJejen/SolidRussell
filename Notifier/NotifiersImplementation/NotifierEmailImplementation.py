from Notifier.INotifier import INotifier
from Notifier.NotifiersBase.EmailNotifier import EmailNotifier


class NotifierEmailImplementation(INotifier):

    def __init__(self, *args, **kwargs):
        self.notifier = EmailNotifier(kwargs['token'])

    def notify(self, *args, **kwargs):
        job = kwargs['job']
        self.notifier.send_email(job)


