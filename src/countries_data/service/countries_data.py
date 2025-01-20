import json
from pathlib import Path
from typing import Any

from ..errors import CountryDataError, CountryNotFoundError, SubdivisionNotFoundError, TranslationNotFoundError
from ..models import CountryData, Subdivision


class CountriesData:
    def __init__(self) -> None:
        self.country_data_path = Path(__file__).parent.parent / "data" / "countries"
        self.subdivisions_data_path = Path(__file__).parent.parent / "data" / "subdivisions"
        self.translations_data_path = Path(__file__).parent.parent / "data" / "translations"

    def _load_json_file(self, file_path: Path) -> dict[str, Any]:
        """Helper method to load JSON files with proper error handling"""
        try:
            with file_path.open() as f:
                return json.load(f)
        except FileNotFoundError as err:
            raise CountryDataError(f"Data file not found: {file_path}") from err
        except json.JSONDecodeError as err:
            raise CountryDataError(f"Invalid JSON data in file: {file_path}") from err

    def get_country_data_by_code(self, country_iso_code: str) -> CountryData | None:
        country_iso_code = country_iso_code.upper()
        file_path = self.country_data_path / f"{country_iso_code}.json"

        country_data = self._load_json_file(file_path)
        if country_iso_code not in country_data:
            raise CountryNotFoundError(country_iso_code)

        return CountryData(**country_data[country_iso_code])

    def get_country_subdivisions_by_code(self, country_iso_code: str) -> list[Subdivision]:
        country_iso_code = country_iso_code.upper()
        file_path = self.subdivisions_data_path / f"{country_iso_code}.json"

        subdivisions_data = self._load_json_file(file_path)

        if not subdivisions_data:
            raise SubdivisionNotFoundError(country_iso_code, "any")

        return [Subdivision(**subdivision) for subdivision in subdivisions_data.values()]

    def get_country_subdivision_by_codes(self, country_iso_code: str, subdivision_code: str) -> Subdivision | None:
        country_iso_code = country_iso_code.upper()
        subdivision_code = subdivision_code.upper()
        file_path = self.subdivisions_data_path / f"{country_iso_code}.json"

        subdivisions_data = self._load_json_file(file_path)

        if subdivision_code not in subdivisions_data:
            raise SubdivisionNotFoundError(country_iso_code, subdivision_code)

        return Subdivision(**subdivisions_data[subdivision_code])

    def get_translated_countries_names_by_lang_code(self, lang_code: str) -> dict:
        lang_code = lang_code.lower()
        file_path = self.translations_data_path / f"countries-{lang_code}.json"

        translations_data = self._load_json_file(file_path)

        if not translations_data:
            raise TranslationNotFoundError(lang_code)

        return translations_data

    def get_translated_country_name_by_codes(self, lang_code: str, country_iso_code: str) -> str | None:
        country_iso_code = country_iso_code.upper()
        lang_code = lang_code.lower()
        file_path = self.translations_data_path / f"countries-{lang_code}.json"

        translations_data = self._load_json_file(file_path)

        if country_iso_code not in translations_data:
            raise TranslationNotFoundError(lang_code, country_iso_code)

        return translations_data[country_iso_code]
