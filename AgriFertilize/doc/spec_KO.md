<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: 엔티티: 농업 비료  
==================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/AgriFertilize/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **농경지 비료화 엔티티에 대한 스키마. 비료를 준다는 것은 고체 동물성 폐기물이나 화학 혼합물을 땅에 뿌려 식물이 잘 자랄 수 있도록 토질을 개선하는 것을 의미합니다**.  
버전: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역 내 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `bill[string]`: 송장 또는 배송 메모 번호  - `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `detail[string]`: 관리되는 비료에 대한 사용자 참고 사항  - `dose[number]`: 투여된 비료 용량  - `enddate[string]`: 비료 처리의 최종 날짜. 이 필드는 비워 둘 수 있습니다.  - `id[*]`: 엔티티의 고유 식별자  - `idcp[array]`: 캠페인에서 비료가 적용된 크롭시그팩의 ID  - `inidate[string]`: 수정 과정의 시작 날짜  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인스트링, 다각형, 멀티포인트, 멀티라인스트링 또는 멀티폴리곤일 수 있습니다.  - `machine[array]`: 비료 적용에 할당된 기계에 대한 정보와 비료의 위생에 대한 정보  - `maf[object]`: 비료 살포 방법에 대한 정보  	- `id[string]`: 비료 적용 모드의 식별자    
	- `name[string]`: 비료 적용 모드 이름    
	- `type[string]`: 비료 적용 모드 유형    
- `measure[object]`: 조치의 세부 사항  	- `code[number]`: 조치에 할당된 부처 코드    
	- `detail[string]`: 측정에 대한 참고 사항    
	- `id[string]`: 측정값의 식별자    
	- `name[string]`: 측정값에 할당된 이름    
	- `prior[string]`: 측정값의 중요도 수준입니다. 사용 가능한 값은 0(우선순위)에서 10(우선순위 낮음) 사이입니다.    
	- `symbol[string]`: 측정값에 할당된 기호    
	- `type[string]`: 측정값 유형    
- `msoup[object]`: 투여된 최종 국물 양에 사용된 측정 정보  	- `code[number]`: 최종 투여된 국물의 양에 사용된 측정값 코드    
	- `detail[string]`: 수프 세부 정보    
	- `id[string]`: msoup의 식별자    
	- `name[string]`: 투여된 최종 국물 양에 사용된 측정값의 이름    
	- `prior[string]`: 최종 수액 투여량에 사용된 측정값에 대한 사전 세부 정보    
	- `symbol[string]`: 최종 투여된 국물의 양에 사용된 측정값의 기호    
	- `type[string]`: 투여된 최종 육수의 양에 사용된 측정 유형    
- `mud[number]`: 하수 슬러지 신청 문서 사용 여부를 나타냅니다.  - `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `plan[string]`: 캠페인에 포함된 구독자 요금제에 대한 정보  - `r10[string]`: 폐기물 승인 번호 R10. 폐기물을 토지에 적용하여 토양을 처리하는 것은 R1001로 코드화된 복구 작업으로 간주됩니다. 잔류물은 농업에 이익을 주거나 농업의 생태적 개선을 목적으로만 농업 토양에 적용되어야 합니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `soup[number]`: 최종 수프 투여량  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `subtype[object]`: 농작물 비료화 엔티티의 하위 유형 세부 정보  	- `aacm[array]`: 하위 유형과 관련된 aacm 객체의 배열, 비료 유형의 아미노산에 대한 정보입니다.    
	- `check[number]`: 하위 유형과 관련된 값 확인    
	- `code[string]`: 하위 유형 코드    
	- `comp[object]`: 하위 유형과 관련된 회사의 세부 정보    
	- `hecm[array]`: 하위 유형, 비료 유형의 정보 중금속과 관련된 hecm 객체의 배열입니다.    
	- `id[number]`: 하위 유형의 식별자    
	- `macm[array]`: 하위 유형과 관련된 macm 객체의 배열, 비료 유형의 다른 다량 영양소에 대한 정보입니다.    
	- `manure[string]`: 분뇨 세부 정보(있는 경우)    
	- `matdet[string]`: 머티리얼 비료 디테일(있는 경우)    
	- `material[object]`: 하위 유형과 연관된 머티리얼 세부 정보    
	- `metadata[array]`: 하위 유형과 연관된 메타데이터 객체 배열    
	- `micm[array]`: 하위 유형과 관련된 미량 개체의 배열, 비료 유형의 미량 영양소에 대한 정보    
	- `mmcm[array]`: 하위 유형과 연관된 mmcm 객체 배열    
	- `name[string]`: 사용된 비료의 유형 및 시비 코드와 연결된 비료의 이름    
	- `notes[string]`: 하위 유형과 관련된 참고 사항    
	- `subcode[string]`: 하위 유형의 하위 코드    
	- `symbol[string]`: 하위 유형의 기호    
- `taf[object]`: 비료 사용 유형에 대한 정보  	- `id[string]`: TAF의 식별자    
	- `name[string]`: 비료 신청 유형 이름    
	- `type[string]`: 비료 적용 유형 유형    
- `target[string]`: 농작물 비료화 엔티티의 대상 세부 정보  - `tmi[object]`: 억제 분자의 유형에 대한 정보  	- `id[string]`: 억제 분자 유형 식별자    
	- `name[string]`: 억제 분자의 유형 이름    
	- `type[string]`: 억제 분자의 종류 유형    
