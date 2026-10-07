/* (Beta) Export of data model AgriCrop of the subject dataModel.Agrifood for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE AgriCrop_type AS ENUM ('AgriCrop');
CREATE TYPE AgriCrop_wateringFrequency_type AS ENUM ('daily', 'weekly', 'biweekly', 'monthly', 'onDemand', 'other');
CREATE TABLE AgriCrop (
  "agroVocConcept" TEXT,
  "alternateName" TEXT,
  "dataProvider" TEXT,
  "dateCreated" TIMESTAMP,
  "dateModified" TIMESTAMP,
  "description" TEXT,
  "harvestingInterval" JSON,
  "hasAgriFertiliser" JSON,
  "hasAgriPest" JSON,
  "hasAgriSoil" JSON,
  "id" TEXT PRIMARY KEY,
  "name" TEXT,
  "owner" JSON,
  "plantingFrom" JSON,
  "relatedSource" JSON,
  "seeAlso" JSON,
  "source" TEXT,
  "type" AgriCrop_type,
  "wateringFrequency" AgriCrop_wateringFrequency_type
);