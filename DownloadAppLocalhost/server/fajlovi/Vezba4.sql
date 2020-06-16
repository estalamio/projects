--- zadatak1
--select distinct posao
--from radnik

--- zadatak2
--select ime, ime_proj
--from radnik, PROJEKAT,UCESCE
--where radnik.Id_radnika=ucesce.Id_radnika and ucesce.Id_projekta=PROJEKAT.Id_projekta and Ime_proj LIKE 'P%' and kvalif not in('KV')

---zadatak3
--delete
--from ucesce
--where funkcija='KONSULTANT' or Id_radnika in(select Id_radnika from radnik where year(Dat_zap)<year('1980'))

---zadatak4
--select ime
--from radnik
--where rukovodilac in(select Id_radnika from radnik where Id_radnika in(select distinct rukovodilac from radnik) and premija is NULL)

---zadatak5
--select ime 
--from radnik
--where id_radnika in(select distinct rukovodilac from radnik) and premija is null


---zadatak1
--update radnik
--set Id_odeljenja=(select id_odeljenja from ODELJENJE where mesto='Dorćol')
--where Id_radnika in (select Id_radnika from radnik where plata<1200 and id_odeljenja in (select id_odeljenja from odeljenje where mesto='Novi Beograd'))

---zadatak2
--select ime_od
--from odeljenje left join radnik on odeljenje.id_odeljenja=radnik.id_odeljenja
--where id_radnika is null and radnik.id_odeljenja=odeljenje.Id_odeljenja

---zadatak2.1
--select radnik.id_radnika, ime, plata+ISNULL(premija,0) as Primanja, ime_proj
--from radnik, projekat,ucesce
--where RADNIK.Id_radnika=ucesce.Id_radnika 
--and ucesce.Id_projekta=PROJEKAT.Id_projekta 
--and radnik.id_radnika 
--not in(select id_radnika from ucesce where id_projekta in(
--select id_projekta from projekat where ime_proj='Izvoz')) and plata+isnull(premija,0)<1500
--order by Primanja desc, Ime_proj asc

---zadatak3
--select ime, posao
--from radnik, ucesce, projekat, odeljenje
--where (kvalif='KV' and radnik.Id_radnika=ucesce.Id_radnika and ucesce.Id_projekta=projekat.Id_projekta and Ime_proj='izvoz') or 
--(kvalif='VKV' and radnik.Id_radnika=ucesce.Id_radnika and ucesce.Id_projekta=projekat.Id_projekta and Ime_proj='uvoz') 

--Select ime,posao
--FROM radnik
--Where (kvalif='KV' and id_radnika IN (Select id_radnika
--FROM UCESCE WHERE id_projekta IN (Select id_projekta FROM Projekat Where
--ime_proj='izvoz'))
--) OR (kvalif='VKV' and id_radnika IN (Select id_radnika
--FROM UCESCE WHERE id_projekta IN
--(Select id_projekta FROM Projekat Where ime_proj='izvoz')))

---zadatak4
--select ime
--from radnik
--where Id_radnika in(select id_radnika from ucesce where id_projekta in(select id_projekta from projekat where ime_proj='izvoz'))
--and Id_radnika in(select id_radnika from ucesce where id_projekta in(select id_projekta from projekat where ime_proj='uvoz'))

---zadatak5
--delete 
--from ucesce
--where Id_projekta=(select Id_projekta from projekat where 
--ime_proj in ('uvoz')) and 
--id_radnika in (select id_radnika from radnik where 
--(id_radnika in(select id_radnika from ucesce where 
--id_projekta in (select Id_projekta from projekat where ime_proj in('izvoz')))) and
--(id_radnika in (select id_radnika from ucesce where id_projekta in(select 
--Id_projekta from projekat where ime_proj in ('uvoz')))))


---zadatak6
--update PROJEKAT
--set Id_projekta=(select id_projekta from projekat where Ime_proj='uvoz')
--where id_projekta in(select Id_projekta from projekat where Ime_proj='izvoz')

---zadatak7
--select ucesce.id_radnika, ime, sum(br_sati) as BrojSati
--from radnik,projekat,odeljenje,ucesce
--where radnik.Id_radnika=ucesce.Id_radnika
--group by ucesce.id_radnika, ime
--having sum(br_sati) between 1500 and 1900
--order by ime asc

---zadatak8
--select ime_od, kvalif, mesto
--from radnik, odeljenje
--where posao='analitičar' and radnik.Id_odeljenja=odeljenje.Id_odeljenja and odeljenje.Id_odeljenja in
--(select Id_odeljenja from radnik 
--group by Id_odeljenja 
--having count(Id_radnika)>3)

---zadatak9
--select ime
--from radnik
--where id_radnika in(
--	select id_radnika
--	from ucesce
--	group by id_radnika
--	having count(*)=1)
--and posao=(select posao from radnik where ime='Mitar')