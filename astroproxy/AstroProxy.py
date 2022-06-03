import aiohttp
from enum import Enum

class NetworkType(Enum):
    BUSINESS = 'Business'
    COLLEGE = 'College'
    HOSTING = 'Hosting'
    MOBILE = 'Mobile'
    RESIDENTAL = 'Residental'
    TRAVEL = 'Travel'


class RotationType(Enum):
    TIME = 'time'
    LINK = 'link'
    REQUEST = 'request'


class RotationTimeType(Enum):
    HOURS = 'hours'
    MINUTES = 'minutes'


class TrafficType(Enum):
    UNLIMITED = 1
    LIMITED = 0


class VPNType(Enum):
    ANDROID = 'android'
    IOS = 'ios'
    WINDOWS = 'windows'
    MACOS = 'macos'
    MIKROTIK = 'mikrotik'


class OrderType(Enum):
    RANDOM = 'random'
    CREATED = 'created'
    ID = 'id'
    NAME = 'name'


class OrderDirectionType(Enum):
    ASC = 'asc'
    DESC = 'desc'


class AstroProxy():
    def __init__(
        self, api_key: str, base_url: str = 'https://astroproxy.com'
    ) -> None:
        self.base_url = base_url
        self.api_key = api_key
        self.session = aiohttp.ClientSession(base_url)

    async def get_balance(self):
        """Получение баланса

        Returns:
            _type_: _description_
        """
        method = 'GET'
        path = '/balance'
        res = await self._request(method, path)
        return res

    async def get_ports(
        self, order: OrderType = OrderType.ID,
        orderDirection: OrderDirectionType = OrderDirectionType.DESC
    ):
        """Получение списка портов

        Returns:
            _type_: _description_
        """
        method = 'GET'
        path = '/ports'
        params = {
            'order': order.value,
            'orderDirection': orderDirection.value
        }
        res = await self._request(method, path, params=params)
        return res

    async def get_countries(self):
        """Получение списка доступных стран

        Returns:
            _type_: _description_
        """
        method = 'GET'
        path = '/countries'
        res = await self._request(method, path)
        return res

    async def get_cities(self, country: str):
        """Получение списка доступных городов

        Args:
            country (str): _description_

        Returns:
            _type_: _description_
        """
        method = 'GET'
        path = '/cities'
        params = {
            'country': country
        }
        res = await self._request(method, path, params=params)
        return res

    async def get_operators(self, country, city, network):
        """Получение списка доступных операторов

        Args:
            country (_type_): _description_
            city (_type_): _description_
            network (_type_): _description_

        Returns:
            _type_: _description_
        """
        method = 'GET'
        path = '/operators'
        params = {
            'country': country,
            'city': city,
            'network': network
        }
        res = await self._request(method, path, params=params)
        return res

    async def get_lists(self):
        """Получение структурированного списка стран, городов, операторов

        Returns:
            _type_: _description_
        """
        method = 'GET'
        path = '/lists'
        res = await self._request(method, path)
        return res

    async def create_port(
        self,
        name: str,
        network: NetworkType,
        country: str,
        city: str,
        rotation_by: RotationType,
        rotation_time_type: RotationTimeType,
        rotation_time: int,
        is_unlimited: TrafficType,
        volume: float,
        username: str,
        password: str,
        ip: str
    ):
        """Создание нового порта

        Args:
            name (str): _description_
            network (NetworkType): _description_
            country (str): _description_
            city (str): _description_
            rotation_by (RotationType): _description_
            rotation_time_type (RotationTimeType): _description_
            rotation_time (int): _description_
            is_unlimited (int): _description_
            volume (float): _description_
            username (str): _description_
            password (str): _description_
            ip (str): _description_

        Returns:
            _type_: _description_
        """
        method = 'post'
        path = '/ports'
        data = {
            'name': name,
            'network': network.value,
            'country': country,
            'city': city,
            'rotation_by': rotation_by.value,
            'rotation_time_type': rotation_time_type.value,
            'rotation_time': rotation_time,
            'is_unlimited': is_unlimited.value,
            'volume': volume,
            'username': username,
            'password': password,
        }
        res = await self._request(method, path, params=data)
        return res

    async def calculate(
        self,
        name: str,
        network: NetworkType,
        country: str,
        city: str,
        rotation_by: RotationType,
        rotation_time_type: RotationTimeType,
        rotation_time: int,
        is_unlimited: TrafficType,
        volume: float,
        username: str,
        password: str,
        ip: str
    ):
        """Расчет стоимости порта

        Args:
            name (str): _description_
            network (NetworkType): _description_
            country (str): _description_
            city (str): _description_
            rotation_by (RotationType): _description_
            rotation_time_type (RotationTimeType): _description_
            rotation_time (int): _description_
            is_unlimited (int): _description_
            volume (float): _description_
            username (str): _description_
            password (str): _description_
            ip (str): _description_

        Returns:
            _type_: _description_
        """
        method = 'post'
        path = '/calculate'
        data = {
            'name': name,
            'network': network.value,
            'country': country,
            'city': city,
            'rotation_by': rotation_by.value,
            'rotation_time_type': rotation_time_type.value,
            'rotation_time': rotation_time,
            'is_unlimited': is_unlimited.value,
            'volume': volume,
            'username': username,
            'password': password,
        }
        res = await self._request(method, path, params=data)
        return res

    async def delete_port(self, port_id: int):
        method = 'DELETE'
        path = f"/ports/{port_id}"
        res = await self._request(method, path)
        return res

    async def update_port(
        self,
        port_id: int,
        name: str,
        vpn: VPNType,
        rotation_by: RotationType,
        rotation_time_type: RotationTimeType,
        rotation_time: int,
        is_unlimited: TrafficType
    ):
        """Обновление порта

        Args:
            port_id (int): _description_
            name (str): _description_
            vpn (VPNType): _description_
            rotation_by (RotationType): _description_
            rotation_time_type (RotationTimeType): _description_
            rotation_time (int): _description_
            is_unlimited (TrafficType): _description_

        Returns:
            _type_: _description_
        """
        method = 'PATCH'
        path = f"/ports/{port_id}"
        params = {
            'name': name,
            'vpn': vpn.value,
            'rotation_by': rotation_by.value,
            'rotation_time_type': rotation_time_type.value,
            'rotation_time': rotation_time,
            'is_unlimited': is_unlimited.value,

        }
        res = await self._request(method, path, params=params)
        return res

    async def renew_port(
        self,
        order_id: int,
        volume: float,
    ):
        """Продление порта

        Args:
            order_id (int): _description_
            volume (float): _description_
        """
        method = 'POST'
        path = f"/ports/{order_id}/renew"
        params = {
            'volume': volume
        }
        res = await self._request(method, path, params=params)
        return res

    async def update_ip(self, port_id: int):
        """Получение нового внешнего IP для порта

        Args:
            port_id (int): _description_
        """
        method = "GET"
        path = f'/ports/{port_id}/newip'
        res = await self._request(method, path)
        return res

    def delete_nones(self, original: dict):
        filtered = {k: v for k, v in original.items() if v is not None}
        return filtered

    async def _request(
        self,
        method,
        path,
        params: dict = {},
        data: dict = {}
    ) -> dict:
        url = '/api/v1' + path
        params['token'] = self.api_key

        params = self.delete_nones(params)
        data = self.delete_nones(data)

        async with self.session.request(
            method, url, params=params, data=data
        ) as response:
            return(await response.json())

    async def close_session(self):
        await self.session.close()
