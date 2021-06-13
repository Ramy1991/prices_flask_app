

-- SELECT  website_name, UIC, unique_product_code, title_en, brand_en, images_url, 
-- item_tybe_en, sub_category_en, item_upc, link_en, product_direct_link_en, rating, number_of_reviews, 
-- JSON_EXTRACT(price_data->>'$.egp.*', CONCAT('$[',JSON_LENGTH(price_data->>'$.egp.*.price')-1,'].price')) 
-- FROM products WHERE item_tybe_en = (
--   SELECT item_tybe_en FROM search_mapping WHERE 
--   MATCH(search_key_s) against('+"tshirt"' IN BOOLEAN MODE) order by search_order ASC limit 2
-- ) AND MATCH(title_en) against('+t shirt' IN NATURAL LANGUAGE MODE ) AND
-- JSON_EXTRACT(price_data->>'$.egp.*', CONCAT('$[',JSON_LENGTH(price_data->>'$.egp.*.price')-1,'].price')) != 'None' AND
-- sold_out = 0 AND country like '%eg%' LIMIT 40;


 WITH r AS (SELECT  website_name, UIC, unique_product_code, title_en, brand_en,
 images_url, item_tybe_em, sub_category_en, item_upc, link_en, 
product_direct_link_en, rating, 
number_of_reviews, JSON_EXTRACT(price_data->>'$.egp.*', CONCAT('$[',JSON_LENGTH(price_data->>'$.egp.*.price')-1,'].price')) 
FROM products WHERE item_tybe_en = (SELECT item_tybe_en FROM search_mapping WHERE 
MATCH(search_key_s) against('+iphone' IN NATURAL LANGUAGE MODE) 
order by search_order ASC limit 1
) AND MATCH(title_en) against('+iphone' IN NATURAL LANGUAGE MODE ) AND
 JSON_EXTRACT(price_data->>'$.egp.*', CONCAT('$[',JSON_LENGTH(price_data->>'$.egp.*.price')-1,'].price')) != 'None' AND
 sold_out = 0 AND country like '%eg%' LIMIT 60) 
SELECT * FROM r
UNION ALL
SELECT  website_name, UIC, unique_product_code, title_en, brand_en, 
images_url, item_tybe_en, sub_category_en,
item_upc, link_en, product_direct_link_en, rating, number_of_reviews, 
JSON_EXTRACT(price_data->>'$.egp.*', CONCAT('$[',JSON_LENGTH(price_data->>'$.egp.*.price')-1,'].price')) 
FROM products WHERE 
MATCH(title_en) against('+iphone' IN BOOLEAN MODE ) 
AND JSON_EXTRACT(price_data->>'$.egp.*', CONCAT('$[',JSON_LENGTH(price_data->>'$.egp.*.price')-1,'].price')) != 'None'
AND sold_out = 0 AND country like '%eg%' AND NOT EXISTS (SELECT * FROM r) LIMIT 60;


