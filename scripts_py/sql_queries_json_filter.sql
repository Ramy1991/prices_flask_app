-- SELECT *, price_data->"$.egp[0].*.price" FROM products WHERE MATCH(title_en) 
-- against('%iphone%' IN NATURAL LANGUAGE MODE) AND JSON_SEARCH(price_data->"$.egp[0].*.price", 'one', "None") IS NULL
-- AND country like '%eg%' LIMIT 100;-- UPDATE products SET sold_out = 1 WHERE JSON_EXTRACT(price_data->>'$.egp.*', CONCAT('$[',JSON_LENGTH(price_data->>'$.egp.*.price')-1,'].price')) = 'None'

SELECT  website_name, UIC, unique_product_code, title_en, brand_en, images_url, item_type_en, sub_category_en,
item_upc, link_en, product_direct_link_en, rating, number_of_reviews, 
JSON_EXTRACT(price_data->>'$.egp.*', CONCAT('$[',JSON_LENGTH(price_data->>'$.egp.*.price')-1,'].price')) 
FROM products WHERE 
MATCH(title_en) against('+samsung 50 inch tv' IN NATURAL LANGUAGE MODE ) 
-- AND item_type_en like 'Mobile Phones' 
AND JSON_EXTRACT(price_data->>'$.egp.*', CONCAT('$[',JSON_LENGTH(price_data->>'$.egp.*.price')-1,'].price')) != 'None'
AND sold_out = 0 AND country like '%eg%' LIMIT 40;


