class INotifier(object):
    def __init__(self, *args, **kwargs):
        pass

    def notify(self, *args, **kwargs):
        raise Exception("NotImplementedException")
