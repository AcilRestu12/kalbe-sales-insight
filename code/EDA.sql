--query 1 : Berapa rata-rata umur customer jika dilihat dari marital statusnya ?
select marital_status as "Status", floor(avg(age)) as "Rata-rata umur"
	from customer where marital_status != '' 
		group by marital_status;

--query 2 : Berapa rata-rata umur customer jika dilihat dari gender nya ?
select gender as "Gender", floor(avg(age)) as "Rata-rata umur"
	from customer 
		group by gender;

--query 3 : Tentukan nama store dengan total quantity terbanyak!
select storename as "Nama store", sum(qty) as "Total quantity" from transaction t
	join store s on t.storeid = s.storeid
		group by storename
			order by "Total quantity" desc
				limit 1;

	
--query 4 : Tentukan nama produk terlaris dengan total amount terbanyak!
select "Product Name" as "Nama product", max(totalamount) as "Total amount"  from "transaction" t
	join product p on t.productid = p.productid 
		group by "Nama product"
			order by "Total amount" desc
				limit 1;
	
	