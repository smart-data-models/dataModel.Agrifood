/* (Beta) Export of data model Animal of the subject dataModel.Agrifood for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Animal_healthCondition_type AS ENUM ('healthy', 'inTreatment', 'sick');
CREATE TYPE Animal_phenologicalCondition_type AS ENUM ('femaleAdult', 'femaleYoung', 'grazingBaby', 'lactatingBaby', 'maleAdult', 'maleYoung');
CREATE TYPE Animal_reproductiveCondition_type AS ENUM ('active', 'inactive', 'inCalf', 'inHeat', 'noStatus');
CREATE TYPE Animal_sex_type AS ENUM ('female', 'male');
CREATE TYPE Animal_species_type AS ENUM ('beef cattle', 'cow', 'dairy cattle', 'goat', 'horse', 'pig', 'sheep');
CREATE TYPE Animal_type AS ENUM ('Animal');
CREATE TYPE Animal_welfareCondition_type AS ENUM ('issue', 'adequate');
CREATE TABLE Animal (
  "address" JSON,
  "alternateName" TEXT,
  "areaServed" TEXT,
  "birthdate" TIMESTAMP,
  "breed" TEXT,
  "calvedBy" JSON,
  "dataProvider" TEXT,
  "dateCreated" TIMESTAMP,
  "dateModified" TIMESTAMP,
  "description" TEXT,
  "fedWith" JSON,
  "healthCondition" Animal_healthCondition_type,
  "id" TEXT PRIMARY KEY,
  "legalId" TEXT,
  "locatedAt" JSON,
  "location" JSON,
  "name" TEXT,
  "ownedBy" JSON,
  "owner" JSON,
  "phenologicalCondition" Animal_phenologicalCondition_type,
  "relatedSource" JSON,
  "reproductiveCondition" Animal_reproductiveCondition_type,
  "seeAlso" JSON,
  "sex" Animal_sex_type,
  "siredBy" JSON,
  "source" TEXT,
  "species" Animal_species_type,
  "type" Animal_type,
  "weight" NUMERIC,
  "welfareCondition" Animal_welfareCondition_type
);