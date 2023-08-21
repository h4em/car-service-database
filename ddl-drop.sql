ALTER TABLE Zamowienie
    DROP CONSTRAINT Auto_serwis_Auto;

ALTER TABLE Zamowienie
    DROP CONSTRAINT Auto_serwis_Pracownik;

ALTER TABLE Zamowienie
    DROP CONSTRAINT Auto_serwis_Serwis;

ALTER TABLE Zamowienie
    DROP CONSTRAINT Auto_serwis_Usluga;

ALTER TABLE Auto
    DROP CONSTRAINT Auto_typAuta;

ALTER TABLE Cennik
    DROP CONSTRAINT Cennik_Usluga;

ALTER TABLE Cennik
    DROP CONSTRAINT Cennik_typAuta;

ALTER TABLE Klient
    DROP CONSTRAINT Klient_Auto;

ALTER TABLE Klient
    DROP CONSTRAINT Klient_Osoba;

ALTER TABLE Pracownik
    DROP CONSTRAINT Pracownik_Osoba;

ALTER TABLE Pracownik_Serwis
    DROP CONSTRAINT Pracownik_Serwis_Pracownik;

ALTER TABLE Pracownik_Serwis
    DROP CONSTRAINT Pracownik_Serwis_Serwis;

ALTER TABLE Pracownik
    DROP CONSTRAINT Pracownik_Stanowisko;

ALTER TABLE Serwis
    DROP CONSTRAINT Serwis_Miasto;

ALTER TABLE Serwis
    DROP CONSTRAINT Serwis_Pracownik;

ALTER TABLE Usluga_Serwis
    DROP CONSTRAINT Usluga_Serwis_Serwis;

ALTER TABLE Usluga_Serwis
    DROP CONSTRAINT Usluga_Serwis_Usluga;

DROP TABLE Auto;

DROP TABLE Cennik;

DROP TABLE Klient;

DROP TABLE Miasto;

DROP TABLE Osoba;

DROP TABLE Pracownik;

DROP TABLE Pracownik_Serwis;

DROP TABLE Serwis;

DROP TABLE Stanowisko;

DROP TABLE Usluga;

DROP TABLE Usluga_Serwis;

DROP TABLE Zamowienie;

DROP TABLE typAuta;

