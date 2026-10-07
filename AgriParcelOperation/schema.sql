/* (Beta) Export of data model AgriParcelOperation of the subject dataModel.Agrifood for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE AgriParcelOperation_operationType_type AS ENUM ('fertiliser', 'inspection', 'pesticide', 'water', 'other');
CREATE TYPE AgriParcelOperation_result_type AS ENUM ('ok', 'aborted', 'failed');
CREATE TYPE AgriParcelOperation_status_type AS ENUM ('planned', 'ongoing', 'finished', 'scheduled', 'cancelled');
CREATE TYPE AgriParcelOperation_type AS ENUM ('AgriParcelOperation');
CREATE TYPE AgriParcelOperation_waterSource_type AS ENUM ('borehole', 'rainfall', 'river', 'rainwater capture', 'water dam', 'commercial supply');
CREATE TABLE AgriParcelOperation (
  "alternateName" TEXT,
  "dataProvider" TEXT,
  "dateCreated" TIMESTAMP,
  "dateModified" TIMESTAMP,
  "description" TEXT,
  "endedAt" TIMESTAMP,
  "hasAgriParcel" JSON,
  "hasAgriProductType" JSON,
  "hasOperator" JSON,
  "id" TEXT PRIMARY KEY,
  "irrigationRecord" TEXT,
  "name" TEXT,
  "operationType" AgriParcelOperation_operationType_type,
  "owner" JSON,
  "plannedEndAt" TIMESTAMP,
  "plannedStartAt" TIMESTAMP,
  "quantity" NUMERIC,
  "relatedSource" JSON,
  "reportedAt" TIMESTAMP,
  "result" AgriParcelOperation_result_type,
  "seeAlso" JSON,
  "source" TEXT,
  "startedAt" TIMESTAMP,
  "status" AgriParcelOperation_status_type,
  "type" AgriParcelOperation_type,
  "waterSource" AgriParcelOperation_waterSource_type,
  "workOrder" TEXT,
  "workRecord" TEXT
);