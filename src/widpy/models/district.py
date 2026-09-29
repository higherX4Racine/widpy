## Copyright (C) 2026 by Higher Expectations for Racine County

from typing import Optional, TYPE_CHECKING

from sqlalchemy.orm import (
    Mapped,
    relationship,
)

from .agency import Agency
from .base import BaseModel

if TYPE_CHECKING:
    from .school import School

class District(Agency, BaseModel):
    r"""One school district, probably tied to a geographic location.
    
    Attributes
    ----------
    schools: list[School]
        the schools that belong to this district
    """
    schools: Mapped[Optional[list["School"]]] = relationship(back_populates="district",
                                                             default_factory=list)
