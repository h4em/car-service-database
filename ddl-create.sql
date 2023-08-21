-- Table: Auto
CREATE TABLE Auto (
    idAuto integer  NOT NULL,
    nrRejestracyjny varchar2(16)  NOT NULL,
    typAuta_idTyp integer  NOT NULL,
    CONSTRAINT Auto_pk PRIMARY KEY (idAuto)
) ;

-- Table: Cennik
CREATE TABLE Cennik (
    Usluga_idUsluga integer  NOT NULL,
    typAuta_idTyp integer  NOT NULL,
    cena number(9,2)  NOT NULL,
    CONSTRAINT Cennik_pk PRIMARY KEY (Usluga_idUsluga,typAuta_idTyp)
) ;

-- Table: Klient
CREATE TABLE Klient (
    Osoba_idOsoba integer  NOT NULL,
    Auto_idAuto integer  NOT NULL,
    CONSTRAINT Klient_pk PRIMARY KEY (Osoba_idOsoba)
) ;

-- Table: Miasto
CREATE TABLE Miasto (
    idMiasto integer  NOT NULL,
    nazwa varchar2(40)  NOT NULL,
    wojewodztwo varchar2(20) NOT NULL,
    CONSTRAINT Miasto_pk PRIMARY KEY (idMiasto)
) ;

-- Table: Osoba
CREATE TABLE Osoba (
    idOsoba integer  NOT NULL,
    imie varchar2(20)  NOT NULL,
    nazwisko varchar2(20)  NOT NULL,
    plec integer  NOT NULL,
    nrTel varchar2(9)  NULL,
    adresEmail varchar2(20)  NULL,
    CONSTRAINT Osoba_pk PRIMARY KEY (idOsoba)
) ;

-- Table: Pracownik
CREATE TABLE Pracownik (
    Osoba_idOsoba integer  NOT NULL,
    PESEL varchar2(11)  NOT NULL,
    Stanowisko_idStanowisko integer  NOT NULL,
    dataZatrudnienia date  NOT NULL,
    dataZwolnienia date  NULL,
    CONSTRAINT Pracownik_pk PRIMARY KEY (Osoba_idOsoba)
) ;

-- Table: Pracownik_Serwis
CREATE TABLE Pracownik_Serwis (
    Serwis_idSerwis integer  NOT NULL,
    Pracownik_Osoba_idOsoba integer  NOT NULL,
    CONSTRAINT Pracownik_Serwis_pk PRIMARY KEY (Pracownik_Osoba_idOsoba,Serwis_idSerwis)
) ;

-- Table: Serwis
CREATE TABLE Serwis (
    idSerwis integer  NOT NULL,
    Miasto_idMiasto integer  NOT NULL,
    Adres varchar2(40)  NOT NULL,
    Pracownik_Osoba_idOsoba integer  NOT NULL,
    CONSTRAINT Serwis_pk PRIMARY KEY (idSerwis)
) ;

-- Table: Stanowisko
CREATE TABLE Stanowisko (
    idStanowisko integer  NOT NULL,
    nazwa varchar2(20)  NOT NULL,
    CONSTRAINT Stanowisko_pk PRIMARY KEY (idStanowisko)
) ;

-- Table: Usluga
CREATE TABLE Usluga (
    idUsluga integer  NOT NULL,
    nazwa varchar2(20)  NOT NULL,
    CONSTRAINT Usluga_pk PRIMARY KEY (idUsluga)
) ;

-- Table: Usluga_Serwis
CREATE TABLE Usluga_Serwis (
    Serwis_idSerwis integer  NOT NULL,
    Usluga_idUsluga integer  NOT NULL,
    CONSTRAINT Usluga_Serwis_pk PRIMARY KEY (Serwis_idSerwis,Usluga_idUsluga)
) ;

-- Table: Zamowienie
CREATE TABLE Zamowienie (
    idZamowienie integer  NOT NULL,
    Auto_idAuto integer  NOT NULL,
    Serwis_idSerwis integer  NOT NULL,
    Pracownik_Osoba_idOsoba integer  NOT NULL,
    Usluga_idUsluga integer  NOT NULL,
    dataRozpoczecia date  NULL,
    dataZakonczenia date  NULL,
    status varchar2(10)  NOT NULL,
    CONSTRAINT Zamowienie_pk PRIMARY KEY (idZamowienie)
) ;

-- Table: typAuta
CREATE TABLE typAuta (
    idTyp integer  NOT NULL,
    nazwa varchar2(20)  NOT NULL,
    CONSTRAINT typAuta_pk PRIMARY KEY (idTyp)
) ;

