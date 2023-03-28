<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：农业温室（AgriGreenhouse  
======================<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/AgriGreenhouse/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述：**该实体包含对通用温室（AgriParcel的一种类型）内记录的条件的统一描述。  
版本：0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `alternateName[string]`: 这个项目的一个替代名称  - `belongsTo[*]`: 温室所属的实体  - `co2[number]`: 测量的室内C02浓度，名义上是mg/L  . Model: [http://schema.org/Number](http://schema.org/Number)- `dailyLight[number]`: 每日累计光照，单位为每平方米千瓦  . Model: [http://schema.org/Number](http://schema.org/Number)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `drainFlow[object]`: 观察到的排水流速，单位为升/秒  . Model: [http://schema.org/Number](http://schema.org/Number)- `hasAgriParcelChildren[array]`: 该实体相关的次级AgriParcel记录  - `hasAgriParcelParent[*]`: 指的是与该实体有关的AgriParcel实体  - `hasDevice[array]`: 参考与该温室相关的物联网设备，即传感器、控制器。  . Model: [http://schema.org/URL](http://schema.org/URL)- `hasWaterQualityObserved[array]`: 参考该实体的一个或多个当前水质观察记录  - `hasWeatherObserved[*]`: 对该实体的当前天气观测记录的引用  - `id[*]`: 实体的唯一标识符  - `leafTemperature[number]`: 叶子的平均温度，名义上是摄氏度。  . Model: [http://schema.org/Number](http://schema.org/Number)- `name[string]`: 这个项目的名称。  - `ownedBy[*]`: AgriGreenhouse的所有者（个人或组织）。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `relatedSource[array]`: 当前实体在外部应用程序中可能拥有的ID列表  - `relativeHumidity[number]`: 内部相对湿度，以0和1之间的数字表示，代表0%到100（%）的范围。<br/><br/>0 <= relativeHumidity <= 1  . Model: [http://schema.org/Number](http://schema.org/Number)- `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `type[string]`: NGSI实体类型。它必须是AgriGreenhouse  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `hasAgriParcelParent`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
这个实体主要与农业垂直领域和相关的物联网应用有关。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AgriGreenhouse:    
  description: 'This entity contains a harmonised description of the conditions recorded within a generic greenhouse, a type of AgriParcel.'    
  properties:    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    belongsTo:    
      anyOf:    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Entity the Greenhouse belongs to    
      x-ngsi:    
        type: Relationship    
    co2:    
      description: The measured interior C02 concentration nominally in mg/L    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: mg/L    
    dailyLight:    
      description: Daily Accumulated light measured in kW per square metre    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: kw/m2    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity.    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    drainFlow:    
      description: The observed drain flow rate in litres per second    
      properties:    
        maxValue:    
          minimum: 0    
          type: number    
        minValue:    
          minimum: 0    
          type: number    
        unitText:    
          type: string    
        value:    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: L/s    
    hasAgriParcelChildren:    
      description: Related sub AgriParcel records to which this entity relates    
      items:    
        anyOf: &agrigreenhouse_-_properties_-_hasdevice_-_items_-_anyof    
          - description: Property. Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: Property. Identifier format of any NGSI entity    
            format: uri    
            type: string    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Relationship    
    hasAgriParcelParent:    
      anyOf:    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Reference to the AgriParcel entity to which this entity relates    
      x-ngsi:    
        type: Relationship    
    hasDevice:    
      description: 'Reference to the IoT devices associated with this greenhouse i.e. sensors, controls.'    
      items:    
        anyOf: *agrigreenhouse_-_properties_-_hasdevice_-_items_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
    hasWaterQualityObserved:    
      description: Reference to one or more water quality observation records current for this entity    
      items:    
        anyOf: *agrigreenhouse_-_properties_-_hasdevice_-_items_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Relationship    
    hasWeatherObserved:    
      anyOf:    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Reference to the weather observation record current for this entity    
      x-ngsi:    
        type: Relationship    
    id:    
      anyOf: *agrigreenhouse_-_properties_-_hasdevice_-_items_-_anyof    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    leafTemperature:    
      description: The average leaf temperature nominally in degrees centigrade.    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    name:    
      description: The name of this item.    
      type: string    
      x-ngsi:    
        type: Property    
    ownedBy:    
      anyOf:    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Owner (Person or Organization) of the AgriGreenhouse    
      x-ngsi:    
        type: Relationship    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *agrigreenhouse_-_properties_-_hasdevice_-_items_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    relatedSource:    
      description: List of IDs the current entity may have in external applications    
      items:    
        properties:    
          application:    
            anyOf: *agrigreenhouse_-_properties_-_hasdevice_-_items_-_anyof    
            description: Property. Unique identifier of the entity    
          applicationEntityId:    
            type: string    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    relativeHumidity:    
      description: The inside relative humidity expressed as a number between 0 and 1 representing the range 0% to 100 (%).<br/><br/>0 <= relativeHumidity <= 1    
      maximum: 1.0    
      minimum: 0.0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: Degrees centigrade    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity Type. It has to be AgriGreenhouse    
      enum:    
        - AgriGreenhouse    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - hasAgriParcelParent    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Agrifood/blob/master/AgriGreenhouse/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Agrifood/AgriGreenhouse/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### AgriGreenhouse NGSI-v2 关键值示例  
这里是一个以JSON-LD格式作为关键值的AgriGreenhouse的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的背景数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:AgriGreenhouse:df72dc57-1eb9-42a3-88a9-8647ecc954b4",  
  "type": "AgriGreenhouse",  
  "dateCreated": "2017-01-01T01:20:00Z",  
  "dateModified": "2017-05-04T12:30:00Z",  
  "ownedBy": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c",  
  "relatedSource": [  
    {  
      "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
      "applicationEntityId": "app:greenhouse1"  
    }  
  ],  
  "seeAlso": [  
    "https://example.org/concept/agrigreenhouse",  
    "https://datamodel.org/example/agrigreenhouse"  
  ],  
  "belongsTo": "urn:ngsi-ld:AgriFarm:f67adcbc-4479-22bc-9de1-cb228de7a765",  
  "hasAgriParcelParent": "urn:ngsi-ld:AgriParcel:c8b475e5-84a8-4346-ad79-cde1d2a4028b",  
  "hasAgriParcelChildren": [  
    "urn:ngsi-ld:AgriParcel:8c3a525d-b42e-4048-bcdd-a119d8ddb0a5",  
    "urn:ngsi-ld:AgriParcel:178d74c1-e6fe-4042-b955-2c164fc90b83"  
  ],  
  "hasWeatherObserved": "urn:ngsi-ld:WeatherObserved:c720cec5-ac6f-40b7-8e89-becb75702d0d",  
  "hasWaterQualityObserved": [  
    "urn:ngsi-ld:WaterQualityObserved:49f86e0b-bb90-4751-a1c3-d5a891920807",  
    "urn:ngsi-ld:WaterQualityObserved:853bf420-43fc-11e8-942f-6b7615517118"  
  ],  
  "relativeHumidity": 0.4,  
  "leafTemperature": 22,  
  "co2": 28,  
  "dailyLight": 24,  
  "drainFlow": {  
    "value": 33,  
    "maxValue": 50,  
    "minValue": 25,  
    "unitText": "Litre per second"  
  },  
  "hasDevice": [  
    "urn:ngsi-ld:Device:4a40aeba-4474-11e8-86bf-03d82e958ce6",  
    "urn:ngsi-ld:Device:63217d24-4474-11e8-9da2-c3dd3c36891b",  
    "urn:ngsi-ld:Device:68e091dc-4474-11e8-a398-df010c53b416",  
    "urn:ngsi-ld:6f44b54e-4474-11e8-8577-d7ff6a8ef551"  
  ]  
}  
```  
</details>  
#### AgriGreenhouse NGSI-v2规范化示例  
下面是一个以JSON-LD格式规范化的AgriGreenhouse的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:AgriGreenhouse:df72dc57-1eb9-42a3-88a9-8647ecc954b4",  
  "type": "AgriGreenhouse",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2017-01-01T01:20:00Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2017-05-04T12:30:00Z"  
  },  
  "ownedBy": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c"  
  },  
  "relatedSource": {  
    "value": [  
      {  
        "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
        "applicationEntityId": "app:greenhouse1"  
      }  
    ]  
  },  
  "seeAlso": {  
    "value": [  
      "https://example.org/concept/agrigreenhouse",  
      "https://datamodel.org/example/agrigreenhouse"  
    ]  
  },  
  "belongsTo": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:AgriFarm:f67adcbc-4479-22bc-9de1-cb228de7a765"  
  },  
  "hasAgriParcelParent": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:AgriParcel:c8b475e5-84a8-4346-ad79-cde1d2a4028b"  
  },  
  "hasAgriParcelChildren": {  
    "type": "Relationship",  
    "value": [  
      "urn:ngsi-ld:AgriParcel:8c3a525d-b42e-4048-bcdd-a119d8ddb0a5",  
      "urn:ngsi-ld:AgriParcel:178d74c1-e6fe-4042-b955-2c164fc90b83"  
    ]  
  },  
  "hasWeatherObserved": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:WeatherObserved:c720cec5-ac6f-40b7-8e89-becb75702d0d"  
  },  
  "hasWaterQualityObserved": {  
    "type": "Relationship",  
    "value": [  
      "urn:ngsi-ld:WaterQualityObserved:49f86e0b-bb90-4751-a1c3-d5a891920807",  
      "urn:ngsi-ld:WaterQualityObserved:853bf420-43fc-11e8-942f-6b7615517118"  
    ]  
  },  
  "relativeHumidity": {  
    "type": "Property",  
    "value": 0.4  
  },  
  "leafTemperature": {  
    "type": "Property",  
    "value": 22  
  },  
  "co2": {  
    "type": "Property",  
    "value": 28  
  },  
  "dailyLight": {  
    "type": "Property",  
    "value": 24  
  },  
  "drainFlow": {  
    "type": "Property",  
    "value": {  
      "value": 33,  
      "maxValue": 50,  
      "minValue": 25,  
      "unitText": "Litre per second"  
    }  
  },  
  "hasDevice": {  
    "type": "Relationship",  
    "value": [  
      "urn:ngsi-ld:Device:4a40aeba-4474-11e8-86bf-03d82e958ce6",  
      "urn:ngsi-ld:Device:63217d24-4474-11e8-9da2-c3dd3c36891b",  
      "urn:ngsi-ld:Device:68e091dc-4474-11e8-a398-df010c53b416",  
      "urn:ngsi-ld:6f44b54e-4474-11e8-8577-d7ff6a8ef551"  
    ]  
  }  
}  
```  
</details>  
#### AgriGreenhouse NGSI-LD关键值示例  
这里是一个以JSON-LD格式作为关键值的AgriGreenhouse的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:AgriGreenhouse:df72dc57-1eb9-42a3-88a9-8647ecc954b4",  
    "type": "AgriGreenhouse",  
    "belongsTo": "urn:ngsi-ld:AgriFarm:f67adcbc-4479-22bc-9de1-cb228de7a765",  
    "co2": 28,  
    "createdAt": "2017-01-01T01:20:00Z",  
    "dailyLight": 24,  
    "drainFlow": {  
        "maxValue": 50,  
        "minValue": 25,  
        "unitText": "Litre per second",  
        "value": 33  
    },  
    "hasAgriParcelChildren": [  
        "urn:ngsi-ld:AgriParcel:8c3a525d-b42e-4048-bcdd-a119d8ddb0a5",  
        "urn:ngsi-ld:AgriParcel:178d74c1-e6fe-4042-b955-2c164fc90b83"  
    ],  
    "hasAgriParcelParent": "urn:ngsi-ld:AgriParcel:c8b475e5-84a8-4346-ad79-cde1d2a4028b",  
    "hasDevice": [  
        "urn:ngsi-ld:Device:4a40aeba-4474-11e8-86bf-03d82e958ce6",  
        "urn:ngsi-ld:Device:63217d24-4474-11e8-9da2-c3dd3c36891b",  
        "urn:ngsi-ld:Device:68e091dc-4474-11e8-a398-df010c53b416",  
        "urn:ngsi-ld:6f44b54e-4474-11e8-8577-d7ff6a8ef551"  
    ],  
    "hasWaterQualityObserved": [  
        "urn:ngsi-ld:WaterQualityObserved:49f86e0b-bb90-4751-a1c3-d5a891920807",  
        "urn:ngsi-ld:WaterQualityObserved:853bf420-43fc-11e8-942f-6b7615517118"  
    ],  
    "hasWeatherObserved": "urn:ngsi-ld:WeatherObserved:c720cec5-ac6f-40b7-8e89-becb75702d0d",  
    "leafTemperature": 22,  
    "modifiedAt": "2017-05-04T12:30:00Z",  
    "ownedBy": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c",  
    "relatedSource": [  
        {  
            "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
            "applicationEntityId": "app:greenhouse1"  
        }  
    ],  
    "relativeHumidity": 0.4,  
    "seeAlso": [  
        "https://example.org/concept/agrigreenhouse",  
        "https://datamodel.org/example/agrigreenhouse"  
    ],  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Agrifood/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### AgriGreenhouse NGSI-LD规范化示例  
