<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
エンティティ動物    
========<!-- /10-Header -->    
<!-- 15-License -->    
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/Animal/LICENSE.md)    
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
グローバルな記述：**ある場所と時間における動物の状態の観察。このデータモデルは UCO と SensoWave が IoF2020 UC ShareBeef のために開発したものである。    
バージョン: 0.0.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## プロパティのリスト    
<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。    
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。      
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `birthdate[date-time]`: 動物の生年月日  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `breed[string]`: 動物の品種  - `calvedBy[*]`: 動物の母  - `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `fedWith[*]`: 動物に使用する食料  - `healthCondition[string]`: 動物のフェノロジーの状態。Enum:' 健康, 病気, 治療中'.  - `id[*]`: エンティティの一意識別子  - `legalId[string]`: 動物の法的ID  - `locatedAt[*]`: AgriParcelの関係  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `ownedBy[*]`: 動物の飼い主  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `phenologicalCondition[string]`: 動物のフェノロジーの状態。Enum:'lactatingBaby, grazingBaby, maleAdult, femaleAdult, maleYoung, femaleYoung'.  - `relatedSource[array]`: 現在のエンティティが外部アプリケーションで持つ可能性のあるIDのリスト  - `reproductiveCondition[string]`: 動物の生殖状態。Enum:'noStatus, inactive, inCalf, inHeat, active'.  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `sex[string]`: 動物の性別。Enum:'male, female'  - `siredBy[*]`: 動物の父  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `species[string]`: その動物が属する種。この列挙型は増やすことができる。  . Model: [Enum:cow, goat, horse, pig, sheep, dairy cattle, beef cattle· https://schema.org/Text](Enum:cow, goat, horse, pig, sheep, dairy cattle, beef cattle· https://schema.org/Text)- `type[string]`: NGSIエンティティタイプ：動物でなければならない  - `weight[number]`: 動物の体重を数値で表す  . Model: [http://schema.org/Number](http://schema.org/Number)- `welfareCondition[string]`: 動物福祉の指標。Enum:'issue, adequate'  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
必須プロパティ    
- `id`  - `legalId`  - `sex`  - `species`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
提案された動物データモデルは、より一般的な観点から作成され、UCで使用される機器やセンサーから得られる情報に適応するよう試みられている。次の図は牛肉チェーンについて記述したものである。この図では、食肉チェーンのさまざまな利害関係者が、その相互作用の一部と同様に説明されている。![](../resources/diagram1.jpg)。このデータモデルを使用する際には、提案するソリューションで生成される情報を扱うために、いくつかのエンティティを定義する必要がある。これらすべてのエンティティの中で、このソリューションの中心となる動物のエンティティがまず目立つ。    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## プロパティのデータモデル記述    
アルファベット順（クリックで詳細表示）    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
Animal:      
  description: An observation of animal conditions at a certain place and time. This data model has been developed for the IoF2020 UC ShareBeef by UCO and SensoWave.      
  properties:      
    address:      
      description: The mailing address      
      properties:      
        addressCountry:      
          description: 'The country. For example, Spain'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressCountry      
            type: Property      
        addressLocality:      
          description: 'The locality in which the street address is, and which is in the region'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressLocality      
            type: Property      
        addressRegion:      
          description: 'The region in which the locality is, and which is in the country'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressRegion      
            type: Property      
        district:      
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'      
          type: string      
          x-ngsi:      
            type: Property      
        postOfficeBoxNumber:      
          description: 'The post office box number for PO box addresses. For example, 03578'      
          type: string      
          x-ngsi:      
            model: https://schema.org/postOfficeBoxNumber      
            type: Property      
        postalCode:      
          description: 'The postal code. For example, 24004'      
          type: string      
          x-ngsi:      
            model: https://schema.org/https://schema.org/postalCode      
            type: Property      
        streetAddress:      
          description: The street address      
          type: string      
          x-ngsi:      
            model: https://schema.org/streetAddress      
            type: Property      
        streetNr:      
          description: Number identifying a specific property on a public street      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/address      
        type: Property      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    areaServed:      
      description: The geographic area where a service or offered item is provided      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    birthdate:      
      description: Animal's birthdate      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    breed:      
      description: Breed of the animal      
      type: string      
      x-ngsi:      
        type: Property      
    calvedBy:      
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
      description: Mother of the animal      
      x-ngsi:      
        type: Relationship      
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
    fedWith:      
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
      description: Food used for the animal      
      x-ngsi:      
        type: Relationship      
    healthCondition:      
      description: 'Phenological condition of the animal. Enum:'' healthy, sick, inTreatment'''      
      enum:      
        - healthy      
        - inTreatment      
        - sick      
      type: string      
      x-ngsi:      
        type: Property      
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
    legalId:      
      description: Legal ID of the animal      
      type: string      
      x-ngsi:      
        type: Property      
    locatedAt:      
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
      description: Id of the AgriParcel relationship      
      x-ngsi:      
        type: Relationship      
    location:      
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
      oneOf:      
        - description: Geojson reference to the item. Point      
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
          title: GeoJSON Point      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. LineString      
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
          title: GeoJSON LineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. Polygon      
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
          title: GeoJSON Polygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiPoint      
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
          title: GeoJSON MultiPoint      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
          title: GeoJSON MultiLineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
          title: GeoJSON MultiPolygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
      x-ngsi:      
        type: GeoProperty      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    ownedBy:      
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
      description: The owner of the animal      
      x-ngsi:      
        type: Relationship      
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
    phenologicalCondition:      
      description: 'Phenological condition of the animal. Enum:''lactatingBaby, grazingBaby, maleAdult, femaleAdult, maleYoung, femaleYoung'''      
      enum:      
        - femaleAdult      
        - femaleYoung      
        - grazingBaby      
        - lactatingBaby      
        - maleAdult      
        - maleYoung      
      type: string      
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
    reproductiveCondition:      
      description: 'Reproductive condition of the animal. Enum:''noStatus, inactive, inCalf, inHeat, active'''      
      enum:      
        - active      
        - inactive      
        - inCalf      
        - inHeat      
        - noStatus      
      type: string      
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
    sex:      
      description: 'Sex of the animal. Enum:''male, female'''      
      enum:      
        - female      
        - male      
      type: string      
      x-ngsi:      
        type: Property      
    siredBy:      
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
      description: Father of the animal      
      x-ngsi:      
        type: Relationship      
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    species:      
      description: Species to which the animal belongs. This enum can be increased      
      enum:      
        - beef cattle      
        - cow      
        - dairy cattle      
        - goat      
        - horse      
        - pig      
        - sheep      
      type: string      
      x-ngsi:      
        model: 'Enum:cow, goat, horse, pig, sheep, dairy cattle, beef cattle· https://schema.org/Text'      
        type: Property      
    type:      
      description: 'NGSI Entity Type: It has to be Animal'      
      enum:      
        - Animal      
      type: string      
      x-ngsi:      
        type: Property      
    weight:      
      description: The weight of the animal as a number      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Relationship      
        units: kg      
    welfareCondition:      
      description: 'Indicator of the animal welfare. Enum:''issue, adequate'''      
      enum:      
        - issue      
        - adequate      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
    - species      
    - legalId      
    - sex      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Agrifood/blob/master/Animal/LICENSE.md      
  x-model-schema: ""      
  x-model-tags: ""      
  x-version: 0.0.2      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## ペイロードの例    
#### 動物 NGSI-v2 キー値の例    
以下は、JSON-LD形式のAnimalをkey-valuesとした例である。options=keyValues`を使うとNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返す。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Animal:ca3f1295-500c-4aa3-b745-d143097d5c01",  
  "type": "Animal",  
  "species": "sheep",  
  "relatedSource": [  
    {  
      "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
      "applicationEntityId": "app:sheep1"  
    }  
  ],  
  "legalId": "ES142589652140",  
  "birthdate": "2017-01-01T01:20:00Z",  
  "dateModified": "2017-05-04T12:30:00Z",  
  "sex": "female",  
  "breed": "Merina",  
  "calvedBy": "urn:ngsi-ld:Animal:aa9f1295-425c-8ba3-b745-b653097d5a87",  
  "siredBy": "urn:ngsi-ld:Animal:aa9f1295-425c-8ba3-b745-b653097d5a87",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -4.754444444,  
      41.640833333  
    ]  
  },  
  "weight": 65.3,  
  "ownedBy": "http://person.org/leon",  
  "locatedAt": "urn:ngsi-ld:AgriParcel:1ea0f120-4474-11e8-9919-672036642081",  
  "phenologicalCondition": "maleAdult",  
  "reproductiveCondition": "inCalf",  
  "healthCondition": "healthy",  
  "fedWith": "urn:ngsi-ld:FEED:1ea0f120-4474-11e8-9919-0000000081",  
  "welfareCondition": "adequate"  
}  
```  
</details>    
#### 動物 NGSI-v2 正規化例    
以下は、正規化されたJSON-LD形式のAnimalの例である。これはNGSI-v2と互換性があり、オプションを使用しない場合、個々のエンティティのコンテキストデータを返します。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Animal:ca3f1295-500c-4aa3-b745-d143097d5c01",  
  "type": "Animal",  
  "species": {  
    "type": "Text",  
    "value": "sheep"  
  },  
  "relatedSource": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
        "applicationEntityId": "app:sheep1"  
      }  
    ]  
  },  
  "legalId": {  
    "type": "Text",  
    "value": "ES142589652140"  
  },  
  "birthdate": {  
    "type": "DateTime",  
    "value": "2017-01-01T01:20:00Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2017-05-04T12:30:00Z"  
  },  
  "sex": {  
    "type": "Text",  
    "value": "female"  
  },  
  "breed": {  
    "type": "Text",  
    "value": "Merina"  
  },  
  "calvedBy": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Animal:aa9f1295-425c-8ba3-b745-b653097d5a87"  
  },  
  "siredBy": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Animal:aa9f1295-425c-8ba3-b745-b653097d5a87"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -4.754444444,  
        41.640833333  
      ]  
    }  
  },  
  "weight": {  
    "type": "Number",  
    "value": 65.3  
  },  
  "ownedBy": {  
    "type": "Text",  
    "value": "http://person.org/leon"  
  },  
  "locatedAt": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:AgriParcel:1ea0f120-4474-11e8-9919-672036642081"  
  },  
  "phenologicalCondition": {  
    "type": "Text",  
    "value": "maleAdult"  
  },  
  "reproductiveCondition": {  
    "type": "Text",  
    "value": "inCalf"  
  },  
  "healthCondition": {  
    "type": "Text",  
    "value": "healthy"  
  },  
  "fedWith": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:FEED:1ea0f120-4474-11e8-9919-0000000081"  
  },  
  "welfareCondition": {  
    "type": "Text",  
    "value": "adequate"  
  }  
}  
```  
</details>    
#### 動物 NGSI-LD キー値の例    
JSON-LD形式のAnimalをkey-valuesとした例である。options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Animal:ca3f1295-500c-4aa3-b745-d143097d5c01",  
  "type": "Animal",  
  "birthdate": "2017-01-01T01:20:00Z",  
  "breed": "Merina",  
  "calvedBy": "urn:ngsi-ld:Animal:aa9f1295-425c-8ba3-b745-b653097d5a87",  
  "fedWith": "urn:ngsi-ld:FEED:1ea0f120-4474-11e8-9919-0000000081",  
  "healthCondition": "healthy",  
  "legalId": "ES142589652140",  
  "locatedAt": "urn:ngsi-ld:AgriParcel:1ea0f120-4474-11e8-9919-672036642081",  
  "location": {  
    "coordinates": [  
      -4.754444444,  
      41.640833333  
    ],  
    "type": "Point"  
  },  
  "modifiedAt": "2017-05-04T12:30:00Z",  
  "ownedBy": "http://person.org/leon",  
  "phenologicalCondition": "maleAdult",  
  "relatedSource": [  
    {  
      "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
      "applicationEntityId": "app:sheep1"  
    }  
  ],  
  "reproductiveCondition": "inCalf",  
  "sex": "female",  
  "siredBy": "urn:ngsi-ld:Animal:aa9f1295-425c-8ba3-b745-b653097d5a87",  
  "species": "sheep",  
  "weight": 65.3,  
  "welfareCondition": "adequate",  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Agrifood/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### 動物 NGSI-LD 正規化例    
