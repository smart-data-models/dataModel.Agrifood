from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, confloat, constr


class DrainFlow(BaseModel):
    maxValue: Optional[confloat(ge=0.0)] = Field(
        None, description='Maximum value of the drain flow'
    )
    minValue: Optional[confloat(ge=0.0)] = Field(
        None, description='Minimum value of the drain flow'
    )
    unitText: Optional[str] = Field(
        None, description='Description of the units of the drainflow'
    )
    value: Optional[confloat(ge=0.0)] = Field(
        None, description='Value of the drain flow'
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
    AgriGreenhouse = 'AgriGreenhouse'


class AgriGreenhouse(BaseModel):
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    belongsTo: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Entity the Greenhouse belongs to')
    co2: Optional[float] = Field(
        None, description='The measured interior C02 concentration nominally in mg/L'
    )
    dailyLight: Optional[float] = Field(
        None, description='Daily Accumulated light measured in kW per square metre'
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
    drainFlow: Optional[DrainFlow] = Field(
        None, description='The observed drain flow rate in litres per second'
    )
    hasAgriParcelChildren: Optional[
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
        None, description='Related sub AgriParcel records to which this entity relates'
    )
    hasAgriParcelParent: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description='Reference to the AgriParcel entity to which this entity relates',
    )
    hasDevice: Optional[
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
        description='Reference to the IoT devices associated with this greenhouse i.e. sensors, controls',
    )
    hasWaterQualityObserved: Optional[
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
        description='Reference to one or more water quality observation records current for this entity',
    )
    hasWeatherObserved: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description='Reference to the weather observation record current for this entity',
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
    leafTemperature: Optional[float] = Field(
        None, description='The average leaf temperature nominally in degrees centigrade'
    )
    name: Optional[str] = Field(None, description='The name of this item')
    ownedBy: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Owner (Person or Organization) of the AgriGreenhouse')
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
    relatedSource: Optional[List[RelatedSourceItem]] = Field(
        None,
        description='List of IDs the current entity may have in external applications',
    )
    relativeHumidity: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None,
        description='The inside relative humidity expressed as a number between 0 and 1 representing the range 0% to 100 (%).<br/><br/>0 <= relativeHumidity <= 1',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    type: Optional[Type] = Field(
        None, description='NGSI Entity Type. It has to be AgriGreenhouse'
    )
