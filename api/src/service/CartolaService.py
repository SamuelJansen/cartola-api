import time
from python_helper import Constant as c
from python_framework import Service, ServiceMethod
from python_helper import ObjectHelper

from config import CartolaConfig


@Service()
class CartolaService:

    @ServiceMethod()
    def gatherModelList(self):
        return self.repository.cartola.saveAll({
            f'{uri.replace(c.FOWARD_SLASH, c.DASH)[1:]}{c.DASH}{time.time():0<18}'.replace(c.DOT, c.DASH) : self.client.cartola.gather(uri)
            for uri in CartolaConfig.API_URLS
        })
