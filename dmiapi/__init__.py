import json

import aiohttp
from aiohttp.hdrs import USER_AGENT

import logging

from .constants import *

_LOGGER = logging.getLogger(__name__)

class DmiApi(object):
    """This class allows access to the Danish Metrology Institute (DMI) API.

    Note that it is based on trial and error, there is very little
    official documentation about this API yet, so use at your own risk.
    """    

    def __init__(self):
        """Initialize the class.
        """

    @classmethod
    async def forecast(cls, station_id):
        """Fetch the latest CSV data."""
        try:
            headers = {
                USER_AGENT: '{}/{}'.format('pydmiapi', '1.0'),
            }

            params = {
                API_PARAM_COMMAND: API_COMMAND_FORECAST,
                API_PARAM_ID: int(station_id),
            }            
            
            async with aiohttp.ClientSession() as session:
                async with session.get(API_BASE_URL,
                                       params = params,
                                       headers = headers,
                                       timeout = API_TIMEOUT) as response:
                    _LOGGER.debug("Request '%s' finished with status code %s", response.url, response.status)
                    print(await response.text('utf8'))
        except:
            _LOGGER.exception("While fetching forecast")
