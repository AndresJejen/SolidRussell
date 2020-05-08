import uuid


class Repository:
    def __init__(self):
        self.persistence = {}

    def put(self, job):
        service_id = uuid.uuid4().hex
        self.persistence[service_id] = job
        return service_id

    def find_by_id(self, service_id):
        job = self.persistence[service_id]
        return job

    def update_state(self, service_id, state):
        job = self.find_by_id(service_id)
        job.state = state
        self.persistence[service_id] = job
        return job
