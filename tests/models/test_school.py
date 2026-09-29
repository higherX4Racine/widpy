## Copyright (C) 2026 by Higher Expectations for Racine County

from sqlalchemy import select

from widpy import District, School


def test_school(session):
    Pawnee = District(nces_code="444222",
                      dpi_code="4242")
    Eagleton = District(nces_code="424242",
                           dpi_code="4422")

    S = [
        School(nces_code="44442222",
               dpi_code="0001",
               district=Pawnee),
        School(nces_code="44442223",
               dpi_code="0002",
               district=Pawnee),
        School(nces_code="22224444",
               dpi_code="0003",
               district=Eagleton),
        School(nces_code="22224445",
               dpi_code="0004",
               district=Eagleton),
    ]

    with session() as sesh:
        sesh.add_all(S)
        sesh.commit()

        eaglets = sesh.scalars(
            select(School).where(School.district==Eagleton)
        ).all()
        assert "0003" in [x.dpi_code for x in eaglets]
        assert "0004" in [x.dpi_code for x in eaglets]

        pawns = sesh.scalars(
            select(School).where(School.district==Pawnee)
        ).all()
        assert "0001" in [x.dpi_code for x in pawns]
        assert "0002" in [x.dpi_code for x in pawns]
