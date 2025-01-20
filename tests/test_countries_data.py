from pathlib import Path

import pytest
from loguru import logger

from countries_data.errors import CountryDataError
from countries_data.service.countries_data import CountriesData


def get_countries_code_list() -> list[str]:
    return [
        str(f)[-7:-5] for f in (Path(__file__).parent.parent / "src" / "countries_data" / "data" / "countries").iterdir() if f.is_file()
    ]


def get_subdivisions_code_list() -> list[str]:
    return [
        str(f)[-7:-5] for f in (Path(__file__).parent.parent / "src" / "countries_data" / "data" / "subdivisions").iterdir() if f.is_file()
    ]


def get_translations_code_list() -> list[str]:
    return [
        str(f)[10:-5] for f in (Path(__file__).parent.parent / "src" / "countries_data" / "data" / "translations").iterdir() if f.is_file()
    ]


@pytest.fixture
def country_data_service() -> CountriesData:
    return CountriesData()


class TestGetCountryDataByCode:
    def test_get_country_data_by_code_il_uppercase(self, country_data_service: CountriesData) -> None:
        country_data = country_data_service.get_country_data_by_code(country_iso_code="IL")
        assert country_data is not None

    def test_get_country_data_by_code_il_lowercase(self, country_data_service: CountriesData) -> None:
        country_data = country_data_service.get_country_data_by_code(country_iso_code="il")
        assert country_data is not None

    def test_get_country_data_by_code_unknown(self, country_data_service: CountriesData) -> None:
        with pytest.raises(CountryDataError):
            country_data_service.get_country_data_by_code(country_iso_code="XX")

    def test_get_country_data_by_code_empty(self, country_data_service: CountriesData) -> None:
        with pytest.raises(CountryDataError):
            country_data_service.get_country_data_by_code(country_iso_code="")

    def test_get_country_data_by_code_responses(self, country_data_service: CountriesData) -> None:
        countries = get_countries_code_list()
        logger.info(countries)
        for country_code in countries:
            logger.info(f"running for: {country_code}")
            country_data = country_data_service.get_country_data_by_code(country_iso_code=country_code)
            assert country_data is not None


class TestGetCountrySubdivisionsByCode:
    def test_get_country_subdivisions_by_code_il_uppercase(self, country_data_service: CountriesData) -> None:
        subdivision_data = country_data_service.get_country_subdivisions_by_code(country_iso_code="IL")
        assert subdivision_data is not None

    def test_get_country_subdivisions_by_code_il_lowercase(self, country_data_service: CountriesData) -> None:
        subdivision_data = country_data_service.get_country_subdivisions_by_code(country_iso_code="il")
        assert subdivision_data is not None

    def test_get_country_subdivisions_by_code_unknown(self, country_data_service: CountriesData) -> None:
        with pytest.raises(CountryDataError):
            country_data_service.get_country_subdivisions_by_code(country_iso_code="XX")

    def test_get_country_subdivisions_by_code_empty(self, country_data_service: CountriesData) -> None:
        with pytest.raises(CountryDataError):
            country_data_service.get_country_subdivisions_by_code(country_iso_code="")

    def test_get_country_subdivisions_by_code_responses(self, country_data_service: CountriesData) -> None:
        countries = get_subdivisions_code_list()
        logger.info(countries)
        for country_code in countries:
            logger.info(f"running for: {country_code}")
            country_data = country_data_service.get_country_subdivisions_by_code(country_iso_code=country_code)
            assert country_data is not None


class TestGetCountrySubdivisionByCodes:
    def test_get_country_subdivision_by_codes_il_d_uppercase(self, country_data_service: CountriesData) -> None:
        subdivision_data = country_data_service.get_country_subdivision_by_codes(country_iso_code="IL", subdivision_code="D")
        assert subdivision_data is not None

    def test_get_country_subdivision_by_codes_il_d_lowercase_uppercase(self, country_data_service: CountriesData) -> None:
        subdivision_data = country_data_service.get_country_subdivision_by_codes(country_iso_code="il", subdivision_code="D")
        assert subdivision_data is not None

    def test_get_country_subdivision_by_codes_il_d_lowercase(self, country_data_service: CountriesData) -> None:
        subdivision_data = country_data_service.get_country_subdivision_by_codes(country_iso_code="il", subdivision_code="d")
        assert subdivision_data is not None

    def test_get_country_subdivision_by_codes_il_d_uppercase_lowercase(self, country_data_service: CountriesData) -> None:
        subdivision_data = country_data_service.get_country_subdivision_by_codes(country_iso_code="IL", subdivision_code="d")
        assert subdivision_data is not None

    def test_get_country_subdivision_by_codes_unknown(self, country_data_service: CountriesData) -> None:
        with pytest.raises(CountryDataError):
            country_data_service.get_country_subdivision_by_codes(country_iso_code="XX", subdivision_code="XX")

    def test_get_country_subdivision_by_codes_empty(self, country_data_service: CountriesData) -> None:
        with pytest.raises(CountryDataError):
            country_data_service.get_country_subdivision_by_codes(country_iso_code="", subdivision_code="")
