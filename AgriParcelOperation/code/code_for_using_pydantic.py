from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, confloat, constr


class OperationType(Enum):
    fertiliser = 'fertiliser'
    inspection = 'inspection'
    pesticide = 'pesticide'
    water = 'water'
    other = 'other'


class RelatedSourceItem(BaseModel):
    application: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    applicationEntityId: Optional[str] = Field(
        None, description='Identifier in the external application'
    )


class Result(Enum):
    ok = 'ok'
    aborted = 'aborted'
    failed = 'failed'


class Status(Enum):
    planned = 'planned'
    ongoing = 'ongoing'
    finished = 'finished'
    scheduled = 'scheduled'
    cancelled = 'cancelled'


class Type(Enum):
    AgriParcelOperation = 'AgriParcelOperation'


class WaterSource(Enum):
    borehole = 'borehole'
    rainfall = 'rainfall'
    river = 'river'
    rainwater_capture = 'rainwater capture'
    water_dam = 'water dam'
    commercial_supply = 'commercial supply'


class AgriParcelOperation(BaseModel):
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    endedAt: Optional[AwareDatetime] = Field(
        None, description='Timestamp when the operation actually finished'
    )
    hasAgriParcel: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Reference to the AgriParcel')
    hasAgriProductType: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Reference to the AgriProductType used/applied')
    hasOperator: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Reference to the operator conducting the operation')
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    irrigationRecord: Optional[AnyUrl] = Field(
        None, description='Relationship with the irrigation record of the execution'
    )
    name: Optional[str] = Field(None, description='The name of this item')
    operationType: Optional[OperationType] = Field(
        None,
        description="A choice from an enumerated list describing the operation performed on the parcel. Enum:'fertiliser, inspection, pesticide, water, other'",
    )
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    plannedEndAt: Optional[AwareDatetime] = Field(
        None,
        description='The planned end date/timestamp for the operation. <br/><br/>Note that this is advisory and the actual time the operation finishes may be before or after the planned end',
    )
    plannedStartAt: Optional[AwareDatetime] = Field(
        None,
        description='The planned start date/timestamp for the operation. Note that this is advisory and the actual time the operation starts may be before or after the planned start',
    )
    quantity: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The total quantity of water or product used/ applied. It is recommended this is measured in litres for liquids or kilogrammes for solids',
    )
    relatedSource: Optional[List[RelatedSourceItem]] = Field(
        None,
        description='List of IDs the current entity may have in external applications',
    )
    reportedAt: Optional[AwareDatetime] = Field(
        None, description='Timestamp when the event fault was reported'
    )
    result: Optional[Result] = Field(
        None,
        description="A description of the results of the operation. Enum:'ok, aborted, failed'",
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    startedAt: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp when the operation actually started to be performed',
    )
    status: Optional[Status] = Field(
        None,
        description="A choice from an enumerated list describing the status. Enum:'planned, ongoing, finished, scheduled, cancelled'",
    )
    type: Optional[Type] = Field(
        None, description='NGSI Entity Type. It has to be AgriParcelOperation'
    )
    waterSource: Optional[WaterSource] = Field(
        None,
        description="Type of water sources. Enum:'borehole, rainfall, river, rainwater capture, water dam, commercial supply'",
    )
    workOrder: Optional[AnyUrl] = Field(
        None, description='Relationship with the workorder for the execution'
    )
    workRecord: Optional[AnyUrl] = Field(
        None, description='Relationship with the work record of the execution'
    )
