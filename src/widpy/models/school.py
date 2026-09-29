## Copyright (C) 2026 by Higher Expectations for Racine County

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from .agency import Agency
from .base import BaseModel

if TYPE_CHECKING:
    from .district import District


class School(Agency, BaseModel):
    r"""One school building/locus of instruction
    
    Attributes
    ----------
    distric: District
        The school district that this school belongs to
    """
    district_id: Mapped[int] = mapped_column(ForeignKey("district.id"),
                                             init=False)
    district: Mapped["District"] = relationship(back_populates="schools")
