from python_framework import HttpClient, HttpClientMethod, HttpStatus

from config import CartolaConfig


@HttpClient(
    url = CartolaConfig.API_BASE_URL
)
class CartolaClient :

    @HttpClientMethod(
        # logRequest = True,
        # logResponse = True,
        requestClass = [str]
    )
    def gather(self, url):
        return self.get(additionalUrl=url)
