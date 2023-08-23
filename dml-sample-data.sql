--typAuta
INSERT INTO typAuta (idTyp, nazwa)
VALUES (1, 'Osobowy');

INSERT INTO typAuta (idTyp, nazwa)
VALUES (2, 'Terenowy');

INSERT INTO typAuta (idTyp, nazwa)
VALUES (3, 'Camper');

--Osoba
INSERT INTO Osoba (idOsoba, imie, nazwisko, plec, nrTel, adresEmail)
VALUES (1, 'Jan', 'Kowalski', 1, '123456789', 'jankowalsk@gmail.com');

INSERT INTO Osoba (idOsoba, imie, nazwisko, plec, nrTel, adresEmail)
VALUES (2, 'Anna', 'Nowak', 2, '987654321', 'annanowak@gmail.com');

INSERT INTO Osoba (idOsoba, imie, nazwisko, plec, nrTel, adresEmail)
VALUES (3, 'Piotr', 'Nowicki', 1, NULL, 'piotrnow@gmail.com');

INSERT INTO Osoba (idOsoba, imie, nazwisko, plec, nrTel, adresEmail)
VALUES (4, 'Adam', 'Przegub', 1, NULL, 'przegub@gmail.com');

INSERT INTO Osoba (idOsoba, imie, nazwisko, plec, nrTel, adresEmail)
VALUES (5, 'Maja', 'Nowicka', 2, '999666777', 'nowicka@gmail.com');

INSERT INTO Osoba (idOsoba, imie, nazwisko, plec, nrTel, adresEmail)
VALUES (6, 'Krystian', 'Nowak', 1, '666999777', 'krystian@gmail.com');

INSERT INTO Osoba (idOsoba, imie, nazwisko, plec, nrTel, adresEmail)
VALUES (7, 'Slawek', 'Mrozek', 1, '887654321', 'slawoj@gmail.com');

INSERT INTO Osoba (idOsoba, imie, nazwisko, plec, nrTel, adresEmail)
VALUES (8, 'Adam', 'Sandler', 1, NULL, 'przegub@gmail.com');

INSERT INTO Osoba (idOsoba, imie, nazwisko, plec, nrTel, adresEmail)
VALUES (9, 'Kasia', 'Bogaj', 2, '999666777', 'bogaj@gmail.com');

INSERT INTO Osoba (idOsoba, imie, nazwisko, plec, nrTel, adresEmail)
VALUES (10, 'Bogusz', 'Nowak', 1, '666999777', 'bogusz@gmail.com');

INSERT INTO Osoba (idOsoba, imie, nazwisko, plec, nrTel, adresEmail)
VALUES (11, 'Antek', 'Kaczmarek', 1, '887654321', 'kaczm@gmail.com');

INSERT INTO Osoba (idOsoba, imie, nazwisko, plec, nrTel, adresEmail)
VALUES (12, 'Wiktor', 'Nowak', 1, '666999777', 'wikno@gmail.com');

INSERT INTO Osoba (idOsoba, imie, nazwisko, plec, nrTel, adresEmail)
VALUES (13, 'Antek', 'Kostana', 1, '887654321', 'antek@gmail.com');

--Usluga
INSERT INTO Usluga (idUsluga, nazwa)
VALUES (1, 'Naprawa silnika');

INSERT INTO Usluga (idUsluga, nazwa)
VALUES (2, 'Wymiana opon');

INSERT INTO Usluga (idUsluga, nazwa)
VALUES (3, 'Przegląd techniczny');

INSERT INTO Usluga (idUsluga, nazwa)
VALUES (4, 'Wymiana oleju');

--Miasto
INSERT INTO Miasto (idMiasto, nazwa, wojewodztwo)
VALUES (1, 'Warszawa', 'Mazowieckie');

INSERT INTO Miasto (idMiasto, nazwa, wojewodztwo)
VALUES (2, 'Kraków', 'Małopolskie');

INSERT INTO Miasto (idMiasto, nazwa, wojewodztwo)
VALUES (3, 'Gdańsk', 'Pomorskie');

--Stanowisko
INSERT INTO Stanowisko (idStanowisko, nazwa)
VALUES (1, 'Dyrektor');

INSERT INTO Stanowisko (idStanowisko, nazwa)
VALUES (2, 'Mechanik');

INSERT INTO Stanowisko (idStanowisko, nazwa)
VALUES (3, 'Sprzedawca');

--Auto
INSERT INTO Auto (idAuto, nrRejestracyjny, typAuta_idTyp)
VALUES (1, 'ABC123', 1);

INSERT INTO Auto (idAuto, nrRejestracyjny, typAuta_idTyp)
VALUES (2, 'DEF456', 2);

INSERT INTO Auto (idAuto, nrRejestracyjny, typAuta_idTyp)
VALUES (3, 'GHI789', 1);

INSERT INTO Auto (idAuto, nrRejestracyjny, typAuta_idTyp)
VALUES (4, 'JKL012', 3);

