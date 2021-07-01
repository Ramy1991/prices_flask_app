supported_website_xp = {
    # //*[@id='imageBlockThumbs']/span/div/img/@src
    # //*[@id='landingImage']/@src
    'amazon.': {
        'image_xp': "//*[@id='imgTagWrapperId']/img/@data-old-hires | //*[@id='imgBlkFront']/@data-a-dynamic-image | //div[@id='ebooks-main-image-container']/div/div/img/@src | //div[@id='audibleimageblock_feature_div']//img/@src",
        'price_xp': "//*[@id='priceblock_ourprice']/text() | //*[@id='priceblock_dealprice']/text() | //*[@id='buyNewSection']/h5/div/div[2]/div/span[2]/text() | //*[@id='cerberus-data-metrics']/@data-asin-price | //span[@class='a-color-base']/span//text() | //*[@id='newBuyBoxPrice']/text() | //*[@id='rentPrice']/text()",
        'title_xp': "//*[@id='productTitle']/text()",
        'uid_xp': "//*[@id='cerberus-data-metrics']/@data-asin | //*[contains(text(),'ISBN-10')]/ancestor::li[1]/text() | //input[@id='ASIN']/@value",
        'url_xp': "//link[@rel='canonical']/@href",
        'drop_down_size_XP': "//ul[@class='a-nostyle a-list-link']//li//text()",
        'item_size': "//*[@id='dropdown_selected_size_name']/span/span/span//text()"
    },
    'btech.com': {
        'image_xp': "//div[@id='tab-images-content']/a[1]/@href",
        'price_xp': "//input[@id='gtm_price']/@value",
        'title_xp': "//input[@id='gtm_name']/@value",
        'uid_xp': "//input[@id='gtm_id']/@value",
        'url_xp': "//*[@property='og:url']/@content"
    },
    'jumia.com': {
        'image_xp': "//meta[@property='og:image']/@content",
        'price_xp': "//script[3]/text()",
        'title_xp': "//*[@id='jm']//section//div/h1/text()",
        'uid_xp': "//*[contains(text(),'SKU')]//ancestor::li[1]/text()",
        'url_xp': "//meta[@property='og:url']/@content"
    },
    'noon.com': {
        'image_xp': "//*[@property='og:image']/@content",
        'price_xp': "//script[@id='__NEXT_DATA__']/text()",
        'title_xp': "//*[@id='content']/div/div/div[3]/div/div[1]/div[2]/div[1]/h1/text() | //*[@id='__next']/div/section/div/div[1]/div/div[2]/div[1]/div[2]/h1/text()",
        'uid_xp': "//script[@id='__NEXT_DATA__']/text()",
        'url_xp': "//*[@rel='canonical']/@href"
    },
    'souq.com': {
        'image_xp': "//*[contains(@class, 'item-img-container')]//div[1]/a[1]//img/@data-url | //*[contains(@class, 'vip-outofstock-item-img-container')]//img/@src",
        'price_xp': "//*[@class='text-default price-container']//div[1]/h3[1]/text()",
        'title_xp': "//*[contains(@class, 'product-title')]/*[1]/text()",
        'uid_xp': "//*[contains(text(),'Item EAN')]//following-sibling::dd[1]/text() | //*[contains(text(),'الرقم المميز للسلعة')]//following-sibling::dd[1]/text()",
        'url_xp': "//meta[@property='og:url']/@content"
    }
}


# country
def currency(url):
    countries = {"amazon.com": "USD", "amazon.ae": "AED", "amazon.it": "EUR", "amazon.fr": "EUR",
                 "amazon.de": "EUR", "amazon.es": "EUR", "amazon.co.uk": "£", "amazon.com.br": "R$",
                 "amazon.ca": "CDN", "amazon.com.mx": "$", "amazon.in": "₹", "amazon.co.jp": "￥",
                 "amazon.sg": "S$", "amazon.com.tr": "₺", "amazon.com.au": "$", "souq.com/eg-": "EGP",
                 "souq.com/sa-": "SAR", "btech.com": "EGP", "jumia.com.eg": "EGP", "jumia.com.ng": "₦",
                 "noon.com/uae": "AED", "noon.com/egypt": "EGP", "noon.com/saudi": "SAR", "amazon.sa": "SAR"}
    for country in countries:
        if country in url:
            return countries.get(country)


