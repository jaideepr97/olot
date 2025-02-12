# generated by datamodel-codegen:
#   filename:  image-layout-schema.json
#   timestamp: 2024-12-04T11:33:36+00:00

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field


class ImageLayoutVersion(Enum):
    field_1_0_0 = '1.0.0'


class OCIImageLayout(BaseModel):
    imageLayoutVersion: ImageLayoutVersion = Field(
        ..., description='version of the OCI Image Layout (in the oci-layout file)'
    )