INSERT INTO Auto (idAuto, nrRejestracyjny, typAuta_idTyp)
VALUES (5, 'JWP997', 3);

--Pracownik
INSERT INTO Pracownik (Osoba_idOsoba, PESEL, Stanowisko_idStanowisko, dataZatrudnienia, dataZwolnienia)
VALUES (1, '12345678881', 1, DATE '2022-01-01', NULL);

INSERT INTO Pracownik (Osoba_idOsoba, PESEL, Stanowisko_idStanowisko, dataZatrudnienia, dataZwolnienia)
VALUES (6, '98765432109', 2, DATE '2022-02-15', DATE '2023-05-31');

INSERT INTO Pracownik (Osoba_idOsoba, PESEL, Stanowisko_idStanowisko, dataZatrudnienia, dataZwolnienia)
VALUES (3, '56789333345', 2, DATE '2022-03-10', NULL);

INSERT INTO Pracownik (Osoba_idOsoba, PESEL, Stanowisko_idStanowisko, dataZatrudnienia, dataZwolnienia)
VALUES (4, '56789066645', 1, DATE '2022-03-10', NULL);

INSERT INTO Pracownik (Osoba_idOsoba, PESEL, Stanowisko_idStanowisko, dataZatrudnienia, dataZwolnienia)
VALUES (5, '56789066645', 3, DATE '2022-03-10', NULL);

INSERT INTO Pracownik (Osoba_idOsoba, PESEL, Stanowisko_idStanowisko, dataZatrudnienia, dataZwolnienia)
VALUES (7, '56712366645', 1, DATE '2022-03-11', NULL);

INSERT INTO Pracownik (Osoba_idOsoba, PESEL, Stanowisko_idStanowisko, dataZatrudnienia, dataZwolnienia)
VALUES (12, '56789066645', 2, DATE '2022-03-10', NULL);

INSERT INTO Pracownik (Osoba_idOsoba, PESEL, Stanowisko_idStanowisko, dataZatrudnienia, dataZwolnienia)
VALUES (13, '99912366645', 2, DATE '2022-03-11', NULL);

--Klient (1 klient moze miec tylko 1 samochod !!! to jest straszny blad)
INSERT INTO Klient (Osoba_idOsoba, Auto_idAuto)
VALUES (2, 1);

INSERT INTO Klient (Osoba_idOsoba, Auto_idAuto)
VALUES (8, 2);

INSERT INTO Klient (Osoba_idOsoba, Auto_idAuto)
VALUES (9, 3);

INSERT INTO Klient (Osoba_idOsoba, Auto_idAuto)
VALUES (10, 4);

INSERT INTO Klient (Osoba_idOsoba, Auto_idAuto)
VALUES (11, 5);

--Serwis
INSERT INTO Serwis (idSerwis, Miasto_idMiasto, Adres, Pracownik_Osoba_idOsoba)
VALUES (1, 1, 'ul. Bielszowicka 1', 4);

INSERT INTO Serwis (idSerwis, Miasto_idMiasto, Adres, Pracownik_Osoba_idOsoba)
VALUES (2, 1, 'ul. Marszalkowska 12', 7);

INSERT INTO Serwis (idSerwis, Miasto_idMiasto, Adres, Pracownik_Osoba_idOsoba)
VALUES (3, 2, 'ul. Pomorska 3', 1);

--Cennik
INSERT INTO Cennik (Usluga_idUsluga, typAuta_idTyp, cena)
VALUES (1, 1, 800.00);

INSERT INTO Cennik (Usluga_idUsluga, typAuta_idTyp, cena)
VALUES (1, 2, 1200.00);

INSERT INTO Cennik (Usluga_idUsluga, typAuta_idTyp, cena)
VALUES (1, 3, 1800.00);

INSERT INTO Cennik (Usluga_idUsluga, typAuta_idTyp, cena)
VALUES (2, 1, 150.00);

INSERT INTO Cennik (Usluga_idUsluga, typAuta_idTyp, cena)
VALUES (2, 2, 200.00);

INSERT INTO Cennik (Usluga_idUsluga, typAuta_idTyp, cena)
VALUES (2, 3, 250.00);

INSERT INTO Cennik (Usluga_idUsluga, typAuta_idTyp, cena)
VALUES (3, 1, 900.00);

INSERT INTO Cennik (Usluga_idUsluga, typAuta_idTyp, cena)
VALUES (3, 2, 1000.00);

INSERT INTO Cennik (Usluga_idUsluga, typAuta_idTyp, cena)
VALUES (3, 3, 1900.00);

INSERT INTO Cennik (Usluga_idUsluga, typAuta_idTyp, cena)
VALUES (4, 1, 100.00);

INSERT INTO Cennik (Usluga_idUsluga, typAuta_idTyp, cena)
VALUES (4, 2, 120.00);

INSERT INTO Cennik (Usluga_idUsluga, typAuta_idTyp, cena)
VALUES (4, 3, 190.00);

