---zadatak1
--select Id_odeljenja, avg(plata) AS 'ProcesnaPlata'
--from radnik
--group by Id_odeljenja
--having avg(plata)>2000

---zadatak2
--select Ime_proj, count(radnik.Id_radnika)
--from projekat, radnik,ucesce
--where UCESCE.Id_projekta=PROJEKAT.Id_projekta
--group by Ime_proj
--having count(radnik.Id_radnika)>3

---zadatak3
--select ime, (plata+isnull(premija,0)) as 'Primanja'
--from radnik
--WHERE plata+premija > (SELECT AVG(plata + ISNULL(premija,0)) FROM radnik)

---zadatak4
--select radnik.id_radnika, ime, Ime_proj, plata+isnull(premija,0) as [UKUPNA PRIMANJA]
--from radnik, projekat, ucesce
--where  RADNIK.Id_radnika = UCESCE.ID_radnika and PROJEKAT.Id_projekta=UCESCE.Id_projekta AND Ime_proj not in('izvoz') and (plata +
--ISNULL(premija,0)) <1500
--order by (plata+isnull(premija,0)) desc, Ime_proj asc

---zadatak5
--SELECT Ime, Posao, PROJEKAT.Id_projekta, Ime_proj 
--FROM RADNIK 
--RIGHT JOIN UCESCE 
--ON RADNIK.Id_radnika=UCESCE.Id_radnika RIGHT JOIN PROJEKAT 
--ON PROJEKAT.Id_projekta=UCESCE.Id_projekta


---zadatak6
--select radnik.ime, projekat.Ime_proj
--from ((radnik
--INNER JOIN ucesce on radnik.Id_radnika=ucesce.Id_radnika)
--INNER JOIN projekat on ucesce.Id_projekta=projekat.Id_projekta);

---zadatak7
--insert into projekat VALUES(600, 'Obrazovanje', 2000000, NULL)

---zadatak8
--create table Upravnik(id_radnika int not null, ime varchar(25), dat_zap DATETIME, id_odeljenja int not null)
--insert into Upravnik(id_radnika, ime, dat_zap, id_odeljenja)

--select id_radnika, ime, Dat_zap, Id_odeljenja 
--from radnik
--where posao='Upravnik'

---zadatak9
--update radnik 
--set premija=plata*0.4
--where Id_odeljenja in(select Id_odeljenja from odeljenje where Mesto='Dorćol') and posao not in('direktor','upravnik')

---zadatak10
update radnik
set premija=case 
when premija is null then 10 
when premija between 0 and 1000 then premija*0.9 
else premija end