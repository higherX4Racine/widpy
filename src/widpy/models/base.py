## Copyright (C) 2026 by Higher Expectations for Racine County

from typing import Optional

from sqlalchemy.orm import (
    DeclarativeBase,
    declared_attr,
    Mapped,
    MappedAsDataclass,
    mapped_column,
)

class BaseModel(MappedAsDataclass, DeclarativeBase):
    r"""Not an actual table, but all tables have a name and a pk called "id."
    
    Attributes
    ----------
    id : int
        the primary key for the table
    """
    
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    id: Mapped[int] = mapped_column(primary_key=True,
                                    init=False)
