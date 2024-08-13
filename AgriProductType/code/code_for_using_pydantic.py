from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, constr


class CategoryEnum(Enum):
    cropNutrition = 'cropNutrition'
    cropProtection = 'cropProtection'
    cropVariety = 'cropVariety'
    fertiliser = 'fertiliser'
    harvestCommodity = 'harvestCommodity'


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


class Type(Enum):
    AgriProductType = 'AgriProductType'


class AgriProductType(BaseModel):
    agroVocConcept: Optional[AnyUrl] = Field(
        None, description='Reference to the agrovoc term associated with this item'
    )
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    category: Optional[List[CategoryEnum]] = Field(
        None,
        description="Category of the product. Enum:'fertiliser, cropNutrition, cropProtection, cropVariety, harvestCommodity'",
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
    hasAgriProductTypeChildren: Optional[
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
        description='Reference to child product types i.e. immediately below this entity in the hierarchy',
    )
    hasAgriProductTypeParent: Optional[
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
        description='Reference to the parent product type i.e. immediately above the entity in the hierarchy',
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
    relatedSource: Optional[List[RelatedSourceItem]] = Field(
        None,
        description='List of IDs the current entity may have in external applications',
    )
    root: Optional[bool] = Field(
        None,
        description='A logical indicator that this product is the root of an AgriProductType hierarchy. Logical true indicates it is the root',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    type: Optional[Type] = Field(
        None, description='NGSI Entity Type: It has to be AgriProductType'
    )
