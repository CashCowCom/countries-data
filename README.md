# Country Data Management

A Python package for managing and retrieving country-related data, including country information, subdivisions, and translated country names.

## Features

- Retrieve country data using ISO country codes
- Access country subdivisions (states, provinces, etc.)
- Get translated country names in different languages
- Handle data from JSON files stored in a structured directory format

## Installation

```bash
pip install countries-data
```

## Usage

### Initialize the Client

```python
from countries_data import CountriesData

client = CountriesData()
```

### Get Country Data

```python
from countries_data import CountriesData

client = CountriesData()
# Get data for a specific country using ISO code
country_data = client.get_country_data_by_code("US")
```

### Get Subdivisions

```python
from countries_data import CountriesData

client = CountriesData()

# Get all subdivisions for a country as list
subdivisions = client.get_country_subdivisions_by_code("US")

# Get a specific subdivision by code
subdivision = client.get_country_subdivision_by_codes("US", "CA")
```

### Get Translations

```python
from countries_data import CountriesData

client = CountriesData()

# Get all country names in a specific language
spanish_names = client.get_translated_countries_names_by_lang_code("es")

# Get a specific country name in a language
spanish_name = client.get_translated_country_name_by_codes("es", "US")
```

## Data Format

### Country Data
The country data JSON files should follow this structure:
```json
{
    "US": {
        "address_format": "{{recipient}}\n{{street}}\n{{city}} {{region_short}} {{postalcode}}\n{{country}}",
        "alpha2": "US",
        "alpha3": "USA",
        "continent": "North America",
        "country_code": "1",
        "currency_code": "USD",
        "distance_unit": "mi",
        "gec": "US",
        "geo": {
            "latitude": 38.8833,
            "longitude": -77.0167,
            "max_latitude": 71.5388001,
            "max_longitude": -66.885417,
            "min_latitude": 18.7763,
            "min_longitude": 170.5957,
            "bounds": {
                "northeast": {
                    "lat": 71.5388001,
                    "lng": -66.885417
                },
                "southwest": {
                    "lat": 18.7763,
                    "lng": 170.5957
                }
            }
        },
        "international_prefix": "011",
        "ioc": "USA",
        "iso_long_name": "The United States of America",
        "iso_short_name": "United States",
        "languages_official": ["en"],
        "languages_spoken": ["en", "es"],
        "national_destination_code_lengths": [3],
        "national_number_lengths": [10],
        "national_prefix": "1",
        "nationality": "American",
        "number": "840",
        "postal_code": true,
        "postal_code_format": "\\d{5}(-\\d{4})?",
        "region": "Americas",
        "start_of_week": "sunday",
        "subregion": "Northern America",
        "un_locode": "US",
        "un_member": true,
        "unofficial_names": ["United States", "USA", "United States of America"],
        "vat_rates": {
            "standard": null,
            "reduced": [],
            "super_reduced": null,
            "parking": null
        },
        "vehicle_registration_code": "USA",
        "world_region": "AMER"
    }
}
```

### Subdivision Data
The subdivision data JSON files should follow this structure:
```json
{
    "CA": {
        "name": "California",
        "code": "CA",
        "unofficial_names": ["CA", "Calif."],
        "geo": {
            "latitude": 36.778261,
            "longitude": -119.4179324,
            "max_latitude": 42.009518,
            "max_longitude": -114.131211,
            "min_latitude": 32.528832,
            "min_longitude": -124.482003,
            "bounds": {
                "northeast": {
                    "lat": 42.009518,
                    "lng": -114.131211
                },
                "southwest": {
                    "lat": 32.528832,
                    "lng": -124.482003
                }
            }
        },
        "translations": {
            "en": "California",
            "af": "Kalifornië",
            "ar": "كاليفورنيا",
            "az": "Kaliforniya",
            "be": "Каліфорнія",
            "bg": "Калифорния",
            "ca": "Califòrnia",
            "cs": "Kalifornie",
            "da": "Californien",
            "de": "Kalifornien",
            "es": "California",
            "et": "California",
            "eu": "Kalifornia",
            "fa": "کالیفرنیا",
            "fi": "Kalifornia",
            "fr": "Californie",
            "he": "קליפורניה",
            "hy": "Կալիֆորնիա",
            "id": "California",
            "it": "California",
            "ja": "カリフォルニア州",
            "ka": "კალიფორნია",
            "ko": "캘리포니아",
            "lt": "Kalifornija",
            "lv": "Kalifornija",
            "ms": "California",
            "nb": "California",
            "nl": "Californië",
            "pl": "Kalifornia",
            "pt": "Califórnia",
            "ro": "California",
            "ru": "Калифорния",
            "sr": "Калифорнија",
            "sv": "Kalifornien",
            "tr": "Kaliforniya",
            "uk": "Каліфорнія",
            "ur": "کیلیفورنیا",
            "vi": "California",
            "zh": "加利福尼亚州",
            "ceb": "California",
            "sr_Latn": "Kalifornija",
            "ccp": "কেলিফোর্নিয়া",
            "hu": "Kalifornia",
            "kk": "Калифорния",
            "mk": "Калифорнија",
            "no": "California",
            "cy": "California",
            "el": "Καλιφόρνια",
            "mn": "Калифорни",
            "ta": "கலிபோர்னியா"
        },
        "comments": null,
        "type": "state"
    }
}
```

### Translation Data
The translation files should follow this structure:
```json
{
    "US": "Estados Unidos",
    "CA": "Canadá",
    "MX": "México"
}
```

## Error Handling

The package includes robust error handling:
- Returns `None` for non-existent country codes
- Returns `None` for non-existent subdivision codes
- Returns empty list `[]` for countries without subdivisions
- Returns empty dict `{}` for missing translation files
- Logs errors using the `loguru` logger

## Dependencies

- Python 3.6+
- loguru
- pathlib

## License

MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