- `type[string]`: NGSI 엔티티 유형. 농업 비료여야 합니다.  - `typsoil[string]`: 농작물 비료화 엔티티와 관련된 토양 유형  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AgriFertilize:    
  description: 'Schema for AgriFertilize entity. To fertilize land means to improve its quality in order to make plants grow well on it, by spreading solid animal waste or a chemical mixture on it'    
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
    bill:    
      description: Invoice or delivery note number    
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
    detail:    
      description: User notes on administered fertilizer    
      type: string    
      x-ngsi:    
        type: Property    
    dose:    
      description: Fertilizer dose administered    
      type: number    
      x-ngsi:    
        type: Property    
    enddate:    
      description: Final date of fertilizer process. This field can be empty    
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
        type: Relationship    
    idcp:    
      description: IDs of the CropSigpac on which the fertilizer is applied in the campaign    
      items:    
        description: Every element of the array of IDs of the CropSigpac on which the fertilizer is applied    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    inidate:    
      description: The start date of the fertilization process    
      type: string    
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
    machine:    
      description: Information on the machinery assigned to the application of the fertilizer as well as information on its hygiene    
      items:    
        description: Every element in the array of machines used    
        properties:    
          detail:    
            description: This field contains the value associated to the machine    
            type: string    
            x-ngsi:    
              type: Property    
          id:    
            description: Identifier unique of the machine    
            type: string    
            x-ngsi:    
              type: Property    
          idmachine:    
            description: This field contains the value associated to the internal id    
            type: string    
            x-ngsi:    
              type: Property    
          product:    
            description: This field contains the value associated to the product that the machine applies    
            type: string    
            x-ngsi:    
              type: Property    
          type:    
            description: This field contains the type of machine    
            type: string    
            x-ngsi:    
              type: Property    
        type: object    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    maf:    
      description: Information on fertilizer application methods    
      properties:    
        id:    
          description: Identifier of fertilizer application mode    
          type: string    
          x-ngsi:    
            type: Property    
        name:    
          description: Name of fertilizer application mode    
          type: string    
          x-ngsi:    
            type: Property    
        type:    
          description: Type of fertilizer application mode    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    measure:    
      description: Details of the measure    
      properties:    
        code:    
          description: Ministry code assigned to the measure    
          type: number    
          x-ngsi:    
            type: Property    
        detail:    
          description: Notes about the measurement    
          type: string    
          x-ngsi:    
            type: Property    
        id:    
          description: Identifier of the measure    
          type: string    
          x-ngsi:    
            type: Property    
        name:    
          description: Name assigned to the measure    
          type: string    
          x-ngsi:    
            type: Property    
        prior:    
          description: Level of importance of the measure. Available values are between 0 (priority) and 10 (least priority)    
          type: string    
          x-ngsi:    
            type: Property    
        symbol:    
          description: Symbol assigned to the measure    
          type: string    
          x-ngsi:    
            type: Property    
        type:    
          description: Type of the measure    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    msoup:    
      description: Information on the measurement used for the final amount of broth administered    
      properties:    
        code:    
          description: Code of the measure used for the final amount of broth administered    
          type: number    
          x-ngsi:    
            type: Property    
        detail:    
          description: Details of the msoup    
          type: string    
          x-ngsi:    
            type: Property    
        id:    
          description: Identifier of the msoup    
          type: string    
          x-ngsi:    
            type: Property    
        name:    
          description: Name of the measure used for the final amount of broth administered    
          type: string    
          x-ngsi:    
            type: Property    
        prior:    
          description: Prior details of the measure used for the final amount of broth administered    
          type: string    
          x-ngsi:    
            type: Property    
        symbol:    
          description: Symbol of the measure used for the final amount of broth administered    
          type: string    
          x-ngsi:    
            type: Property    
        type:    
          description: Type of the measure used for the final amount of broth administered    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    mud:    
      description: Indicates whether sewage sludge application document has been used or not    
      type: number    
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
          type: Relationship    
      type: array    
      x-ngsi:    
        type: Property    
    plan:    
      description: Information about the subscriber plans that are part of the campaign    
      type: string    
      x-ngsi:    
        type: Property    
    r10:    
      description: Waste authorisation number R10. The treatment of soil by applying waste to the land is considered a recovery operation coded as R1001. Residues must be applied to agricultural soils exclusively for the purpose of producing a benefit to agriculture or an ecological improvement of the same    
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
    soup:    
      description: Final soup amount administered    
      type: number    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    subtype:    
      description: Subtype details of the AgriFertilize entity    
      properties:    
        aacm:    
          description: 'Array of aacm objects associated with the subtype, information on amino acids of the fertilizer type'    
          items:    
            description: 'Every element of the accm '    
            properties:    
              id:    
                description: Identifier of aacm    
                type: number    
                x-ngsi:    
                  type: Property    
              subtype:    
                description: Subtype details of aacm    
                properties:    
                  code:    
                    description: Code of the aacm subtype    
                    type: number    
                    x-ngsi:    
                      type: Property    
                  id:    
                    description: Identifier of the aacm subtype    
                    type: number    
                    x-ngsi:    
                      type: Property    
                  name:    
                    description: Name of the amino acids of the fertilizer type    
                    type: string    
                    x-ngsi:    
                      type: Property    
                  subtype:    
                    description: Nested subtype details of aacm    
                    properties:    
                      id:    
                        description: Identifier of the nested aacm subtype    
                        type: number    
                        x-ngsi:    
                          type: Property    
                      name:    
                        description: Name of the nested aacm subtype    
                        type: string    
                        x-ngsi:    
                          type: Property    
                      type:    
                        description: Type of the nested aacm subtype    
                        type: string    
                        x-ngsi:    
                          type: Property    
                    type: object    
                    x-ngsi:    
                      type: Property    
                  symbol:    
                    description: Symbol of the aacm subtype    
                    type: string    
                    x-ngsi:    
                      type: Property    
                  type:    
                    description: Type of the aacm subtype    
                    type: string    
                    x-ngsi:    
                      type: Property    
                type: object    
                x-ngsi:    
                  type: Property    
              type:    
                description: 'This field contains the type associated to the aacm, information on amino acids of the fertilizer type'    
                type: string    
                x-ngsi:    
                  type: Property    
              value:    
                description: This field contains the value associated to the aacm    
                type: number    
                x-ngsi:    
                  type: Property    
            type: object    
            x-ngsi:    
              type: Property    
          type: array    
          x-ngsi:    
            type: Property    
        check:    
          description: Check value associated with the subtype    
          type: number    
          x-ngsi:    
            type: Property    
        code:    
          description: Code of the subtype    
          type: string    
          x-ngsi:    
            type: Property    
        comp:    
          description: Details of the company associated with the subtype    
          properties:    
            id:    
              description: Identifier of the company    
              type: number    
              x-ngsi:    
                type: Property    
            name:    
              description: Name of the company that owns the fertilizer    
              type: string    
              x-ngsi:    
                type: Property    
            type:    
              description: Type of the company    
              type: string    
              x-ngsi:    
                type: Property    
            vat:    
              description: VAT of the company that owns the fertilizer    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        hecm:    
          description: 'Array of hecm objects associated with the subtype, information heavy metals of the fertilizer type'    
          items:    
            description: Every element of the hecm array    
            properties:    
              id:    
                description: Identifier of hecm    
                type: number    
                x-ngsi:    
                  type: Property    
              subtype:    
                description: Subtype details of hecm    
                properties:    
                  code:    
                    description: Code of the hecm subtype    
                    type: number    
                    x-ngsi:    
                      type: Property    
                  id:    
                    description: Identifier of the hecm subtype    
                    type: number    
                    x-ngsi:    
                      type: Property    
                  name:    
                    description: Name of the heavy metals of the fertilizer type    
                    type: string    
                    x-ngsi:    
                      type: Property    
                  subtype:    
                    description: Nested subtype details of hecm    
                    properties:    
                      id:    
                        description: Identifier of the nested hecm subtype    
                        type: number    
                        x-ngsi:    
                          type: Property    
                      name:    
                        description: Name of the nested hecm subtype    
                        type: string    
                        x-ngsi:    
                          type: Property    
                      type:    
                        description: Type of the nested hecm subtype    
                        type: string    
                        x-ngsi:    
                          type: Property    
                    type: object    
                    x-ngsi:    
                      type: Property    
                  symbol:    
                    description: Symbol of the hecm subtype    
                    type: string    
                    x-ngsi:    
                      type: Property    
                  type:    
                    description: Type of the hecm subtype    
                    type: string    
                    x-ngsi:    
                      type: Property    
                type: object    
                x-ngsi:    
                  type: Property    
              type:    
                description: 'This field contains the type associated to the hecm, information on heavy metals of the fertilizer type'    
                type: string    
                x-ngsi:    
                  type: Property    
              value:    
                description: This field contains the value associated to the hecm    
                type: number    
                x-ngsi:    
                  type: Property    
            type: object    
            x-ngsi:    
              type: Property    
          type: array    
          x-ngsi:    
            type: Property    
        id:    
          description: Identifier of the subtype    
          type: number    
          x-ngsi:    
            type: Property    
        macm:    
          description: 'Array of macm objects associated with the subtype, information on other macronutrients of the fertilizer type'    
          items:    
            description: The individual objects inside the macm    
            properties:    
              id:    
                description: Identifier of macm    
                type: number    
                x-ngsi:    
                  type: Property    
              subtype:    
                description: Subtype details of macm    
                properties:    
                  code:    
                    description: Code of the macm subtype    
                    type: number    
                    x-ngsi:    
                      type: Property    
                  id:    
                    description: Identifier of the macm subtype    
                    type: number    
                    x-ngsi:    
                      type: Property    
                  name:    
                    description: Name of the other macronutrients of the fertilizer type    
                    type: string    
                    x-ngsi:    
                      type: Property    
                  subtype:    
                    description: Nested subtype details of macm    
                    properties:    
                      id:    
                        description: Identifier of the nested macm subtype    
                        type: number    
                        x-ngsi:    
                          type: Property    
                      name:    
                        description: Name of the nested macm subtype    
                        type: string    
                        x-ngsi:    
                          type: Property    
                      type:    
                        description: Type of the nested macm subtype    
                        type: string    
                        x-ngsi:    
                          type: Property    
                    type: object    
                    x-ngsi:    
                      type: Property    
                  symbol:    
                    description: Symbol of the macm subtype    
                    type: string    
                    x-ngsi:    
                      type: Property    
                  type:    
                    description: Type of the macm subtype    
                    type: string    
                    x-ngsi:    
                      type: Property    
                type: object    
                x-ngsi:    
                  type: Property    
              type:    
                description: 'This field contains the type associated to the macm, information on other macronutrients of the fertilizer type'    
                type: string    
                x-ngsi:    
                  type: Property    
              value:    
                description: This field contains the value associated to the macm    
                type: number    
                x-ngsi:    
                  type: Property    
            type: object    
            x-ngsi:    
              type: Property    
          type: array    
          x-ngsi:    
            type: Property    
        manure:    
          description: 'Manure details, if any'    
          type: string    
          x-ngsi:    
            type: Property    
        matdet:    
          description: 'Material fertilize detail, if any'    
          type: string    
          x-ngsi:    
            type: Property    
        material:    
          description: Material details associated with the subtype    
          properties:    
            id:    
              description: Identifier of the material    
              type: number    
              x-ngsi:    
                type: Property    
            name:    
              description: Name of the material that uses compost or fertilizer    
              type: string    
              x-ngsi:    
                type: Property    
            type:    
              description: Type of the material that uses compost or fertilizer    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        metadata:    
          description: Array of metadata objects associated with the subtype    
          items:    
            description: Every group of elements in the metadata    
            properties:    
              date:    
                description: Date associated with the metadata    
                format: date-time    
                type: string    
                x-ngsi:    
                  type: Property    
              type:    
                description: Type of metadata    
                type: string    
                x-ngsi:    
                  type: Property    
              user:    
                description: User details associated with the metadata    
                properties:    
                  email:    
                    description: Email of the user    
                    type: string    
                    x-ngsi:    
                      type: Property    
                  id:    
                    description: Identifier of the user    
                    type: string    
                    x-ngsi:    
                      type: Property    
                  loginname:    
                    description: Login name of the user    
                    type: string    
                    x-ngsi:    
                      type: Property    
                  name:    
                    description: Name of the user in the system    
                    type: string    
                    x-ngsi:    
                      type: Property    
                  surname:    
                    description: Surname of the user    
                    type: string    
                    x-ngsi:    
                      type: Property    
                  type:    
                    description: Type of the user    
                    type: string    
                    x-ngsi:    
                      type: Property    
                  vat:    
                    description: VAT (identification number) of the user    
                    type: string    
                    x-ngsi:    
                      type: Property    
                type: object    
                x-ngsi:    
                  type: Property    
            type: object    
            x-ngsi:    
              type: Property    
          type: array    
          x-ngsi:    
            type: Property    
        micm:    
          description: 'Array of micm objects associated with the subtype, information on micronutrients of the type of fertilizer'    
          items:    
            description: Every element of the micm    
            properties:    
              id:    
                description: Identifier of micm    
                type: number    
                x-ngsi:    
                  type: Property    
              subtype:    
                description: Subtype details of micm    
                properties:    
                  code:    
                    description: Code of the micm subtype    
                    type: number    
                    x-ngsi:    
                      type: Property    
                  id:    
                    description: Identifier of the micm subtype    
                    type: number    
                    x-ngsi:    
                      type: Property    
                  name:    
                    description: Name of the micronutrients of the type of fertilizer    
                    type: string    
                    x-ngsi:    
                      type: Property    
                  subtype:    
                    description: Nested subtype details of micm    
                    properties:    
                      id:    
                        description: Identifier of the nested micm subtype    
                        type: number    
                        x-ngsi:    
                          type: Property    
                      name:    
                        description: Name of the nested micm subtype    
                        type: string    
                        x-ngsi:    
                          type: Property    
                      type:    
                        description: Type of the nested micm subtype    
                        type: string    
                        x-ngsi:    
                          type: Property    
                    type: object    
                    x-ngsi:    
                      type: Property    
                  symbol:    
                    description: Symbol of the micm subtype    
                    type: string    
                    x-ngsi:    
                      type: Property    
                  type:    
                    description: Type of the micm subtype    
                    type: string    
                    x-ngsi:    
                      type: Property    
                type: object    
                x-ngsi:    
                  type: Property    
              type:    
                description: 'This field contains the type associated to the micm, information on micronutrients of the type of fertilizer'    
                type: string    
                x-ngsi:    
                  type: Property    
              value:    
                description: This field contains the value associated to the micm    
                type: number    
                x-ngsi:    
                  type: Property    
            type: object    
            x-ngsi:    
              type: Property    
          type: array    
          x-ngsi:    
            type: Property    
        mmcm:    
          description: Array of mmcm objects associated with the subtype    
          items:    
            description: Every element in the mmdm array    
            properties:    
              id:    
                description: Identifier of mmcm    
                type: number    
                x-ngsi:    
                  type: Property    
              subtype:    
                description: Subtype details of mmcm    
                properties:    
                  code:    
                    description: Code of the mmcm subtype    
                    type: number    
                    x-ngsi:    
                      type: Property    
                  id:    
                    description: Identifier of the mmcm subtype    
                    type: number    
                    x-ngsi:    
                      type: Property    
                  name:    
                    description: Name of the main macronutrient of the fertilizer type    
                    type: string    
                    x-ngsi:    
                      type: Property    
                  subtype:    
                    description: Nested subtype details of mmcm    
                    properties:    
                      id:    
                        description: Identifier of the nested mmcm subtype    
                        type: number    
                        x-ngsi:    
                          type: Property    
                      name:    
                        description: Name of the nested mmcm subtype    
                        type: string    
                        x-ngsi:    
                          type: Property    
                      type:    
                        description: Type of the nested mmcm subtype    
                        type: string    
                        x-ngsi:    
                          type: Property    
                    type: object    
                    x-ngsi:    
                      type: Property    
                  symbol:    
                    description: Symbol of the mmcm subtype    
                    type: string    
                    x-ngsi:    
                      type: Property    
                  type:    
                    description: Type of the mmcm subtype    
                    type: string    
                    x-ngsi:    
                      type: Property    
                type: object    
                x-ngsi:    
                  type: Property    
              type:    
                description: 'This field contains the type associated to the mmcm, information on the main macronutrients of the fertilizer type'    
                type: string    
                x-ngsi:    
                  type: Property    
              value:    
                description: This field contains the value associated to the mmcm    
                type: number    
                x-ngsi:    
                  type: Property    
            type: object    
            x-ngsi:    
              type: Property    
          type: array    
          x-ngsi:    
            type: Property    
        name:    
          description: Name of the type of fertilizer used and associated with the fertilization code    
          type: string    
          x-ngsi:    
            type: Property    
        notes:    
          description: Notes associated with the subtype    
          type: string    
          x-ngsi:    
            type: Property    
        subcode:    
          description: Subcode of the subtype    
          type: string    
          x-ngsi:    
            type: Property    
        symbol:    
          description: Symbol of the subtype    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    taf:    
      description: Information on types of fertilizer application    
      properties:    
        id:    
          description: Identifier of the TAF    
          type: string    
          x-ngsi:    
            type: Property    
        name:    
          description: Name of the types of fertilizer application    
          type: string    
          x-ngsi:    
            type: Property    
        type:    
          description: Type of the types of fertilizer application    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    target:    
      description: Target details for the AgriFertilize entity    
      type: string    
      x-ngsi:    
        type: Property    
    tmi:    
      description: Information on the types of inhibitory molecule    
      properties:    
        id:    
          description: Identifier of the types of inhibitory molecule    
          type: string    
          x-ngsi:    
            type: Property    
        name:    
          description: Name of the types of inhibitory molecule    
          type: string    
          x-ngsi:    
            type: Property    
        type:    
          description: Type of the types of inhibitory molecule    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity Type. It has to be AgriFertilize    
      enum:    
        - AgriFertilize    
      type: string    
      x-ngsi:    
        type: Property    
    typsoil:    
      description: Type of soil associated with the AgriFertilize entity    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2024 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Agrifood/blob/master/AgriFertilize/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Agrifood/AgriFertilize/schema.json    
  x-model-tags: 'Agrifood, AgriFertilize'    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### AgriFertilize NGSI-v2 키 값 예시  
