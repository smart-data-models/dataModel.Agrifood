<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体：农业害虫    
=======<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/AgriPest/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全球描述：**该实体包含对农业害虫的统一描述。**    
版本： 0.0.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 属性列表    
<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。    
- `agroVocConcept[uri]`: 提及与本项目相关的 agrovoc 术语  . Model: [http://schema.org/URL](http://schema.org/URL)- `alternateName[string]`: 该项目的替代名称  - `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `hasAgriProductType[array]`: 参考可用于处理该害虫的推荐产品类型  . Model: [http://schema.org/URL](http://schema.org/URL)- `id[*]`: 实体的唯一标识符  - `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `relatedSource[array]`: 当前实体在外部应用程序中可能拥有的 ID 列表  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `type[string]`: NGSI 实体类型：必须是农业害虫  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
所需属性    
- `id`  - `name`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
该实体主要从事农业垂直行业和相关物联网应用。    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 属性的数据模型描述    
按字母顺序排列（点击查看详情）    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
AgriPest:      
  description: 'This entity contains a harmonised description of an agricultural pest. '      
  properties:      
    agroVocConcept:      
      description: Reference to the agrovoc term associated with this item      
      format: uri      
      type: string      
      x-ngsi:      
        model: http://schema.org/URL      
        type: Relationship      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dateCreated:      
      description: Entity creation timestamp. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    hasAgriProductType:      
      description: Reference to the recommended types of product that can be used to treat this pest      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        model: http://schema.org/URL      
        type: Relationship      
    id:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Unique identifier of the entity      
      x-ngsi:      
        type: Property      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    owner:      
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    relatedSource:      
      description: List of IDs the current entity may have in external applications      
      items:      
        properties:      
          application:      
            anyOf:      
              - description: Identifier format of any NGSI entity      
                maxLength: 256      
                minLength: 1      
                pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
                type: string      
                x-ngsi:      
                  type: Property      
              - description: Identifier format of any NGSI entity      
                format: uri      
                type: string      
                x-ngsi:      
                  type: Property      
            description: Unique identifier of the entity      
            x-ngsi:      
              type: Property      
          applicationEntityId:      
            description: Identifier in the external application      
            type: string      
            x-ngsi:      
              type: Property      
        type: object      
      type: array      
      x-ngsi:      
        type: Property      
    seeAlso:      
      description: list of uri pointing to additional resources about the item      
      oneOf:      
        - items:      
            format: uri      
            type: string      
          minItems: 1      
          type: array      
        - format: uri      
          type: string      
      x-ngsi:      
        type: Property      
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    type:      
      description: 'NGSI Entity Type: It has to be AgriPest'      
      enum:      
        - AgriPest      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
    - name      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Agrifood/blob/master/AgriPest/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.Agrifood/AgriPest/schema.json      
  x-model-tags: ""      
  x-version: 0.0.2      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 有效载荷示例    
#### AgriPest NGSI-v2 键值示例    
下面是一个以 JSON-LD 格式作为键值的 AgriPest 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AgriPest:fb3f1295-500c-4aa3-b995-c909097d5c01",  
  "type": "AgriPest",  
  "dateCreated": "2017-01-01T01:20:00Z",  
  "dateModified": "2017-05-04T12:30:00Z",  
  "name": "Grasshopper",  
  "alternateName": "Chorthippus parallelus",  
  "relatedSource": [  
    {  
      "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
      "applicationEntityId": "app:pest1"  
    }  
  ],  
  "seeAlso": [  
    "https://example.org/concept/pest",  
    "https://datamodel.org/example/pest"  
  ],  
  "agroVocConcept": "http://aims.fao.org/aos/agrovoc/c_31924",  
  "description": "Common European grasshopper",  
  "hasAgriProductType": [  
    "urn:ngsi-ld:AgriProductType:06afffde-4488-11e8-861a-cfcf50aaa9cc",  
    "urn:ngsi-ld:AgriProductType:0c094486-4488-11e8-a15f-afa816790c64",  
    "urn:ngsi-ld:AgriProductType:14bf9f26-4488-11e8-9e3d-bfb78de66dd3"  
  ]  
}  
```  
</details>    
#### AgriPest NGSI-v2 标准化示例    
下面是一个规范化 JSON-LD 格式的 AgriPest 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AgriPest:fb3f1295-500c-4aa3-b995-c909097d5c01",  
  "type": "AgriPest",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2017-01-01T01:20:00Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2017-05-04T12:30:00Z"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Grasshopper"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Chorthippus parallelus"  
  },  
  "relatedSource": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
        "applicationEntityId": "app:pest1"  
      }  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "https://example.org/concept/pest",  
      "https://datamodel.org/example/pest"  
    ]  
  },  
  "agroVocConcept": {  
    "type": "Text",  
    "value": "http://aims.fao.org/aos/agrovoc/c_31924"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Common European grasshopper"  
  },  
  "hasAgriProductType": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:AgriProductType:06afffde-4488-11e8-861a-cfcf50aaa9cc",  
      "urn:ngsi-ld:AgriProductType:0c094486-4488-11e8-a15f-afa816790c64",  
      "urn:ngsi-ld:AgriProductType:14bf9f26-4488-11e8-9e3d-bfb78de66dd3"  
    ]  
  }  
}  
```  
</details>    
#### AgriPest NGSI-LD 键值示例    
下面是一个以 JSON-LD 格式作为键值的 AgriPest 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AgriPest:fb3f1295-500c-4aa3-b995-c909097d5c01",  
  "type": "AgriPest",  
  "agroVocConcept": "http://aims.fao.org/aos/agrovoc/c_31924",  
  "alternateName": "Chorthippus parallelus",  
  "createdAt": "2017-01-01T01:20:00Z",  
  "description": "Common European grasshopper",  
  "hasAgriProductType": [  
    "urn:ngsi-ld:AgriProductType:06afffde-4488-11e8-861a-cfcf50aaa9cc",  
    "urn:ngsi-ld:AgriProductType:0c094486-4488-11e8-a15f-afa816790c64",  
    "urn:ngsi-ld:AgriProductType:14bf9f26-4488-11e8-9e3d-bfb78de66dd3"  
  ],  
  "modifiedAt": "2017-05-04T12:30:00Z",  
  "name": "Grasshopper",  
  "relatedSource": [  
    {  
      "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
      "applicationEntityId": "app:farm1"  
    }  
  ],  
  "seeAlso": [  
    "https://example.org/concept/pest",  
    "https://datamodel.org/example/pest"  
  ],  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Agrifood/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### AgriPest NGSI-LD 归一化示例    
