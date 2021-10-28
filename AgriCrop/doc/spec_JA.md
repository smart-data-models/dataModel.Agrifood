エンティティアグリクロップ  
=============  
[オープンライセンス](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/AgriCrop/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述。**このエンティティは、一般的な作物の調和された記述を含んでいます。このエンティティは、主に農業の垂直方向と関連するIoTアプリケーションに関連付けられています。  

## プロパティのリスト  

- `agroVocConcept`: 定義されたコンセプトとAgroVocの語彙とのリンク  - `alternateName`: このアイテムの別称  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `description`: このアイテムの説明  - `harvestingInterval`: この作物の推奨収穫間隔日のリスト。ISO8601の繰り返しの日付間隔を使って指定されています。<br/><br/>**interval, description**<br/><br/>ここで**interval**は**start date/end date**<br/><br/>--MM-DD/--MM-DD<br/><br/>この開始日からこの終了日まで、毎年繰り返すことを意味します。  - `hasAgriFertiliser`: この作物の栽培に適した推奨される肥料の種類を参照。  - `hasAgriPest`: この作物を攻撃することが知られている害虫についての言及  - `hasAgriSoil`: この作物の栽培に適した推奨される土壌の種類を参照してください。  - `id`: エンティティのユニークな識別子  - `name`: このアイテムの名前です。  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `plantingFrom`: この作物の推奨植え付け間隔日のリスト。ISO8601の繰り返しの日付間隔を使って指定します。<br/><br/>**interval, description**<br/><br/>ここで**interval**は**start date/end date**<br/><br/>--MM-DD/--MM-DD<br/><br/>この開始日からこの終了日まで、毎年繰り返すことを意味します。  - `relatedSource`: 外部アプリケーションで現在のエンティティが持つ可能性のあるIDのリスト  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `type`: NGSI Entity Type. AgriCropである必要があります。  - `wateringFrequency`: 推奨される散水スケジュールの説明。列挙されたリストからの選択。以下のいずれかです。**daily、weekly、biweekly、monthly、onDemand、other**。Enum:'毎日、毎週、隔週、毎月、オンデマンド、その他'    
必須項目  
- `id`  - `name`  - `type`    
この事業体は、主に農業の縦割りと関連するIoTアプリケーションに関連しています。  
## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AgriCrop:    
  description: 'This entity contains a harmonised description of a generic crop. This entity is primarily associated with the agricultural vertical and related IoT applications.'    
  properties:    
    agroVocConcept:    
      description: 'The link with the defined concept into the AgroVoc vocabulary'    
      format: uri    
      type: string    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
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
    harvestingInterval:    
      description: 'A list of the recommended harvesting interval date(s) for this crop. Specified using ISO8601 repeating date intervals: <br/><br/>**interval, description**<br/><br/>Where **interval** is in the form of **start date/end date**<br/><br/>--MM-DD/--MM-DD<br/><br/>Meaning repeat each year from this start date to this end date.'    
      items:    
        - type: object    
          values:    
            dateRange:    
              pattern: ^-[0-1][0-9]-[0-3][0-9]/-[0-1][0-9]-[0-3][0-9]$    
              type: string    
            description:    
              type: string    
      maxItems: 2    
      minItems: 2    
      type: array    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Property    
    hasAgriFertiliser:    
      description: 'Reference to the recommended types of fertiliser suitable for growing this crop.'    
      items:    
        - anyOf:    
            - description: 'Property. Identifier format of any NGSI entity'    
              maxLength: 256    
              minLength: 1    
              pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
              type: string    
            - description: 'Property. Identifier format of any NGSI entity'    
              format: uri    
              type: string    
      type: array    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
    hasAgriPest:    
      description: 'Reference to the pests known to attack this crop'    
      items:    
        anyOf:    
          - description: 'Property. Identifier format of any NGSI entity'    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: 'Property. Identifier format of any NGSI entity'    
            format: uri    
            type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    hasAgriSoil:    
      description: 'Reference to the recommended types of soil suitable for growing this crop.'    
      items:    
        anyOf:    
          - description: 'Property. Identifier format of any NGSI entity'    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: 'Property. Identifier format of any NGSI entity'    
            format: uri    
            type: string    
      type: array    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
    id:    
      anyOf: &agricrop_-_properties_-_owner_-_items_-_anyof    
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
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *agricrop_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    plantingFrom:    
      description: 'A list of the recommended planting interval date(s) for this crop. Specified using ISO8601 repeating date intervals: <br/><br/>**interval, description**<br/><br/>Where **interval** is in the form of **start date/end date**<br/><br/>--MM-DD/--MM-DD<br/><br/>Meaning repeat each year from this start date to this end date.'    
      items:    
        - type: object    
          values:    
            dateRange:    
              pattern: ^-[0-1][0-9]-[0-3][0-9]/-[0-1][0-9]-[0-3][0-9]$    
              type: string    
            description:    
              type: string    
      maxItems: 2    
      minItems: 2    
      type: array    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Property    
    relatedSource:    
      description: 'List of IDs the current entity may have in external applications'    
      items:    
        - type: object    
          values:    
            application:    
              anyOf: *agricrop_-_properties_-_owner_-_items_-_anyof    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity Type. it has to be AgriCrop'    
      enum:    
        - AgriCrop    
      type: string    
      x-ngsi:    
        type: Property    
    wateringFrequency:    
      description: 'A description of the recommended watering schedule. A choice from an enumerated list. One of: **daily, weekly, biweekly, monthly, onDemand, other**. Enum:''daily, weekly, biweekly, monthly, onDemand,    other'''    
      enum:    
        - daily    
        - weekly    
        - biweekly    
        - monthly    
        - onDemand    
        - other    
      type: string    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Property    
        units: ""    
  required:    
    - id    
    - type    
    - name    
  type: object    
```  
</details>    
## ペイロードの例  
#### AgriCrop NGSI-v2 キー・バリューの例  
AgriCropをkey-valuesとしてJSON-LD形式で出力した例です。これは`options=keyValues`を使った場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:AgriCrop:df72dc57-1eb9-42a3-88a9-8647ecc954b4",  
  "type": "AgriCrop",  
  "dateCreated": "2017-01-01T01:20:00Z",  
  "dateModified": "2017-05-04T12:30:00Z",  
  "name": "Wheat",  
  "alternateName": "Triticum aestivum",  
  "agroVocConcept": "http://aims.fao.org/aos/agrovoc/c_7951",  
  "seeAlso": [  
    "https://example.org/concept/wheat",  
    "https://datamodel.org/example/wheat"  
  ],  
  "description": "Spring wheat",  
  "relatedSource": [  
    {  
      "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
      "applicationEntityId": "app:weat"  
    }  
  ],  
  "hasAgriSoil": [  
    "urn:ngsi-ld:AgriSoil:00411b56-bd1b-4551-96e0-a6e7fde9c840",  
    "urn:ngsi-ld:AgriSoil:e8a8389a-edf5-4345-8d2c-b98ac1ce8e2a"  
  ],  
  "hasAgriFertiliser": [  
    "urn:ngsi-ld:AgriFertiliser:1b0d6cf7-320c-4a2b-b2f1-4575ea850c73",  
    "urn:ngsi-ld:AgriFertiliser:380973c8-4d3b-4723-a899-0c0c5cc63e7e"  
  ],  
  "hasAgriPest": [  
    "urn:ngsi-ld:AgriPest:1b0d6cf7-320c-4a2b-b2f1-4575ea850c73",  
    "urn:ngsi-ld:AgriPest:380973c8-4d3b-4723-a899-0c0c5cc63e7e"  
  ],  
  "plantingFrom": [  
    {  
      "dateRange": "-09-28/-10-12",  
      "description": "Best Season"  
    },  
    {  
      "dateRange": "-10-11/-10-18",  
      "description": "Season OK"  
    }  
  ],  
  "harvestingInterval": [  
    {  
      "dateRange": "-03-21/-04-01",  
      "description": "Best Season"  
    },  
    {  
      "dateRange": "-04-02/-04-15",  
      "description": "Season OK"  
    }  
  ],  
  "wateringFrequency": "daily"  
}  
```  
#### AgriCrop NGSI-v2の正規化例  
ここでは、正規化されたJSON-LD形式のAgriCropの例を示します。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:AgriCrop:df72dc57-1eb9-42a3-88a9-8647ecc954b4",  
  "type": "AgriCrop",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2017-01-01T01:20:00Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2017-05-04T12:30:00Z"  
  },  
  "name": {  
    "value": "Wheat"  
  },  
  "alternateName": {  
    "value": "Triticum aestivum"  
  },  
  "agroVocConcept": {  
    "type": "URL",  
    "value": "http://aims.fao.org/aos/agrovoc/c_7951"  
  },  
  "seeAlso": {  
    "value": [  
      "https://example.org/concept/wheat",  
      "https://datamodel.org/example/wheat"  
    ]  
  },  
  "description": {  
    "value": "Spring wheat"  
  },  
  "relatedSource": {  
    "value": [  
      {  
        "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
        "applicationEntityId": "app:weat"  
      }  
    ]  
  },  
  "hasAgriSoil": {  
    "type": "Relationship",  
    "value": [  
      "urn:ngsi-ld:AgriSoil:00411b56-bd1b-4551-96e0-a6e7fde9c840",  
      "urn:ngsi-ld:AgriSoil:e8a8389a-edf5-4345-8d2c-b98ac1ce8e2a"  
    ]  
  },  
  "hasAgriFertiliser": {  
    "type": "Relationship",  
    "value": [  
      "urn:ngsi-ld:AgriFertiliser:1b0d6cf7-320c-4a2b-b2f1-4575ea850c73",  
      "urn:ngsi-ld:AgriFertiliser:380973c8-4d3b-4723-a899-0c0c5cc63e7e"  
    ]  
  },  
  "hasAgriPest": {  
    "type": "Relationship",  
    "value": [  
      "urn:ngsi-ld:AgriPest:1b0d6cf7-320c-4a2b-b2f1-4575ea850c73",  
      "urn:ngsi-ld:AgriPest:380973c8-4d3b-4723-a899-0c0c5cc63e7e"  
    ]  
  },  
  "plantingFrom": {  
    "value": [  
      {  
        "dateRange": "-09-28/-10-12",  
        "description": "Best Season"  
      },  
      {  
        "dateRange": "-10-11/-10-18",  
        "description": "Season OK"  
      }  
    ]  
  },  
  "harvestingInterval": {  
    "value": [  
      {  
        "dateRange": "-03-21/-04-01",  
        "description": "Best Season"  
      },  
      {  
        "dateRange": "-04-02/-04-15",  
        "description": "Season OK"  
      }  
    ]  
  },  
  "wateringFrequency": {  
    "value": "daily"  
  }  
}  
```  
#### AgriCrop NGSI-LDのキーバリューの例  
AgriCropをkey-valuesとしてJSON-LD形式で表現した例を示します。これは`options=keyValues`を使った場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:AgriCrop:df72dc57-1eb9-42a3-88a9-8647ecc954b4",  
  "type": "AgriCrop",  
  "createdAt": "2017-01-01T01:20:00Z",  
  "modifiedAt": "2017-05-04T12:30:00Z",  
  "name": {  
    "type": "Property",  
    "value": "Wheat"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Triticum aestivum"  
  },  
  "agroVocConcept": {  
    "type": "Property",  
    "value": "http://aims.fao.org/aos/agrovoc/c_7951"  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "https://example.org/concept/wheat",  
      "https://datamodel.org/example/wheat"  
    ]  
  },  
  "description": {  
    "type": "Property",  
    "value": "Spring wheat"  
  },  
  "relatedSource": {  
    "type": "Property",  
    "value": [  
      {  
        "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
        "applicationEntityId": "app:weat"  
      }  
    ]  
  },  
  "hasAgriSoil": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:AgriSoil:00411b56-bd1b-4551-96e0-a6e7fde9c840",  
      "urn:ngsi-ld:AgriSoil:e8a8389a-edf5-4345-8d2c-b98ac1ce8e2a"  
    ]  
  },  
  "hasAgriFertiliser": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:AgriFertiliser:1b0d6cf7-320c-4a2b-b2f1-4575ea850c73",  
      "urn:ngsi-ld:AgriFertiliser:380973c8-4d3b-4723-a899-0c0c5cc63e7e"  
    ]  
  },  
  "hasAgriPest": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:AgriPest:1b0d6cf7-320c-4a2b-b2f1-4575ea850c73",  
      "urn:ngsi-ld:AgriPest:380973c8-4d3b-4723-a899-0c0c5cc63e7e"  
    ]  
  },  
  "plantingFrom": {  
    "type": "Property",  
    "value": [  
      {  
        "dateRange": "-09-28/-10-12",  
        "description": "Best Season"  
      },  
      {  
        "dateRange": "-10-11/-10-18",  
        "description": "Season OK"  
      }  
    ]  
  },  
  "harvestingInterval": {  
    "type": "Property",  
    "value": [  
      {  
        "dateRange": "-03-21/-04-01",  
        "description": "Best Season"  
      },  
      {  
        "dateRange": "-04-02/-04-15",  
        "description": "Season OK"  
      }  
    ]  
  },  
  "wateringFrequency": {  
    "type": "Property",  
    "value": "daily"  
  }  
}  
```  
#### AgriCrop NGSI-LDの正規化例  
ここでは、正規化されたJSON-LD形式のAgriCropの例を示します。これは、オプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "agroVocConcept": "http://aims.fao.org/aos/agrovoc/c_7951",  
  "alternateName": "Triticum aestivum",  
  "createdAt": "2017-01-01T01:20:00Z",  
  "description": "Spring wheat",  
  "harvestingInterval": [  
    {  
      "dateRange": "-03-21/-04-01",  
      "description": "Best Season"  
    },  
    {  
      "dateRange": "-04-02/-04-15",  
      "description": "Season OK"  
    }  
  ],  
  "hasAgriFertiliser": [  
    "urn:ngsi-ld:AgriFertiliser:1b0d6cf7-320c-4a2b-b2f1-4575ea850c73",  
    "urn:ngsi-ld:AgriFertiliser:380973c8-4d3b-4723-a899-0c0c5cc63e7e"  
  ],  
  "hasAgriPest": [  
    "urn:ngsi-ld:AgriPest:1b0d6cf7-320c-4a2b-b2f1-4575ea850c73",  
    "urn:ngsi-ld:AgriPest:380973c8-4d3b-4723-a899-0c0c5cc63e7e"  
  ],  
  "hasAgriSoil": [  
    "urn:ngsi-ld:AgriSoil:00411b56-bd1b-4551-96e0-a6e7fde9c840",  
    "urn:ngsi-ld:AgriSoil:e8a8389a-edf5-4345-8d2c-b98ac1ce8e2a"  
  ],  
  "id": "urn:ngsi-ld:AgriCrop:df72dc57-1eb9-42a3-88a9-8647ecc954b4",  
  "modifiedAt": "2017-05-04T12:30:00Z",  
  "name": "Wheat",  
  "plantingFrom": [  
    {  
      "dateRange": "-09-28/-10-12",  
      "description": "Best Season"  
    },  
    {  
      "dateRange": "-10-11/-10-18",  
      "description": "Season OK"  
    }  
  ],  
  "relatedSource": [  
    {  
      "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
      "applicationEntityId": "app:weat"  
    }  
  ],  
  "seeAlso": [  
    "https://example.org/concept/wheat",  
    "https://datamodel.org/example/wheat"  
  ],  
  "type": "AgriCrop",  
  "wateringFrequency": "daily"  
}  
```  