-- Reference: Auto_serwis_Auto (table: Zamowienie)
ALTER TABLE Zamowienie ADD CONSTRAINT Auto_serwis_Auto
    FOREIGN KEY (Auto_idAuto)
    REFERENCES Auto (idAuto);

-- Reference: Auto_serwis_Pracownik (table: Zamowienie)
ALTER TABLE Zamowienie ADD CONSTRAINT Auto_serwis_Pracownik
    FOREIGN KEY (Pracownik_Osoba_idOsoba)
    REFERENCES Pracownik (Osoba_idOsoba);

-- Reference: Auto_serwis_Serwis (table: Zamowienie)
ALTER TABLE Zamowienie ADD CONSTRAINT Auto_serwis_Serwis
    FOREIGN KEY (Serwis_idSerwis)
    REFERENCES Serwis (idSerwis);

-- Reference: Auto_serwis_Usluga (table: Zamowienie)
ALTER TABLE Zamowienie ADD CONSTRAINT Auto_serwis_Usluga
    FOREIGN KEY (Usluga_idUsluga)
    REFERENCES Usluga (idUsluga);

-- Reference: Auto_typAuta (table: Auto)
ALTER TABLE Auto ADD CONSTRAINT Auto_typAuta
    FOREIGN KEY (typAuta_idTyp)
    REFERENCES typAuta (idTyp);

-- Reference: Cennik_Usluga (table: Cennik)
ALTER TABLE Cennik ADD CONSTRAINT Cennik_Usluga
    FOREIGN KEY (Usluga_idUsluga)
    REFERENCES Usluga (idUsluga);

-- Reference: Cennik_typAuta (table: Cennik)
ALTER TABLE Cennik ADD CONSTRAINT Cennik_typAuta
    FOREIGN KEY (typAuta_idTyp)
    REFERENCES typAuta (idTyp);

-- Reference: Klient_Auto (table: Klient)
ALTER TABLE Klient ADD CONSTRAINT Klient_Auto
    FOREIGN KEY (Auto_idAuto)
    REFERENCES Auto (idAuto);

-- Reference: Klient_Osoba (table: Klient)
ALTER TABLE Klient ADD CONSTRAINT Klient_Osoba
    FOREIGN KEY (Osoba_idOsoba)
    REFERENCES Osoba (idOsoba);

-- Reference: Pracownik_Osoba (table: Pracownik)
ALTER TABLE Pracownik ADD CONSTRAINT Pracownik_Osoba
    FOREIGN KEY (Osoba_idOsoba)
    REFERENCES Osoba (idOsoba);

-- Reference: Pracownik_Serwis_Pracownik (table: Pracownik_Serwis)
ALTER TABLE Pracownik_Serwis ADD CONSTRAINT Pracownik_Serwis_Pracownik
    FOREIGN KEY (Pracownik_Osoba_idOsoba)
    REFERENCES Pracownik (Osoba_idOsoba);

-- Reference: Pracownik_Serwis_Serwis (table: Pracownik_Serwis)
ALTER TABLE Pracownik_Serwis ADD CONSTRAINT Pracownik_Serwis_Serwis
    FOREIGN KEY (Serwis_idSerwis)
    REFERENCES Serwis (idSerwis);

-- Reference: Pracownik_Stanowisko (table: Pracownik)
ALTER TABLE Pracownik ADD CONSTRAINT Pracownik_Stanowisko
    FOREIGN KEY (Stanowisko_idStanowisko)
    REFERENCES Stanowisko (idStanowisko);

-- Reference: Serwis_Miasto (table: Serwis)
ALTER TABLE Serwis ADD CONSTRAINT Serwis_Miasto
    FOREIGN KEY (Miasto_idMiasto)
    REFERENCES Miasto (idMiasto);

-- Reference: Serwis_Pracownik (table: Serwis)
ALTER TABLE Serwis ADD CONSTRAINT Serwis_Pracownik
    FOREIGN KEY (Pracownik_Osoba_idOsoba)
    REFERENCES Pracownik (Osoba_idOsoba);

-- Reference: Usluga_Serwis_Serwis (table: Usluga_Serwis)
ALTER TABLE Usluga_Serwis ADD CONSTRAINT Usluga_Serwis_Serwis
    FOREIGN KEY (Serwis_idSerwis)
    REFERENCES Serwis (idSerwis);

-- Reference: Usluga_Serwis_Usluga (table: Usluga_Serwis)
ALTER TABLE Usluga_Serwis ADD CONSTRAINT Usluga_Serwis_Usluga
    FOREIGN KEY (Usluga_idUsluga)
    REFERENCES Usluga (idUsluga);

