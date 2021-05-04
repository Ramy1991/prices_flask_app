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
        'item_size': "//*[@id='dropdown_selected_size_name']/span/span/span//text()"
    },
    'btech.com': {
        'image_xp': "//*[@class='product-item-view ']//a//div//img/@src",
        'price_xp': "//span[@data-price-type='finalPrice']/@data-price-amount",
        'title_xp': "//*[@class='product-item-view ']//a//div/div[1]/h2//text()",
        'uid_xp': "///*[@class='product-item-view ']/a/div/div/@data-product-id",
        'url_xp': "//*[@class='product-item-view ']/a/@href"
    },
    'jumia.com': {
        'image_xp': "//div[@class='img-c']/img[1]/@data-src",
        'price_xp': "//div[@class='prc']/text()",
        'title_xp': "//h3[@class='name']/text()",
        'uid_xp': "//a[@class='core']/@data-id",
        'url_xp': "//a[@class='core']/@href"
    },
    'noon.com': {
        'image_xp': "//div[@class='lazyload-wrapper']//img/@src",
        'price_xp': "//span[@class='currency']//following-sibling::strong//text()",
        'title_xp': "//*[@class='productContainer']//div/@title",
        'uid_xp': "//*[@class='productContainer']/a/@id",
        'url_xp': "//*[@class='productContainer']/a/@href"
    },
    'souq.com': {
        'image_xp': "//img[contains(@class,'imageUrl')]/@data-src | //div[@class='img-bucket']/a/@data-img",
        'price_xp': "//h3[contains(@class, 'itemPrice')]//text() | //span[contains(@class, 'itemPrice')]//text()",
        'title_xp': "//h1[contains(@class, 'itemTitle')]//text() | //h6[contains(@class, 'itemTitle')]/a//text()",
        'uid_xp': "//*[@id='content-body']//div/@data-ean",
        'url_xp': "//a[contains(@class,'img-bucket img-link itemLink')]/@href | //div[@class='img-bucket']/a/@href"
    }

}


def country_lang(arg1, arg2):
    country_list = ['af', 'al', 'dz', 'as', 'ad', 'ao', 'ai', 'aq', 'ag', 'ar', 'am', 'aw', 'au', 'at', 'az', 'bs',
                    'bh', 'bd', 'bb', 'by', 'be', 'bz', 'bj', 'bm', 'bt', 'bo', 'bq', 'ba', 'bw', 'bv', 'br', 'io',
                    'bn', 'bg', 'bf', 'bi', 'cv', 'kh', 'cm', 'ca', 'ky', 'cf', 'td', 'cl', 'cn', 'cx', 'cc', 'co',
                    'km', 'cd', 'cg', 'ck', 'cr', 'hr', 'cu', 'cw', 'cy', 'cz', 'ci', 'dk', 'dj', 'dm', 'do', 'ec',
                    'eg', 'sv', 'gq', 'er', 'ee', 'sz', 'et', 'fk', 'fo', 'fj', 'fi', 'fr', 'gf', 'pf', 'tf', 'ga',
                    'gm', 'ge', 'de', 'gh', 'gi', 'gr', 'gl', 'gd', 'gp', 'gu', 'gt', 'gg', 'gn', 'gw', 'gy', 'ht',
                    'hm', 'va', 'hn', 'hk', 'hu', 'is', 'in', 'id', 'ir', 'iq', 'ie', 'im', 'il', 'it', 'jm', 'jp',
                    'je', 'jo', 'kz', 'ke', 'ki', 'kp', 'kr', 'kw', 'kg', 'la', 'lv', 'lb', 'ls', 'lr', 'ly', 'li',
                    'lt', 'lu', 'mo', 'mg', 'mw', 'my', 'mv', 'ml', 'mt', 'mh', 'mq', 'mr', 'mu', 'yt', 'mx', 'fm',
                    'md', 'mc', 'mn', 'me', 'ms', 'ma', 'mz', 'mm', 'na', 'nr', 'np', 'nl', 'nc', 'nz', 'ni', 'ne',
                    'ng', 'nu', 'nf', 'mp', 'no', 'om', 'pk', 'pw', 'ps', 'pa', 'pg', 'py', 'pe', 'ph', 'pn', 'pl',
                    'pt', 'pr', 'qa', 'mk', 'ro', 'ru', 'rw', 're', 'bl', 'sh', 'kn', 'lc', 'mf', 'pm', 'vc', 'ws',
                    'sm', 'st', 'sa', 'sn', 'rs', 'sc', 'sl', 'sg', 'sx', 'sk', 'si', 'sb', 'so', 'za', 'gs', 'ss',
                    'es', 'lk', 'sd', 'sr', 'sj', 'se', 'ch', 'sy', 'tw', 'tj', 'tz', 'th', 'tl', 'tg', 'tk', 'to',
                    'tt', 'tn', 'tr', 'tm', 'tc', 'tv', 'ug', 'ua', 'ae', 'gb', 'um', 'us', 'uy', 'uz', 'vu', 've',
                    'vn', 'vg', 'vi', 'wf', 'eh', 'ye', 'zm', 'zw', 'ax']
    lang_list = ['en', 'ar']
    if len(arg1) and len(arg2) == 2 and arg1 in country_list and arg1 in lang_list:
        return True
    else:
        return False

# from scrapy.crawler import CrawlerProcess
# import spider.spider.spiders.Amazon as amazon
# from scrapy.utils.project import get_project_settings
#
# process = CrawlerProcess(get_project_settings())
# process.crawl(amazon.SouqSpider)
# process.start()
