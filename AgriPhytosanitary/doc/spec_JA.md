<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティアグリフィトサニタリー  
=================<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.Agrifood/blob/master/AgriPhytosanitary/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述：**アグリフィトサニタリー・エンティティのスキーマ。植物検疫とは、植物の健康に関するものである。  
バージョン: 0.0.1  
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
	- `streetNr[string]`: 公道上の特定の物件を特定する番号    
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `batch[string]`: 在庫受取ロット番号  - `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `detail[string]`: 植物検疫製品に関するその他の詳細  - `distributed[string]`: キャンペーンで投与された植物検疫の消費量が、在庫項目間で均等に分配されなければならないか否かを示す。  - `dose[string]`: 植物検疫の投与量  - `dt[string]`: 製品の流通または使用に関する日付  - `efficacy[object]`: 植物検疫製品の有効性の詳細  	- `detail[string]`: 効能に関する詳細情報    
	- `id[string]`: 効能記録の識別子    
	- `name[string]`: 効能記録の名称    
	- `type[string]`: 効能の種類    
- `entrylimit[string]`: 製品用途のエントリー・リミットまたは閾値  - `id[*]`: エンティティの一意識別子  - `idcp[array]`: キャンペーンで非化学的植物防疫が実施されるCropSigpacのID  - `idtpismv[array]`: キャンペーンで投与された植物検疫製品にリンクされたストックエントリーのID  - `infection[string]`: キャンペーンの対象となる感染症に関する情報  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `machine[array]`: 植物検疫の適用に割り当てられた機械およびその衛生に関する情報  - `mdt[string]`: 変更日（該当する場合  - `measur[string]`: 測定の詳細（該当する場合  - `measure[string]`: 投与量の単位  - `mst[string]`: 変更状況（該当する場合  - `name[string]`: このアイテムの名前  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `pp[string]`: 製品に関する前処理情報  - `preventive[string]`: 製品に関する予防措置  - `recipe[string]`: 製品のレシピまたは処方の詳細  - `seclimit[string]`: 製品の用途に関する二次規制値または閾値  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `soup[string]`: 最終投与スープ量  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `speed[string]`: 植物検疫製品の申請速度  - `st[string]`: 植物検疫製品のステータス  - `subtype[object]`: 植物検疫製品のサブタイプに関する詳細情報  	- `cdate[string]`: 植物検疫の取り消し日    
	- `ci[array]`: 植物検疫上の作物と感染症に関する情報    
	- `code[string]`: 植物検疫製品の種類に割り当てられたコード    
	- `comp[object]`: サブタイプに関連する会社の詳細    
	- `edate[string]`: 植物検疫の種類の有効期限    
	- `id[string]`: サブタイプ識別子    
	- `idate[string]`: 植物検疫の種類の登録日    
	- `idpdf[string]`: 植物検疫製品の種類に割り当てられた識別子。URL経由で公式情報にアクセスするために使用される（旧PDF）    
	- `idtf[array]`: 植物検疫タイプの機能タイプの識別子    
	- `ldate[string]`: 植物検疫製品の種類の販売制限日    
	- `mix[number]`: 植物検疫製品が混和性であるか（値 = 1）、または混和性でないか（値 = 0）を示す。    
	- `name[string]`: 植物検疫製品の種類に割り当てられた名称    
	- `names[array]`: 植物検疫の種類の通称    
	- `prod[object]`: 植物検疫製品の種類に関する情報    
	- `rdate[string]`: 植物検疫の種類の更新日    
	- `subs[object]`: 有効成分に関する情報    
	- `type[string]`: サブタイプの分類    
- `surface[string]`: 製品の塗布面積  - `tj[array]`: キャンペーンにおいて非化学的植物防疫を実施する動機となる正当な理由の種類に関する情報  - `type[string]`: NGSIエンティティタイプ。AgriPhytosanitaryでなければならない。  - `typerisk[string]`: 植物検疫製品に関連するリスクの種類  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AgriPhytosanitary:    
  description: Schema for AgriPhytosanitary entity. Phytosanitary means relating to the health of plants    
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
    batch:    
      description: Stock receipt lot number    
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
      description: Additional details about the phytosanitary product    
      type: string    
      x-ngsi:    
        type: Property    
    distributed:    
      description: Indicates whether the consumption of the phytosanitary administered in the campaign has to be distributed equally between the stock entries or not    
      type: string    
      x-ngsi:    
        type: Property    
    dose:    
      description: Dose of phytosanitary administered    
      type: string    
      x-ngsi:    
        type: Property    
    dt:    
      description: Date related to the product's distribution or usage    
      type: string    
      x-ngsi:    
        type: Property    
    efficacy:    
      description: Efficacy details of the phytosanitary product    
      properties:    
        detail:    
          description: Detailed information about the efficacy    
          type: string    
          x-ngsi:    
            type: Property    
        id:    
          description: Identifier for the efficacy record    
          type: string    
          x-ngsi:    
            type: Property    
        name:    
          description: Name of the efficacy record    
          type: string    
          x-ngsi:    
            type: Property    
        type:    
          description: Type of efficacy    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    entrylimit:    
      description: Entry limit or threshold for the product's application    
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
      description: IDs of the CropSigpac on which the non-chemical phytosanitary defense is administered in the campaign    
      items:    
        description: Every element in the CropSigpac on which the non-chemical phytosanitary defense is administered in the campaign    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    idtpismv:    
      description: IDs of stock entries linked to the phytosanitary product administered in the campaign    
      items:    
        description: Every element of the  stock entries linked to the phytosanitary product administered in the campaign    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    infection:    
      description: Information about infections that are part of the campaign    
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
      description: Information on the machinery assigned to the application of the phytosanitary as well as information on its hygiene    
      items:    
        description: 'Every element of he array of machinery assigned to the application of the phytosanitary '    
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
    mdt:    
      description: 'Modification date, if applicable'    
      type: string    
      x-ngsi:    
        type: Property    
    measur:    
      description: 'Measurement details, if applicable'    
      type: string    
      x-ngsi:    
        type: Property    
    measure:    
      description: Unit of measure for the dose    
      type: string    
      x-ngsi:    
        type: Property    
    mst:    
      description: 'Modification status, if applicable'    
      type: string    
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
    pp:    
      description: Pre-processing information related to the product    
      type: string    
      x-ngsi:    
        type: Property    
    preventive:    
      description: Preventive measures associated with the product    
      type: string    
      x-ngsi:    
        type: Property    
    recipe:    
      description: Recipe or formulation details for the product    
      type: string    
      x-ngsi:    
        type: Property    
    seclimit:    
      description: Secondary limit or threshold for the product's application    
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
      type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    speed:    
      description: Application speed for the phytosanitary product    
      type: string    
      x-ngsi:    
        type: Property    
    st:    
      description: Status of the phytosanitary product    
      type: string    
      x-ngsi:    
        type: Property    
    subtype:    
      description: Detailed information about the subtype of the phytosanitary product    
      properties:    
        cdate:    
          description: Cancellation date of the type of phytosanitary    
          type: string    
          x-ngsi:    
            type: Property    
        ci:    
          description: Information on crops and infections of the phytosanitary type    
          items:    
            description: Every element in the array of crops and infections of the phytosanitary type    
            type: string    
            x-ngsi:    
              type: Property    
          type: array    
          x-ngsi:    
            type: Property    
        code:    
          description: Code assigned to the type of phytosanitary product    
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
              description: Name of the company    
              type: string    
              x-ngsi:    
                type: Property    
            type:    
              description: Type of the company    
              type: string    
              x-ngsi:    
                type: Property    
            vat:    
              description: VAT of the company    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        edate:    
          description: Expiration date of the type of phytosanitary    
          type: string    
          x-ngsi:    
            type: Property    
        id:    
          description: Subtype identifier    
          type: string    
          x-ngsi:    
            type: Property    
        idate:    
          description: Date of registration of the type of phytosanitary    
          type: string    
          x-ngsi:    
            type: Property    
        idpdf:    
          description: Identifier assigned to the type of phytosanitary product. Used to access official information via a URL (old PDF)    
          type: string    
          x-ngsi:    
            type: Property    
        idtf:    
          description: Identifiers of the function types of the phytosanitary type    
          items:    
            description: Every element in the idft array    
            type: number    
            x-ngsi:    
              type: Property    
          type: array    
          x-ngsi:    
            type: Property    
        ldate:    
          description: Sale limit date of the type of phytosanitary product    
          type: string    
          x-ngsi:    
            type: Property    
        mix:    
          description: Indicates whether the phytosanitary product is miscible (value = 1) or not (value = 0)    
          type: number    
          x-ngsi:    
            type: Property    
        name:    
          description: Name assigned to the type of phytosanitary product    
          type: string    
          x-ngsi:    
            type: Property    
        names:    
          description: Common names of the type of phytosanitary    
          items:    
            description: 'Every element in the names array '    
            type: string    
            x-ngsi:    
              type: Property    
          type: array    
          x-ngsi:    
            type: Property    
        prod:    
          description: Information on the types of phytosanitary product    
          properties:    
            id:    
              description: Identifier assigned to the type of phytosanitary product    
              type: number    
              x-ngsi:    
                type: Property    
            name:    
              description: Name assigned to the type of phytosanitary product    
              type: string    
              x-ngsi:    
                type: Property    
            type:    
              description: Type of product    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        rdate:    
          description: Renewal date of the type of phytosanitary    
          type: string    
          x-ngsi:    
            type: Property    
        subs:    
          description: Information on active ingredients    
          properties:    
            id:    
              description: Identifier assigned to the active matter    
              type: string    
              x-ngsi:    
                type: Property    
            name:    
              description: Name assigned to the active matter    
              type: string    
              x-ngsi:    
                type: Property    
            type:    
              description: Type of substance    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        type:    
          description: Subtype classification    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    surface:    
      description: Surface area for application of the product    
      type: string    
      x-ngsi:    
        type: Property    
    tj:    
      description: Information on the types of justification that motivate the administration of non-chemical phytosanitary defense in the campaign    
      items:    
        description: Every element of the array of types of justification that motivate the administration of non-chemical phytosanitary defense    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity Type. It has to be AgriPhytosanitary    
      enum:    
        - AgriPhytosanitary    
      type: string    
      x-ngsi:    
        type: Property    
    typerisk:    
      description: Type of risk associated with the phytosanitary product    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2024 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Agrifood/blob/master/AgriPhytosanitary/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Agrifood/AgriPhytosanitary/schema.json    
  x-model-tags: 'Agrifood, AgriPhytosanitary'    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### AgriPhytosanitary NGSI-v2 キー値の例  
JSON-LD形式のAgriPhytosanitaryのkey-valuesの例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:AgriPhytosanitary:2",  
    "type": "AgriPhytosanitary",  
    "dateCreated": "2023-09-25T15:34:21",  
    "dateModified": "2023-09-25T15:34:21",  
    "name": "11179 - Microthiol special disperss",  
    "subtype": {  
        "type": "TypePhytosanitary",  
        "id": "183",  
        "idpdf": "88013",  
        "code": "11179",  
        "name": "Microthiol Special Disperss",  
        "names": [  
            "Colpenn",  
            "Microthiol Special Disperss",  
            "Sulf 80 Wg"  
        ],  
        "idate": "01-01-1970",  
        "rdate": "",  
        "edate": "15-04-2025",  
        "cdate": "",  
        "ldate": "",  
        "mix": 1,  
        "idtf": [  
            11,  
            1  
        ],  
        "comp": {  
            "type": "Company",  
            "id": 1,  
            "name": "Upl Iberia S.a.",  
            "vat": "A08103343"  
        },  
        "subs": {  
            "type": "Substance",  
            "id": "1",  
            "name": "Azufre 80% [Wg] P/P"  
        },  
        "prod": {  
            "type": "TypeProduct",  
            "id": 1,  
            "name": "Producto fitosanitario registrado"  
        },  
        "ci": []  
    },  
    "dose": "1",  
    "measure": "1",  
    "efficacy": {  
        "type": "TypeEfficacy",  
        "id": "1",  
        "name": "Buena",  
        "detail": ""  
    },  
    "typerisk": "1",  
    "infection": "1",  
    "detail": "1",  
    "tj": [],  
    "idtpismv": [],  
    "distributed": "0",  
    "batch": "",  
    "soup": "0",  
    "dt": "0",  
    "mdt": "",  
    "st": "0",  
    "mst": "",  
    "preventive": "0",  
    "pp": "0",  
    "speed": "0",  
    "recipe": "0",  
    "surface": "60.1027",  
    "entrylimit": "0",  
    "seclimit": "0",  
    "machine": [  
        {  
            "type": "MachineInfoPhytosanitary",  
            "id": "1",  
            "product": "Agua",  
            "detail": "",  
            "idmachine": "8"  
        }  
    ],  
    "idcp": [  
        "1",  
        "2",  
        "3",  
        "4",  
        "5",  
        "6",  
        "7",  
        "8",  
        "9",  
        "10",  
        "11",  
        "12"  
    ],  
    "measur": ""  
}  
```  
</details>  
#### 農業植物検疫 NGSI-v2 正規化例  
以下は、正規化された JSON-LD 形式の AgriPhytosanitary の例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:AgriPhytosanitary:2",  
  "type": "AgriPhytosanitary",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2023-09-25T15:34:21.000Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2023-09-25T15:34:21.000Z"  
  },  
  "name": {  
    "type": "Text",  
    "value": "11179 - Microthiol special disperss"  
  },  
  "subtype": {  
    "type": "StructuredValue",  
    "value": {  
      "type": "TypePhytosanitary",  
      "id": {  
        "type": "Text",  
        "value": "183"  
      },  
      "idpdf": {  
        "type": "Text",  
        "value": "88013"  
      },  
      "code": {  
        "type": "Text",  
        "value": "11179"  
      },  
      "name": {  
        "type": "Text",  
        "value": "Microthiol Special Disperss"  
      },  
      "names": {  
        "type": "StructuredValue",  
        "value": [  
          {  
            "type": "Text",  
            "value": "Colpenn"  
          },  
          {  
            "type": "Text",  
            "value": "Microthiol Special Disperss"  
          },  
          {  
            "type": "Text",  
            "value": "Sulf 80 Wg"  
          }  
        ]  
      },  
      "idate": {  
        "type": "DateTime",  
        "value": "1970-01-01T00:00:00.000Z"  
      },  
      "rdate": {  
        "type": "DateTime",  
        "value": ""  
      },  
      "edate": {  
        "type": "DateTime",  
        "value": "2025-04-15T00:00:00.000Z"  
      },  
      "cdate": {  
        "type": "DateTime",  
        "value": ""  
      },  
      "ldate": {  
        "type": "DateTime",  
        "value": ""  
      },  
      "mix": {  
        "type": "Number",  
        "value": 1  
      },  
      "idtf": {  
        "type": "StructuredValue",  
        "value": [  
          {  
            "type": "Number",  
            "value": 11  
          },  
          {  
            "type": "Number",  
            "value": 1  
          }  
        ]  
      },  
      "comp": {  
        "type": "StructuredValue",  
        "value": {  
          "type": "Company",  
          "id": {  
            "type": "Number",  
            "value": 1  
          },  
          "name": {  
            "type": "Text",  
            "value": "Upl Iberia S.a."  
          },  
          "nif": {  
            "type": "Text",  
            "value": "A08103343"  
          }  
        }  
      },  
      "subs": {  
        "type": "StructuredValue",  
        "value": {  
          "type": "Substance",  
          "id": {  
            "type": "Text",  
            "value": "1"  
          },  
          "name": {  
            "type": "Text",  
            "value": "Azufre 80% [Wg] P/P"  
          }  
        }  
      },  
      "prod": {  
        "type": "StructuredValue",  
        "value": {  
          "type": "TypeProduct",  
          "id": {  
            "type": "Number",  
            "value": 1  
          },  
          "name": {  
            "type": "Text",  
            "value": "Producto fitosanitario registrado"  
          }  
        }  
      },  
      "ci": {  
        "type": "StructuredValue",  
        "value": []  
      }  
    }  
  },  
  "dose": {  
    "type": "Text",  
    "value": "1"  
  },  
  "measure": {  
    "type": "Text",  
    "value": "1"  
  },  
  "efficacy": {  
    "type": "StructuredValue",  
    "value": {  
      "type": "TypeEfficacy",  
      "id": {  
        "type": "Text",  
        "value": "1"  
      },  
      "name": {  
        "type": "Text",  
        "value": "Buena"  
      },  
      "detail": {  
        "type": "Text",  
        "value": ""  
      }  
    }  
  },  
  "typerisk": {  
    "type": "Text",  
    "value": "1"  
  },  
  "infection": {  
    "type": "Text",  
    "value": "1"  
  },  
  "detail": {  
    "type": "Text",  
    "value": "1"  
  },  
  "tj": {  
    "type": "StructuredValue",  
    "value": []  
  },  
  "idtpismv": {  
    "type": "StructuredValue",  
    "value": []  
  },  
  "distributed": {  
    "type": "Text",  
    "value": "0"  
  },  
  "batch": {  
    "type": "Text",  
    "value": ""  
  },  
  "soup": {  
    "type": "Text",  
    "value": "0"  
  },  
  "dt": {  
    "type": "Text",  
    "value": "0"  
  },  
  "mdt": {  
    "type": "Text",  
    "value": ""  
  },  
  "st": {  
    "type": "Text",  
    "value": "0"  
  },  
  "mst": {  
    "type": "Text",  
    "value": ""  
  },  
  "preventive": {  
    "type": "Text",  
    "value": "0"  
  },  
  "pp": {  
    "type": "Text",  
    "value": "0"  
  },  
  "speed": {  
    "type": "Text",  
    "value": "0"  
  },  
  "recipe": {  
    "type": "Text",  
    "value": "0"  
  },  
  "surface": {  
    "type": "Text",  
    "value": "60.1027"  
  },  
  "entrylimit": {  
    "type": "Text",  
    "value": "0"  
  },  
  "seclimit": {  
    "type": "Text",  
    "value": "0"  
  },  
  "machine": {  
    "type": "StructuredValue",  
    "value": []  
  },  
  "idcp": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "type": "Text",  
        "value": "1"  
      },  
      {  
        "type": "Text",  
        "value": "2"  
      },  
      {  
        "type": "Text",  
        "value": "3"  
      },  
      {  
        "type": "Text",  
        "value": "4"  
      }  
    ]  
  },  
  "measur": {  
    "type": "Text",  
    "value": ""  
  }  
}  
```  
</details>  
#### 農業植物検疫 NGSI-LD キー値の例  
JSON-LD形式のAgriPhytosanitaryのkey-valuesの例である。これは NGSI-LD と互換性があり、`options=keyValues` を使うと個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:dataModel:id:DSZK70282457",  
  "type": "AgriPhytosanitary",  
  "dateCreated": "2023-09-25T15:34:21",  
  "dateModified": "2023-09-25T15:34:21",  
  "name": "11179 - Microthiol special disperss",  
  "subtype": {  
    "type": "TypePhytosanitary",  
    "id": "183",  
    "idpdf": "88013",  
    "code": "11179",  
    "name": "Microthiol Special Disperss",  
    "names": [  
      "Colpenn",  
      "Microthiol Special Disperss",  
      "Sulf 80 Wg"  
    ],  
    "idate": "01-01-1970",  
    "rdate": "",  
    "edate": "15-04-2025",  
    "cdate": "",  
    "ldate": "",  
    "mix": 1,  
    "idtf": [  
      11,  
      1  
    ],  
    "comp": {  
      "type": "Company",  
      "id": 1,  
      "name": "Upl Iberia S.a.",  
      "nif": "A08103343"  
    },  
    "subs": {  
      "type": "Substance",  
      "id": "1",  
      "name": "Azufre 80% [Wg] P/P"  
    },  
    "prod": {  
      "type": "TypeProduct",  
      "id": 1,  
      "name": "Producto fitosanitario registrado"  
    },  
    "ci": []  
  },  
  "dose": "1",  
  "measure": "1",  
  "efficacy": {  
    "type": "TypeEfficacy",  
    "id": "1",  
    "name": "Buena",  
    "detail": ""  
  },  
  "typerisk": "1",  
  "infection": "1",  
  "detail": "1",  
  "tj": [],  
  "idtpismv": [],  
  "distributed": "0",  
  "batch": "",  
  "soup": "0",  
  "dt": "0",  
  "mdt": "",  
  "st": "0",  
  "mst": "",  
  "preventive": "0",  
  "pp": "0",  
  "speed": "0",  
  "recipe": "0",  
  "surface": "60.1027",  
  "entrylimit": "0",  
  "seclimit": "0",  
  "machine": [],  
  "idcp": [  
    "1",  
    "2",  
    "3",  
    "4",  
    "5",  
    "6",  
    "7",  
    "8",  
    "9",  
    "10",  
    "11",  
    "12"  
  ],  
  "measur": "",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Agrifood/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### 農業植物検疫 NGSI-LD 正規化例  
以下は、正規化された JSON-LD 形式の AgriPhytosanitary の例である。これは、オプションを使用しない場合、NGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:AgriPhytosanitary:2",  
  "type": "AgriPhytosanitary",  
  "dateCreated": {  
    "type": "Property",  
    "value": "2023-09-25T15:34:21.000Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2023-09-25T15:34:21.000Z"  
  },  
  "name": {  
    "type": "Property",  
    "value": "11179 - Microthiol special disperss"  
  },  
  "subtype": {  
    "type": "Property",  
    "value": {  
      "type": "TypePhytosanitary",  
      "id": {  
        "type": "Property",  
        "value": "183"  
      },  
      "idpdf": {  
        "type": "Property",  
        "value": "88013"  
      },  
      "code": {  
        "type": "Property",  
        "value": "11179"  
      },  
      "name": {  
        "type": "Property",  
        "value": "Microthiol Special Disperss"  
      },  
      "names": {  
        "type": "Property",  
        "value": [  
          {  
            "type": "Property",  
            "value": "Colpenn"  
          },  
          {  
            "type": "Property",  
            "value": "Microthiol Special Disperss"  
          },  
          {  
            "type": "Property",  
            "value": "Sulf 80 Wg"  
          }  
        ]  
      },  
      "idate": {  
        "type": "Property",  
        "value": "1970-01-01T00:00:00.000Z"  
      },  
      "rdate": {  
        "type": "Property",  
        "value": ""  
      },  
      "edate": {  
        "type": "Property",  
        "value": "2025-04-15T00:00:00.000Z"  
      },  
      "cdate": {  
        "type": "Property",  
        "value": ""  
      },  
      "ldate": {  
        "type": "Property",  
        "value": ""  
      },  
      "mix": {  
        "type": "Property",  
        "value": 1  
      },  
      "idtf": {  
        "type": "Property",  
        "value": [  
          {  
            "type": "Property",  
            "value": 11  
          },  
          {  
            "type": "Property",  
            "value": 1  
          }  
        ]  
      },  
      "comp": {  
        "type": "Property",  
        "value": {  
          "type": "Company",  
          "id": {  
            "type": "Property",  
            "value": 1  
          },  
          "name": {  
            "type": "Property",  
            "value": "Upl Iberia S.a."  
          },  
          "nif": {  
            "type": "Property",  
            "value": "A08103343"  
          }  
        }  
      },  
      "subs": {  
        "type": "Property",  
        "value": {  
          "type": "Substance",  
          "id": {  
            "type": "Property",  
            "value": "1"  
          },  
          "name": {  
            "type": "Property",  
            "value": "Azufre 80% [Wg] P/P"  
          }  
        }  
      },  
      "prod": {  
        "type": "Property",  
        "value": {  
          "type": "TypeProduct",  
          "id": {  
            "type": "Property",  
            "value": 1  
          },  
          "name": {  
            "type": "Property",  
            "value": "Producto fitosanitario registrado"  
          }  
        }  
      },  
      "ci": {  
        "type": "Property",  
        "value": []  
      }  
    }  
  },  
  "dose": {  
    "type": "Property",  
    "value": "1"  
  },  
  "measure": {  
    "type": "Property",  
    "value": "1"  
  },  
  "efficacy": {  
    "type": "Property",  
    "value": {  
      "type": "TypeEfficacy",  
      "id": {  
        "type": "Property",  
        "value": "1"  
      },  
      "name": {  
        "type": "Property",  
        "value": "Buena"  
      },  
      "detail": {  
        "type": "Property",  
        "value": ""  
      }  
    }  
  },  
  "typerisk": {  
    "type": "Property",  
    "value": "1"  
  },  
  "infection": {  
    "type": "Property",  
    "value": "1"  
  },  
  "detail": {  
    "type": "Property",  
    "value": "1"  
  },  
  "tj": {  
    "type": "Property",  
    "value": []  
  },  
  "idtpismv": {  
    "type": "Property",  
    "value": []  
  },  
  "distributed": {  
    "type": "Property",  
    "value": "0"  
  },  
  "batch": {  
    "type": "Property",  
    "value": ""  
  },  
  "soup": {  
    "type": "Property",  
    "value": "0"  
  },  
  "dt": {  
    "type": "Property",  
    "value": "0"  
  },  
  "mdt": {  
    "type": "Property",  
    "value": ""  
  },  
  "st": {  
    "type": "Property",  
    "value": "0"  
  },  
  "mst": {  
    "type": "Property",  
    "value": ""  
  },  
  "preventive": {  
    "type": "Property",  
    "value": "0"  
  },  
  "pp": {  
    "type": "Property",  
    "value": "0"  
  },  
  "speed": {  
    "type": "Property",  
    "value": "0"  
  },  
  "recipe": {  
    "type": "Property",  
    "value": "0"  
  },  
  "surface": {  
    "type": "Property",  
    "value": "60.1027"  
  },  
  "entrylimit": {  
    "type": "Property",  
    "value": "0"  
  },  
  "seclimit": {  
    "type": "Property",  
    "value": "0"  
  },  
  "machine": {  
    "type": "Property",  
    "value": []  
  },  
  "idcp": {  
    "type": "Property",  
    "value": [  
      {  
        "type": "Property",  
        "value": "1"  
      },  
      {  
        "type": "Property",  
        "value": "2"  
      },  
      {  
        "type": "Property",  
        "value": "3"  
      },  
      {  
        "type": "Property",  
        "value": "4"  
      }  
    ]  
  },  
  "measur": {  
    "type": "Property",  
    "value": ""  
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
