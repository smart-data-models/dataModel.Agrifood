<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
エンティティアグリグリーンハウス    
================<!-- /10-Header -->    
<!-- 15-License -->    
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/AgriGreenhouse/LICENSE.md)    
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
グローバルな記述：**このエンティティには、AgriParcel の一種である一般的な温室内に記録された条件の調和された記述が含まれる。    
バージョン: 0.0.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## プロパティのリスト    
<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。    
- `alternateName[string]`: この項目の別名  - `belongsTo[*]`: 温室が属する団体  - `co2[number]`: 測定された室内C02濃度（単位：mg/L  . Model: [http://schema.org/Number](http://schema.org/Number)- `dailyLight[number]`: 毎日の積算光量（単位：kW/平方メートル  . Model: [http://schema.org/Number](http://schema.org/Number)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `drainFlow[object]`: 観測された排水流量（リットル毎秒  . Model: [http://schema.org/Number](http://schema.org/Number)	- `maxValue`:       
	- `minValue`:       
	- `unitText`:       
- `hasAgriParcelChildren[array]`: このエンティティに関連するサブAgriParcelレコード  - `hasAgriParcelParent[*]`: このエンティティが関連するAgriParcelエンティティへの参照  - `hasDevice[array]`: この温室に関連するIoTデバイス（センサー、制御装置など）への言及  . Model: [http://schema.org/URL](http://schema.org/URL)- `hasWaterQualityObserved[array]`: この事業体について現在行われている1つ以上の水質観測記録への言及  - `hasWeatherObserved[*]`: このエンティティの現在の気象観測記録への参照  - `id[*]`: エンティティの一意識別子  - `leafTemperature[number]`: 葉の平均温度（公称摂氏温度  . Model: [http://schema.org/Number](http://schema.org/Number)- `name[string]`: このアイテムの名前  - `ownedBy[*]`: アグリ温室の所有者（個人または団体  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `relatedSource[array]`: 現在のエンティティが外部アプリケーションで持つ可能性のあるIDのリスト  - `relativeHumidity[number]`: 内部の相対湿度を0～100（%）の範囲で0～1の数値で表します。<br/><br/>0 <= relativeHumidity <= 1  . Model: [http://schema.org/Number](http://schema.org/Number)- `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `type[string]`: NGSI事業体タイプ。AgriGreenhouseでなければならない。  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
必須プロパティ    
- `hasAgriParcelParent`  - `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
この企業は主に農業分野と関連するIoTアプリケーションに関連している。    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## プロパティのデータモデル記述    
アルファベット順（クリックで詳細表示）    
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
        type: Relationship      
    hasAgriParcelParent:      
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
      description: Reference to the AgriParcel entity to which this entity relates      
      x-ngsi:      
        type: Relationship      
    hasDevice:      
      description: 'Reference to the IoT devices associated with this greenhouse i.e. sensors, controls'      
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
    hasWaterQualityObserved:      
      description: Reference to one or more water quality observation records current for this entity      
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
        type: Relationship      
    hasWeatherObserved:      
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
      description: Reference to the weather observation record current for this entity      
      x-ngsi:      
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
    leafTemperature:      
      description: The average leaf temperature nominally in degrees centigrade      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
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
      description: Owner (Person or Organization) of the AgriGreenhouse      
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
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
## ペイロードの例    
#### AgriGreenhouse NGSI-v2 キー値の例    
JSON-LD形式のAgriGreenhouseのkey-valuesの例です。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると個々のエンティティのコンテキストデータを返す。    
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
#### AgriGreenhouse NGSI-v2 正規化例    
以下は、正規化されたJSON-LD形式のAgriGreenhouseの例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。    
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
    "type": "Text",  
    "value": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c"  
  },  
  "relatedSource": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
        "applicationEntityId": "app:greenhouse1"  
      }  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "https://example.org/concept/agrigreenhouse",  
      "https://datamodel.org/example/agrigreenhouse"  
    ]  
  },  
  "belongsTo": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:AgriFarm:f67adcbc-4479-22bc-9de1-cb228de7a765"  
  },  
  "hasAgriParcelParent": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:AgriParcel:c8b475e5-84a8-4346-ad79-cde1d2a4028b"  
  },  
  "hasAgriParcelChildren": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:AgriParcel:8c3a525d-b42e-4048-bcdd-a119d8ddb0a5",  
      "urn:ngsi-ld:AgriParcel:178d74c1-e6fe-4042-b955-2c164fc90b83"  
    ]  
  },  
  "hasWeatherObserved": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:WeatherObserved:c720cec5-ac6f-40b7-8e89-becb75702d0d"  
  },  
  "hasWaterQualityObserved": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:WaterQualityObserved:49f86e0b-bb90-4751-a1c3-d5a891920807",  
      "urn:ngsi-ld:WaterQualityObserved:853bf420-43fc-11e8-942f-6b7615517118"  
    ]  
  },  
  "relativeHumidity": {  
    "type": "Number",  
    "value": 0.4  
  },  
  "leafTemperature": {  
    "type": "Number",  
    "value": 22  
  },  
  "co2": {  
    "type": "Number",  
    "value": 28  
  },  
  "dailyLight": {  
    "type": "Number",  
    "value": 24  
  },  
  "drainFlow": {  
    "type": "StructuredValue",  
    "value": {  
      "value": 33,  
      "maxValue": 50,  
      "minValue": 25,  
      "unitText": "Litre per second"  
    }  
  },  
  "hasDevice": {  
    "type": "StructuredValue",  
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
#### AgriGreenhouse NGSI-LD キー値の例    
JSON-LD形式のAgriGreenhouseのkey-valuesの例です。options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。    
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
#### AgriGreenhouse NGSI-LD 正規化例    
以下は、正規化されたJSON-LD形式のAgriGreenhouseの例である。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。    
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
