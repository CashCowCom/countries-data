import pytest

from country_registry.service.country_registry import CountryRegistry


@pytest.fixture
def country_data_service() -> CountryRegistry:
    return CountryRegistry()

class TestGetCountryDataByCode:
    def test_get_country_data_by_code_il_uppercase(self, country_data_service: CountryRegistry)->None:
        country_data = country_data_service.get_country_data_by_code(country_iso_code="IL")
        assert country_data is not None

    def test_get_country_data_by_code_il_lowercase(self, country_data_service: CountryRegistry)->None:
        country_data = country_data_service.get_country_data_by_code(country_iso_code="il")
        assert country_data is not None

    def test_get_country_data_by_code_unknown(self, country_data_service: CountryRegistry)->None:
        country_data = country_data_service.get_country_data_by_code(country_iso_code="XX")
        assert country_data is None

    def test_get_country_data_by_code_empty(self, country_data_service: CountryRegistry)->None:
        country_data = country_data_service.get_country_data_by_code(country_iso_code=None)
        assert country_data is None

class TestGetCountrySubdivisionsByCode:
    def test_get_country_subdivisions_by_code_il_uppercase(self, country_data_service: CountryRegistry)->None:
        subdivision_data = country_data_service.get_country_subdivisions_by_code(country_iso_code="IL")
        assert subdivision_data is not None

    def test_get_country_subdivisions_by_code_il_lowercase(self, country_data_service: CountryRegistry)->None:
        subdivision_data = country_data_service.get_country_subdivisions_by_code(country_iso_code="il")
        assert subdivision_data is not None

    def test_get_country_subdivisions_by_code_unknown(self, country_data_service: CountryRegistry)->None:
        subdivision_data = country_data_service.get_country_subdivisions_by_code(country_iso_code="XX")
        assert subdivision_data == []

    def test_get_country_subdivisions_by_code_empty(self, country_data_service: CountryRegistry)->None:
        subdivision_data = country_data_service.get_country_subdivisions_by_code(country_iso_code=None)
        assert subdivision_data == []

class TestGetCountrySubdivisionByCodes:
    def test_get_country_subdivision_by_codes_il_d_uppercase(self, country_data_service: CountryRegistry)->None:
        subdivision_data = country_data_service.get_country_subdivision_by_codes(country_iso_code="IL", subdivision_code="D")
        assert subdivision_data is not None

    def test_get_country_subdivision_by_codes_il_d_lowercase_uppercase(self, country_data_service: CountryRegistry)->None:
        subdivision_data = country_data_service.get_country_subdivision_by_codes(country_iso_code="il", subdivision_code="D")
        assert subdivision_data is not None

    def test_get_country_subdivision_by_codes_il_d_lowercase(self, country_data_service: CountryRegistry)->None:
        subdivision_data = country_data_service.get_country_subdivision_by_codes(country_iso_code="il", subdivision_code="d")
        assert subdivision_data is not None

    def test_get_country_subdivision_by_codes_il_d_uppercase_lowercase(self, country_data_service: CountryRegistry)->None:
        subdivision_data = country_data_service.get_country_subdivision_by_codes(country_iso_code="IL", subdivision_code="d")
        assert subdivision_data is not None

    def test_get_country_subdivision_by_codes_unknown(self, country_data_service: CountryRegistry)->None:
        subdivision_data = country_data_service.get_country_subdivision_by_codes(country_iso_code="XX", subdivision_code="XX")
        assert subdivision_data is None

    def test_get_country_subdivision_by_codes_empty(self, country_data_service: CountryRegistry)->None:
        subdivision_data = country_data_service.get_country_subdivision_by_codes(country_iso_code=None, subdivision_code=None)
        assert subdivision_data is None
