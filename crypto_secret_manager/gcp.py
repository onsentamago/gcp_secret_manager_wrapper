class GCP:

    def __init__(self, project_id: str):
        self.project_id = project_id

    def get_secret(self, secret_id: str, version_id: str):
        return 'ok'
