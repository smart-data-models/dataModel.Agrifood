<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。舱室  
=====<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/Compartment/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述。**建筑物或部门中的人工区域，由某些传感器来测量。一个隔间不一定是一个物理隔间。它可以是一个部门，也可以是一个部门内由同一传感器测量的几个笔的组合。**。  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `additionalInfo[array]`: 由传感器/平台发送的所有原始值的列表，包括所有可能的、不包括在主结构中的额外属性。它是一个类似于这样的JSON结构。{ '温度': '32', '湿度': '42'}  - `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `arrivalTimestamp[string]`: 动物被放入隔间的日期和时间  . Model: [https://schema.org/Datetime](https://schema.org/Datetime)- `avgGrowth[number]`: 该隔间内动物体重的平均增长情况  . Model: [https://schema.org/Number.](https://schema.org/Number.)- `avgWeight[number]`: 这个隔间里的猪的平均体重  . Model: [https://schema.org/Number](https://schema.org/Number)- `buildingId[*]`: 隔间所在建筑的唯一标识符。  - `co2[number]`: 舱内的二氧化碳浓度  - `companyId[*]`: 公司的唯一标识符  - `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `empty[boolean]`: 如果隔间是空的，则为真/假值  - `farmId[*]`: 隔间所在农场的唯一标识符。  - `feedConsumption[number]`: 从隔间内的喂食站吃过的食物总量  - `humidity[number]`: 代表车厢内大气中的水蒸气量的数量  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: 实体的唯一标识符  - `lastUpdate[number]`: 在隔间内进行测量的日期和时间。Unix时间戳  - `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `luminosity[number]`: 某一波长的光源在车厢内的亮度  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: 这个项目的名称。  - `numAnimals[number]`: 隔间内的动物数量  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `parentCompartmentId[*]`: 该隔间的唯一标识符，该隔间是该隔间的一部分。它只在一个隔间包含其他隔间时使用。  - `relatedSource[array]`: 当前实体在外部应用程序中可能拥有的ID列表  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `sex[string]`: 隔间内所含动物的性别  - `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `temperature[number]`: 隔间的温度。  - `type[string]`: NGSI的实体类型。它必须是隔间。  - `waterConsumption[number]`: 从隔间内的一个或多个水龙头流出的水的总量  - `weightStDev[number]`: 与隔间内的猪/仔猪的平均重量有关的标准偏差  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `lastUpdate`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Compartment:    
  description: 'Artificial area in a building or department that is measured by certain sensors. A compartment is not necessarily a physical separator. It can be a department or a grouping of several pens within a department that are being measured by the same sensor.'    
  properties:    
    additionalInfo:    
      description: 'list of all the raw values sent by the sensor/platform with all the possible extra properties that are not included in the main structure. It is a JSON structure similar to this: { ''temperature'': ''32'', ''humidity'':''42''}'    
      items:    
        properties:    
          parameter:    
            type: string    
          value:    
            type: string    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    arrivalTimestamp:    
      description: 'Date and Time at which the animal were inserted in the compartment'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Datetime    
        type: Property    
    avgGrowth:    
      description: 'The average growth in weight of the animals in this compartment'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number.    
        type: Property    
    avgWeight:    
      description: 'The average weight of the pigs in this compartment'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    buildingId:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of a building the compartment is located in'    
      x-ngsi:    
        type: Relationship    
    co2:    
      description: 'The CO2 concentration in the compartment'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    companyId:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of a company'    
      x-ngsi:    
        type: Relationship    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    empty:    
      description: 'True/False value if the compartment is empty'    
      type: boolean    
      x-ngsi:    
        type: Property    
    farmId:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of a farm where the compartment is located in'    
      x-ngsi:    
        type: Relationship    
    feedConsumption:    
      description: 'The total amount of food that has been eaten from the feeding station(s) in the compartment'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    humidity:    
      description: 'Quantity representing the amount of water vapour in the atmosphere in the compartment'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &compartment_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    lastUpdate:    
      description: 'Date and time at which the measurements in the compartment were taken. Unix timestamp'    
      type: number    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'GeoProperty. Geojson reference to the item. Point'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      x-ngsi:    
        type: GeoProperty    
    luminosity:    
      description: 'The brightness of a light source of a certain wavelength at the compartment'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    numAnimals:    
      description: 'Number of animals in the compartment'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *compartment_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    parentCompartmentId:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the  compartment where this compartment is a part of. It is used only when a compartment contains other compartments'    
      x-ngsi:    
        type: Relationship    
    relatedSource:    
      description: 'List of IDs the current entity may have in external applications'    
      items:    
        properties:    
          application:    
            anyOf: *compartment_-_properties_-_owner_-_items_-_anyof    
            description: 'Property. Unique identifier of the entity'    
          applicationEntityId:    
            type: string    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
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
    sex:    
      description: 'The sex of the animals contained in the compartment'    
      enum:    
        - M    
        - F    
        - unknown    
        - ""    
      type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    temperature:    
      description: 'Temperature of the compartment.'    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. it has to be Compartment'    
      enum:    
        - Compartment    
      type: string    
      x-ngsi:    
        type: Property    
    waterConsumption:    
      description: 'The total amount of water that came out from the tap or taps in the compartment'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    weightStDev:    
      description: 'The standard deviation associated to the average weight of the pigs/piglets contained in the compartment'    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - lastUpdate    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Agrifood/blob/master/Compartment/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Agrifood/Compartment/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### Compartment NGSI-v2 key-values 示例  
