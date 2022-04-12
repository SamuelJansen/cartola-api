from python_helper import log
from globals import getGlobalsInstance
globalsInstance = getGlobalsInstance()

API_BASE_URL = globalsInstance.getSetting('cartola.api.base-url')

API_URLS = [
    globalsInstance.getSetting('cartola.api.end-points.market-athletes'),
    globalsInstance.getSetting('cartola.api.end-points.matches'),
    globalsInstance.getSetting('cartola.api.end-points.positions'),
    globalsInstance.getSetting('cartola.api.end-points.market-status'),
    globalsInstance.getSetting('cartola.api.end-points.scored-athletes'),
    globalsInstance.getSetting('cartola.api.end-points.market-highlights-reserves'),
    globalsInstance.getSetting('cartola.api.end-points.market-highlights')
]
