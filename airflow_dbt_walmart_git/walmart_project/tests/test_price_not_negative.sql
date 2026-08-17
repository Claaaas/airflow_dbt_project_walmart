-- Test custom : vérifier que price n'est pas négatif
select *
from {{ ref('products_t') }}
where price < 0
   or price is null
