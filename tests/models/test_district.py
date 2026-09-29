## Copyright (C) 2026 by Higher Expectations for Racine County

from sqlalchemy import select

from widpy import District


def test_district(session):
    D = [
        District(dpi_code="0000", nces_code="000000"),
        District(dpi_code="1000", nces_code="000001"),
        District(dpi_code="1100", nces_code="000011"),
        District(dpi_code="1110", nces_code="000111"),
    ]

    with session() as sesh:
        sesh.add_all(D)

        sesh.commit()

        DD = sesh.scalars(
            select(District).where(District.dpi_code.like(r"%00%"))
        ).all()

        assert len(DD) == 3
        assert DD[0].dpi_code in ["0000", "1000", "1100"]
        assert DD[1].dpi_code in ["0000", "1000", "1100"]
        assert DD[2].dpi_code in ["0000", "1000", "1100"]

