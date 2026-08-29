select brand, model,color from cars
where color is '%red%' 
and brand != 'Ferrari' 
and sold is False

select brand, model, color from cars
where color not in ('%red%', '%blue%', '%white%')
and brand not in ('Aston Martin', 'Bentley', 'Jaguar')
and sold is False

select brand, model, year, sold from cars
where ((brand = 'Dodge' and year between 1960 and 1969)
or (brand ='Ford' or brand = 'Triumph' 
and year between 1970 and 1979)
and sold is not true

