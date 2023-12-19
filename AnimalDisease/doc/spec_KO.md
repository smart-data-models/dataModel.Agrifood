<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: 동물 질병    
==========<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/AnimalDisease/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **가축 농장의 동물 질병을 모델링하는 오브젝트입니다.**    
버전: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 속성 목록    
<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.    
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.      
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호      
- `alternateName[string]`: 이 항목의 대체 이름  - `animals[array]`: 질병 진단을 받은 동물 또는 동물 목록. 모델 https://github.com/smart-data-models/dataModel.Agrifood/blob/master/Animal/schema.json  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `date[date-time]`: 수의사가 질병을 진단한 날짜  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `diagnosticTest[string]`: 수의사가 질병을 판별하기 위해 동물에게 실시한 진단 검사  - `disease[string]`: 동물 질병. 수의사가 진단한 동물의 질병을 나타냅니다. 스페인 질병 출처 https://www.mapa.gob.es/es/ganaderia/temas/sanidad-animal-higiene-ganadera/sanidad-animal/enfermedades/  - `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `type[string]`: NGSI 엔티티 유형입니다. 동물 질병이어야 합니다.  - `veterinarian[uri]`: 진단 수의사. 처방 수의사와의 관계  - `veterinarianTreatment[uri]`: 질병을 치료하기 위해 수의사가 진단한 치료. https://github.com/smart-data-models/dataModel.Agrifood/blob/master/VeterinarianTreatment/schema.json  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
필수 속성    
- `disease`  - `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 속성에 대한 데이터 모델 설명    
알파벳순으로 정렬(자세한 내용을 보려면 클릭)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
AnimalDisease:      
  description: Object modelling an animal disease for a livestock farm.      
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
    animals:      
      description: 'Animals or list of animals diagnosed with the disease. Model https://github.com/smart-data-models/dataModel.Agrifood/blob/master/Animal/schema.json'      
      items:      
        format: uri      
        type: string      
      type: array      
      x-ngsi:      
        type: Relationship      
    areaServed:      
      description: The geographic area where a service or offered item is provided      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    date:      
      description: Date of diagnosis of the disease by a veterinarian      
      format: date-time      
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
    diagnosticTest:      
      description: Diagnostic test performed in the animals for the determination of the disease by a veterinarian      
      type: string      
      x-ngsi:      
        type: Property      
    disease:      
      description: 'Animal disease. Indicates the disease the animal has as diagnosed by a veterinarian. Spanish source of diseases https://www.mapa.gob.es/es/ganaderia/temas/sanidad-animal-higiene-ganadera/sanidad-animal/enfermedades/'      
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
      description: NGSI entity type. It has to be AnimalDisease      
      enum:      
        - AnimalDisease      
      type: string      
      x-ngsi:      
        type: Property      
    veterinarian:      
      description: Diagnostic veterinarian. Relationship to the prescribing veterinarian      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    veterinarianTreatment:      
      description: 'Medical treatment diagnosed by the veterinarian to treat the disease. https://github.com/smart-data-models/dataModel.Agrifood/blob/master/VeterinarianTreatment/schema.json'      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
  required:      
    - id      
    - type      
    - disease      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Agrifood/blob/master/AnimalDisease/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.Agrifood/AnimalDisease/schema.json      
  x-model-tags: I4Trust      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 페이로드 예시    
#### 동물 질병 NGSI-v2 키 값 예시    
다음은 키 값으로 JSON-LD 형식의 AnimalDisease의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AnimalDisease:ca3f1295-500c-4aa3-b745-d143097d5c01",  
  "type": "AnimalDisease",  
  "disease": "Lameness",  
  "diagnosticTest": "Visual inspection",  
  "date": "2022-01-01T01:20:00Z",  
  "animals": [  
    "urn:ngsi-ld:Animal:ca3f1295-500c-4aa3-b745-d143097d5c01",  
    "urn:ngsi-ld:Animal:bb3f1295-500c-4aa3-b745-d143097d4321"  
  ],  
  "veterinarianTreatment": "urn:ngsi-ld:VeterinarianTreatment:ca3f1295-500c-4aa3-b745-d143097d5c65",  
  "veterinarian": "urn:ngsi-ld:Veterinarian:ca3f1295-500c-4aa3-b745-d143097d5d11"  
}  
```  
</details>    
#### AnimalDisease NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 AnimalDisease 예제입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AnimalDisease:ca3f1295-500c-4aa3-b745-d143097d5c01",  
  "type": "AnimalDisease",  
  "disease": {  
    "type": "Text",  
    "value": "Lameness"  
  },  
  "diagnosticTest": {  
    "type": "Text",  
    "value": "Visual inspection"  
  },  
  "date": {  
    "type": "DateTime",  
    "value": "2022-01-01T01:20:00Z"  
  },  
  "animals": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Animal:ca3f1295-500c-4aa3-b745-d143097d5c01",  
      "urn:ngsi-ld:Animal:bb3f1295-500c-4aa3-b745-d143097d4321"  
    ]  
  },  
  "veterinarianTreatment": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VeterinarianTreatment:ca3f1295-500c-4aa3-b745-d143097d5c65"  
  },  
  "veterinarian": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Veterinarian:ca3f1295-500c-4aa3-b745-d143097d5d11"  
  }  
}  
```  
</details>    
#### 동물 질병 NGSI-LD 키 값 예시    
다음은 키 값으로 JSON-LD 형식의 AnimalDisease의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AnimalDisease:ca3f1295-500c-4aa3-b745-d143097d5c01",  
  "type": "AnimalDisease",  
  "disease": "Lameness",  
  "diagnosticTest": "Visual inspection",  
  "date": "2022-01-01T01:20:00Z",  
  "animals": [  
    "urn:ngsi-ld:Animal:ca3f1295-500c-4aa3-b745-d143097d5c01",  
    "urn:ngsi-ld:Animal:bb3f1295-500c-4aa3-b745-d143097d4321"  
  ],  
  "veterinarianTreatment": "urn:ngsi-ld:VeterinarianTreatment:ca3f1295-500c-4aa3-b745-d143097d5c65",  
  "veterinarian": "urn:ngsi-ld:Veterinarian:ca3f1295-500c-4aa3-b745-d143097d5d11",  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.Agrifood/context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Agrifood/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### AnimalDisease NGSI-LD 정규화 예시    
다음은 정규화된 JSON-LD 형식의 AnimalDisease 예제입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:AnimalDisease:ca3f1295-500c-4aa3-b745-d143097d5c01",  
    "type": "AnimalDisease",  
    "disease": {  
        "type": "Property",  
        "value": "Lameness"  
    },  
    "diagnosticTest": {  
        "type": "Property",  
        "value": "Visual inspection"  
    },  
    "date": {  
        "type": "Property",  
        "value": {  
            "@type": "Date-Time",  
            "@value": "2022-01-01T01:20:00Z"  
        }  
    },  
    "animals": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:Animal:ca3f1295-500c-4aa3-b745-d143097d5c01",  
            "urn:ngsi-ld:Animal:bb3f1295-500c-4aa3-b745-d143097d4321"  
        ]  
    },  
    "veterinarianTreatment": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:VeterinarianTreatment:ca3f1295-500c-4aa3-b745-d143097d5c65"  
    },  
    "veterinarian": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Veterinarian:ca3f1295-500c-4aa3-b745-d143097d5d11"  
    },  
    "@context": [  
        "https://smart-data-models.github.io/dataModel.Agrifood/context.jsonld",  
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