下面是一个规范化 JSON-LD 格式的 AgriPest 示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:AgriPest:fb3f1295-500c-4aa3-b995-c909097d5c01",  
    "type": "AgriPest",  
    "agroVocConcept": {  
        "type": "Property",  
        "value": "http://aims.fao.org/aos/agrovoc/c_31924"  
    },  
    "alternateName": {  
        "type": "Property",  
        "value": "Chorthippus parallelus"  
    },  
    "createdAt": "2017-01-01T01:20:00Z",  
    "description": {  
        "type": "Property",  
        "value": "Common European grasshopper"  
    },  
    "hasAgriProductType": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:AgriProductType:06afffde-4488-11e8-861a-cfcf50aaa9cc",  
            "urn:ngsi-ld:AgriProductType:0c094486-4488-11e8-a15f-afa816790c64",  
            "urn:ngsi-ld:AgriProductType:14bf9f26-4488-11e8-9e3d-bfb78de66dd3"  
        ]  
    },  
    "modifiedAt": "2017-05-04T12:30:00Z",  
    "name": {  
        "type": "Property",  
        "value": "Grasshopper"  
    },  
    "relatedSource": {  
        "type": "Property",  
        "value": [  
            {  
                "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
                "applicationEntityId": "app:farm1"  
            }  
        ]  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": [  
            "https://example.org/concept/pest",  
            "https://datamodel.org/example/pest"  
        ]  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Agrifood/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
