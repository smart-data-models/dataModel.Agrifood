<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。钢笔  
=====<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/Pen/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述。**建筑或部门内或外部的围栏区域，容纳一群动物。围栏中的动物可以自由移动和互动。圈舍之间往往没有完全隔开（半墙、铁栏、栅栏......），使得相邻圈舍的动物有可能看到/接触到**。  
版本：0.2.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `additionalInfo[array]`: 由传感器/平台发送的所有原始值的列表，包括所有可能的、不包括在主结构中的额外属性。它是一个类似于这样的JSON结构。{'name': 'temperature', 'value' : 32}。  - `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `arrivalTimestamp[string]`: 动物到达围栏的日期和时间  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `avgGrowth[number]`: 本栏内动物的平均体重增长情况  . Model: [https://schema.org/Number](https://schema.org/Number)- `avgWeight[number]`: 本栏中动物的平均体重。  . Model: [https://schema.org/Number](https://schema.org/Number)- `buildingId[*]`: 项目所在大楼的唯一标识符  . Model: [https://schema.org/URL.](https://schema.org/URL.)- `co2[number]`: 项目中的二氧化碳浓度  . Model: [https://schema.org/Number](https://schema.org/Number)- `companyId[*]`: 公司的唯一标识符  . Model: [https://schema.org/URL](https://schema.org/URL)- `compartmentId[*]`: 钢笔所处隔间的唯一标识。  . Model: [https://schema.org/URL](https://schema.org/URL)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `deadAnimalsSinceDateOfArrival[number]`: 自抵达之日起，死亡动物的数量  . Model: [https://schema.org/Number](https://schema.org/Number)- `description[string]`: 对这个项目的描述  - `farmId[*]`: 笔者所在农场的唯一标识符。  . Model: [https://schema.org/URL](https://schema.org/URL)- `feedConsumption[number]`: 从围栏中的喂食站吃到的食物总量。它是通过进食量和特定结构来衡量的，每次只让一只动物进食。  . Model: [https://schema.org/Number](https://schema.org/Number)- `humidity[number]`: 代表笔者在大气中的水蒸气量的数量。  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: 实体的唯一标识符  - `lastUpdate[string]`: 项目中测量的日期和时间  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `luminosity[number]`: 某一波长的光源在物品上的亮度  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: 这个项目的名称。  - `numAnimals[number]`: 围栏中的动物数量。  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `relatedSource[array]`: 当前实体在外部应用程序中可能拥有的ID列表  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `sex[string]`: 栏内所含动物的性别  . Model: [https://schema.org/Number](https://schema.org/Number)- `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `temperature[number]`: 笔的温度。  Unirs:' 摄氏度  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI实体类型。它必须是Pen  - `waterConsumption[number]`: 从栏内的水龙头或水龙头流出的水的总量。它是通过流量计和特定结构来测量的，每次只让一只动物喝。  . Model: [https://schema.org/Number](https://schema.org/Number)- `weightStDev[number]`: 与栏内动物的平均重量有关的标准偏差。  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
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
Pen:    
  description: 'Fenced area in a building or department or outside housing a group of animals. Animals in a pen can move and interact freely. Pens are often not completely separated from each other (half walls, iron bars, fences,…), making it possible that animals from neighbouring pens can see/touch'    
  properties:    
    additionalInfo:    
      description: 'list of all the raw values sent by the sensor/platform with all the possible extra properties that are not included in the main structure. It is a JSON structure similar to this: {''name'': ''temperature'', ''value'' : 32}'    
      items:    
        properties:    
          name:    
            type: string    
          value:    
            anyOf:    
              - type: string    
              - type: number    
              - type: boolean    
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
      description: 'Date and Time for the arrival of animals to the Pen'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    avgGrowth:    
      description: 'The average growth in weight of the animal in this pen'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    avgWeight:    
      description: 'The average weight of the animal in this Pen. '    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Kg    
    buildingId:    
      anyOf:    
        - description: 'Property. Identifier with format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity.'    
          format: uri    
          type: string    
      description: 'Unique identifier of the Building the item is located in'    
      x-ngsi:    
        model: https://schema.org/URL.    
        type: Relationship    
    co2:    
      description: 'The CO2 concentration in the item'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
        model: https://schema.org/URL    
        type: Relationship    
    compartmentId:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the Compartment the Pen is located in.'    
      x-ngsi:    
        model: https://schema.org/URL    
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
    deadAnimalsSinceDateOfArrival:    
      description: 'Number of dead animals since the date of arrival'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
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
      description: 'Unique identifier of the Farm the Pen is located in.'    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    feedConsumption:    
      description: 'The total amount of food that has been eaten from the feeding station(s) in the pen.It is measured through feed intakes and specific structure to let only one animal at a time to eat'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Kg    
    humidity:    
      description: 'Quantity representing the amount of water vapour in the atmosphere in the pen. '    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &pen_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Date and time at which the measurements in the item were taken'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
        units: Seconds    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
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
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
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
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
        type: Geoproperty    
    luminosity:    
      description: 'The brightness of a light source of a certain wavelength at the item'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: LUX    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    numAnimals:    
      description: 'Number of animals contained in the Pen.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *pen_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    relatedSource:    
      description: 'List of IDs the current entity may have in external applications'    
      items:    
        - type: object    
          values:    
            application:    
              anyOf: *pen_-_properties_-_owner_-_items_-_anyof    
              description: 'Property. Unique identifier of the entity'    
            applicationEntityId:    
              type: string    
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
      description: 'The sex of the animals contained in the pen'    
      enum:    
        - M    
        - F    
        - unknown    
        - ""    
      type: string    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    temperature:    
      description: 'Temperature of the Pen.  Unirs:'' Celsius degree'''    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI Entity type. it has to be Pen'    
      enum:    
        - Pen    
      type: string    
      x-ngsi:    
        type: Property    
    waterConsumption:    
      description: 'The total amount of water that came out from the tap or taps in the pen. It is measured through flowmeters and specific structure to let only one animal at a time drink.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    weightStDev:    
      description: 'The standard deviation associated to the average weight of the animals contained in the Pen.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required:    
    - id    
    - type    
    - lastUpdate    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Agrifood/blob/master/Pen/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Agrifood/Pen/schema.json    
  x-model-tags: ""    
  x-version: 0.2.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### Pen NGSI-v2关键值示例  
