## Copyright (C) 2026 by Higher Expectations for Racine County

from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped,
    MappedAsDataclass,
    mapped_column,
)


class Agency(MappedAsDataclass):
    r"""Either a school or a school district
    
    Attributes
    ----------
    dpi_code: String
        a 4-digit code from the Wisconsin Department of Public Instruction
    nces_code: String
        a 6-digit code from the United States Department of Education

    """

    dpi_code: Mapped[str] = mapped_column(String(4))
    nces_code: Mapped[Optional[str]] = mapped_column(String(6))
