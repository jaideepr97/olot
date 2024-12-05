# generated by datamodel-codegen:
#   filename:  defs.json
#   timestamp: 2024-12-05T10:30:59+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Int8(BaseModel):
    type: str
    minimum: int
    maximum: int


class Int16(BaseModel):
    type: str
    minimum: int
    maximum: int


class Int32(BaseModel):
    type: str
    minimum: int
    maximum: int


class Int64(BaseModel):
    type: str
    minimum: int
    maximum: int


class Uint8(BaseModel):
    type: str
    minimum: int
    maximum: int


class Uint16(BaseModel):
    type: str
    minimum: int
    maximum: int


class Uint32(BaseModel):
    type: str
    minimum: int
    maximum: int


class Uint64(BaseModel):
    type: str
    minimum: int
    maximum: int


class OneOfItem(BaseModel):
    field_ref: Optional[str] = Field(None, alias='$ref')
    type: Optional[str] = None


class Uint16Pointer(BaseModel):
    oneOf: List[OneOfItem]


class Uint64Pointer(BaseModel):
    oneOf: List[OneOfItem]


class Media(BaseModel):
    binaryEncoding: str


class Base64(BaseModel):
    type: str
    media: Media


class OneOfItem2(BaseModel):
    type: str


class StringPointer(BaseModel):
    oneOf: List[OneOfItem2]


class Field1(BaseModel):
    type: str


class PatternProperties(BaseModel):
    field__1__: Field1 = Field(..., alias='.{1,}')


class MapStringString(BaseModel):
    type: str
    patternProperties: PatternProperties


class PatternProperties1(BaseModel):
    field__1__: Field1 = Field(..., alias='.{1,}')


class MapStringObject(BaseModel):
    type: str
    patternProperties: PatternProperties1


class Definitions(BaseModel):
    int8: Int8
    int16: Int16
    int32: Int32
    int64: Int64
    uint8: Uint8
    uint16: Uint16
    uint32: Uint32
    uint64: Uint64
    uint16Pointer: Uint16Pointer
    uint64Pointer: Uint64Pointer
    base64: Base64
    stringPointer: StringPointer
    mapStringString: MapStringString
    mapStringObject: MapStringObject


class Model(BaseModel):
    description: str
    definitions: Definitions
