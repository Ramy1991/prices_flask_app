<?php
include 'Classes/PHPExcel/IOFactory.php';
include 'Super_Cate.php';
require_once 'DB_Access.php';
function getCellNamaFromNumber($num)
{
    $numeric = ($num) % 26;
    $letter = chr(65 + $numeric);
    $num2 = intval(($num) / 26);
    if ($num2 > 0) {
        return getCellNamaFromNumber($num2 - 1) . $letter;
    } else {
        return $letter;
    }
}

function unique_code($limit)
{
    return strtoupper(substr(base_convert(sha1(uniqid(mt_rand())), 16, 36), 0, $limit));
}

function remove_special_characters($string)
{
    $string2 = preg_replace("/['|\\\|,|\s\/|-|.|@|$|%|(|)|_|&|+|=|^|{|}|<|>|\"|!|?|:|;]+/", "-", $string);
    return preg_replace("/[-]+/", "-", $string2);
}
$objPHPExcel = PHPExcel_IOFactory::load('scrapy.xlsx');
$worksheet = $objPHPExcel->getSheet(0);
$lastRow = $worksheet->getHighestRow();
$allDataInSheet = $objPHPExcel->setActiveSheetIndex(0)->rangeToArray('A1:Z1');

$Unique_Product_Code_key = array_search('ean', $allDataInSheet[0]);
$Country_key = array_search('Country', $allDataInSheet[0]);
$Brand_ar_key = array_search('Brand_ar', $allDataInSheet[0]);
$Brand_en_key = array_search('Brand_en', $allDataInSheet[0]);
$Description_ar_key = array_search('Description_ar', $allDataInSheet[0]);
$Description_en_key = array_search('Description_en', $allDataInSheet[0]);
$Item_Specs_ar_key = array_search('Item_Specs_ar', $allDataInSheet[0]);
$Item_Specs_en_key = array_search('Item_Specs_en', $allDataInSheet[0]);
$Item_Type_AR_key = array_search('Item_Type_AR', $allDataInSheet[0]);
$Item_Type_EN_key = array_search('Item_Type_EN', $allDataInSheet[0]);
$Price_EG_key = array_search('Price_EG', $allDataInSheet[0]);
$Product_Direct_Link_ar_key = array_search('Product_Direct_Link_ar', $allDataInSheet[0]);
$Product_Direct_Link_en_key = array_search('Product_Direct_Link_en', $allDataInSheet[0]);
$Sold_Out_key = array_search('Sold_Out', $allDataInSheet[0]);
$images_key = array_search('images', $allDataInSheet[0]);
$title_ar_key = array_search('title_ar', $allDataInSheet[0]);
$title_en_key = array_search('title_en', $allDataInSheet[0]);
$UPCs_key = array_search('UPCs', $allDataInSheet[0]);

$souq_affliate_link = 'aff';

