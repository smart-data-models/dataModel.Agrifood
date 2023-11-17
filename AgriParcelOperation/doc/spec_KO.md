<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entity: AgriParcelOperation    
===========================<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/AgriParcelOperation/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **이 엔티티에는 한 필지의 토지에서 수행되는 일반적인 작업에 대한 조화로운 설명이 포함되어 있습니다. 이 엔티티는 주로 농업 업종 및 관련 IoT 애플리케이션과 연관되어 있습니다.**    
버전: 0.0.3    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 속성 목록    
<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.    
- `alternateName[string]`: 이 항목의 대체 이름  - `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `endedAt[date-time]`: 작업이 실제로 완료된 타임스탬프  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `hasAgriParcel[*]`: 아그리파셀 참조  - `hasAgriProductType[*]`: 사용/적용된 농산품 유형에 대한 참조  - `hasOperator[*]`: 작업을 수행하는 운영자에 대한 참조  - `id[*]`: 엔티티의 고유 식별자  - `irrigationRecord[uri]`: 실행의 관개 기록과의 관계  . Model: [http://schema.org/URL](http://schema.org/URL)- `name[string]`: 이 항목의 이름  - `operationType[string]`: 소포에서 수행된 작업을 설명하는 열거형 목록에서 선택합니다. 열거형: '비료, 검사, 살충제, 물, 기타'  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `plannedEndAt[date-time]`: 작업의 예정된 종료 날짜/타임스탬프입니다. <br/><br/>이 값은 권고 사항이며 실제 작업 종료 시간은 계획된 종료 시간 이전 또는 이후일 수 있습니다.  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `plannedStartAt[date-time]`: 작업의 예정된 시작 날짜/타임스탬프입니다. 이는 권고 사항이며 실제 작업 시작 시간은 계획된 시작 시간 이전 또는 이후일 수 있습니다.  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `quantity[number]`: 사용/도포한 물 또는 제품의 총 양입니다. 액체의 경우 리터, 고체의 경우 킬로그램 단위로 측정하는 것이 좋습니다.  . Model: [http://schema.org/Number](http://schema.org/Number)- `relatedSource[array]`: 현재 엔터티가 외부 애플리케이션에서 가질 수 있는 ID 목록  - `reportedAt[date-time]`: 이벤트 오류가 보고된 타임스탬프  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `result[string]`: 작업 결과에 대한 설명입니다. Enum:'확인, 중단, 실패'  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `startedAt[date-time]`: 작업이 실제로 수행되기 시작한 타임스탬프  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `status[string]`: 상태를 설명하는 열거형 목록에서 선택합니다. 열거형: '계획됨, 진행 중, 완료됨, 예약됨, 취소됨'  - `type[string]`: NGSI 엔티티 유형. AgriParcelOperation이어야 합니다.  - `waterSource[string]`: 수원 유형. 열거형: '시추공, 강우, 하천, 빗물 포집, 수력 댐, 상업용 공급'  . Model: [http://schema.org/Text](http://schema.org/Text)- `workOrder[uri]`: 실행을 위한 작업 주문과의 관계  . Model: [http://schema.org/URL](http://schema.org/URL)- `workRecord[uri]`: 실행 작업 기록과의 관계  . Model: [http://schema.org/URL](http://schema.org/URL)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
필수 속성    
- `hasAgriParcel`  - `id`  - `plannedEndAt`  - `plannedStartAt`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
이 법인은 주로 농업 분야 및 관련 IoT 애플리케이션과 관련이 있습니다.    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 속성에 대한 데이터 모델 설명    
알파벳순으로 정렬(자세한 내용을 보려면 클릭)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
AgriParcelOperation:      
  description: This entity contains a harmonised description of a generic operations performed on a parcel of land. This entity is primarily associated with the agricultural vertical and related IoT applications.      
  properties:      
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
    endedAt:      
      description: Timestamp when the operation actually finished      
      format: date-time      
      type: string      
      x-ngsi:      
        model: http://schema.org/DateTime      
        type: Property      
    hasAgriParcel:      
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
      description: Reference to the AgriParcel      
      x-ngsi:      
        type: Relationship      
    hasAgriProductType:      
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
      description: Reference to the AgriProductType used/applied      
      x-ngsi:      
        type: Relationship      
    hasOperator:      
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
      description: Reference to the operator conducting the operation      
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
    irrigationRecord:      
      description: Relationship with the irrigation record of the execution      
      format: uri      
      type: string      
      x-ngsi:      
        model: http://schema.org/URL      
        type: Relationship      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    operationType:      
      description: 'A choice from an enumerated list describing the operation performed on the parcel. Enum:''fertiliser, inspection, pesticide, water, other'''      
      enum:      
        - fertiliser      
        - inspection      
        - pesticide      
        - water      
        - other      
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
    plannedEndAt:      
      description: The planned end date/timestamp for the operation. <br/><br/>Note that this is advisory and the actual time the operation finishes may be before or after the planned end      
      format: date-time      
      type: string      
      x-ngsi:      
        model: http://schema.org/DateTime      
        type: Property      
    plannedStartAt:      
      description: The planned start date/timestamp for the operation. Note that this is advisory and the actual time the operation starts may be before or after the planned start      
      format: date-time      
      type: string      
      x-ngsi:      
        model: http://schema.org/DateTime      
        type: Property      
    quantity:      
      description: The total quantity of water or product used/ applied. It is recommended this is measured in litres for liquids or kilogrammes for solids      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
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
    reportedAt:      
      description: Timestamp when the event fault was reported      
      format: date-time      
      type: string      
      x-ngsi:      
        model: http://schema.org/DateTime      
        type: Property      
    result:      
      description: 'A description of the results of the operation. Enum:''ok, aborted, failed'''      
      enum:      
        - ok      
        - aborted      
        - failed      
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
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    startedAt:      
      description: Timestamp when the operation actually started to be performed      
      format: date-time      
      type: string      
      x-ngsi:      
        model: http://schema.org/DateTime      
        type: Property      
    status:      
      description: 'A choice from an enumerated list describing the status. Enum:''planned, ongoing, finished, scheduled, cancelled'''      
      enum:      
        - planned      
        - ongoing      
        - finished      
        - scheduled      
        - cancelled      
      type: string      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI Entity Type. It has to be AgriParcelOperation      
      enum:      
        - AgriParcelOperation      
      type: string      
      x-ngsi:      
        type: Property      
    waterSource:      
      description: 'Type of water sources. Enum:''borehole, rainfall, river, rainwater capture, water dam, commercial supply'''      
      enum:      
        - borehole      
        - rainfall      
        - river      
        - rainwater capture      
        - water dam      
        - commercial supply      
      type: string      
      x-ngsi:      
        model: http://schema.org/Text      
        type: Property      
    workOrder:      
      description: Relationship with the workorder for the execution      
      format: uri      
      type: string      
      x-ngsi:      
        model: http://schema.org/URL      
        type: Relationship      
    workRecord:      
      description: Relationship with the work record of the execution      
      format: uri      
      type: string      
      x-ngsi:      
        model: http://schema.org/URL      
        type: Relationship      
  required:      
    - id      
    - type      
    - hasAgriParcel      
    - plannedStartAt      
    - plannedEndAt      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Agrifood/blob/master/AgriParcelOperation/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.Agrifood/AgriParcelOperation/schema.json      
  x-model-tags: ""      
  x-version: 0.0.3      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 페이로드 예시    
#### AgriParcelOperation NGSI-v2 키값 예시    
다음은 키-값으로 JSON-LD 형식의 AgriParcelOperation의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AgriParcelOperation:e1e9d3a3-074f-46f1-9375-52000d05a62b",  
  "type": "AgriParcelOperation",  
  "dateCreated": "2017-01-01T01:20:00Z",  
  "dateModified": "2017-05-04T12:30:00Z",  
  "relatedSource": [  
    {  
      "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
      "applicationEntityId": "app:parcelop1"  
    }  
  ],  
  "seeAlso": [  
    "https://example.org/concept/agriparcelop",  
    "https://datamodel.org/example/agriparcelop"  
  ],  
  "hasAgriParcel": "urn:ngsi-ld:AgriParcel:318366a9-7643-4d8e-9a11-c76a8c29d8eb",  
  "operationType": "fertiliser",  
  "description": "Monthly fertiliser application",  
  "result": "ok",  
  "plannedStartAt": "2016-08-22T10:18:16Z",  
  "plannedEndAt": "2016-08-28T10:18:16Z",  
  "status": "finished",  
  "hasOperator": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c",  
  "startedAt": "2016-08-22T10:18:16Z",  
  "endedAt": "2016-08-28T10:18:16Z",  
  "reportedAt": "2016-08-28T10:18:16Z",  
  "hasAgriProductType": "urn:ngsi-ld:AgriProductType:a8f616b8-13fb-473a-8e61-b7a80c6c93ec",  
  "quantity": 40,  
  "waterSource": "rainwater capture",  
  "workOrder": "https://example.com/agriparcelrecords/workorder1",  
  "workRecord": "https://example.com/agriparcelrecords/workrecord1",  
  "irrigationRecord": "https://example.com/agriparcelrecords/irrigationrecord1"  
}  
```  
</details>    
#### AgriParcelOperation NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 AgriParcelOperation의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AgriParcelOperation:e1e9d3a3-074f-46f1-9375-52000d05a62b",  
  "type": "AgriParcelOperation",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2017-01-01T01:20:00Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2017-05-04T12:30:00Z"  
  },  
  "relatedSource": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
        "applicationEntityId": "app:parcelop1"  
      }  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "https://example.org/concept/agriparcelop",  
      "https://datamodel.org/example/agriparcelop"  
    ]  
  },  
  "hasAgriParcel": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:AgriParcel:318366a9-7643-4d8e-9a11-c76a8c29d8eb"  
  },  
  "operationType": {  
    "type": "Text",  
    "value": "fertiliser"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Monthly fertiliser application"  
  },  
  "result": {  
    "type": "Text",  
    "value": "ok"  
  },  
  "plannedStartAt": {  
    "type": "DateTime",  
    "value": "2016-08-22T10:18:16Z"  
  },  
  "plannedEndAt": {  
    "type": "DateTime",  
    "value": "2016-08-28T10:18:16Z"  
  },  
  "status": {  
    "type": "Text",  
    "value": "finished"  
  },  
  "hasOperator": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c"  
  },  
  "startedAt": {  
    "type": "DateTime",  
    "value": "2016-08-22T10:18:16Z"  
  },  
  "endedAt": {  
    "type": "DateTime",  
    "value": "2016-08-28T10:18:16Z"  
  },  
  "reportedAt": {  
    "type": "DateTime",  
    "value": "2016-08-28T10:18:16Z"  
  },  
  "hasAgriProductType": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:AgriProductType:a8f616b8-13fb-473a-8e61-b7a80c6c93ec"  
  },  
  "quantity": {  
    "type": "Number",  
    "value": 40  
  },  
  "waterSource": {  
    "type": "Text",  
    "value": "rainwater capture"  
  },  
  "workOrder": {  
    "type": "Text",  
    "value": "https://example.com/agriparcelrecords/workorder1"  
  },  
  "workRecord": {  
    "type": "Text",  
    "value": "https://example.com/agriparcelrecords/workrecord1"  
  },  
  "irrigationRecord": {  
    "type": "Text",  
    "value": "https://example.com/agriparcelrecords/irrigationrecord1"  
  }  
}  
```  
</details>    
#### AgriParcelOperation NGSI-LD 키 값 예시    
다음은 키-값으로 JSON-LD 형식의 AgriParcelOperation의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AgriParcelOperation:e1e9d3a3-074f-46f1-9375-52000d05a62b",  
  "type": "AgriParcelOperation",  
  "createdAt": "2017-01-01T01:20:00Z",  
  "description": "Monthly fertiliser application",  
  "endedAt": "2016-08-22T10:18:16Z",  
  "hasAgriParcel": "urn:ngsi-ld:AgriParcel:318366a9-7643-4d8e-9a11-c76a8c29d8eb",  
  "hasAgriProductType": "urn:ngsi-ld:AgriProductType:a8f616b8-13fb-473a-8e61-b7a80c6c93ec",  
  "hasOperator": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c",  
  "irrigationRecord": "https://example.com/agriparcelrecords/irrigationrecord1",  
  "modifiedAt": "2017-05-04T12:30:00Z",  
  "operationType": "fertiliser",  
  "plannedEndAt": "2016-08-22T10:18:16Z",  
  "plannedStartAt": "2016-08-22T10:18:16Z",  
  "quantity": 40,  
  "relatedSource": [  
    {  
      "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
      "applicationEntityId": "app:parcelop1"  
    }  
  ],  
  "reportedAt": "2016-08-22T10:18:16Z",  
  "result": "ok",  
  "seeAlso": [  
    "https://example.org/concept/agriparcelop",  
    "https://datamodel.org/example/agriparcelop"  
  ],  
  "startedAt": "2016-08-22T10:18:16Z",  
  "status": "finished",  
  "waterSource": "rainwater capture",  
  "workOrder": "https://example.com/agriparcelrecords/workorder1",  
  "workRecord": "https://example.com/agriparcelrecords/workrecord1",  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Agrifood/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### AgriParcelOperation NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 AgriParcelOperation의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:AgriParcelOperation:e1e9d3a3-074f-46f1-9375-52000d05a62b",  
    "type": "AgriParcelOperation",  
    "createdAt": "2017-01-01T01:20:00Z",  
    "description": {  
        "type": "Property",  
        "value": "Monthly fertiliser application"  
    },  
    "endedAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-08-22T10:18:16Z"  
        }  
    },  
    "hasAgriParcel": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:AgriParcel:318366a9-7643-4d8e-9a11-c76a8c29d8eb"  
    },  
    "hasAgriProductType": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:AgriProductType:a8f616b8-13fb-473a-8e61-b7a80c6c93ec"  
    },  
    "hasOperator": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c"  
    },  
    "irrigationRecord": {  
        "type": "Property",  
        "value": "https://example.com/agriparcelrecords/irrigationrecord1"  
    },  
    "modifiedAt": "2017-05-04T12:30:00Z",  
    "operationType": {  
        "type": "Property",  
        "value": "fertiliser"  
    },  
    "plannedEndAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-08-22T10:18:16Z"  
        }  
    },  
    "plannedStartAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-08-22T10:18:16Z"  
        }  
    },  
    "quantity": {  
        "type": "Property",  
        "value": 40,  
        "unitCode": "KGM"  
    },  
    "relatedSource": {  
        "type": "Property",  
        "value": [  
            {  
                "application": "urn:ngsi-ld:AgriApp:72d9fb43-53f8-4ec8-a33c-fa931360259a",  
                "applicationEntityId": "app:parcelop1"  
            }  
        ]  
    },  
    "reportedAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-08-22T10:18:16Z"  
        }  
    },  
    "result": {  
        "type": "Property",  
        "value": "ok"  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": [  
            "https://example.org/concept/agriparcelop",  
            "https://datamodel.org/example/agriparcelop"  
        ]  
    },  
    "startedAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-08-22T10:18:16Z"  
        }  
    },  
    "status": {  
        "type": "Property",  
        "value": "finished"  
    },  
    "waterSource": {  
        "type": "Property",  
        "value": "rainwater capture"  
    },  
    "workOrder": {  
        "type": "Property",  
        "value": "https://example.com/agriparcelrecords/workorder1"  
    },  
    "workRecord": {  
        "type": "Property",  
        "value": "https://example.com/agriparcelrecords/workrecord1"  
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