这里有一个JSON-LD格式的Pen作为key-values的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "e24b1aa9-d9bf-4f50-8583-3d51ade41588",  
  "type": "Pen",  
  "additionalInfo": [  
    {  
      "name": "Farm1FeedTray",  
      "value": 1  
    },  
    {  
      "name": "Farm1DepartmentId",  
      "value": "43"  
    },  
    {  
      "name": "Farm1ValveId",  
      "value": "69"  
    },  
    {  
      "name": "Farm1PenId",  
      "value": "1"  
    },  
    {  
      "name": "Farm1BuildingId",  
      "value": "2"  
    }  
  ],  
  "buildingId": "5ee3dbc8-343b-40a7-ac04-dec67215ff98",  
  "companyId": "4579b77f-31c1-44ef-b200-9a2407cc82e9",  
  "compartmentId": "ab8680c6-3e82-40fb-8577-f6a0ab717586",  
  "empty": false,  
  "farmId": "3b6473e3-fdc9-4646-b1cf-d41e3af58eff",  
  "lastUpdate": "2020-04-12T20:44:55",  
  "sex": "",  
  "temperature": 25  
}  
```  
</details>  
#### 笔NGSI-v2正常化的例子  
这里有一个JSON-LD格式的笔的例子，是规范化的。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "e24b1aa9-d9bf-4f50-8583-3d51ade41588",  
  "type": "pen",  
  "additionalInfo": {  
    "type": "array",  
    "value": [  
      {  
        "name": "Farm1FeedTray",  
        "value": 1  
      },  
      {  
        "name": "Farm1DepartmentId",  
        "value": "43"  
      },  
      {  
        "name": "Farm1ValveId",  
        "value": "69"  
      },  
      {  
        "name": "Farm1PenId",  
        "value": "1"  
      },  
      {  
        "name": "Farm1BuildingId",  
        "value": "2"  
      }  
    ]  
  },  
  "buildingId": {  
    "type": "string",  
    "value": "5ee3dbc8-343b-40a7-ac04-dec67215ff98"  
  },  
  "companyId": {  
    "type": "string",  
    "value": "4579b77f-31c1-44ef-b200-9a2407cc82e9"  
  },  
  "compartmentId": {  
    "type": "string",  
    "value": "ab8680c6-3e82-40fb-8577-f6a0ab717586"  
  },  
  "empty": {  
    "type": "boolean",  
    "value": "false"  
  },  
  "farmId": {  
    "type": "string",  
    "value": "3b6473e3-fdc9-4646-b1cf-d41e3af58eff"  
  },  
  "lastUpdate": {  
    "type": "string",  
    "value": "2020-04-12T20:44:55"  
  },  
  "sex": {  
    "type": "string",  
    "value": ""  
  },  
  "temperature": {  
    "type": "number",  
    "value": 25  
  }  
}  
```  
</details>  
#### 笔NGSI-LD关键值示例  
这里有一个JSON-LD格式的Pen作为key-values的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "e24b1aa9-d9bf-4f50-8583-3d51ade41588",  
    "type": "Pen",  
    "additionalInfo": [  
        {  
            "name": "Farm1FeedTray",  
            "value": 1  
        },  
        {  
            "name": "Farm1DepartmentId",  
            "value": "43"  
        },  
        {  
            "name": "Farm1ValveId",  
            "value": "69"  
        },  
        {  
            "name": "Farm1PenId",  
            "value": "1"  
        },  
        {  
            "name": "Farm1BuildingId",  
            "value": "2"  
        }  
    ],  
    "buildingId": "5ee3dbc8-343b-40a7-ac04-dec67215ff98",  
    "companyId": "4579b77f-31c1-44ef-b200-9a2407cc82e9",  
    "compartmentId": "ab8680c6-3e82-40fb-8577-f6a0ab717586",  
    "empty": false,  
    "farmId": "3b6473e3-fdc9-4646-b1cf-d41e3af58eff",  
    "lastUpdate": "2020-04-12T20:44:55",  
    "sex": "",  
    "temperature": 25,  
    "@context": [  
        "https://smart-data-models.github.io/data-models/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Agrifood/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### 笔NGSI-LD正常化的例子  
这里有一个JSON-LD格式的笔的例子，是规范化的。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "e24b1aa9-d9bf-4f50-8583-3d51ade41588",  
    "type": "Pen",  
    "additionalInfo": {  
        "type": "array",  
        "value": [  
            {  
                "name": "Farm1FeedTray",  
                "value": 1  
            },  
            {  
                "name": "Farm1DepartmentId",  
                "value": "43"  
            },  
            {  
                "name": "Farm1ValveId",  
                "value": "69"  
            },  
            {  
                "name": "Farm1PenId",  
                "value": "1"  
            },  
            {  
                "name": "Farm1BuildingId",  
                "value": "2"  
            }  
        ]  
    },  
    "buildingId": {  
        "type": "string",  
        "value": "5ee3dbc8-343b-40a7-ac04-dec67215ff98"  
    },  
    "companyId": {  
        "type": "string",  
        "value": "4579b77f-31c1-44ef-b200-9a2407cc82e9"  
    },  
    "compartmentId": {  
        "type": "string",  
        "value": "ab8680c6-3e82-40fb-8577-f6a0ab717586"  
    },  
    "empty": {  
        "type": "boolean",  
        "value": "false"  
    },  
    "farmId": {  
        "type": "string",  
        "value": "3b6473e3-fdc9-4646-b1cf-d41e3af58eff"  
    },  
    "lastUpdate": {  
        "type": "string",  
        "value": "2020-04-12T20:44:55"  
    },  
    "sex": {  
        "type": "string",  
        "value": ""  
    },  
    "temperature": {  
        "type": "number",  
        "value": 25  
    },  
    "@context": [  
        "https://smart-data-models.github.io/data-models/context.jsonld",  
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
