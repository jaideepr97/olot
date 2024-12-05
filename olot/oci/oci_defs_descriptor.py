# generated by datamodel-codegen:
#   filename:  defs-descriptor.json
#   timestamp: 2024-12-05T11:15:48+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class MediaType(BaseModel):
    id: str
    type: str
    pattern: str


class Digest(BaseModel):
    description: str
    type: str
    pattern: str


class Items(BaseModel):
    type: str
    format: str


class Urls(BaseModel):
    description: str
    type: str
    items: Items


class Annotations(BaseModel):
    field_ref: str = Field(..., alias='$ref')


class Definitions(BaseModel):
    mediaType: MediaType
    digest: Digest
    urls: Urls
    annotations: Annotations


class Model(BaseModel):
    description: str
    definitions: Definitions
