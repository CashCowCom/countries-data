class CountryDataError(Exception):
    """Base exception for CountriesData related errors"""


class CountryNotFoundError(CountryDataError):
    """Raised when a country with the given ISO code is not found"""

    def __init__(self, country_code: str) -> None:
        self.country_code = country_code
        super().__init__(f"Country with ISO code '{country_code}' not found")


class SubdivisionNotFoundError(CountryDataError):
    """Raised when a subdivision with the given code is not found"""

    def __init__(self, country_code: str, subdivision_code: str) -> None:
        self.country_code = country_code
        self.subdivision_code = subdivision_code
        super().__init__(f"Subdivision '{subdivision_code}' not found for country '{country_code}'")


class TranslationNotFoundError(CountryDataError):
    """Raised when a translation is not found for the given language or country"""

    def __init__(self, lang_code: str, country_code: str | None = None) -> None:
        self.lang_code = lang_code
        self.country_code = country_code
        message = (
            f"Translation not found for country '{country_code}' in language '{lang_code}'"
            if country_code
            else f"Translations not found for language '{lang_code}'"
        )
        super().__init__(message)