for ($row = 2; $row <= $lastRow; $row++) {
    $objPHPExcel->getActiveSheet()->getStyle(getCellNamaFromNumber($Unique_Product_Code_key) . $row)->getNumberFormat()->setFormatCode('0');
    $objPHPExcel->getActiveSheet()->getStyle(getCellNamaFromNumber($UPCs_key) . $row)->getNumberFormat()->setFormatCode('0');
    $Unique_Product_Code = $worksheet->getCell(getCellNamaFromNumber($Unique_Product_Code_key) . $row)->getFormattedValue();
    $Country_data = $worksheet->getCell(getCellNamaFromNumber($Country_key) . $row)->getValue();
    $Brand_ar_data = $worksheet->getCell(getCellNamaFromNumber($Brand_ar_key) . $row)->getValue();
    $Brand_en_data = $worksheet->getCell(getCellNamaFromNumber($Brand_en_key) . $row)->getValue();
    $Description_ar_data = $worksheet->getCell(getCellNamaFromNumber($Description_ar_key) . $row)->getValue();
    $Description_en_data = $worksheet->getCell(getCellNamaFromNumber($Description_en_key) . $row)->getValue();
    $Item_Specs_ar_data = $worksheet->getCell(getCellNamaFromNumber($Item_Specs_ar_key) . $row)->getValue();
    $Item_Specs_en_data = $worksheet->getCell(getCellNamaFromNumber($Item_Specs_en_key) . $row)->getValue();
    $Item_Type_AR_data = $worksheet->getCell(getCellNamaFromNumber($Item_Type_AR_key) . $row)->getValue();
    $Item_Type_EN_data = $worksheet->getCell(getCellNamaFromNumber($Item_Type_EN_key) . $row)->getValue();
    $Price_EG_data = $worksheet->getCell(getCellNamaFromNumber($Price_EG_key) . $row)->getValue();
    $Product_Direct_Link_ar_data = $worksheet->getCell(getCellNamaFromNumber($Product_Direct_Link_ar_key) . $row)->getValue();
    $Product_Direct_Link_en_data = $worksheet->getCell(getCellNamaFromNumber($Product_Direct_Link_en_key) . $row)->getValue();
    $Sold_Out_data = $worksheet->getCell(getCellNamaFromNumber($Sold_Out_key) . $row)->getValue();
    $images_data = $worksheet->getCell(getCellNamaFromNumber($images_key) . $row)->getValue();
    $title_ar_data = $worksheet->getCell(getCellNamaFromNumber($title_ar_key) . $row)->getValue();
    $title_en_data = $worksheet->getCell(getCellNamaFromNumber($title_en_key) . $row)->getValue();
    $UPCs_data = $worksheet->getCell(getCellNamaFromNumber($UPCs_key) . $row)->getFormattedValue();

    $title_en_data2 = preg_replace("/'/", "''", $title_en_data);
    $title_ar_data2 = preg_replace("/'/", "''", $title_ar_data);
    $Brand_en_data2 = preg_replace("/'/", "''", $Brand_en_data);
    $Brand_ar_data2 = preg_replace("/'/", "''", $Brand_ar_data);
    $Description_en_data2 = preg_replace("/'/", "''", $Description_en_data);
    $Description_ar_data2 = preg_replace("/'/", "''", $Description_ar_data);
    $Item_Specs_en_data2 = preg_replace("/'/", "''", $Item_Specs_en_data);
    $Item_Specs_ar_data2 = preg_replace("/'/", "''", $Item_Specs_ar_data);
    $Item_Type_EN_data2 = preg_replace("/'/", "''", $Item_Type_EN_data);
    $Item_Type_AR_data2 = preg_replace("/'/", "''", $Item_Type_AR_data);
    $UIC = 'A0' . unique_code(8);

    $URL_EN = remove_special_characters($title_en_data2);
    $URL_AR = remove_special_characters($title_ar_data2);

    $Cate_URL_EN = remove_special_characters($Item_Type_EN_data2);
    $Cate_URL_AR = remove_special_characters($Item_Type_AR_data2);

    $Super_Category = $Super_cate[preg_replace("/\s+/", " ", $Item_Type_EN_data)];

    if ($Super_Category == '') {
        $sub_category_en = "not_found";
        $sub_category_ar = "not_found";
    } else {
        $Super_Category2 = explode('@', $Super_Category);
        $sub_category_en = $Super_Category2[0];
        $sub_category_ar = $Super_Category2[1];
        $sub_category_URL_EN = preg_replace("/'/", "''", remove_special_characters($sub_category_en));
    }

    $link_en = $Cate_URL_EN . "/" . $URL_EN . "/" . $UIC;
    $link_ar = $Cate_URL_AR . "/" . $URL_AR . "/" . $UIC;
    $sql = "INSERT INTO Products (Unique_Product_Code, Country, sub_category_URL_EN, sub_category_en, sub_category_ar, Item_Type_EN, Item_Type_AR, Title_EN, Title_AR, Brand_EN, Brand_AR, Description_EN, Description_AR, Item_Specs_en, Item_Specs_ar, Images_URL, Product_Direct_Link_EN, Product_Direct_Link_AR, Price_EG, Item_UPC, Sold_Out, Affiliate_Link, URL_EN, URL_AR, UIC, Cate_URL_EN, Cate_URL_AR, link_en, link_ar, added_to_specs, Website_Name)
            VALUES ('$Unique_Product_Code', '$Country_data', '$sub_category_URL_EN','$sub_category_en', '$sub_category_ar','$Item_Type_EN_data2', '$Item_Type_AR_data2', '$title_en_data2', '$title_ar_data2', '$Brand_en_data2', '$Brand_ar_data2', '$Description_en_data2', '$Description_ar_data2', '$Item_Specs_en_data2', '$Item_Specs_ar_data2', '$images_data', '$Product_Direct_Link_en_data', '$Product_Direct_Link_ar_data', '$Price_EG_data', '$UPCs_data', '$Sold_Out_data', '$souq_affliate_link', '$URL_EN', '$URL_AR', '$UIC', '$Cate_URL_EN', '$Cate_URL_AR', '$link_en', '$link_ar', 'No', 'souq.com');";

    if ($conn->query($sql) === true) {
        echo $row; //echo "New record created successfully </br>";
    } else {
        echo $conn->error . '</br>';
        die("Connection failed2: " . $conn->error);
    }
}

// $sql_sumary = 'SELECT Item_Type_EN, COUNT(*) as item_count FROM Products GROUP BY Item_Type_EN';
// $result_sumary = $conn->query($sql_sumary);
// if ($result_sumary->num_rows > 0) {
//     while ($row_cate = $result_sumary->fetch_assoc()) {
//         $Item_Type_EN = preg_replace("/'/", "''", $row_cate["Item_Type_EN"]);
//         $sql_update = 'UPDATE Item_Category SET Item_Type_Item_Count = ' . $row_cate["item_count"] . ' WHERE Item_Type = ' . "'" . $Item_Type_EN . "'";
//         if ($conn->query($sql_update) === true) {
//             echo "New record created successfully </br>";
//         } else {
//             die("Connection failed3: " . $conn->error);
//         }
//     }
// }

// $sql_sumary2 = 'SELECT sub_category_en, COUNT(*) as item_count2 FROM Products GROUP BY sub_category_en';
// $result_sumary2 = $conn->query($sql_sumary2);
// if ($result_sumary2->num_rows > 0) {
//     while ($row_cate2 = $result_sumary2->fetch_assoc()) {
//         $sub_category_en = preg_replace("/'/", "''", $row_cate2["sub_category_en"]);
//         $sql_update2 = 'UPDATE Item_Category SET Super_Cate_Item_Count = ' . $row_cate2["item_count2"] . ' WHERE sub_category_en = ' . "'" . $sub_category_en . "'";
//         if ($conn->query($sql_update2) === true) {
//             echo "New record created successfully </br>";
//         } else {
//             die("Connection failed4: " . $conn->error);
//         }
//     }
// }
