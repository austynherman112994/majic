import pulsar

class PulsarPublisher:
    def __init__(self, client):
        self.client = client

        super().__init__()

    @staticmethod
    def build(host):
        client = pulsar(host)
        return PulsarPublisher(client)

    def publish(self, key):
        raise NotImplemented("Cache get_obj must be overridden")

    def close(self):
        self.client.close()