다음은 키 값으로 JSON-LD 형식의 AgriFertilize의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
	"id": "urn:ngsi-ld:AgriFertilize:1",  
	"type": "AgriFertilize",  
	"dateCreated": "2024-05-30T09:14:44",  
	"dateModified": "2024-05-30T09:14:44",  
	"name": "",  
	"subtype": {  
		"type": "TypeFertilize",  
		"id": 1339,  
		"code": "F0002478/2025",  
		"name": "Abono Organico Npk (Ca) 1,5-1-2 (2) Mezcla De Origen Animal Y Vegetal Sirlepur",  
		"mmcm": [{  
				"type": "CM",  
				"id": 10000,  
				"subtype": {  
					"type": "TCM",  
					"id": 1,  
					"subtype": {  
						"type": "SCM",  
						"id": 1,  
						"name": "Macronutriente principal"  
					},  
					"code": 1,  
					"name": "Nitrógeno total",  
					"symbol": "% N total"  
				},  
				"value": 1.5  
			},  
			{  
				"type": "CM",  
				"id": 10001,  
				"subtype": {  
					"type": "TCM",  
					"id": 6,  
					"subtype": {  
						"type": "SCM",  
						"id": 1,  
						"name": "Macronutriente principal"  
					},  
					"code": 6,  
					"name": "Óxido de fósforo total",  
					"symbol": "% P2O5 total"  
				},  
				"value": 1  
			},  
			{  
				"type": "CM",  
				"id": 10002,  
				"subtype": {  
					"type": "TCM",  
					"id": 9,  
					"subtype": {  
						"type": "SCM",  
						"id": 1,  
						"name": "Macronutriente principal"  
					},  
					"code": 9,  
					"name": "Óxido de potasio",  
					"symbol": "% K2O total"  
				},  
				"value": 2  
			}  
		],  
		"macm": [{  
			"type": "CM",  
			"id": 44578,  
			"subtype": {  
				"type": "TCM",  
				"id": 2,  
				"subtype": {  
					"type": "SCM",  
					"id": 2,  
					"name": "Otro macronutriente"  
				},  
				"code": 2,  
				"name": "Nitrógeno orgánico",  
				"symbol": "% N orgánico"  
			},  
			"value": 1.5  
		}],  
		"hecm": [{  
			"type": "CM",  
			"id": 44582,  
			"subtype": {  
				"type": "TCM",  
				"id": 16,  
				"subtype": {  
					"type": "SCM",  
					"id": 4,  
					"name": "Metal pesado"  
				},  
				"code": 2,  
				"name": "Cobre",  
				"symbol": "% Cu"  
			},  
			"value": 0.0001  
		}],  
		"micm": [{  
			"type": "CM",  
			"id": 44581,  
			"subtype": {  
				"type": "TCM",  
				"id": 22,  
				"subtype": {  
					"type": "SCM",  
					"id": 3,  
					"name": "Micronutriente"  
				},  
				"code": 1,  
				"name": "Boro",  
				"symbol": "% Bo"  
			},  
			"value": 1.1  
		}],  
		"accm": [{  
			"type": "CM",  
			"id": 58492,  
			"subtype": {  
				"type": "TCM",  
				"id": 33,  
				"subtype": {  
					"type": "SCM",  
					"id": 5,  
					"name": "Ácido"  
				},  
				"code": -1,  
				"name": "Ácido húmico",  
				"symbol": "% Hum"  
			},  
			"value": 1  
		}],  
		"aacm": [{  
			"type": "CM",  
			"id": 58494,  
			"subtype": {  
				"type": "TCM",  
				"id": 40,  
				"subtype": {  
					"type": "SCM",  
					"id": 6,  
					"name": "Aminoácido"  
				},  
				"code": -1,  
				"name": "Glicina",  
				"symbol": "% Gly"  
			},  
			"value": 1  
		}],  
		"otcm": [{  
			"type": "CM",  
			"id": 58496,  
			"subtype": {  
				"type": "TCM",  
				"id": 54,  
				"subtype": {  
					"type": "SCM",  
					"id": 7,  
					"name": "Otro"  
				},  
				"code": -1,  
				"name": "Manitol",  
				"symbol": "% manitol"  
			},  
			"value": 0.4  
		}],  
		"comp": {  
			"type": "Company",  
			"id": 269,  
			"name": "Organicos Pedrin, S.l",  
			"nif": ""  
		},  
		"manure": "",  
		"material": {  
			"type": "TMF",  
			"id": 15,  
			"name": "Productos fertilizantes: abonos orgánicos"  
		},  
		"matdet": "",  
		"provider": "",  
		"nif": "",  
		"check": 0,  
		"metadata": [{  
			"type": "Create",  
			"user": {  
				"type": "UserMetadata",  
				"id": "1",  
				"loginname": "sistema",  
				"email": "",  
				"name": "Sistema",  
				"surname": "",  
				"nif": ""  
			},  
			"date": "2024-02-09T15:48:46"  
		}],  
		"reviewed": "1"  
	},  
	"inidate": "2025-05-30T09:14:44",  
	"enddate": "",  
	"dose": 10,  
	"measure": {  
		"type": "Measure",  
		"id": "501",  
		"subtype": {  
			"type": "TypeMeasure",  
			"id": "6",  
			"name": "Fertilizante"  
		},  
		"code": 17,  
		"name": "Kilogramo por hectárea",  
		"symbol": "kg/ha",  
		"prior": "1",  
		"detail": ""  
	},  
	"soup": 1000,  
	"msoup": {  
		"type": "Measure",  
		"id": "514",  
		"subtype": {  
			"type": "TypeMeasure",  
			"id": "6",  
			"name": "Fertilizante"  
		},  
		"code": 4,  
		"name": "Litro",  
		"symbol": "l",  
		"prior": "3",  
		"detail": ""  
	},  
	"r10": "",  
	"mud": 0,  
	"bill": "",  
	"plan": "",  
	"taf": {  
		"type": "TAF",  
		"id": "1",  
		"name": "Abonado de fondo"  
	},  
	"maf": {  
		"type": "MAF",  
		"id": "1",  
		"name": "Esparcido general"  
	},  
	"tmi": {  
		"type": "TMI",  
		"id": "1",  
		"name": "Sin especificar",  
		"acronym": ""  
	},  
	"machine": [{  
		"type": "MachineInfoFertilize",  
		"id": "1",  
		"product": "Agua",  
		"detail": "",  
		"idmachine": "8"  
	}],  
	"detail": "",  
	"idcp": [  
		"13",  
		"14",  
		"15"  
	]  
}  
```  
</details>  
#### AgriFertilize NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 AgriFertilize의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:AgriFertilize:1",  
  "type": "AgriFertilize",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2024-05-30T09:14:44.000Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2024-05-30T09:14:44.000Z"  
  },  
  "name": {  
    "type": "Text",  
    "value": ""  
  },  
  "subtype": {  
    "type": "StructuredValue",  
    "value": {  
      "type": "TypeFertilize",  
      "id": {  
        "type": "Number",  
        "value": 1339  
      },  
      "code": {  
        "type": "Text",  
        "value": "F0002478/2025"  
      },  
      "name": {  
        "type": "Text",  
        "value": "Abono Organico Npk (Ca) 1,5-1-2 (2) Mezcla De Origen Animal Y Vegetal Sirlepur"  
      },  
      "mmcm": {  
        "type": "StructuredValue",  
        "value": [  
          {  
            "type": "CM",  
            "id": {  
              "type": "Number",  
              "value": 10000  
            },  
            "value": {  
              "type": "Number",  
              "value": 1.5  
            },  
            "subtype": {  
              "type": "StructuredValue",  
              "value": {  
                "type": "TCM",  
                "id": {  
                  "type": "Number",  
                  "value": 1  
                },  
                "subtype": {  
                  "type": "StructuredValue",  
                  "value": {  
                    "type": "SCM",  
                    "id": {  
                      "type": "Number",  
                      "value": 1  
                    },  
                    "name": {  
                      "type": "Text",  
                      "value": "Macronutriente principal"  
                    }  
                  }  
                },  
                "code": {  
                  "type": "Number",  
                  "value": 1  
                },  
                "name": {  
                  "type": "Text",  
                  "value": "Nitrógeno total"  
                },  
                "symbol": {  
                  "type": "Text",  
                  "value": "% N total"  
                }  
              }  
            }  
          },  
          {  
            "type": "CM",  
            "id": {  
              "type": "Number",  
              "value": 10001  
            },  
            "value": {  
              "type": "Number",  
              "value": 1  
            },  
            "subtype": {  
              "type": "StructuredValue",  
              "value": {  
                "type": "TCM",  
                "id": {  
                  "type": "Number",  
                  "value": 6  
                },  
                "subtype": {  
                  "type": "StructuredValue",  
                  "value": {  
                    "type": "SCM",  
                    "id": {  
                      "type": "Number",  
                      "value": 1  
                    },  
                    "name": {  
                      "type": "Text",  
                      "value": "Macronutriente principal"  
                    }  
                  }  
                },  
                "code": {  
                  "type": "Number",  
                  "value": 6  
                },  
                "name": {  
                  "type": "Text",  
                  "value": "Óxido de fósforo total"  
                },  
                "symbol": {  
                  "type": "Text",  
                  "value": "% P2O5 total"  
                }  
              }  
            }  
          },  
          {  
            "type": "CM",  
            "id": {  
              "type": "Number",  
              "value": 10002  
            },  
            "value": {  
              "type": "Number",  
              "value": 2  
            },  
            "subtype": {  
              "type": "StructuredValue",  
              "value": {  
                "type": "TCM",  
                "id": {  
                  "type": "Number",  
                  "value": 9  
                },  
                "subtype": {  
                  "type": "StructuredValue",  
                  "value": {  
                    "type": "SCM",  
                    "id": {  
                      "type": "Number",  
                      "value": 1  
                    },  
                    "name": {  
                      "type": "Text",  
                      "value": "Macronutriente principal"  
                    }  
                  }  
                },  
                "code": {  
                  "type": "Number",  
                  "value": 9  
                },  
                "name": {  
                  "type": "Text",  
                  "value": "Óxido de potasio"  
                },  
                "symbol": {  
                  "type": "Text",  
                  "value": "% K2O total"  
                }  
              }  
            }  
          }  
        ]  
      },  
      "macm": {  
        "type": "StructuredValue",  
        "value": []  
      },  
      "hecm": {  
        "type": "StructuredValue",  
        "value": []  
      },  
      "micm": {  
        "type": "StructuredValue",  
        "value": []  
      },  
      "accm": {  
        "type": "StructuredValue",  
        "value": []  
      },  
      "aacm": {  
        "type": "StructuredValue",  
        "value": []  
      },  
      "otcm": {  
        "type": "StructuredValue",  
        "value": []  
      },  
      "comp": {  
        "type": "StructuredValue",  
        "value": {  
          "type": "Company",  
          "id": {  
            "type": "Number",  
            "value": 269  
          },  
          "name": {  
            "type": "Text",  
            "value": "Organicos Pedrin, S.l"  
          },  
          "nif": {  
            "type": "Text",  
            "value": ""  
          }  
        }  
      },  
      "manure": {  
        "type": "Text",  
        "value": ""  
      },  
      "material": {  
        "type": "StructuredValue",  
        "value": {  
          "type": "TMF",  
          "id": {  
            "type": "Number",  
            "value": 15  
          },  
          "name": {  
            "value": "Productos fertilizantes: abonos orgánicos"  
          }  
        }  
      },  
      "matdet": {  
        "type": "Text",  
        "value": ""  
      },  
      "provider": {  
        "type": "Text",  
        "value": ""  
      },  
      "nif": {  
        "type": "Text",  
        "value": ""  
      },  
      "check": {  
        "type": "Number",  
        "value": 0  
      },  
      "metadata": {  
        "type": "StructuredValue",  
        "value": [  
          {  
            "type": "Create",  
            "user": {  
              "type": "StructuredValue",  
              "value": {  
                "type": "UserMetadata",  
                "id": {  
                  "type": "Text",  
                  "value": "1"  
                },  
                "loginname": {  
                  "type": "Text",  
                  "value": "sistema"  
                },  
                "email": {  
                  "type": "Text",  
                  "value": ""  
                },  
                "name": {  
                  "type": "Text",  
                  "value": "Sistema"  
                },  
                "surname": {  
                  "type": "Text",  
                  "value": ""  
                },  
                "nif": {  
                  "type": "Text",  
                  "value": ""  
                }  
              }  
            },  
            "date": {  
              "type": "DateTime",  
              "value": "2024-02-09T15:48:46.000Z"  
            }  
          }  
        ]  
      },  
      "reviewed": {  
        "type": "Number",  
        "value": 1  
      }  
    }  
  },  
  "inidate": {  
    "type": "DateTime",  
    "value": "2024-05-30T09:14:44.000Z"  
  },  
  "enddate": {  
    "type": "Text",  
    "value": ""  
  },  
  "dose": {  
    "type": "Number",  
    "value": 10  
  },  
  "measure": {  
    "type": "StructuredValue",  
    "value": {  
      "type": "Measure",  
      "id": {  
        "type": "Text",  
        "value": "501"  
      },  
      "subtype": {  
        "type": "StructuredValue",  
        "value": {  
          "type": "TypeMeasure",  
          "id": {  
            "type": "Number",  
            "value": 6  
          },  
          "name": {  
            "type": "Text",  
            "value": "Fertilizante"  
          }  
        }  
      },  
      "code": {  
        "type": "Number",  
        "value": 17  
      },  
      "name": {  
        "type": "Text",  
        "value": "Kilogramo por hectárea"  
      },  
      "symbol": {  
        "type": "Text",  
        "value": "kg/ha"  
      },  
      "prior": {  
        "type": "Text",  
        "value": "1"  
      },  
      "detail": {  
        "type": "Text",  
        "value": ""  
      }  
    }  
  },  
  "soup": {  
    "type": "Number",  
    "value": 1000  
  },  
  "msoup": {  
    "type": "StructuredValue",  
    "value": {  
      "type": "Measure",  
      "id": {  
        "type": "Text",  
        "value": "514"  
      },  
      "subtype": {  
        "type": "StructuredValue",  
        "value": {  
          "type": "TypeMeasure",  
          "id": {  
            "type": "Number",  
            "value": 6  
          },  
          "name": {  
            "type": "Text",  
            "value": "Fertilizante"  
          }  
        }  
      },  
      "code": {  
        "type": "Number",  
        "value": 4  
      },  
      "name": {  
        "type": "Text",  
        "value": "Litro"  
      },  
      "symbol": {  
        "type": "Text",  
        "value": "l"  
      },  
      "prior": {  
        "type": "Text",  
        "value": "3"  
      },  
      "detail": {  
        "type": "Text",  
        "value": ""  
      }  
    }  
  },  
  "r10": {  
    "type": "Text",  
    "value": ""  
  },  
  "mud": {  
    "type": "Number",  
    "value": 0  
  },  
  "bill": {  
    "type": "Text",  
    "value": ""  
  },  
  "plan": {  
    "type": "Text",  
    "value": ""  
  },  
  "taf": {  
    "type": "StructuredValue",  
    "value": {  
      "type": "TAF",  
      "id": {  
        "type": "Text",  
        "value": "1"  
      },  
      "name": {  
        "type": "Text",  
        "value": "Abonado de fondo"  
      }  
    }  
  },  
  "maf": {  
    "type": "StructuredValue",  
    "value": {  
      "type": "MAF",  
      "id": {  
        "type": "Text",  
        "value": "1"  
      },  
      "name": {  
        "type": "Text",  
        "value": "Esparcido general"  
      }  
    }  
  },  
  "tmi": {  
    "type": "StructuredValue",  
    "value": {  
      "type": "TMI",  
      "id": {  
        "type": "Text",  
        "value": "1"  
      },  
      "name": {  
        "type": "Text",  
        "value": "Sin especificar"  
      },  
      "acronym": {  
        "type": "Text",  
        "value": ""  
      }  
    }  
  },  
  "machine": {  
    "type": "StructuredValue",  
    "value": []  
  },  
  "detail": {  
    "type": "Text",  
    "value": ""  
  },  
  "idcp": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "type": "Text",  
        "value": "13"  
      },  
      {  
        "type": "Text",  
        "value": "14"  
      },  
      {  
        "type": "Text",  
        "value": "15"  
      }  
    ]  
  }  
}  
```  
</details>  
#### AgriFertilize NGSI-LD 키 값 예시  
다음은 키 값으로 JSON-LD 형식의 AgriFertilize의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:dataModel:id:1-1",  
  "type": "AgriFertilize",  
  "dateCreated": "2023-06-01T12:00:00Z",  
  "dateModified": "2024-06-01T12:00:00Z",  
  "dose": 50.5,  
  "enddate": "2024-06-30T12:00:00Z",  
  "inidate": "2024-06-01T12:00:00Z",  
  "measure": {  
    "detail": "Measurement details",  
    "id": "measure123",  
    "name": "MeasureName",  
    "prior": "5",  
    "type": "TypeA",  
    "code": 101,  
    "symbol": "M"  
  },  
  "name": "Fertilizer Campaign 2024",  
  "subtype": {  
    "aacm": [  
      {  
        "type": "CM",  
        "id": 58492,  
        "subtype": {  
          "type": "TCM",  
          "id": 33,  
          "subtype": {  
            "type": "SCM",  
            "id": 5,  
            "name": "Ácido"  
          },  
          "code": -1,  
          "name": "Ácido húmico",  
          "symbol": "% Hum"  
        },  
        "value": 1  
      }  
    ],  
    "check": 75,  
    "code": "ST123",  
    "comp": {  
      "id": 789,  
      "name": "Fertilizer Company Ltd.",  
      "nif": "B12345678",  
      "type": "Producer"  
    },  
    "hecm": [  
      {  
        "type": "CM",  
        "id": 44582,  
        "subtype": {  
          "type": "TCM",  
          "id": 16,  
          "subtype": {  
            "type": "SCM",  
            "id": 4,  
            "name": "Metal pesado"  
          },  
          "code": 2,  
          "name": "Cobre",  
          "symbol": "% Cu"  
        },  
        "value": 0.0001  
      }  
    ],  
    "id": 456,  
    "macm": [  
      {  
        "type": "CM",  
        "id": 47901,  
        "subtype": {  
          "type": "TCM",  
          "id": 2,  
          "subtype": {  
            "type": "SCM",  
            "id": 2,  
            "name": "Otro macronutriente"  
          },  
          "code": 2,  
          "name": "Nitrógeno orgánico",  
          "symbol": "% N orgánico"  
        },  
        "value": 4.5  
      }  
    ],  
    "manure": "",  
    "matdet": "",  
    "material": {  
      "id": 654,  
      "name": "Organic Material",  
      "type": "TypeB"  
    },  
    "metadata": [  
      {  
        "date": "2024-05-01T12:00:00Z",  
        "type": "MetaType",  
        "user": {  
          "email": "user@example.com",  
          "id": "user123",  
          "loginname": "userlogin",  
          "name": "John Doe",  
          "nif": "12345678A",  
          "surname": "Doe",  
          "type": "Admin"  
        }  
      }  
    ],  
    "micm": [  
      {  
        "type": "CM",  
        "id": 44581,  
        "subtype": {  
          "type": "TCM",  
          "id": 22,  
          "subtype": {  
            "type": "SCM",  
            "id": 3,  
            "name": "Micronutriente"  
          },  
          "code": 1,  
          "name": "Boro",  
          "symbol": "% Bo"  
        },  
        "value": 1.1  
      }  
    ],  
    "mmcm": [  
      {  
        "id": 987,  
        "value": 111,  
        "subtype": {  
          "code": 202,  
          "id": 808,  
          "name": "Subtype Name",  
          "subtype": {  
            "id": 909,  
            "name": "Nested Subtype Name",  
            "type": "NestedType"  
          },  
          "symbol": "S",  
          "type": "SubtypeA"  
        }  
      }  
    ],  
    "name": "Subtype A",  
    "notes": "Subtype notes",  
    "subcode": "SUB123",  
    "symbol": "S"  
  },  
  "target": "Field A",  
  "typsoil": "Clay",  
  "bill": "INV123456",  
  "detail": "User notes on administered fertilizer.",  
  "idcp": [  
    "CropSigpac123",  
    "CropSigpac456"  
  ],  
  "machine": [  
    {  
      "type": "MachineInfoFertilize",  
      "id": "1",  
      "product": "Agua",  
      "detail": "",  
      "idmachine": "8"  
    }  
  ],  
  "maf": {  
    "id": "maf123",  
    "name": "MAF Name",  
    "type": "MAFType"  
  },  
  "msoup": {  
    "detail": "MSOUP Details",  
    "id": "msoup123",  
    "name": "MSOUP Name",  
    "prior": "2",  
    "type": "TypeMSOUP",  
    "code": 404,  
    "symbol": "S"  
  },  
  "mud": 1,  
  "plan": "",  
  "r10": "R1023456",  
  "soup": 100,  
  "taf": {  
    "id": "taf123",  
    "name": "TAF Name",  
    "type": "TAFType"  
  },  
  "tmi": {  
    "id": "tmi123",  
    "name": "TMI Name",  
    "type": "TMIType"  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Agrifood/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### AgriFertilize NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 AgriFertilize의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:AgriFertilize:1",  
  "type": "AgriFertilize",  
  "dateCreated": {  
    "type": "Property",  
    "value": "2024-05-30T09:14:44.000Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2024-05-30T09:14:44.000Z"  
  },  
  "name": {  
    "type": "Property",  
    "value": ""  
  },  
  "subtype": {  
    "type": "Property",  
    "value": {  
      "type": "TypeFertilize",  
      "id": {  
        "type": "Property",  
        "value": 1339  
      },  
      "code": {  
        "type": "Property",  
        "value": "F0002478/2025"  
      },  
      "name": {  
        "type": "Property",  
        "value": "Abono Organico Npk (Ca) 1,5-1-2 (2) Mezcla De Origen Animal Y Vegetal Sirlepur"  
      },  
      "mmcm": {  
        "type": "Property",  
        "value": [  
          {  
            "type": "CM",  
            "id": {  
              "type": "Property",  
              "value": 10000  
            },  
            "subtype": {  
              "type": "Property",  
              "value": {  
                "type": "TCM",  
                "id": {  
                  "type": "Property",  
                  "value": 1  
                },  
                "subtype": {  
                  "type": "Property",  
                  "value": {  
                    "type": "SCM",  
                    "id": {  
                      "type": "Property",  
                      "value": 1  
                    },  
                    "name": {  
                      "type": "Property",  
                      "value": "Macronutriente principal"  
                    }  
                  }  
                },  
                "code": {  
                  "type": "Property",  
                  "value": 1  
                },  
                "name": {  
                  "type": "Property",  
                  "value": "Nitrógeno total"  
                },  
                "symbol": {  
                  "type": "Property",  
                  "value": "% N total"  
                }  
              }  
            },  
            "value": {  
              "type": "Property",  
              "value": 1.5  
            }  
          },  
          {  
            "type": "CM",  
            "id": {  
              "type": "Property",  
              "value": 10001  
            },  
            "subtype": {  
              "type": "Property",  
              "value": {  
                "type": "TCM",  
                "id": {  
                  "type": "Property",  
                  "value": 6  
                },  
                "subtype": {  
                  "type": "Property",  
                  "value": {  
                    "type": "SCM",  
                    "id": {  
                      "type": "Property",  
                      "value": 1  
                    },  
                    "name": {  
                      "type": "Property",  
                      "value": "Macronutriente principal"  
                    }  
                  }  
                },  
                "code": {  
                  "type": "Property",  
                  "value": 6  
                },  
                "name": {  
                  "type": "Property",  
                  "value": "Óxido de fósforo total"  
                },  
                "symbol": {  
                  "type": "Property",  
                  "value": "% P2O5 total"  
                }  
              }  
            },  
            "value": {  
              "type": "Property",  
              "value": 1  
            }  
          },  
          {  
            "type": "CM",  
            "id": {  
              "type": "Property",  
              "value": 10002  
            },  
            "subtype": {  
              "type": "Property",  
              "value": {  
                "type": "TCM",  
                "id": {  
                  "type": "Property",  
                  "value": 9  
                },  
                "subtype": {  
                  "type": "Property",  
                  "value": {  
                    "type": "SCM",  
                    "id": {  
                      "type": "Property",  
                      "value": 1  
                    },  
                    "name": {  
                      "type": "Property",  
                      "value": "Macronutriente principal"  
                    }  
                  }  
                },  
                "code": {  
                  "type": "Property",  
                  "value": 9  
                },  
                "name": {  
                  "type": "Property",  
                  "value": "Óxido de potasio"  
                },  
                "symbol": {  
                  "type": "Property",  
                  "value": "% K2O total"  
                }  
              }  
            },  
            "value": {  
              "type": "Property",  
              "value": 2  
            }  
          }  
        ]  
      },  
      "macm": {  
        "type": "Property",  
        "value": []  
      },  
      "hecm": {  
        "type": "Property",  
        "value": []  
      },  
      "micm": {  
        "type": "Property",  
        "value": []  
      },  
      "accm": {  
        "type": "Property",  
        "value": []  
      },  
      "aacm": {  
        "type": "Property",  
        "value": []  
      },  
      "otcm": {  
        "type": "Property",  
        "value": []  
      },  
      "comp": {  
        "type": "Property",  
        "value": {  
          "type": "Company",  
          "id": {  
            "type": "Property",  
            "value": 269  
          },  
          "name": {  
            "type": "Property",  
            "value": "Organicos Pedrin, S.l"  
          },  
          "nif": {  
            "type": "Property",  
            "value": ""  
          }  
        }  
      },  
      "manure": {  
        "type": "Property",  
        "value": ""  
      },  
      "material": {  
        "type": "Property",  
        "value": {  
          "type": "TMF",  
          "id": {  
            "type": "Property",  
            "value": 15  
          },  
          "name": {  
            "type": "Property",  
            "value": "Productos fertilizantes: abonos orgánicos"  
          }  
        }  
      },  
      "matdet": {  
        "type": "Property",  
        "value": ""  
      },  
      "provider": {  
        "type": "Property",  
        "value": ""  
      },  
      "nif": {  
        "type": "Property",  
        "value": ""  
      },  
      "check": {  
        "type": "Property",  
        "value": 0  
      },  
      "metadata": {  
        "type": "Property",  
        "value": [  
          {  
            "type": "Create",  
            "user": {  
              "type": "Property",  
              "value": {  
                "type": "UserMetadata",  
                "id": {  
                  "type": "Property",  
                  "value": "1"  
                },  
                "loginname": {  
                  "type": "Property",  
                  "value": "sistema"  
                },  
                "email": {  
                  "type": "Property",  
                  "value": ""  
                },  
                "name": {  
                  "type": "Property",  
                  "value": "Sistema"  
                },  
                "surname": {  
                  "type": "Property",  
                  "value": ""  
                },  
                "nif": {  
                  "type": "Property",  
                  "value": ""  
                }  
              }  
            },  
            "date": {  
              "type": "Property",  
              "value": "2024-02-09T15:48:46.000Z"  
            }  
          }  
        ]  
      },  
      "reviewed": {  
        "type": "Property",  
        "value": 1  
      }  
    }  
  },  
  "inidate": {  
    "type": "Property",  
    "value": "2024-05-30T09:14:44.000Z"  
  },  
  "enddate": {  
    "type": "Property",  
    "value": ""  
  },  
  "dose": {  
    "type": "Property",  
    "value": 10  
  },  
  "measure": {  
    "type": "Property",  
    "value": {  
      "type": "Measure",  
      "id": {  
        "type": "Property",  
        "value": "501"  
      },  
      "subtype": {  
        "type": "Property",  
        "value": {  
          "type": "TypeMeasure",  
          "id": {  
            "type": "Property",  
            "value": 6  
          },  
          "name": {  
            "type": "Property",  
            "value": "Fertilizante"  
          }  
        }  
      },  
      "code": {  
        "type": "Property",  
        "value": 17  
      },  
      "name": {  
        "type": "Property",  
        "value": "Kilogramo por hectárea"  
      },  
      "symbol": {  
        "type": "Property",  
        "value": "kg/ha"  
      },  
      "prior": {  
        "type": "Property",  
        "value": "1"  
      },  
      "detail": {  
        "type": "Property",  
        "value": ""  
      }  
    }  
  },  
  "soup": {  
    "type": "Property",  
    "value": 1000  
  },  
  "msoup": {  
    "type": "Property",  
    "value": {  
      "type": "Measure",  
      "id": {  
        "type": "Property",  
        "value": "514"  
      },  
      "subtype": {  
        "type": "Property",  
        "value": {  
          "type": "TypeMeasure",  
          "id": {  
            "type": "Property",  
            "value": 6  
          },  
          "name": {  
            "type": "Property",  
            "value": "Fertilizante"  
          }  
        }  
      },  
      "code": {  
        "type": "Property",  
        "value": 4  
      },  
      "name": {  
        "type": "Property",  
        "value": "Litro"  
      },  
      "symbol": {  
        "type": "Property",  
        "value": "l"  
      },  
      "prior": {  
        "type": "Property",  
        "value": "3"  
      },  
      "detail": {  
        "type": "Property",  
        "value": ""  
      }  
    }  
  },  
  "r10": {  
    "type": "Property",  
    "value": ""  
  },  
  "mud": {  
    "type": "Property",  
    "value": 0  
  },  
  "bill": {  
    "type": "Property",  
    "value": ""  
  },  
  "plan": {  
    "type": "Property",  
    "value": ""  
  },  
  "taf": {  
    "type": "Property",  
    "value": {  
      "type": "TAF",  
      "id": {  
        "type": "Property",  
        "value": "1"  
      },  
      "name": {  
        "type": "Property",  
        "value": "Abonado de fondo"  
      }  
    }  
  },  
  "maf": {  
    "type": "Property",  
    "value": {  
      "type": "MAF",  
      "id": {  
        "type": "Property",  
        "value": "1"  
      },  
      "name": {  
        "type": "Property",  
        "value": "Esparcido general"  
      }  
    }  
  },  
  "tmi": {  
    "type": "Property",  
    "value": {  
      "type": "TMI",  
      "id": {  
        "type": "Property",  
        "value": "1"  
      },  
      "name": {  
        "type": "Property",  
        "value": "Sin especificar"  
      },  
      "acronym": {  
        "type": "Property",  
        "value": ""  
      }  
    }  
  },  
  "machine": {  
    "type": "Property",  
    "value": []  
  },  
  "detail": {  
    "type": "Property",  
    "value": ""  
  },  
  "idcp": {  
    "type": "Property",  
    "value": [  
      {  
        "type": "Property",  
        "value": "13"  
      },  
      {  
        "type": "Property",  
        "value": "14"  
      },  
      {  
        "type": "Property",  
        "value": "15"  
      }  
    ]  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Agrifood/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
규모 단위를 다루는 방법에 대한 답변은 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
