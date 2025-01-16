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

countries_data = CountriesData()
```

### Get Country Data

```python
from countries_data import CountriesData

countries_data = CountriesData()
# Get data for a specific country using ISO code
country_data = countries_data.get_country_data_by_code("US")
```

### Get Subdivisions

```python
from countries_data import CountriesData

countries_data = CountriesData()

# Get all subdivisions for a country as list
subdivisions = countries_data.get_country_subdivisions_by_code("US")

# Get a specific subdivision by code
subdivision = countries_data.get_country_subdivision_by_codes("US", "CA")
```

### Get Translations

```python
from countries_data import CountriesData

countries_data = CountriesData()

# Get all country names in a specific language
spanish_names = countries_data.get_translated_countries_names_by_lang_code("es")

# Get a specific country name in a language
spanish_name = countries_data.get_translated_country_name_by_codes("es", "US")
```

## Data Format
TODO add data format here

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
