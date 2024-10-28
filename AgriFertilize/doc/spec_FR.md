<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : AgriFertilize  
======================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Agrifood/blob/master/AgriFertilize/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Schéma de l'entité AgriFertilize. Fertiliser un terrain signifie améliorer sa qualité pour que les plantes y poussent bien, en y épandant des déchets animaux solides ou un mélange chimique**.  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse postale et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La région dans laquelle se trouve la localité et qui se trouve dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local.    
	- `postOfficeBoxNumber[string]`: Le numéro de la boîte postale pour les adresses de boîtes postales. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Numéro identifiant une propriété spécifique sur une voie publique    
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `bill[string]`: Numéro de la facture ou du bon de livraison  - `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `detail[string]`: Notes de l'utilisateur sur l'engrais administré  - `dose[number]`: Dose d'engrais administrée  - `enddate[string]`: Date finale du processus de fertilisation. Ce champ peut être vide  - `id[*]`: Identifiant unique de l'entité  - `idcp[array]`: ID des CropSigpac sur lesquels l'engrais est appliqué dans le cadre de la campagne  - `inidate[string]`: La date de début du processus de fécondation  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `machine[array]`: Informations sur les machines affectées à l'application de l'engrais ainsi que sur leur hygiène  - `maf[object]`: Informations sur les méthodes d'application des engrais  	- `id[string]`: Identifiant du mode d'application de l'engrais    
	- `name[string]`: Nom du mode d'application de l'engrais    
	- `type[string]`: Type de mode d'application de l'engrais    
- `measure[object]`: Détails de la mesure  	- `code[number]`: Code du ministère attribué à la mesure    
	- `detail[string]`: Notes sur la mesure    
	- `id[string]`: Identifiant de la mesure    
	- `name[string]`: Nom attribué à la mesure    
	- `prior[string]`: Niveau d'importance de la mesure. Les valeurs disponibles sont comprises entre 0 (priorité) et 10 (moindre priorité).    
	- `symbol[string]`: Symbole attribué à la mesure    
	- `type[string]`: Type de mesure    
- `msoup[object]`: Information sur la mesure utilisée pour la quantité finale de bouillon administrée  	- `code[number]`: Code de la mesure utilisée pour la quantité finale de bouillon administrée    
	- `detail[string]`: Détails de la soupe    
	- `id[string]`: Identifiant du msoup    
	- `name[string]`: Nom de la mesure utilisée pour la quantité finale de bouillon administrée    
	- `prior[string]`: Détails préalables de la mesure utilisée pour la quantité finale de bouillon administrée    
	- `symbol[string]`: Symbole de la mesure utilisée pour la quantité finale de bouillon administrée    
	- `type[string]`: Type de mesure utilisée pour la quantité finale de bouillon administrée    
- `mud[number]`: Indique si le document d'application des boues d'épuration a été utilisé ou non.  - `name[string]`: Le nom de cet élément  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `plan[string]`: Informations sur les plans d'abonnement qui font partie de la campagne  - `r10[string]`: Numéro d'autorisation des déchets R10. Le traitement des sols par l'épandage de déchets est considéré comme une opération de valorisation codée R1001. Les résidus doivent être appliqués aux sols agricoles exclusivement dans le but de produire un bénéfice pour l'agriculture ou une amélioration écologique de celle-ci.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `soup[number]`: Montant final de la soupe administrée  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `subtype[object]`: Détails du sous-type de l'entité AgriFertilize  	- `aacm[array]`: Tableau d'objets aacm associés au sous-type, informations sur les acides aminés du type d'engrais    
	- `check[number]`: Valeur de contrôle associée au sous-type    
	- `code[string]`: Code du sous-type    
	- `comp[object]`: Détails de l'entreprise associée au sous-type    
	- `hecm[array]`: Tableau d'objets hecm associés au sous-type, informations sur les métaux lourds du type d'engrais    
	- `id[number]`: Identifiant du sous-type    
	- `macm[array]`: Tableau d'objets macm associés au sous-type, informations sur les autres macronutriments du type d'engrais    
	- `manure[string]`: Détails du fumier, le cas échéant    
	- `matdet[string]`: Détail de la fertilisation matérielle, le cas échéant    
	- `material[object]`: Détails du matériel associé au sous-type    
	- `metadata[array]`: Tableau des objets de métadonnées associés au sous-type    
	- `micm[array]`: Tableau d'objets micm associés au sous-type, informations sur les micronutriments du type d'engrais.    
	- `mmcm[array]`: Tableau des objets mmcm associés au sous-type    
	- `name[string]`: Nom du type d'engrais utilisé et associé au code de fertilisation    
	- `notes[string]`: Notes associées au sous-type    
	- `subcode[string]`: Sous-code du sous-type    
	- `symbol[string]`: Symbole du sous-type    
- `taf[object]`: Informations sur les types d'application d'engrais  	- `id[string]`: Identifiant du TAF    
	- `name[string]`: Nom des types d'application d'engrais    
	- `type[string]`: Type d'application d'engrais    
- `target[string]`: Détails de la cible pour l'entité AgriFertilize  - `tmi[object]`: Informations sur les types de molécules inhibitrices  	- `id[string]`: Identifiant des types de molécules inhibitrices    
	- `name[string]`: Nom des types de molécules inhibitrices    
	- `type[string]`: Type de molécule inhibitrice    
- `type[string]`: Type d'entité NGSI. Il doit s'agir d'AgriFertilize  - `typsoil[string]`: Type de sol associé à l'entité AgriFertilize  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Modèle de données description des propriétés  
Classés par ordre alphabétique (cliquez pour plus de détails)  
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
## Exemples de charges utiles  
#### AgriFertilize NGSI-v2 valeurs-clés Exemple  
Voici un exemple d'AgriFertilize au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### AgriFertilize NGSI-v2 normalisé Exemple  
Voici un exemple d'AgriFertilize au format JSON-LD tel que normalisé. Ce format est compatible avec l'INSG-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### AgriFertilize Valeurs clés de la NGSI-LD Exemple  
Voici un exemple d'AgriFertilize au format JSON-LD sous forme de valeurs-clés. Ce format est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### AgriFertilize NGSI-LD normalisé Exemple  
Voici un exemple d'AgriFertilize au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
