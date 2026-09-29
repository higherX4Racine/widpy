## Copyright (C) 2026 by Higher Expectations for Racine County

from typing import Generator

from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import Session, sessionmaker

import pytest

from widpy.models.base import BaseModel


@pytest.fixture(scope="module")
def engine() -> Generator[Engine]:
    r"""An SQLite engine with BaseModel's metadata"""
    e = create_engine("sqlite://")
    BaseModel.metadata.create_all(e)

    yield e


@pytest.fixture(scope = "module")
def session(engine) -> Session:
    r"""A stand-alone session for interacting with the database"""
    return sessionmaker(engine)
