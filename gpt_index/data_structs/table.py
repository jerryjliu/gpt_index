"""Struct store schema."""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from dataclasses_json import DataClassJsonMixin

from gpt_index.data_structs.data_structs import IndexStruct


@dataclass
class StructDatapoint(DataClassJsonMixin):
    """Struct outputs."""

    # map from field name to StructValue
    fields: Dict[str, Any]


@dataclass
class BaseStructTable(IndexStruct):
    """Struct outputs."""


@dataclass
class SQLStructTable(BaseStructTable):
    """SQL struct outputs."""
