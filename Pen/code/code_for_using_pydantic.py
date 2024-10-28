from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import (
    AnyUrl,
    AwareDatetime,
    BaseModel,
    Field,
    RootModel,
    confloat,
    constr,
)


class AdditionalInfoItem(BaseModel):
    name: Optional[str] = None
    value: Optional[Union[str, float, bool]] = None


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


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


class Sex(Enum):
    M = 'M'
    F = 'F'
    unknown = 'unknown'
    field_ = ''


class Type6(Enum):
    Pen = 'Pen'


class Pen(BaseModel):
    additionalInfo: Optional[List[AdditionalInfoItem]] = Field(
        None,
        description="list of all the raw values sent by the sensor/platform with all the possible extra properties that are not included in the main structure. It is a JSON structure similar to this: {'name': 'temperature', 'value' : 32}",
    )
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    arrivalTimestamp: Optional[AwareDatetime] = Field(
        None, description='Date and Time for the arrival of animals to the Pen'
    )
    avgGrowth: Optional[confloat(ge=0.0)] = Field(
        None, description='The average growth in weight of the animal in this pen'
    )
    avgWeight: Optional[confloat(ge=0.0)] = Field(
        None, description='The average weight of the animal in this Pen. '
    )
    buildingId: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None, description='Unique identifier of the Building the item is located in'
    )
    co2: Optional[confloat(ge=0.0)] = Field(
        None, description='The CO2 concentration in the item'
    )
    companyId: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of a company')
    compartmentId: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None, description='Unique identifier of the Compartment the Pen is located in'
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
    deadAnimalsSinceDateOfArrival: Optional[confloat(ge=0.0)] = Field(
        None, description='Number of dead animals since the date of arrival'
    )
    description: Optional[str] = Field(None, description='A description of this item')
    farmId: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the Farm the Pen is located in')
    feedConsumption: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The total amount of food that has been eaten from the feeding station(s) in the pen.It is measured through feed intakes and specific structure to let only one animal at a time to eat',
    )
    humidity: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None,
        description='Quantity representing the amount of water vapour in the atmosphere in the pen. ',
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
    lastUpdate: Optional[AwareDatetime] = Field(
        None,
        description='Date and time at which the measurements in the item were taken',
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    luminosity: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The brightness of a light source of a certain wavelength at the item',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    numAnimals: Optional[confloat(ge=0.0)] = Field(
        None, description='Number of animals contained in the Pen'
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
    relatedSource: Optional[List[RelatedSourceItem]] = Field(
        None,
        description='List of IDs the current entity may have in external applications',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    sex: Optional[Sex] = Field(
        None, description='The sex of the animals contained in the pen'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    temperature: Optional[float] = Field(
        None, description="Temperature of the Pen.  Unirs:' Celsius degree'"
    )
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. it has to be Pen'
    )
    waterConsumption: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The total amount of water that came out from the tap or taps in the pen. It is measured through flowmeters and specific structure to let only one animal at a time drink',
    )
    weightStDev: Optional[float] = Field(
        None,
        description='The standard deviation associated to the average weight of the animals contained in the Pen',
    )
