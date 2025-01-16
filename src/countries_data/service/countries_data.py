import json
from pathlib import Path

from loguru import logger
from models import CountryData, Subdivision


class CountriesData:
    def __init__(self)-> None:
        self.country_data_path = (
                Path(__file__).parent /  "data" / "countries"
        )
        self.subdivisions_data_path = (
                Path(__file__).parent /  "data" / "subdivisions"
        )
        self.translations_data_path = (
                Path(__file__).parent /  "data" / "translations"
        )

    def get_country_data_by_code(self, country_iso_code: str)-> CountryData | None:
        with (self.country_data_path / f"{country_iso_code}.json").open() as f:
            country_data = json.load(f)
            logger.info(country_data)

            if country_iso_code not in country_data:
                logger.error(
                    f"Country code {country_iso_code} not found in country data",
                )
                return None

            return CountryData(**country_data[country_iso_code])

    def get_country_subdivisions_by_code(self, country_iso_code: str)-> list[Subdivision]:
        with (self.subdivisions_data_path / f"{country_iso_code}.json").open() as f:
            subdivisions_data = json.load(f)
            logger.info(subdivisions_data)

            subdivisions_list = [Subdivision(**subdivision) for subdivision in subdivisions_data.values]

            return subdivisions_list

    def get_country_subdivision_by_codes(self, country_iso_code: str, subdivision_code: str)-> Subdivision | None:
        with (self.subdivisions_data_path / f"{country_iso_code}.json").open() as f:
            subdivisions_data = json.load(f)
            logger.info(subdivisions_data)

            if subdivision_code not in subdivisions_data:
                logger.error(
                    f"Subdivision code {subdivision_code} not found in subdivision data",
                )
                return None

            return Subdivision(**subdivisions_data[subdivision_code])

    def get_translated_countries_names_by_lang_code(self, lang_code: str)-> dict:
        with (self.translations_data_path / f"countries-{lang_code}.json").open() as f:
            translations_data = json.load(f)
            logger.info(translations_data)

            return translations_data

    def get_translated_country_name_by_codes(self, lang_code: str,  country_iso_code: str)-> str | None:
        with (self.translations_data_path / f"countries-{lang_code}.json").open() as f:
            translations_data = json.load(f)
            logger.info(translations_data)

            if country_iso_code not in translations_data:
                logger.error(
                    f"Country code {country_iso_code} not found in translations data",
                )
                return None

            return translations_data[country_iso_code]
