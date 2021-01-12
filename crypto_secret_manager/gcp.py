from google.cloud import secretmanager


class GCP:

    def __init__(self, project_id: str):
        self.__project_id = project_id
        self.__client = secretmanager.SecretManagerServiceClient()

    def get_secret(self, secret_id: str, version_id: str = 'latest') -> str:
        name = f"projects/{self.__project_id}/secrets/{secret_id}/versions/{version_id}"
        response = self.__client.access_secret_version(request={"name": name})
        return response.payload.data.decode('UTF-8')