--Usluga_serwis

INSERT INTO Usluga_Serwis (Serwis_idSerwis, Usluga_idUsluga)
VALUES (1, 1);

INSERT INTO Usluga_Serwis (Serwis_idSerwis, Usluga_idUsluga)
VALUES (1, 2);

INSERT INTO Usluga_Serwis (Serwis_idSerwis, Usluga_idUsluga)
VALUES (1, 3);

INSERT INTO Usluga_Serwis (Serwis_idSerwis, Usluga_idUsluga)
VALUES (2, 1);

INSERT INTO Usluga_Serwis (Serwis_idSerwis, Usluga_idUsluga)
VALUES (2, 3);

INSERT INTO Usluga_Serwis (Serwis_idSerwis, Usluga_idUsluga)
VALUES (3, 2);

--Pracownik_serwis
INSERT INTO Pracownik_Serwis (Serwis_idSerwis, Pracownik_Osoba_idOsoba)
VALUES (3, 1);

INSERT INTO Pracownik_Serwis (Serwis_idSerwis, Pracownik_Osoba_idOsoba)
VALUES (1, 4);

INSERT INTO Pracownik_Serwis (Serwis_idSerwis, Pracownik_Osoba_idOsoba)
VALUES (1, 3);

INSERT INTO Pracownik_Serwis (Serwis_idSerwis, Pracownik_Osoba_idOsoba)
VALUES (1, 5);

INSERT INTO Pracownik_Serwis (Serwis_idSerwis, Pracownik_Osoba_idOsoba)
VALUES (2, 13);

INSERT INTO Pracownik_Serwis (Serwis_idSerwis, Pracownik_Osoba_idOsoba)
VALUES (2, 7);

INSERT INTO Pracownik_Serwis (Serwis_idSerwis, Pracownik_Osoba_idOsoba)
VALUES (3, 12);

INSERT INTO Pracownik_Serwis (Serwis_idSerwis, Pracownik_Osoba_idOsoba)
VALUES (2, 6);

--Zamowienie
INSERT INTO Zamowienie (idZamowienie, Auto_idAuto, Serwis_idSerwis, Pracownik_Osoba_idOsoba, Usluga_idUsluga, dataRozpoczecia, dataZakonczenia, status)
VALUES (1, 1, 1, 3, 1, TO_DATE('2023-06-20', 'YYYY-MM-DD'), TO_DATE('2023-06-25', 'YYYY-MM-DD'), 'Zakonczona');

INSERT INTO Zamowienie (idZamowienie, Auto_idAuto, Serwis_idSerwis, Pracownik_Osoba_idOsoba, Usluga_idUsluga, dataRozpoczecia, dataZakonczenia, status)
VALUES (2, 1, 1, 3, 4, TO_DATE('2023-06-18', 'YYYY-MM-DD'), NULL, 'W trakcie');

INSERT INTO Zamowienie (idZamowienie, Auto_idAuto, Serwis_idSerwis, Pracownik_Osoba_idOsoba, Usluga_idUsluga, dataRozpoczecia, dataZakonczenia, status)
VALUES (3, 2, 1, 3, 2, TO_DATE('2023-06-13', 'YYYY-MM-DD'), TO_DATE('2023-06-16', 'YYYY-MM-DD'), 'Zakonczona');

INSERT INTO Zamowienie (idZamowienie, Auto_idAuto, Serwis_idSerwis, Pracownik_Osoba_idOsoba, Usluga_idUsluga, dataRozpoczecia, dataZakonczenia, status)
VALUES (4, 3, 2, 6, 3, TO_DATE('2023-06-19', 'YYYY-MM-DD'), NULL, 'Oczekuje');

INSERT INTO Zamowienie (idZamowienie, Auto_idAuto, Serwis_idSerwis, Pracownik_Osoba_idOsoba, Usluga_idUsluga, dataRozpoczecia, dataZakonczenia, status)
VALUES (5, 3, 2, 13, 1, TO_DATE('2023-06-15', 'YYYY-MM-DD'), TO_DATE('2023-06-18', 'YYYY-MM-DD'), 'Zakonczona');

INSERT INTO Zamowienie (idZamowienie, Auto_idAuto, Serwis_idSerwis, Pracownik_Osoba_idOsoba, Usluga_idUsluga, dataRozpoczecia, dataZakonczenia, status)
VALUES (6, 4, 3, 12, 1, TO_DATE('2023-06-19', 'YYYY-MM-DD'), NULL, 'W trakcie');

INSERT INTO Zamowienie (idZamowienie, Auto_idAuto, Serwis_idSerwis, Pracownik_Osoba_idOsoba, Usluga_idUsluga, dataRozpoczecia, dataZakonczenia, status)
VALUES (7, 5, 2, 7, 3, TO_DATE('2023-06-20', 'YYYY-MM-DD'), NULL, 'W trakcie');