下面是一个以JSON-LD格式规范化的AgriGreenhouse的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:AgriGreenhouse:df72dc57-1eb9-42a3-88a9-8647ecc954b4",  
    "type": "AgriGreenhouse",  
    "belongsTo": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:AgriFarm:f67adcbc-4479-22bc-9de1-cb228de7a765"  
    },  
    "co2": {  
        "type": "Property",  
        "value": 28,  
        "unitCode": "M1",  
        "observedAt": "2016-08-22T19:20Z"  
    },  
    "createdAt": "2017-01-01T01:20:00Z",  
    "dailyLight": {  
        "type": "Property",  
        "value": 24,  
        "unitCode": "N78",  
        "observedAt": "2016-08-22T19:20Z"  
    },  
    "drainFlow": {  
        "type": "Property",  
        "value": {  
            "value": 33,  
            "maxValue": 50,  
            "minValue": 25,  
            "unitText": "Litre per second"  
        },  
        "unitCode": "G51",  
        "observedAt": "2016-08-22T19:20Z"  
    },  
    "hasAgriParcelChildren": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:AgriParcel:8c3a525d-b42e-4048-bcdd-a119d8ddb0a5",  
            "urn:ngsi-ld:AgriParcel:178d74c1-e6fe-4042-b955-2c164fc90b83"  
        ]  
    },  
    "hasAgriParcelParent": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:AgriParcel:c8b475e5-84a8-4346-ad79-cde1d2a4028b"  
    },  
    "hasDevice": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:Device:4a40aeba-4474-11e8-86bf-03d82e958ce6",  
            "urn:ngsi-ld:Device:63217d24-4474-11e8-9da2-c3dd3c36891b",  
            "urn:ngsi-ld:Device:68e091dc-4474-11e8-a398-df010c53b416",  
            "urn:ngsi-ld:6f44b54e-4474-11e8-8577-d7ff6a8ef551"  
        ]  
    },  
    "hasWaterQualityObserved": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:WaterQualityObserved:49f86e0b-bb90-4751-a1c3-d5a891920807",  
            "urn:ngsi-ld:WaterQualityObserved:853bf420-43fc-11e8-942f-6b7615517118"  
        ]  
    },  
    "hasWeatherObserved": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:WeatherObserved:c720cec5-ac6f-40b7-8e89-becb75702d0d"  
    },  
    "leafTemperature": {  
        "type": "Property",  
        "value": 22,  
        "unitCode": "CEL",  
        "observedAt": "2016-08-22T19:20Z"  
    },  
    "modifiedAt": "2017-05-04T12:30:00Z",  
    "ownedBy": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c"  
    },  
    "relatedSource": {  
        "type": "Property",  
        "value": [  
            {  
                "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
                "applicationEntityId": "app:greenhouse1"  
            }  
        ]  
    },  
    "relativeHumidity": {  
        "type": "Property",  
        "value": 0.4,  
        "unitCode": "C62",  
        "observedAt": "2016-08-22T19:20Z"  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": [  
            "https://example.org/concept/agrigreenhouse",  
            "https://datamodel.org/example/agrigreenhouse"  
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
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