supported_search_website_xp = {

    'amazon.': {
        'image_xp': "//div[contains(@class,'s-result-item') and @data-asin[string-length()>0]]//span[@class='a-price-whole'][string-length(text()) > 0]/ancestor::div[8]//img/@src",
        'price_xp': "//div[contains(@class,'s-result-item') and @data-asin[string-length()>0]]//span[@class='a-price-whole'][string-length(text()) > 0]/ancestor::div[8 and 9]//span[@class='a-price-whole']/text()",
        'title_xp': "//div[contains(@class,'s-result-item') and @data-asin[string-length()>0]]//span[@class='a-price-whole'][string-length(text()) > 0]/ancestor::div[8]//h2/a/span//text()",
        'uid_xp': "//div[contains(@class,'s-result-item') and @data-asin[string-length()>0]]//span[@class='a-price-whole'][string-length(text()) > 0]/ancestor::div[8 and 9]/@data-asin",
        'url_xp': "//div[contains(@class,'s-result-item') and @data-asin[string-length()>0]]//span[@class='a-price-whole'][string-length(text()) > 0]/ancestor::div[8]//h2/a/@href",
        'drop_down_size_XP': "//ul[@class='a-nostyle a-list-link']//li//text()",
        'item_size': "//*[@id='dropdown_selected_size_name']/span/span/span//text()",
        'cate_xp': "//*[@id='departments']/ul/li[1]//a/span[1]//text()"
    },
    'btech.com': {
        'image_xp': "//*[@class='product-item-view ']//a//div//img/@src",
        'price_xp': "//span[@data-price-type='finalPrice']/@data-price-amount",
        'title_xp': "//*[@class='product-item-view ']//a//div/div[1]/h2//text()",
        'uid_xp': "//*[@class='product-item-view ']/a/div/div/@data-product-id",
        'url_xp': "//*[@class='product-item-view ']/a/@href",
        'cate_xp': "//*[@class='product-item-view ']/a/div/div/@data-product-id"
    },
    'jumia.com': {
        'image_xp': "//div[@class='img-c']/img[1]/@data-src",
        'price_xp': "//div[@class='prc']/text()",
        'title_xp': "//h3[@class='name']/text()",
        'uid_xp': "//a[@class='core']/@data-id",
        'url_xp': "//a[@class='core']/@href",
        'cate_xp': "//a[@class='core']/@data-category"
    },
    'noon.com': {
        'image_xp': "//div[@class='lazyload-wrapper']//img/@src",
        'price_xp': "//span[@class='currency']//following-sibling::strong//text()",
        'title_xp': "//*[@class='productContainer']//div/@title",
        'uid_xp': "//*[@class='productContainer']/a/@id",
        'url_xp': "//*[@class='productContainer']/a/@href",
        'cate_xp': "//ul[@class='level01']/li/div/button[@class='categoryLink'][1]/@id"
    },
    'souq.com': {
        'image_xp': "//img[contains(@class,'imageUrl')]/@data-src | //div[@class='img-bucket']/a/@data-img",
        'price_xp': "//h3[contains(@class, 'itemPrice')]//text() | //span[contains(@class, 'itemPrice')]//text()",
        'title_xp': "//h1[contains(@class, 'itemTitle')]//text() | //h6[contains(@class, 'itemTitle')]/a//text()",
        'uid_xp': "//*[@id='content-body']//div/@data-ean",
        'url_xp': "//a[contains(@class,'img-bucket img-link itemLink')]/@href | //div[@class='img-bucket']/a/@href",
        'cate_xp': "//*[@id='id_type_item-accordion']/div/ul/li[1]/@data-refinement"
    }

}

