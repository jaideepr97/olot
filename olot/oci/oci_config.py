# generated by datamodel-codegen:
#   filename:  config-schema.json
#   timestamp: 2024-12-04T08:15:20+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field

from olot.utils.types import MapStringString, MapStringObject


class Type(Enum):
    layers = 'layers'


class Rootfs(BaseModel):
    diff_ids: List[str]
    type: Type


class HistoryItem(BaseModel):
    created: Optional[datetime] = None
    author: Optional[str] = None
    created_by: Optional[str] = None
    comment: Optional[str] = None
    empty_layer: Optional[bool] = None


# class MapStringObject(BaseModel):
#     __root__: Dict[constr(regex=r'.{1,}'), Dict[str, Any]]


# class Int8(BaseModel):
#     __root__: conint(ge=-128, le=127)


# class Int16(BaseModel):
#     __root__: conint(ge=-32768, le=32767)


# class Int32(BaseModel):
#     __root__: conint(ge=-2147483648, le=2147483647)


# class Int64(BaseModel):
#     __root__: conint(ge=-9223372036854776000, le=9223372036854776000)


# class Uint8(BaseModel):
#     __root__: conint(ge=0, le=255)


# class Uint16(BaseModel):
#     __root__: conint(ge=0, le=65535)


# class Uint32(BaseModel):
#     __root__: conint(ge=0, le=4294967295)


# class Uint64(BaseModel):
#     __root__: conint(ge=0, le=18446744073709552000)


# class Uint16Pointer(BaseModel):
#     __root__: Optional[Uint16]


# class Uint64Pointer(BaseModel):
#     __root__: Optional[Uint64]


# class Base64(BaseModel):
#     __root__: str


# class StringPointer(BaseModel):
#     __root__: Optional[str]


# class MapStringString(BaseModel):
#     __root__: Dict[constr(regex=r'.{1,}'), str]


class Config(BaseModel):
    User: Optional[str] = None
    ExposedPorts: Optional[MapStringObject] = None
    Env: Optional[List[str]] = None
    Entrypoint: Optional[List[str]] = None
    Cmd: Optional[List[str]] = None
    Volumes: Optional[MapStringObject] = None
    WorkingDir: Optional[str] = None
    Labels: Optional[MapStringString] = None
    StopSignal: Optional[str] = None
    ArgsEscaped: Optional[bool] = None


class OCIManifestConfig(BaseModel):
    created: Optional[datetime] = None
    author: Optional[str] = None
    architecture: str
    variant: Optional[str] = None
    os: str
    os_version: Optional[str] = Field(None, alias='os.version')
    os_features: Optional[List[str]] = Field(None, alias='os.features')
    config: Optional[Config] = None
    rootfs: Rootfs
    history: Optional[List[HistoryItem]] = None
