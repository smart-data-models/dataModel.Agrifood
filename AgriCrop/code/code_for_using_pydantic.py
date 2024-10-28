from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, constr


class HarvestingIntervalItem(BaseModel):
    dateRange: Optional[
        constr(pattern=r'^-[0-1][0-9]-[0-3][0-9]/-[0-1][0-9]-[0-3][0-9]$')
    ] = Field(None, description='Range of dates in a string format')
    description: Optional[str] = Field(
        None, description='Descriptions of the range dates'
    )


class PlantingFromItem(BaseModel):
    dateRange: Optional[
        constr(pattern=r'^-[0-1][0-9]-[0-3][0-9]/-[0-1][0-9]-[0-3][0-9]$')
    ] = Field(None, description='Range of dates in a string format')
    description: Optional[str] = Field(
        None, description='Descriptions of the range dates'
    )


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
    ] = Field(
        None, description='Identifier of the entity describing the external application'
    )
    applicationEntityId: Optional[str] = Field(
        None, description='Identifier in the external application'
    )


class Type(Enum):
    AgriCrop = 'AgriCrop'


class WateringFrequency(Enum):
    daily = 'daily'
    weekly = 'weekly'
    biweekly = 'biweekly'
    monthly = 'monthly'
    onDemand = 'onDemand'
    other = 'other'


class AgriCrop(BaseModel):
    agroVocConcept: Optional[AnyUrl] = Field(
        None,
        description='The link with the defined concept into the AgroVoc vocabulary',
    )
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
    harvestingInterval: Optional[List[HarvestingIntervalItem]] = Field(
        None,
        description='A list of the recommended harvesting interval date(s) for this crop. Specified using ISO8601 repeating date intervals: <br/><br/>**interval, description**<br/><br/>Where **interval** is in the form of **start date/end date**<br/><br/>--MM-DD/--MM-DD<br/><br/>Meaning repeat each year from this start date to this end date',
        max_length=2,
        min_length=2,
    )
    hasAgriFertiliser: Optional[
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
        description='Reference to the recommended types of fertiliser suitable for growing this crop',
    )
    hasAgriPest: Optional[
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
    ] = Field(None, description='Reference to the pests known to attack this crop')
    hasAgriSoil: Optional[
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
        description='Reference to the recommended types of soil suitable for growing this crop',
    )
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
    name: Optional[str] = Field(None, description='The name of this item')
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
    plantingFrom: Optional[List[PlantingFromItem]] = Field(
        None,
        description='A list of the recommended planting interval date(s) for this crop. Specified using ISO8601 repeating date intervals: <br/><br/>**interval, description**<br/><br/>Where **interval** is in the form of **start date/end date**<br/><br/>--MM-DD/--MM-DD<br/><br/>Meaning repeat each year from this start date to this end date',
        max_length=2,
        min_length=2,
    )
    relatedSource: Optional[List[RelatedSourceItem]] = Field(
        None,
        description='List of IDs the current entity may have in external applications',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    type: Optional[Type] = Field(
        None, description='NGSI Entity Type. it has to be AgriCrop'
    )
    wateringFrequency: Optional[WateringFrequency] = Field(
        None,
        description="A description of the recommended watering schedule. A choice from an enumerated list. One of: **daily, weekly, biweekly, monthly, onDemand, other**. Enum:'daily, weekly, biweekly, monthly, onDemand,    other'",
    )