country_alpha2_currency = {
    'AS': {
        'currency': 'USD',
        'country_mane': 'AMERICAN SAMOA'
    },
    'AD': {
        'currency': 'EUR',
        'country_mane': 'ANDORRA '
    },
    'AT': {
        'currency': 'EUR',
        'country_mane': 'AUSTRIA'
    },
    'BE': {
        'currency': 'EUR',
        'country_mane': 'BELGIUM'
    },
    'BT': {
        'currency': 'INR',
        'country_mane': 'BHUTAN'
    },
    'IO': {
        'currency': 'USD',
        'country_mane': 'BRITISH INDIAN OCEAN TERRITORY'
    },
    'CA': {
        'currency': 'CAD',
        'country_mane': 'CANADA'
    },
    'EC': {
        'currency': 'USD',
        'country_mane': 'ECUADOR'
    },
    'EG': {
        'currency': 'EGP',
        'country_mane': 'EGYPT'
    },
    'SV': {
        'currency': 'USD',
        'country_mane': 'EL SALVADOR'
    },
    'FI': {
        'currency': 'EUR',
        'country_mane': 'FINLAND '
    },
    'FR': {
        'currency': 'EUR',
        'country_mane': 'FRANCE'
    },
    'GF': {
        'currency': 'EUR',
        'country_mane': 'FRENCH GUIANA '
    },
    'TF': {
        'currency': 'EUR',
        'country_mane': 'FRENCH SOUTHERN TERRITORIES'
    },
    'DE': {
        'currency': 'EUR',
        'country_mane': 'GERMANY'
    },
    'GR': {
        'currency': 'EUR',
        'country_mane': 'GREECE'
    },
    'GP': {
        'currency': 'EUR',
        'country_mane': 'GUADELOUPE'
    },
    'GU': {
        'currency': 'USD',
        'country_mane': 'GUAM'
    },
    'HT': {
        'currency': 'USD',
        'country_mane': 'HAITI'
    },
    'VA': {
        'currency': 'EUR',
        'country_mane': 'HOLY SEE (VATICAN CITY STATE)'
    },
    'IN': {
        'currency': 'INR',
        'country_mane': 'INDIA'
    },
    'IE': {
        'currency': 'EUR',
        'country_mane': 'IRELAND'
    },
    'IT': {
        'currency': 'EUR',
        'country_mane': 'ITALY'
    },
    'LU': {
        'currency': 'EUR',
        'country_mane': 'LUXEMBOURG'
    },
    'MH': {
        'currency': 'USD',
        'country_mane': 'MARSHALL ISLANDS'
    },
    'MQ': {
        'currency': 'EUR',
        'country_mane': 'MARTINIQUE'
    },
    'YT': {
        'currency': 'EUR',
        'country_mane': 'MAYOTTE'
    },
    'FM': {
        'currency': 'USD',
        'country_mane': 'MICRONESIA, FEDERATED STATES OF'
    },
    'MC': {
        'currency': 'EUR',
        'country_mane': 'MONACO'
    },
    'NL': {
        'currency': 'EUR',
        'country_mane': 'NETHERLANDS'
    },
    'MP': {
        'currency': 'USD',
        'country_mane': 'NORTHERN MARIANA ISLANDS'
    },
    'PW': {
        'currency': 'USD',
        'country_mane': 'PALAU'
    },
    'PA': {
        'currency': 'USD',
        'country_mane': 'PANAMA'
    },
    'PT': {
        'currency': 'EUR',
        'country_mane': 'PORTUGAL'
    },
    'PR': {
        'currency': 'USD',
        'country_mane': 'PUERTO RICO'
    },
    'QA': {
        'currency': 'QAR',
        'country_mane': 'QATAR'
    },
    'RE': {
        'currency': 'EUR',
        'country_mane': 'REUNION'
    },
    'PM': {
        'currency': 'EUR',
        'country_mane': 'SAINT PIERRE AND MIQUELON'
    },
    'SM': {
        'currency': 'EUR',
        'country_mane': 'SAN MARINO'
    },
    'SA': {
        'currency': 'SAR',
        'country_mane': 'SAUDI ARABIA'
    },
    'CS': {
        'currency': 'EUR',
        'country_mane': 'SERBIA & MONTENEGRO'
    },
    'ES': {
        'currency': 'EUR',
        'country_mane': 'SPAIN'
    },
    'TL': {
        'currency': 'USD',
        'country_mane': 'TIMOR-LESTE'
    },
    'TC': {
        'currency': 'USD',
        'country_mane': 'TURKS AND CAICOS ISLANDS'
    },
    'AE': {
        'currency': 'AED',
        'country_mane': 'UNITED ARAB EMIRATES'
    },
    'GB': {
        'currency': 'GBP',
        'country_mane': 'UNITED KINGDOM'
    },
    'US': {
        'currency': 'USD',
        'country_mane': 'UNITED STATES'
    },
    'UM': {
        'currency': 'USD',
        'country_mane': 'UNITED STATES MINOR OUTLYING ISLANDS'
    },
    'VG': {
        'currency': 'USD',
        'country_mane': 'VIRGIN ISLANDS, BRITISH'
    },
    'VI': {
        'currency': 'USD',
        'country_mane': 'VIRGIN ISLANDS, U.S'
    }
}

# validate country and land


# from scrapy.crawler import CrawlerProcess
# import spider.spider.spiders.Amazon as amazon
# from scrapy.utils.project import get_project_settings
#
# process = CrawlerProcess(get_project_settings())
# process.crawl(amazon.SouqSpider)
# process.start()
