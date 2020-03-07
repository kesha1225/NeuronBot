from .base import BaseMethod
from vk.types.responses import database as m


class Database(BaseMethod):
    async def get_chairs(
        self, faculty_id: int = None, offset: int = None, count: int = None
    ):
        """
        Return list of chairs on a specified faculty.
        :param faculty_id: id of the faculty to get chairs from
        :param offset: offset required to get a certain subset of chairs
        :param count: amount of chairs to get


        """
        method = self.get_method_name(self.get_chairs)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetChairs(**r)

    async def get_cities(
        self,
        country_id: int = None,
        region_id: int = None,
        q: str = None,
        need_all: bool = None,
        offset: int = None,
        count: int = None,
    ):
        """
        Return a list of cities.
        :param country_id: Country ID.
        :param region_id: Region ID.
        :param q: Search query.
        :param need_all: '1' — to return all cities in the country, '0' — to return major cities in the country (default),
        :param offset: Offset needed to return a specific subset of cities.
        :param count: Number of cities to return.


        """
        method = self.get_method_name(self.get_cities)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetCities(**r)

    async def get_cities_by_id(self, city_ids: list = None):
        """
        Return information about cities by their IDs.
        :param city_ids: City IDs.


        """
        method = self.get_method_name(self.get_cities_by_id)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetCitiesById(**r)

    async def get_countries(
        self,
        need_all: bool = None,
        code: str = None,
        offset: int = None,
        count: int = None,
    ):
        """
        Return a list of countries.
        :param need_all: '1' — to return a full list of all countries, '0' — to return a list of countries near the current user's country (default).
        :param code: Country codes in [vk.com/dev/country_codes|ISO 3166-1 alpha-2] standard.
        :param offset: Offset needed to return a specific subset of countries.
        :param count: Number of countries to return.


        """
        method = self.get_method_name(self.get_countries)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetCountries(**r)

    async def get_countries_by_id(self, country_ids: list = None):
        """
        Return information about countries by their IDs.
        :param country_ids: Country IDs.


        """
        method = self.get_method_name(self.get_countries_by_id)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetCountriesById(**r)

    async def get_faculties(
        self, university_id: int = None, offset: int = None, count: int = None
    ):
        """
        Return a list of faculties (i.e., university departments).
        :param university_id: University ID.
        :param offset: Offset needed to return a specific subset of faculties.
        :param count: Number of faculties to return.


        """
        method = self.get_method_name(self.get_faculties)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetFaculties(**r)

    async def get_metro_stations(
        self,
        city_id: int = None,
        offset: int = None,
        count: int = None,
        extended: bool = None,
    ):
        """
        Get metro stations by city
        :param city_id:
        :param offset:
        :param count:
        :param extended:


        """
        method = self.get_method_name(self.get_metro_stations)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetMetroStations(**r)

    async def get_metro_stations_by_id(self, station_ids: list = None):
        """
        Get metro station by his id
        :param station_ids:


        """
        method = self.get_method_name(self.get_metro_stations_by_id)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetMetroStationsById(**r)

    async def get_regions(
        self,
        country_id: int = None,
        q: str = None,
        offset: int = None,
        count: int = None,
    ):
        """
        Return a list of regions.
        :param country_id: Country ID, received in [vk.com/dev/database.getCountries|database.getCountries] method.
        :param q: Search query.
        :param offset: Offset needed to return specific subset of regions.
        :param count: Number of regions to return.


        """
        method = self.get_method_name(self.get_regions)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetRegions(**r)

    async def get_school_classes(self, country_id: int = None):
        """
        Return a list of school classes specified for the country.
        :param country_id: Country ID.


        """
        method = self.get_method_name(self.get_school_classes)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetSchoolClasses(**r)

    async def get_schools(
        self,
        q: str = None,
        city_id: int = None,
        offset: int = None,
        count: int = None,
    ):
        """
        Return a list of schools.
        :param q: Search query.
        :param city_id: City ID.
        :param offset: Offset needed to return a specific subset of schools.
        :param count: Number of schools to return.


        """
        method = self.get_method_name(self.get_schools)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetSchools(**r)

    async def get_universities(
        self,
        q: str = None,
        country_id: int = None,
        city_id: int = None,
        offset: int = None,
        count: int = None,
    ):
        """
        Return a list of higher education institutions.
        :param q: Search query.
        :param country_id: Country ID.
        :param city_id: City ID.
        :param offset: Offset needed to return a specific subset of universities.
        :param count: Number of universities to return.


        """
        method = self.get_method_name(self.get_universities)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetUniversities(**r)
