SELECT *, price_data->"$.egp[0].*.price" FROM products WHERE MATCH(title_en) 
against('%iphone%' IN NATURAL LANGUAGE MODE) AND JSON_SEARCH(price_data->"$.egp[0].*.price", 'one', "None") IS NULL
AND country like '%eg%' LIMIT 100;
 
SELECT *, price_data->"$.egp[0].*.price" FROM products WHERE MATCH(title_en) 
against('%iphone%' IN NATURAL LANGUAGE MODE) AND JSON_CONTAINS(price_data->"$.egp[0].*.price", '"None"') = 0
AND country like '%eg%' ORDER BY item_date DESC LIMIT 100;