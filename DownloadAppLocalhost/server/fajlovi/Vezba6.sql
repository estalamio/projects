---zadatak1
--create view View_Staz
--as 
--select ime, prezime, posao
--from radnik
--where DATEDIFF(yy, dat_zap, getdate())>(select datediff(yy, dat_zap, getdate()) from radnik where ime='Slobodan' and prezime='Petrović')

---zadatak2
create view View_Ime