这里是一个以JSON-LD格式作为关键值的 Compartment 的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "a88c6069-86c4-4c09-8621-fc5c58f216e0",  
  "type": "Compartment",  
  "additionalInfo": [  
    {  
      "name": "Farm2FeedTray",  
      "value": "4"  
    },  
    {  
      "name": "Farm2ValveId",  
      "value": ""  
    },  
    {  
      "name": "Farm2DepartmentId",  
      "value": "11"  
    }  
  ],  
  "arrivalTimestamp": "2020-04-14T22:00:00.000Z",  
  "avgGrowth": 1.0,  
  "avgWeight": 45.5,  
  "buildingId": "f6ce5251-e959-4269-9040-8056c6a093d9",  
  "co2": 20,  
  "companyId": "1401c9e0-c441-4bd1-b8d3-fb1194479aa7",  
  "empty": false,  
  "farmId": "7438345c-fdff-45c9-a02f-1d764cbc03a7",  
  "feedConsumption": 8.3,  
  "humidity": 0.7,  
  "lastUpdate": 1589841011000,  
  "luminosity": 3,  
  "name": "",  
  "numAnimals": 22,  
  "outputFeed": 8.2,  
  "parentCompartmentId": "f0ddd929-5a18-479b-9ad6-5947cc2cd05b",  
  "sex": "",  
  "startWeight": 26,  
  "temperature": 25,  
  "waterConsumption": 23,  
  "weightStDev": 2.3  
}  
```  
</details>  
#### Compartment NGSI-v2 normalized Example  
下面是一个以JSON-LD格式规范化的隔间的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "a88c6069-86c4-4c09-8621-fc5c58f216e0"  
  ,  
  "type": "Compartment",  
  "additionalInfo": {  
    "type": "array",  
    "value": [  
      {  
        "name": "Farm2FeedTray",  
        "value": "4"  
      },  
      {  
        "name": "Farm2ValveId",  
        "value": ""  
      },  
      {  
        "name": "Farm2DepartmentId",  
        "value": "11"  
      }  
    ]  
  },  
  "arrivalTimestamp": {  
    "type": "string",  
    "value": "2020-04-14T22:00:00.000Z"  
  },  
  "avgGrowth": {  
    "type": "number",  
    "value": 4  
  },  
  "avgWeight": {  
    "type": "number",  
    "value": 45.5  
  },  
  "buildingId": {  
    "type": "string",  
    "value": "f6ce5251-e959-4269-9040-8056c6a093d9"  
  },  
  "co2": {  
    "type": "number",  
    "value": 20  
  },  
  "companyId": {  
    "type": "string",  
    "value": "1401c9e0-c441-4bd1-b8d3-fb1194479aa7"  
  },  
  "empty": {  
    "type": "boolean",  
    "value": false  
  },  
  "farmId": {  
    "type": "string",  
    "value": "7438345c-fdff-45c9-a02f-1d764cbc03a7"  
  },  
  "feedConsumption": {  
    "type": "number",  
    "value": 8.3  
  },  
  "humidity": {  
    "type": "number",  
    "value": 0.7  
  },  
  "lastUpdate": {  
    "type": "number",  
    "value": 1589841011000  
  },  
  "luminosity": {  
    "type": "number",  
    "value": 3  
  },  
  "name": {  
    "type": "string",  
    "value": ""  
  },  
  "numAnimals": {  
    "type": "number",  
    "value": 22  
  },  
  "outputFeed": {  
    "type": "number",  
    "value": 8.2  
  },  
  "parentCompartmentId": {  
    "type": "string",  
    "value": "f0ddd929-5a18-479b-9ad6-5947cc2cd05b"  
  },  
  "sex": {  
    "type": "string",  
    "value": ""  
  },  
  "startWeight": {  
    "type": "number",  
    "value": 26  
  },  
  "temperature": {  
    "type": "number",  
    "value": 25  
  },  
  "waterConsumption": {  
    "type": "number",  
    "value": 23  
  },  
  "weightStDev": {  
    "type": "number",  
    "value": 2.3  
  }  
}  
```  
</details>  
#### Compartment NGSI-LD key-values 示例  
这里是一个以JSON-LD格式作为key-values的 Compartment的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:a88c6069-86c4-4c09-8621-fc5c58f216e0:001",  
    "type": "Compartment",  
    "additionalInfo": [  
        {  
            "name": "Farm2FeedTray",  
            "value": "4"  
        },  
        {  
            "name": "Farm2ValveId",  
            "value": ""  
        },  
        {  
            "name": "Farm2DepartmentId",  
            "value": "11"  
        }  
    ],  
    "arrivalTimestamp": "2020-04-14T22:00:00.000Z",  
    "avgGrowth": 1.0,  
    "avgWeight": 45.5,  
    "buildingId": "urn:ngsi-ld:f6ce5251-e959-4269-9040-8056c6a093d9:001",  
    "co2": 20,  
    "companyId": "urn:ngsi-ld:1401c9e0-c441-4bd1-b8d3-fb1194479aa7:002",  
    "empty": false,  
    "farmId": "urn:ngsi-ld:7438345c-fdff-45c9-a02f-1d764cbc03a7:005",  
    "feedConsumption": 8.3,  
    "humidity": 0.7,  
    "lastUpdate": 1589841011000,  
    "luminosity": 3,  
    "name": "",  
    "numAnimals": 22,  
    "outputFeed": 8.2,  
    "parentCompartmentId": "urn:ngsi-ld:f0ddd929-5a18-479b-9ad6-5947cc2cd05b:001",  
    "sex": "",  
    "startWeight": 26,  
    "temperature": 25,  
    "waterConsumption": 23,  
    "weightStDev": 2.3,  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/data-models/master/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Agrifood/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### Compartment NGSI-LD normalized Example  
