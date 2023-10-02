/* (Beta) Export of data model AnimalDisease of the subject dataModel.Agrifood for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE AnimalDisease_type AS ENUM ('AnimalDisease');
CREATE TABLE AnimalDisease (address JSON, alternateName TEXT, animals JSON, areaServed TEXT, dataProvider TEXT, date TIMESTAMP, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, diagnosticTest TEXT, disease TEXT, name TEXT, owner JSON, source TEXT, type AnimalDisease_type, veterinarian TEXT, veterinarianTreatment TEXT);