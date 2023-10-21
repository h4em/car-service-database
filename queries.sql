--Wyswietl wszyskie osoby z nazwiskiem 'Nowak'
SELECT idOsoba, imie, nazwisko 
FROM Osoba 
WHERE nazwisko LIKE 'Nowak';

--Wyswietl wszystkie zamowienia ze statusem 'Oczekuje'
SELECT * 
FROM Zamowienie 
WHERE status LIKE 'Oczekuje';

--Wyswietl wszystkich pracownikow obecnie pracujacych jeszcze w filii. 
SELECT * 
FROM Pracownik 
WHERE dataZwolnienia IS NULL;

--Wyswietl dane o wszystkich pracownikach
SELECT * 
FROM Osoba
WHERE idOsoba IN (
    SELECT Osoba_idOsoba 
    FROM Pracownik 
    WHERE Pracownik.Osoba_idOsoba = idOsoba
);

--Dla kazdego miasta wyswietl liczbe znajdujacych sie w nim serwisow
SELECT nazwa, COUNT(*)
FROM Miasto
JOIN Serwis ON Miasto.idMiasto = Serwis.Miasto_idMiasto
GROUP BY nazwa;

--Wyswietl serwis swiadczacy najwiecej roznych uslug
SELECT * 
FROM Serwis 
WHERE idSerwis IN (
    SELECT Serwis_idSerwis
    FROM Usluga_Serwis
    GROUP BY Serwis_idSerwis
    ORDER BY COUNT(*) FETCH FIRST 1 ROW ONLY
);

--Wyswietl stanowisko na ktorym zatrudnionych jest najwiecej osob. 
SELECT nazwa
FROM Pracownik
JOIN Stanowisko ON Pracownik.Stanowisko_idStanowisko = Stanowisko.idStanowisko
GROUP BY nazwa
ORDER BY COUNT(*) DESC
FETCH FIRST 1 ROW ONLY;

--Wyswietl wszystkich pracownikow na stanowisku dyrektor
SELECT * 
FROM Osoba, Pracownik, Stanowisko
WHERE Pracownik.Osoba_idOsoba = Osoba.idOsoba
AND Pracownik.Stanowisko_idStanowisko = Stanowisko.idStanowisko
AND Stanowisko.nazwa LIKE 'Dyrektor'
AND dataZwolnienia IS NULL;

--Dla kazdego serwisu wyswietl ilu pracuje w nim mechanikow
SELECT Serwis.idSerwis, Miasto.nazwa, COUNT(*)
FROM Serwis
JOIN Pracownik_Serwis ON Serwis.idSerwis = Pracownik_Serwis.Serwis_idSerwis
JOIN Pracownik ON Pracownik_Serwis.pracownik_osoba_idosoba = Pracownik.Osoba_idOsoba
JOIN Stanowisko ON Pracownik.stanowisko_idstanowisko = Stanowisko.idStanowisko
JOIN Miasto ON Serwis.Miasto_idmiasto = Miasto.idMiasto
WHERE Stanowisko.nazwa LIKE 'Mechanik'
GROUP BY Serwis.idSerwis, Miasto.nazwa
ORDER BY Serwis.idSerwis;

--Dla kazdego typu auta oblicz sredni koszt swiadczonych uslug
SELECT nazwa, AVG(cena) 
FROM Cennik, typAuta
WHERE Cennik.typAuta_idTyp = typAuta.idTyp
GROUP BY nazwa;

--Dla kazdego serwisu podaj liczbe przeprowadzonych zamowien
SELECT idSerwis, COUNT(*) 
FROM Serwis, Zamowienie
WHERE Serwis.idSerwis = Zamowienie.Serwis_idSerwis
AND Zamowienie.status LIKE 'Zakonczona'
GROUP BY idSerwis;

--Podaj imie i nazwisko klienta ktory zlozyl najwiecej zamowien
SELECT idOsoba, imie, nazwisko
FROM Osoba
JOIN Klient ON Klient.Osoba_idOsoba = Osoba.idOsoba
JOIN Auto ON Klient.Auto_idAuto = Auto.idAuto
JOIN Zamowienie ON Zamowienie.Auto_idAuto = Auto.idAuto
GROUP BY idOsoba, imie, nazwisko
ORDER BY COUNT(*) ASC
FETCH FIRST 1 ROW ONLY;

--Dla kazdego typu auta podaj liczbe przeprowadzonych zamowien.
SELECT nazwa, COUNT(*) 
FROM typAuta, Auto, Zamowienie
WHERE Zamowienie.Auto_idAuto = Auto.idAuto 
AND typAuta.idTyp = auto.typauta_idtyp
GROUP BY nazwa
ORDER BY COUNT(*) DESC;

--Podaj srednia liczbe pracownikow pracujacych w jednym serwisie
SELECT ROUND(AVG(suma), 2) FROM (
    SELECT Serwis_idSerwis, COUNT(*) AS suma
    FROM Pracownik_Serwis
    GROUP BY Serwis_idSerwis
);

--Wyswietl najczesciej wybierana usluge
SELECT nazwa
FROM Usluga
JOIN Zamowienie ON Zamowienie.usluga_idusluga = Usluga.idUsluga
GROUP BY nazwa
ORDER BY COUNT(*) DESC
FETCH FIRST 1 ROW ONLY;

--Wyswietl imie i nazwisko pracownika z najdluzszym stazem
SELECT imie, nazwisko 
FROM Osoba, Pracownik
WHERE Pracownik.Osoba_idOsoba = Osoba.idOsoba
AND dataZatrudnienia = (
    SELECT MAX(dataZatrudnienia)
    FROM Pracownik
);

--Wyswietl typ auta dla ktorego sredni koszt uslugi przekracza 1000zl
SELECT nazwa, AVG(cena) 
FROM Cennik, typAuta
WHERE Cennik.typAuta_idTyp = typAuta.idTyp
GROUP BY nazwa 
HAVING AVG(cena) > 1000.00;

--Wyswietl imiona i nazwiska mechanikow ktorzy przeprowadzili conajmniej 1 naprawe
SELECT DISTINCT Osoba.idOsoba, imie, nazwisko 
FROM Osoba, Pracownik
WHERE Pracownik.Osoba_idOsoba = Osoba.idOsoba 
AND Osoba.idOsoba IN (
    SELECT Pracownik_Osoba_idOsoba FROM Zamowienie
)
ORDER BY Osoba.idOsoba ASC;

--Wyswietl serwisy w ktorych liczba przeprowadzanych uslug jest wieksza od sredniej.
SELECT Serwis.idSerwis, Miasto.nazwa
FROM Serwis, Miasto
WHERE Serwis.Miasto_idMiasto = Miasto.idMiasto
AND Serwis.idSerwis IN (
    SELECT Serwis_idSerwis
    FROM Usluga_Serwis
    GROUP BY Serwis_idSerwis
    HAVING COUNT(*) > (
        SELECT AVG(countUslugi)
        FROM (
            SELECT Serwis_idSerwis, COUNT(*) AS countUslugi
            FROM Usluga_Serwis
            GROUP BY Serwis_idSerwis
        )
    )
);

--Wyswietl typ auta dla ktorego najczesciej byly przeprowadzane uslugi
SELECT typAuta.nazwa
FROM typAuta 
WHERE idTyp = (
    SELECT typAuta_idTyp
    FROM Auto
    JOIN Zamowienie ON Zamowienie.Auto_idAuto = Auto.idAuto 
    GROUP BY typAuta_idTyp
    ORDER BY COUNT(*) DESC
    FETCH FIRST 1 ROW ONLY
);