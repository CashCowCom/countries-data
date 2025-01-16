from typing import Any

from pydantic import BaseModel


class Northeast(BaseModel):
    lat: float
    lng: float


class Southwest(BaseModel):
    lat: float
    lng: float


class Bounds(BaseModel):
    northeast: Northeast
    southwest: Southwest


class Geo(BaseModel):
    latitude: float | None
    longitude: float | None
    max_latitude: float | None
    max_longitude: float | None
    min_latitude: float | None
    min_longitude: float | None
    bounds: Bounds | None = None

class VatRates(BaseModel):
    standard: float | None = None
    reduced: list
    super_reduced: Any
    parking: Any


class CountryData(BaseModel):
    address_format: str | None =None
    alpha2: str
    alpha3: str
    continent: str
    country_code: str
    currency_code: str
    distance_unit: str
    gec: str| None = None
    geo: Geo
    international_prefix: str
    ioc: str | None = None
    iso_long_name: str
    iso_short_name: str
    languages_official: list[str]
    languages_spoken: list[str]
    national_destination_code_lengths: list[int]
    national_number_lengths: list[int]
    national_prefix: str
    nationality: str
    number: str
    postal_code: bool
    postal_code_format: str | None = None
    region: str
    start_of_week: str
    subregion: str
    un_locode: str
    un_member: bool
    unofficial_names: list[str]
    vat_rates: VatRates | None = None
    vehicle_registration_code: str | None = None
    world_region: str



class Translations(BaseModel):
    en: str
    af: str
    ar: str
    az: str
    be: str
    bg: str
    ca: str
    cs: str
    da: str
    de: str
    es: str
    et: str
    eu: str
    fa: str
    fi: str
    fr: str
    he: str
    hy: str
    id: str
    it: str
    ja: str
    ka: str
    ko: str
    lt: str
    lv: str
    ms: str
    nb: str
    nl: str
    pl: str
    pt: str
    ro: str
    ru: str
    sr: str
    sv: str
    tr: str
    uk: str
    ur: str
    vi: str
    zh: str
    ceb: str
    sr_Latn: str  # noqa: N815
    ccp: str
    hu: str
    kk: str
    mk: str
    no: str
    cy: str
    el: str
    mn: str
    ta: str


class Subdivision(BaseModel):
    name: str
    code: str
    unofficial_names: list[str]
    geo: Geo | None
    translations: Translations
    comments: Any
    type: str
