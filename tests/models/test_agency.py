## Copyright (C) 2026 by Higher Expectations for Racine County

import pytest

from widpy.models import Agency

@pytest.mark.parametrize("dpi,nces", [
    ("1111", "222222"),
    ("3333", "444444"),
    ])
def test_agency(dpi, nces):
    a = Agency(dpi, nces)
    assert a.dpi_code == dpi
    assert a.nces_code == nces