下面是一个以JSON-LD格式规范化的隔间的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:a88c6069-86c4-4c09-8621-fc5c58f216e0:001",  
    "type": "Compartment",  
    "additionalInfo": {  
        "type": "array",  
        "value": [  
            {  
                "name": "Farm2FeedTray",  
                "value": "4"  
            },  
            {  
                "name": "Farm2ValveId",  
                "value": ""  
            },  
            {  
                "name": "Farm2DepartmentId",  
                "value": "11"  
            }  
        ]  
    },  
    "arrivalTimestamp": {  
        "type": "string",  
        "value": "2020-04-14T22:00:00.000Z"  
    },  
    "avgGrowth": {  
        "type": "boolean",  
        "value": true  
    },  
    "avgWeight": {  
        "type": "number",  
        "value": 45.5  
    },  
    "buildingId": {  
        "type": "string",  
        "value": "f6ce5251-e959-4269-9040-8056c6a093d9"  
    },  
    "co2": {  
        "type": "number",  
        "value": 20  
    },  
    "companyId": {  
        "type": "string",  
        "value": "urn:ngsi-ld:1401c9e0-c441-4bd1-b8d3-fb1194479aa7:007"  
    },  
    "empty": {  
        "type": "boolean",  
        "value": false  
    },  
    "farmId": {  
        "type": "string",  
        "value": "urn:ngsi-ld:7438345c-fdff-45c9-a02f-1d764cbc03a7:001"  
    },  
    "feedConsumption": {  
        "type": "number",  
        "value": 8.3  
    },  
    "humidity": {  
        "type": "number",  
        "value": 0.7  
    },  
    "lastUpdate": {  
        "type": "number",  
        "value": 1589841011000  
    },  
    "luminosity": {  
        "type": "number",  
        "value": 3  
    },  
    "name": {  
        "type": "string",  
        "value": ""  
    },  
    "numAnimals": {  
        "type": "number",  
        "value": 22  
    },  
    "outputFeed": {  
        "type": "number",  
        "value": 8.2  
    },  
    "parentCompartmentId": {  
        "type": "string",  
        "value": "urn:ngsi-ld:f0ddd929-5a18-479b-9ad6-5947cc2cd05b:001"  
    },  
    "sex": {  
        "type": "string",  
        "value": ""  
    },  
    "startWeight": {  
        "type": "number",  
        "value": 26  
    },  
    "temperature": {  
        "type": "number",  
        "value": 25  
    },  
    "waterConsumption": {  
        "type": "number",  
        "value": 23  
    },  
    "weightStDev": {  
        "type": "number",  
        "value": 2.3  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/data-models/master/context.jsonld",  
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
