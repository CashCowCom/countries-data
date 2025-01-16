from pathlib import Path


def get_countries_code_list()-> list[str]:
    return [str(f)[-7:-5] for f in (Path(__file__).parent.parent /  "data" / "countries").iterdir() if f.is_file()]

def get_subdivisions_code_list()-> list[str]:
    return [str(f)[-7:-5] for f in (Path(__file__).parent.parent /  "data" / "subdivisions").iterdir() if f.is_file()]

def get_translations_code_list()-> list[str]:
    return [str(f)[10:-5] for f in (Path(__file__).parent.parent /  "data" / "translations").iterdir() if f.is_file()]