以下は、正規化された JSON-LD 形式の Animal の例である。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Animal:ca3f1295-500c-4aa3-b745-d143097d5c01",  
  "type": "Animal",  
  "birthdate": {  
      "type": "Property",  
      "value": {  
          "@type": "DateTime",  
          "@value": "2017-01-01T01:20:00Z"  
      }  
  },  
  "breed": {  
      "type": "Property",  
      "value": "Merina"  
  },  
  "calvedBy": {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:Animal:aa9f1295-425c-8ba3-b745-b653097d5a87"  
  },  
  "fedWith": {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:FEED:1ea0f120-4474-11e8-9919-0000000081"  
  },  
  "healthCondition": {  
      "type": "Property",  
      "value": "healthy"  
  },  
  "legalId": {  
      "type": "Property",  
      "value": "ES142589652140"  
  },  
  "locatedAt": {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:AgriParcel:1ea0f120-4474-11e8-9919-672036642081"  
  },  
  "location": {  
      "type": "GeoProperty",  
      "value": {  
          "type": "Point",  
          "coordinates": [  
              -4.754444444,  
              41.640833333  
          ]  
      }  
  },  
  "modifiedAt": "2017-05-04T12:30:00Z",  
  "ownedBy": {  
      "type": "Relationship",  
      "object": "http://person.org/leon"  
  },  
  "phenologicalCondition": {  
      "type": "Property",  
      "value": "maleAdult"  
  },  
  "relatedSource": {  
      "type": "Property",  
      "value": [  
          {  
              "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
              "applicationEntityId": "app:sheep1"  
          }  
      ]  
  },  
  "reproductiveCondition": {  
      "type": "Property",  
      "value": "inCalf"  
  },  
  "sex": {  
      "type": "Property",  
      "value": "female"  
  },  
  "siredBy": {  
      "type": "Relationship",  
      "object": "urn:ngsi-ld:Animal:aa9f1295-425c-8ba3-b745-b653097d5a87"  
  },  
  "species": {  
      "type": "Property",  
      "value": "sheep"  
  },  
  "weight": {  
      "type": "Property",  
      "value": 65.3  
  },  
  "welfareCondition": {  
      "type": "Property",  
      "value": "adequate"  
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
