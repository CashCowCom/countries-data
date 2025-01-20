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
    latitude: float | None = None
    longitude: float | None = None
    max_latitude: float | None = None
    max_longitude: float | None = None
    min_latitude: float | None = None
    min_longitude: float | None = None
    bounds: Bounds | None = None


class VatRates(BaseModel):
    standard: float | None = None
    reduced: list
    super_reduced: Any
    parking: Any


class CountryData(BaseModel):
    address_format: str | None = None
    alpha2: str
    alpha3: str
    continent: str
    country_code: str
    currency_code: str
    distance_unit: str
    gec: str | None = None
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
    en: str | None = None
    af: str | None = None
    ar: str | None = None
    az: str | None = None
    be: str | None = None
    bg: str | None = None
    ca: str | None = None
    cs: str | None = None
    da: str | None = None
    de: str | None = None
    es: str | None = None
    et: str | None = None
    eu: str | None = None
    fa: str | None = None
    fi: str | None = None
    fr: str | None = None
    he: str | None = None
    hy: str | None = None
    id: str | None = None
    it: str | None = None
    ja: str | None = None
    ka: str | None = None
    ko: str | None = None
    lt: str | None = None
    lv: str | None = None
    ms: str | None = None
    nb: str | None = None
    nl: str | None = None
    pl: str | None = None
    pt: str | None = None
    ro: str | None = None
    ru: str | None = None
    sr: str | None = None
    sv: str | None = None
    tr: str | None = None
    uk: str | None = None
    ur: str | None = None
    vi: str | None = None
    zh: str | None = None
    ceb: str | None = None
    sr_Latn: str | None = None  # noqa: N815
    ccp: str | None = None
    hu: str | None = None
    kk: str | None = None
    mk: str | None = None
    no: str | None = None
    cy: str | None = None
    el: str | None = None
    mn: str | None = None
    ta: str | None = None


class Subdivision(BaseModel):
    name: str
    code: str
    unofficial_names: list[str] | str | None = None
    geo: Geo | None = None
    translations: Translations | None = None
    comments: Any | None = None
    type: str
