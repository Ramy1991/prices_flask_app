# import timeit
import grequests

#
# def timer(number, repeat):
#     def wrapper(func):
#         runs = timeit.repeat(func, number=number, repeat=repeat)
#         print(sum(runs) / len(runs))
#
#     return wrapper


d = [{
    'item_url_ar': 'https://www.jumia.com.eg/ar/ar/topk-an24-3-in-1-micro-usb-type-c-i-phone-1.2m-3a-fast-usb-charging-cable-blue-21289472.html',
    'item_url_en': 'https://www.jumia.com.eg/topk-an24-3-in-1-micro-usb-type-c-i-phone-1.2m-3a-fast-usb-charging-cable-blue-21289472.html',
    'item_uid': 'TO740EA0GDDR8NAFAMZ', 'item_website': 'jumia.com'}, {
    'item_url_ar': 'https://www.jumia.com.eg/ar/ar/anti-shock-back-cover-for-apple-iphone-11-transparent-generic-mpg777773.html',
    'item_url_en': 'https://www.jumia.com.eg/anti-shock-back-cover-for-apple-iphone-11-transparent-generic-mpg777773.html',
    'item_uid': 'GE810EA0312S8NAFAMZ', 'item_website': 'jumia.com'}, {
    'item_url_ar': 'https://www.jumia.com.eg/ar/ar/iphone-12-pro-max-with-facetime-256gb-pacific-blue-apple-mpg757129.html',
    'item_url_en': 'https://www.jumia.com.eg/iphone-12-pro-max-with-facetime-256gb-pacific-blue-apple-mpg757129.html',
    'item_uid': 'AP848MP0X7H1ONAFAMZ', 'item_website': 'jumia.com'}, {
    'item_url_ar': 'https://www.jumia.com.eg/ar/ar/lightning-to-usb-cable-1m-charging-cable-sync-data-line-cord-for-apple-iphone-ipad-white-generic-mpg765785.html',
    'item_url_en': 'https://www.jumia.com.eg/lightning-to-usb-cable-1m-charging-cable-sync-data-line-cord-for-apple-iphone-ipad-white-generic-mpg765785.html',
    'item_uid': 'GE810EA0FZ7SMNAFAMZ', 'item_website': 'jumia.com'}, {
    'item_url_ar': 'https://www.jumia.com.eg/ar/ar/s-l352-for-iphone-cable-faster-stronger-charger-data-transfer-1m-1.2a-white-joyroom-mpg809211.html',
    'item_url_en': 'https://www.jumia.com.eg/s-l352-for-iphone-cable-faster-stronger-charger-data-transfer-1m-1.2a-white-joyroom-mpg809211.html',
    'item_uid': 'JO326EA16951KNAFAMZ', 'item_website': 'jumia.com'}, {
    'item_url_ar': 'https://www.jumia.com.eg/ar/ar/iphone-12-pro-max-camera-lens-protector-8-layer-full-screen-anti-scratch-generic-mpg818265.html',
    'item_url_en': 'https://www.jumia.com.eg/iphone-12-pro-max-camera-lens-protector-8-layer-full-screen-anti-scratch-generic-mpg818265.html',
    'item_uid': 'GE810EA1K5Y7KNAFAMZ', 'item_website': 'jumia.com'}, {
    'item_url_ar': 'https://www.jumia.com.eg/ar/ar/generic-soft-silicone-back-cover-for-iphone-12-pro-transparent-20267520.html',
    'item_url_en': 'https://www.jumia.com.eg/generic-soft-silicone-back-cover-for-iphone-12-pro-transparent-20267520.html',
    'item_uid': 'GE810EA01J7T6NAFAMZ', 'item_website': 'jumia.com'},
    {'item_url_ar': 'https://www.jumia.com.eg/ar/ar/iphone-12-with-facetime-128gb-blue-apple-mpg756594.html',
     'item_url_en': 'https://www.jumia.com.eg/iphone-12-with-facetime-128gb-blue-apple-mpg756594.html',
     'item_uid': 'AP848MP1B7OIGNAFAMZ', 'item_website': 'jumia.com'}, {
        'item_url_ar': 'https://www.jumia.com.eg/ar/ar/generic-iphone-12-pro-max-high-quality-screen-protector-with-speaker-dust-filter-21168865.html',
        'item_url_en': 'https://www.jumia.com.eg/generic-iphone-12-pro-max-high-quality-screen-protector-with-speaker-dust-filter-21168865.html',
        'item_uid': 'GE810EA0XV9LSNAFAMZ', 'item_website': 'jumia.com'},
    {'item_url_ar': 'https://www.jumia.com.eg/ar/ar/20w-usb-c-power-adapter-white-apple-mpg774113.html',
     'item_url_en': 'https://www.jumia.com.eg/20w-usb-c-power-adapter-white-apple-mpg774113.html',
     'item_uid': 'AP848EL175BIUNAFAMZ', 'item_website': 'jumia.com'}, {
        'item_url_ar': 'https://www.jumia.com.eg/ar/ar/slim-fit-silicone-cover-with-soft-edges-for-apple-iphone-11-blackred-buttons-generic-mpg707077.html',
        'item_url_en': 'https://www.jumia.com.eg/slim-fit-silicone-cover-with-soft-edges-for-apple-iphone-11-blackred-buttons-generic-mpg707077.html',
        'item_uid': 'GE810EA0U8E59NAFAMZ', 'item_website': 'jumia.com'}, {
        'item_url_ar': 'https://www.jumia.com.eg/ar/ar/iphone-x-to-iphone-11-tempered-glass-camera-lens-protector-white-generic-mpg708905.html',
        'item_url_en': 'https://www.jumia.com.eg/iphone-x-to-iphone-11-tempered-glass-camera-lens-protector-white-generic-mpg708905.html',
        'item_uid': 'GE810EA0645JINAFAMZ', 'item_website': 'jumia.com'}, {
        'item_url_ar': 'https://www.jumia.com.eg/ar/ar/generic-phone-stand-compatible-with-iphone-11-pro-xs-xs-max-xr-x-8-7-6-6s-plus-and-all-android-smartphones-black-19859297.html',
        'item_url_en': 'https://www.jumia.com.eg/generic-phone-stand-compatible-with-iphone-11-pro-xs-xs-max-xr-x-8-7-6-6s-plus-and-all-android-smartphones-black-19859297.html',
        'item_uid': 'GE810EA1B7L3NNAFAMZ', 'item_website': 'jumia.com'}, {
        'item_url_ar': 'https://www.jumia.com.eg/ar/ar/iphone-11-high-quality-screen-protector-with-speaker-dust-filter-generic-mpg818264.html',
        'item_url_en': 'https://www.jumia.com.eg/iphone-11-high-quality-screen-protector-with-speaker-dust-filter-generic-mpg818264.html',
        'item_uid': 'GE810EA043LCWNAFAMZ', 'item_website': 'jumia.com'}, {
        'item_url_ar': 'https://www.jumia.com.eg/ar/ar/silicone-back-cover-for-iphone-6-iphone-6s-transparent-anti-shock-generic-mpg779791.html',
        'item_url_en': 'https://www.jumia.com.eg/silicone-back-cover-for-iphone-6-iphone-6s-transparent-anti-shock-generic-mpg779791.html',
        'item_uid': 'GE810EA0RUL22NAFAMZ', 'item_website': 'jumia.com'}, {
        'item_url_ar': 'https://www.jumia.com.eg/ar/ar/generic-dt88-smart-watch-full-touch-men-business-style-metal-band-for-android-ios-phone-black-21482970.html',
        'item_url_en': 'https://www.jumia.com.eg/generic-dt88-smart-watch-full-touch-men-business-style-metal-band-for-android-ios-phone-black-21482970.html',
        'item_uid': 'GE810EA04PXLONAFAMZ', 'item_website': 'jumia.com'}, {
        'item_url_ar': 'https://www.jumia.com.eg/ar/ar/iphone-12-pro-max-ultra-slim-anti-drop-anti-yellowing-cover-transparent-joyroom-mpg815109.html',
        'item_url_en': 'https://www.jumia.com.eg/iphone-12-pro-max-ultra-slim-anti-drop-anti-yellowing-cover-transparent-joyroom-mpg815109.html',
        'item_uid': 'JO326EA0GZEW0NAFAMZ', 'item_website': 'jumia.com'}, {
        'item_url_ar': 'https://www.jumia.com.eg/ar/ar/generic-iphone-11-6.1-inch-slim-soft-silicon-shockproof-edges-cover-with-camera-protection-black-20375766.html',
        'item_url_en': 'https://www.jumia.com.eg/generic-iphone-11-6.1-inch-slim-soft-silicon-shockproof-edges-cover-with-camera-protection-black-20375766.html',
        'item_uid': 'GE810EA13QU9INAFAMZ', 'item_website': 'jumia.com'}, {
        'item_url_ar': 'https://www.jumia.com.eg/ar/ar/generic-iphone-11-pro-max-high-quality-screen-protector-with-speaker-dust-filter-21168862.html',
        'item_url_en': 'https://www.jumia.com.eg/generic-iphone-11-pro-max-high-quality-screen-protector-with-speaker-dust-filter-21168862.html',
        'item_uid': 'GE810EA0G09GGNAFAMZ', 'item_website': 'jumia.com'},
    {'item_url_ar': 'https://www.jumia.com.eg/ar/ar/lightning-charging-cable-100-cm-red-generic-mpg764056.html',
     'item_url_en': 'https://www.jumia.com.eg/lightning-charging-cable-100-cm-red-generic-mpg764056.html',
     'item_uid': 'GE810EL0ADIL9NAFAMZ', 'item_website': 'jumia.com'}, {
        'item_url_ar': 'https://www.jumia.com.eg/ar/ar/king-kong-anti-shock-transparent-cover-for-iphone-11-pro-max-transparent-generic-mpg708906.html',
        'item_url_en': 'https://www.jumia.com.eg/king-kong-anti-shock-transparent-cover-for-iphone-11-pro-max-transparent-generic-mpg708906.html',
        'item_uid': 'GE810EL1KWXHNNAFAMZ', 'item_website': 'jumia.com'}, {
        'item_url_ar': 'https://www.jumia.com.eg/ar/ar/remax-data-cable-lightning-usb-charging-cable-100-cm-blue-22053278.html',
        'item_url_en': 'https://www.jumia.com.eg/remax-data-cable-lightning-usb-charging-cable-100-cm-blue-22053278.html',
        'item_uid': 'RE882EA1FXQZ2NAFAMZ', 'item_website': 'jumia.com'}, {
        'item_url_ar': 'https://www.jumia.com.eg/ar/ar/heat-shrink-tubing-wire-for-all-telephone-cables-5-6-8-10-12-mm-20-pieces-generic-mpg153360.html',
        'item_url_en': 'https://www.jumia.com.eg/heat-shrink-tubing-wire-for-all-telephone-cables-5-6-8-10-12-mm-20-pieces-generic-mpg153360.html',
        'item_uid': 'GE810HL0D39KKNAFAMZ', 'item_website': 'jumia.com'}, {
        'item_url_ar': 'https://www.jumia.com.eg/ar/ar/travel-adapter-charger-for-iphone-5-iphone-6-6s-6-plus-6s-plus-7-7plus-white-generic-mpg42661.html',
        'item_url_en': 'https://www.jumia.com.eg/travel-adapter-charger-for-iphone-5-iphone-6-6s-6-plus-6s-plus-7-7plus-white-generic-mpg42661.html',
        'item_uid': 'GE810EA03Z1TDNAFAMZ', 'item_website': 'jumia.com'}, {
        'item_url_ar': 'https://www.jumia.com.eg/ar/ar/iphone-11-with-camera-sliding-door-design-matte-soft-edges-protective-case-black-generic-mpg761844.html',
        'item_url_en': 'https://www.jumia.com.eg/iphone-11-with-camera-sliding-door-design-matte-soft-edges-protective-case-black-generic-mpg761844.html',
        'item_uid': 'GE810EA15RBLBNAFAMZ', 'item_website': 'jumia.com'}, {
        'item_url_ar': 'https://www.jumia.com.eg/ar/ar/anti-shock-transparent-case-for-iphone-12-pro-max-generic-mpg756690.html',
        'item_url_en': 'https://www.jumia.com.eg/anti-shock-transparent-case-for-iphone-12-pro-max-generic-mpg756690.html',
        'item_uid': 'GE810EL1I1CY6NAFAMZ', 'item_website': 'jumia.com'}, {
        'item_url_ar': 'https://www.jumia.com.eg/ar/ar/soft-silicone-back-cover-for-iphone-11-transparent-generic-mpg707918.html',
        'item_url_en': 'https://www.jumia.com.eg/soft-silicone-back-cover-for-iphone-11-transparent-generic-mpg707918.html',
        'item_uid': 'GE810EA133W3UNAFAMZ', 'item_website': 'jumia.com'}, {
        'item_url_ar': 'https://www.jumia.com.eg/ar/ar/soft-silicone-back-cover-for-iphone-12-transparent-generic-mpg773429.html',
        'item_url_en': 'https://www.jumia.com.eg/soft-silicone-back-cover-for-iphone-12-transparent-generic-mpg773429.html',
        'item_uid': 'GE810EA1IISNENAFAMZ', 'item_website': 'jumia.com'}, {
        'item_url_ar': 'https://www.jumia.com.eg/ar/ar/heat-shrink-tubing-wire-for-all-i-phone-cables-7-mm-1-m-black-generic-mpg165235.html',
        'item_url_en': 'https://www.jumia.com.eg/heat-shrink-tubing-wire-for-all-i-phone-cables-7-mm-1-m-black-generic-mpg165235.html',
        'item_uid': 'GE810HL0OWOBENAFAMZ', 'item_website': 'jumia.com'}, {
        'item_url_ar': 'https://www.jumia.com.eg/ar/ar/kaku-headphone-adapter-iphone-lightning-to-mini-jack-35mm-kaku-2in1-short-audio-converter-lightning-8-pin-ksc-428-black-21228679.html',
        'item_url_en': 'https://www.jumia.com.eg/kaku-headphone-adapter-iphone-lightning-to-mini-jack-35mm-kaku-2in1-short-audio-converter-lightning-8-pin-ksc-428-black-21228679.html',
        'item_uid': 'KA789EA1M5O2SNAFAMZ', 'item_website': 'jumia.com'}, {
        'item_url_ar': 'https://www.jumia.com.eg/ar/ar/joyroom-iphone-12-pro-max-ultra-slim-airbag-anti-drop-anti-yellowing-cover-transparent-21162575.html',
        'item_url_en': 'https://www.jumia.com.eg/joyroom-iphone-12-pro-max-ultra-slim-airbag-anti-drop-anti-yellowing-cover-transparent-21162575.html',
        'item_uid': 'JO326EA0Y8ZFKNAFAMZ', 'item_website': 'jumia.com'}, {
        'item_url_ar': 'https://www.jumia.com.eg/ar/ar/iphone-12-12-pro-6.1-inch-protector-high-quality-ultra-tough-clear-tpu-cover-generic-mpg768581.html',
        'item_url_en': 'https://www.jumia.com.eg/iphone-12-12-pro-6.1-inch-protector-high-quality-ultra-tough-clear-tpu-cover-generic-mpg768581.html',
        'item_uid': 'GE810EA1M16HUNAFAMZ', 'item_website': 'jumia.com'}, {
        'item_url_ar': 'https://www.jumia.com.eg/ar/ar/king-kong-anti-shock-transparent-cover-for-iphone-11-pro-5.8-inch-generic-mpg700484.html',
        'item_url_en': 'https://www.jumia.com.eg/king-kong-anti-shock-transparent-cover-for-iphone-11-pro-5.8-inch-generic-mpg700484.html',
        'item_uid': 'GE810EL1DCV3BNAFAMZ', 'item_website': 'jumia.com'}, {
        'item_url_ar': 'https://www.jumia.com.eg/ar/ar/generic-iphone-12-pro-max-6.7-inch-premium-tempered-glass-screen-protector-black-21965588.html',
        'item_url_en': 'https://www.jumia.com.eg/generic-iphone-12-pro-max-6.7-inch-premium-tempered-glass-screen-protector-black-21965588.html',
        'item_uid': 'GE810EA1GQ2Y8NAFAMZ', 'item_website': 'jumia.com'},
    {'item_url_ar': 'https://www.jumia.com.eg/ar/ar/charging-cable-for-iphone-white-no-brand-mpg123162.html',
     'item_url_en': 'https://www.jumia.com.eg/charging-cable-for-iphone-white-no-brand-mpg123162.html',
     'item_uid': 'GE810EL1GJOUMNAFAMZ', 'item_website': 'jumia.com'}, {
        'item_url_ar': 'https://www.jumia.com.eg/ar/ar/camera-lens-protector-for-iphone-xxsxs-max-change-to-iphone-11-pro11-pro-max-gold-generic-mpg708885.html',
        'item_url_en': 'https://www.jumia.com.eg/camera-lens-protector-for-iphone-xxsxs-max-change-to-iphone-11-pro11-pro-max-gold-generic-mpg708885.html',
        'item_uid': 'GE810EA1N75UGNAFAMZ', 'item_website': 'jumia.com'},
    {'item_url_ar': 'https://www.jumia.com.eg/ar/ar/anti-shock-transparent-case-for-iphone-xxs-generic-mpg698150.html',
     'item_url_en': 'https://www.jumia.com.eg/anti-shock-transparent-case-for-iphone-xxs-generic-mpg698150.html',
     'item_uid': 'GE810EL0736WXNAFAMZ', 'item_website': 'jumia.com'}, {
        'item_url_ar': 'https://www.jumia.com.eg/ar/ar/iphone-11-pro-max-6.5-inch-protector-high-quality-ultra-tough-clear-tpu-cover-generic-mpg786051.html',
        'item_url_en': 'https://www.jumia.com.eg/iphone-11-pro-max-6.5-inch-protector-high-quality-ultra-tough-clear-tpu-cover-generic-mpg786051.html',
        'item_uid': 'GE810EA051LNMNAFAMZ', 'item_website': 'jumia.com'}, {
        'item_url_ar': 'https://www.jumia.com.eg/ar/ar/lightning-to-3.5-mm-aux-audio-adapter-cable-for-iphone-devices-white-generic-mpg765784.html',
        'item_url_en': 'https://www.jumia.com.eg/lightning-to-3.5-mm-aux-audio-adapter-cable-for-iphone-devices-white-generic-mpg765784.html',
        'item_uid': 'GE810EA000QZZNAFAMZ', 'item_website': 'jumia.com'}, {
        'item_url_ar': 'https://www.jumia.com.eg/ar/ar/xdoria-defense-prime-series-protective-case-for-apple-iphone-11-pro-black-19277160.html',
        'item_url_en': 'https://www.jumia.com.eg/xdoria-defense-prime-series-protective-case-for-apple-iphone-11-pro-black-19277160.html',
        'item_uid': 'XD165EA03OEFFNAFAMZ', 'item_website': 'jumia.com'}, {
        'item_url_ar': 'https://egypt.souq.com/eg-ar/ابل-ايفون-xs-ماكس-مع-فيس-تايم-256-جيجا-الجيل-الرابع-ال-تي-اي-رمادي-38545111/i/',
        'item_url_en': 'https://egypt.souq.com/eg-en/ابل-ايفون-xs-ماكس-مع-فيس-تايم-256-جيجا-الجيل-الرابع-ال-تي-اي-رمادي-38545111/i/',
        'item_uid': '2724665446529', 'item_website': 'souq.com'}, {
        'item_url_ar': 'https://egypt.souq.com/eg-ar/ابل-ايفون-xs-ماكس-مع-فيس-تايم-256-جيجا-الجيل-الرابع-ال-تي-اي-فضي-38545136/i/',
        'item_url_en': 'https://egypt.souq.com/eg-en/ابل-ايفون-xs-ماكس-مع-فيس-تايم-256-جيجا-الجيل-الرابع-ال-تي-اي-فضي-38545136/i/',
        'item_uid': '2724665446772', 'item_website': 'souq.com'}, {
        'item_url_ar': 'https://egypt.souq.com/eg-ar/ابل-ايفون-xs-مع-فيس-تايم-64-جيجا-الجيل-الرابع-ال-تي-اي-فضي-38545123/i/',
        'item_url_en': 'https://egypt.souq.com/eg-en/ابل-ايفون-xs-مع-فيس-تايم-64-جيجا-الجيل-الرابع-ال-تي-اي-فضي-38545123/i/',
        'item_uid': '2724665446635', 'item_website': 'souq.com'},
    {'item_url_ar': 'https://egypt.souq.com/eg-ar/ابل-ايفون-12-برو-128جيجابيت-ازرق-132537526/i/',
     'item_url_en': 'https://egypt.souq.com/eg-en/ابل-ايفون-12-برو-128جيجابيت-ازرق-132537526/i/',
     'item_uid': '2725614260050', 'item_website': 'souq.com'},
    {'item_url_ar': 'https://egypt.souq.com/eg-ar/ابل-ايفون-12-برو-ماكس-256جيجابيت-ذهبى-mgd13j-a-132510159/i/',
     'item_url_en': 'https://egypt.souq.com/eg-en/ابل-ايفون-12-برو-ماكس-256جيجابيت-ذهبى-mgd13j-a-132510159/i/',
     'item_uid': '2725613971735', 'item_website': 'souq.com'}, {
        'item_url_ar': 'https://egypt.souq.com/eg-ar/ابل-ايفون-xs-ماكس-مع-فيس-تايم-64-جيجا-الجيل-الرابع-ال-تي-اي-ذهبي-38545134/i/',
        'item_url_en': 'https://egypt.souq.com/eg-en/ابل-ايفون-xs-ماكس-مع-فيس-تايم-64-جيجا-الجيل-الرابع-ال-تي-اي-ذهبي-38545134/i/',
        'item_uid': '2724665446765', 'item_website': 'souq.com'},
    {'item_url_ar': 'https://egypt.souq.com/eg-ar/ابل-ايفون-12-128جيجابيت-اسود-132824230/i/',
     'item_url_en': 'https://egypt.souq.com/eg-en/ابل-ايفون-12-128جيجابيت-اسود-132824230/i/',
     'item_uid': '2725617310691', 'item_website': 'souq.com'}, {
        'item_url_ar': 'https://egypt.souq.com/eg-ar/ابل-ايفون-اكس-ار-مع-فيس-تايم-64-جيجا-الجيل-الرابع-ال-تي-اي-اصفر-38543687/i/',
        'item_url_en': 'https://egypt.souq.com/eg-en/ابل-ايفون-اكس-ار-مع-فيس-تايم-64-جيجا-الجيل-الرابع-ال-تي-اي-اصفر-38543687/i/',
        'item_uid': '2724665431723', 'item_website': 'souq.com'}, {
        'item_url_ar': 'https://egypt.souq.com/eg-ar/هاتف-ابل-ايفون-11-برو-ماكس-مع-فيس-تايم-بشريحة-واحدة-وشريحة-الكترونية-ذاكرة-تخزين-256-جيجا-ذاكرة-وصول-عشوائية-4-جيجا-شبكة-ال-تي-اي-من-الجيل-الرابع-اخضر-غامق-68315146/i/',
        'item_url_en': 'https://egypt.souq.com/eg-en/هاتف-ابل-ايفون-11-برو-ماكس-مع-فيس-تايم-بشريحة-واحدة-وشريحة-الكترونية-ذاكرة-تخزين-256-جيجا-ذاكرة-وصول-عشوائية-4-جيجا-شبكة-ال-تي-اي-من-الجيل-الرابع-اخضر-غامق-68315146/i/',
        'item_uid': '2724969000731', 'item_website': 'souq.com'}, {
        'item_url_ar': 'https://egypt.souq.com/eg-ar/موبايل-ابل-ايفون-ميني12-5-4-بوصة-128-جيجابايت-4-جيجابايت-رام-ارجواني-132811593/i/',
        'item_url_en': 'https://egypt.souq.com/eg-en/موبايل-ابل-ايفون-ميني12-5-4-بوصة-128-جيجابايت-4-جيجابايت-رام-ارجواني-132811593/i/',
        'item_uid': '2725617182489', 'item_website': 'souq.com'}, {
        'item_url_ar': 'https://egypt.souq.com/eg-ar/هاتف-ابل-ايفون-11-مع-فيس-تايم-بشريحة-واحدة-وشريحة-الكترونية-ذاكرة-تخزين-128-جيجا-ذاكرة-وصول-عشوائية-4-جيجا-شبكة-ال-تي-اي-من-الجيل-الرابع-احمر-68312949/i/',
        'item_url_en': 'https://egypt.souq.com/eg-en/هاتف-ابل-ايفون-11-مع-فيس-تايم-بشريحة-واحدة-وشريحة-الكترونية-ذاكرة-تخزين-128-جيجا-ذاكرة-وصول-عشوائية-4-جيجا-شبكة-ال-تي-اي-من-الجيل-الرابع-احمر-68312949/i/',
        'item_uid': '2724968977911', 'item_website': 'souq.com'},
    {'item_url_ar': 'https://egypt.souq.com/eg-ar/ابل-ايفون-12-برو-128جيجابيت-ازرق-131938444/i/',
     'item_url_en': 'https://egypt.souq.com/eg-en/ابل-ايفون-12-برو-128جيجابيت-ازرق-131938444/i/',
     'item_uid': '2725607671450', 'item_website': 'souq.com'},
    {'item_url_ar': 'https://egypt.souq.com/eg-ar/ابل-ايفون-12-برو-128جيجابيت-ذهبى-131931841/i/',
     'item_url_en': 'https://egypt.souq.com/eg-en/ابل-ايفون-12-برو-128جيجابيت-ذهبى-131931841/i/',
     'item_uid': '2725607607480', 'item_website': 'souq.com'},
    {'item_url_ar': 'https://egypt.souq.com/eg-ar/ابل-ايفون-12-برو-ماكس-256جيجابيت-الجرافيت-132660075/i/',
     'item_url_en': 'https://egypt.souq.com/eg-en/ابل-ايفون-12-برو-ماكس-256جيجابيت-الجرافيت-132660075/i/',
     'item_uid': '2725615555186', 'item_website': 'souq.com'},
    {'item_url_ar': 'https://egypt.souq.com/eg-ar/ابل-ايفون-12-برو-ماكس-128جيجابيت-ذهبى-132660094/i/',
     'item_url_en': 'https://egypt.souq.com/eg-en/ابل-ايفون-12-برو-ماكس-128جيجابيت-ذهبى-132660094/i/',
     'item_uid': '2725615566076', 'item_website': 'souq.com'},
    {'item_url_ar': 'https://egypt.souq.com/eg-ar/ابل-ايفون-12-128جيجابيت-اخضر-131931849/i/',
     'item_url_en': 'https://egypt.souq.com/eg-en/ابل-ايفون-12-128جيجابيت-اخضر-131931849/i/',
     'item_uid': '2725607607664', 'item_website': 'souq.com'}, {
        'item_url_ar': 'https://egypt.souq.com/eg-ar/هاتف-ابل-ايفون-11-مع-فيس-تايم-بشريحة-واحدة-وشريحة-الكترونية-ذاكرة-تخزين-128-جيجا-ذاكرة-وصول-عشوائية-4-جيجا-شبكة-ال-تي-اي-من-الجيل-الرابع-اخضر-132103476/i/',
        'item_url_en': 'https://egypt.souq.com/eg-en/هاتف-ابل-ايفون-11-مع-فيس-تايم-بشريحة-واحدة-وشريحة-الكترونية-ذاكرة-تخزين-128-جيجا-ذاكرة-وصول-عشوائية-4-جيجا-شبكة-ال-تي-اي-من-الجيل-الرابع-اخضر-132103476/i/',
        'item_uid': '2725609537440', 'item_website': 'souq.com'},
    {'item_url_ar': 'https://egypt.souq.com/eg-ar/ابل-ايفون-12-128جيجابيت-احمر-131931845/i/',
     'item_url_en': 'https://egypt.souq.com/eg-en/ابل-ايفون-12-128جيجابيت-احمر-131931845/i/',
     'item_uid': '2725607607565', 'item_website': 'souq.com'},
    {'item_url_ar': 'https://egypt.souq.com/eg-ar/ابل-ايفون-12-مينى-128جيجابيت-ازرق-131938465/i/',
     'item_url_en': 'https://egypt.souq.com/eg-en/ابل-ايفون-12-مينى-128جيجابيت-ازرق-131938465/i/',
     'item_uid': '2725607681800', 'item_website': 'souq.com'}, {
        'item_url_ar': 'https://egypt.souq.com/eg-ar/هاتف-ابل-ايفون-11-برو-مع-فيس-تايم-بشريحة-واحدة-وشريحة-الكترونية-ذاكرة-تخزين-64-جيجا-ذاكرة-وصول-عشوائية-4-جيجا-شبكة-ال-تي-اي-من-الجيل-الرابع-ذهبي-68315133/i/',
        'item_url_en': 'https://egypt.souq.com/eg-en/هاتف-ابل-ايفون-11-برو-مع-فيس-تايم-بشريحة-واحدة-وشريحة-الكترونية-ذاكرة-تخزين-64-جيجا-ذاكرة-وصول-عشوائية-4-جيجا-شبكة-ال-تي-اي-من-الجيل-الرابع-ذهبي-68315133/i/',
        'item_uid': '2724969000472', 'item_website': 'souq.com'},
    {'item_url_ar': 'https://egypt.souq.com/eg-ar/ابل-ايفون-12-برو-ماكس-256جيجابيت-ازرق-132537529/i/',
     'item_url_en': 'https://egypt.souq.com/eg-en/ابل-ايفون-12-برو-ماكس-256جيجابيت-ازرق-132537529/i/',
     'item_uid': '2725614266236', 'item_website': 'souq.com'},
    {'item_url_ar': 'https://egypt.souq.com/eg-ar/ابل-ايفون-12-برو-128جيجابيت-الجرافيت-132537527/i/',
     'item_url_en': 'https://egypt.souq.com/eg-en/ابل-ايفون-12-برو-128جيجابيت-الجرافيت-132537527/i/',
     'item_uid': '2725614260128', 'item_website': 'souq.com'}, {
        'item_url_ar': 'https://egypt.souq.com/eg-ar/هاتف-ابل-ايفون-11-مع-فيس-تايم-بشريحة-واحدة-وشريحة-الكترونية-ذاكرة-تخزين-128-جيجا-رام-4-جيجا-شبكة-ال-تي-اي-من-الجيل-الرابع-ابيض-mhdj3j-a-132416673/i/',
        'item_url_en': 'https://egypt.souq.com/eg-en/هاتف-ابل-ايفون-11-مع-فيس-تايم-بشريحة-واحدة-وشريحة-الكترونية-ذاكرة-تخزين-128-جيجا-رام-4-جيجا-شبكة-ال-تي-اي-من-الجيل-الرابع-ابيض-mhdj3j-a-132416673/i/',
        'item_uid': '2725612972498', 'item_website': 'souq.com'},
    {'item_url_ar': 'https://egypt.souq.com/eg-ar/ابل-ايفون-12-برو-ماكس-128جيجابيت-ازرق-132540379/i/',
     'item_url_en': 'https://egypt.souq.com/eg-en/ابل-ايفون-12-برو-ماكس-128جيجابيت-ازرق-132540379/i/',
     'item_uid': '2725614298619', 'item_website': 'souq.com'},
    {'item_url_ar': 'https://egypt.souq.com/eg-ar/ابل-ايفون-12-برو-ماكس-256جيجابيت-ذهبى-131938460/i/',
     'item_url_en': 'https://egypt.souq.com/eg-en/ابل-ايفون-12-برو-ماكس-256جيجابيت-ذهبى-131938460/i/',
     'item_uid': '2725607681701', 'item_website': 'souq.com'}, {
        'item_url_ar': 'https://egypt.souq.com/eg-ar/هاتف-ابل-ايفون-11-مع-فيس-تايم-ذاكرة-تخزين-128-جيجا-ذاكرة-وصول-عشوائية-4-جيجا-شبكة-ال-تي-اي-من-الجيل-الرابع-اسود-شريحة-اتصال-و-شريحة-الكترونية-132103545/i/',
        'item_url_en': 'https://egypt.souq.com/eg-en/هاتف-ابل-ايفون-11-مع-فيس-تايم-ذاكرة-تخزين-128-جيجا-ذاكرة-وصول-عشوائية-4-جيجا-شبكة-ال-تي-اي-من-الجيل-الرابع-اسود-شريحة-اتصال-و-شريحة-الكترونية-132103545/i/',
        'item_uid': '2725609538096', 'item_website': 'souq.com'},
    {'item_url_ar': 'https://egypt.souq.com/eg-ar/ابل-ايفون-12-برو-256جيجابيت-ازرق-131938449/i/',
     'item_url_en': 'https://egypt.souq.com/eg-en/ابل-ايفون-12-برو-256جيجابيت-ازرق-131938449/i/',
     'item_uid': '2725607666708', 'item_website': 'souq.com'},
    {'item_url_ar': 'https://egypt.souq.com/eg-ar/ابل-ايفون-12-برو-128جيجابيت-فضى-131931834/i/',
     'item_url_en': 'https://egypt.souq.com/eg-en/ابل-ايفون-12-برو-128جيجابيت-فضى-131931834/i/',
     'item_uid': '2725607607381', 'item_website': 'souq.com'}, {
        'item_url_ar': 'https://egypt.souq.com/eg-ar/ابل-ايفون-7-مع-فيس-تايم-128-جيجا-الجيل-الرابع-ال-تي-اي-ذهبي-11526697/i/',
        'item_url_en': 'https://egypt.souq.com/eg-en/ابل-ايفون-7-مع-فيس-تايم-128-جيجا-الجيل-الرابع-ال-تي-اي-ذهبي-11526697/i/',
        'item_uid': '2724336886616', 'item_website': 'souq.com'},
    {'item_url_ar': 'https://www.noon.com/egypt-ar/N41044062A/p',
     'item_url_en': 'https://www.noon.com/egypt-en/N41044062A/p', 'item_uid': 'N41044062A',
     'item_website': 'noon.com'}, {'item_url_ar': 'https://www.noon.com/egypt-ar/N41044033A/p',
                                   'item_url_en': 'https://www.noon.com/egypt-en/N41044033A/p',
                                   'item_uid': 'N41044033A', 'item_website': 'noon.com'},
    {'item_url_ar': 'https://www.noon.com/egypt-ar/N41044017A/p',
     'item_url_en': 'https://www.noon.com/egypt-en/N41044017A/p', 'item_uid': 'N41044017A',
     'item_website': 'noon.com'}, {'item_url_ar': 'https://www.noon.com/egypt-ar/N41044009A/p',
                                   'item_url_en': 'https://www.noon.com/egypt-en/N41044009A/p',
                                   'item_uid': 'N41044009A', 'item_website': 'noon.com'},
    {'item_url_ar': 'https://www.noon.com/egypt-ar/N41044064A/p',
     'item_url_en': 'https://www.noon.com/egypt-en/N41044064A/p', 'item_uid': 'N41044064A',
     'item_website': 'noon.com'}, {'item_url_ar': 'https://www.noon.com/egypt-ar/N41044045A/p',
                                   'item_url_en': 'https://www.noon.com/egypt-en/N41044045A/p',
                                   'item_uid': 'N41044045A', 'item_website': 'noon.com'},
    {'item_url_ar': 'https://www.noon.com/egypt-ar/N41044011A/p',
     'item_url_en': 'https://www.noon.com/egypt-en/N41044011A/p', 'item_uid': 'N41044011A',
     'item_website': 'noon.com'}, {'item_url_ar': 'https://www.noon.com/egypt-ar/N41044038A/p',
                                   'item_url_en': 'https://www.noon.com/egypt-en/N41044038A/p',
                                   'item_uid': 'N41044038A', 'item_website': 'noon.com'},
    {'item_url_ar': 'https://www.noon.com/egypt-ar/N41044028A/p',
     'item_url_en': 'https://www.noon.com/egypt-en/N41044028A/p', 'item_uid': 'N41044028A',
     'item_website': 'noon.com'}, {'item_url_ar': 'https://www.noon.com/egypt-ar/N41044025A/p',
                                   'item_url_en': 'https://www.noon.com/egypt-en/N41044025A/p',
                                   'item_uid': 'N41044025A', 'item_website': 'noon.com'},
    {'item_url_ar': 'https://www.noon.com/egypt-ar/N41044053A/p',
     'item_url_en': 'https://www.noon.com/egypt-en/N41044053A/p', 'item_uid': 'N41044053A',
     'item_website': 'noon.com'}, {'item_url_ar': 'https://www.noon.com/egypt-ar/N41044029A/p',
                                   'item_url_en': 'https://www.noon.com/egypt-en/N41044029A/p',
                                   'item_uid': 'N41044029A', 'item_website': 'noon.com'},
    {'item_url_ar': 'https://www.noon.com/egypt-ar/N41247234A/p',
     'item_url_en': 'https://www.noon.com/egypt-en/N41247234A/p', 'item_uid': 'N41247234A',
     'item_website': 'noon.com'}, {'item_url_ar': 'https://www.noon.com/egypt-ar/N41044026A/p',
                                   'item_url_en': 'https://www.noon.com/egypt-en/N41044026A/p',
                                   'item_uid': 'N41044026A', 'item_website': 'noon.com'},
    {'item_url_ar': 'https://www.noon.com/egypt-ar/N41044052A/p',
     'item_url_en': 'https://www.noon.com/egypt-en/N41044052A/p', 'item_uid': 'N41044052A',
     'item_website': 'noon.com'}, {'item_url_ar': 'https://www.noon.com/egypt-ar/N41044008A/p',
                                   'item_url_en': 'https://www.noon.com/egypt-en/N41044008A/p',
                                   'item_uid': 'N41044008A', 'item_website': 'noon.com'},
    {'item_url_ar': 'https://www.noon.com/egypt-ar/N41044047A/p',
     'item_url_en': 'https://www.noon.com/egypt-en/N41044047A/p', 'item_uid': 'N41044047A',
     'item_website': 'noon.com'}, {'item_url_ar': 'https://www.noon.com/egypt-ar/N41044010A/p',
                                   'item_url_en': 'https://www.noon.com/egypt-en/N41044010A/p',
                                   'item_uid': 'N41044010A', 'item_website': 'noon.com'},
    {'item_url_ar': 'https://www.noon.com/egypt-ar/N41044044A/p',
     'item_url_en': 'https://www.noon.com/egypt-en/N41044044A/p', 'item_uid': 'N41044044A',
     'item_website': 'noon.com'}, {'item_url_ar': 'https://www.noon.com/egypt-ar/N41044034A/p',
                                   'item_url_en': 'https://www.noon.com/egypt-en/N41044034A/p',
                                   'item_uid': 'N41044034A', 'item_website': 'noon.com'},
    {'item_url_ar': 'https://www.noon.com/egypt-ar/N41044043A/p',
     'item_url_en': 'https://www.noon.com/egypt-en/N41044043A/p', 'item_uid': 'N41044043A',
     'item_website': 'noon.com'}, {'item_url_ar': 'https://www.noon.com/egypt-ar/N41044035A/p',
                                   'item_url_en': 'https://www.noon.com/egypt-en/N41044035A/p',
                                   'item_uid': 'N41044035A', 'item_website': 'noon.com'},
    {'item_url_ar': 'https://www.noon.com/egypt-ar/N41044051A/p',
     'item_url_en': 'https://www.noon.com/egypt-en/N41044051A/p', 'item_uid': 'N41044051A',
     'item_website': 'noon.com'}, {'item_url_ar': 'https://www.noon.com/egypt-ar/N41233388A/p',
                                   'item_url_en': 'https://www.noon.com/egypt-en/N41233388A/p',
                                   'item_uid': 'N41233388A', 'item_website': 'noon.com'},
    {'item_url_ar': 'https://www.noon.com/egypt-ar/N41247159A/p',
     'item_url_en': 'https://www.noon.com/egypt-en/N41247159A/p', 'item_uid': 'N41247159A',
     'item_website': 'noon.com'}, {'item_url_ar': 'https://www.noon.com/egypt-ar/N41246628A/p',
                                   'item_url_en': 'https://www.noon.com/egypt-en/N41246628A/p',
                                   'item_uid': 'N41246628A', 'item_website': 'noon.com'},
    {'item_url_ar': 'https://www.noon.com/egypt-ar/N41247170A/p',
     'item_url_en': 'https://www.noon.com/egypt-en/N41247170A/p', 'item_uid': 'N41247170A',
     'item_website': 'noon.com'}, {'item_url_ar': 'https://www.noon.com/egypt-ar/N41222413A/p',
                                   'item_url_en': 'https://www.noon.com/egypt-en/N41222413A/p',
                                   'item_uid': 'N41222413A', 'item_website': 'noon.com'},
    {'item_url_ar': 'https://www.noon.com/egypt-ar/N37744183A/p',
     'item_url_en': 'https://www.noon.com/egypt-en/N37744183A/p', 'item_uid': 'N37744183A',
     'item_website': 'noon.com'}, {'item_url_ar': 'https://www.noon.com/egypt-ar/N29897909A/p',
                                   'item_url_en': 'https://www.noon.com/egypt-en/N29897909A/p',
                                   'item_uid': 'N29897909A', 'item_website': 'noon.com'},
    {'item_url_ar': 'https://www.noon.com/egypt-ar/N29897922A/p',
     'item_url_en': 'https://www.noon.com/egypt-en/N29897922A/p', 'item_uid': 'N29897922A',
     'item_website': 'noon.com'}, {'item_url_ar': 'https://www.noon.com/egypt-ar/N29897915A/p',
                                   'item_url_en': 'https://www.noon.com/egypt-en/N29897915A/p',
                                   'item_uid': 'N29897915A', 'item_website': 'noon.com'},
    {'item_url_ar': 'https://www.noon.com/egypt-ar/N29897917A/p',
     'item_url_en': 'https://www.noon.com/egypt-en/N29897917A/p', 'item_uid': 'N29897917A',
     'item_website': 'noon.com'}, {'item_url_ar': 'https://www.noon.com/egypt-ar/N29897943A/p',
                                   'item_url_en': 'https://www.noon.com/egypt-en/N29897943A/p',
                                   'item_uid': 'N29897943A', 'item_website': 'noon.com'},
    {'item_url_ar': 'https://www.noon.com/egypt-ar/N29897923A/p',
     'item_url_en': 'https://www.noon.com/egypt-en/N29897923A/p', 'item_uid': 'N29897923A',
     'item_website': 'noon.com'}, {'item_url_ar': 'https://www.noon.com/egypt-ar/N29897942A/p',
                                   'item_url_en': 'https://www.noon.com/egypt-en/N29897942A/p',
                                   'item_uid': 'N29897942A', 'item_website': 'noon.com'},
    {'item_url_ar': 'https://www.noon.com/egypt-ar/N29897941A/p',
     'item_url_en': 'https://www.noon.com/egypt-en/N29897941A/p', 'item_uid': 'N29897941A',
     'item_website': 'noon.com'}, {'item_url_ar': 'https://www.noon.com/egypt-ar/N32648766A/p',
                                   'item_url_en': 'https://www.noon.com/egypt-en/N32648766A/p',
                                   'item_uid': 'N32648766A', 'item_website': 'noon.com'},
    {'item_url_ar': 'https://www.noon.com/egypt-ar/N29897911A/p',
     'item_url_en': 'https://www.noon.com/egypt-en/N29897911A/p', 'item_uid': 'N29897911A',
     'item_website': 'noon.com'}, {'item_url_ar': 'https://www.noon.com/egypt-ar/N29884743A/p',
                                   'item_url_en': 'https://www.noon.com/egypt-en/N29884743A/p',
                                   'item_uid': 'N29884743A', 'item_website': 'noon.com'},
    {'item_url_ar': 'https://www.noon.com/egypt-ar/N29897939A/p',
     'item_url_en': 'https://www.noon.com/egypt-en/N29897939A/p', 'item_uid': 'N29897939A',
     'item_website': 'noon.com'}, {'item_url_ar': 'https://www.noon.com/egypt-ar/N29897926A/p',
                                   'item_url_en': 'https://www.noon.com/egypt-en/N29897926A/p',
                                   'item_uid': 'N29897926A', 'item_website': 'noon.com'},
    {'item_url_ar': 'https://www.noon.com/egypt-ar/N32648796A/p',
     'item_url_en': 'https://www.noon.com/egypt-en/N32648796A/p', 'item_uid': 'N32648796A',
     'item_website': 'noon.com'}, {'item_url_ar': 'https://www.noon.com/egypt-ar/N29884746A/p',
                                   'item_url_en': 'https://www.noon.com/egypt-en/N29884746A/p',
                                   'item_uid': 'N29884746A', 'item_website': 'noon.com'},
    {'item_url_ar': 'https://www.noon.com/egypt-ar/N29884748A/p',
     'item_url_en': 'https://www.noon.com/egypt-en/N29884748A/p', 'item_uid': 'N29884748A',
     'item_website': 'noon.com'}, {'item_url_ar': 'https://www.noon.com/egypt-ar/N12311034A/p',
                                   'item_url_en': 'https://www.noon.com/egypt-en/N12311034A/p',
                                   'item_uid': 'N12311034A', 'item_website': 'noon.com'},
    {'item_url_ar': 'https://www.noon.com/egypt-ar/N41280924A/p',
     'item_url_en': 'https://www.noon.com/egypt-en/N41280924A/p', 'item_uid': 'N41280924A',
     'item_website': 'noon.com'}, {'item_url_ar': 'https://www.noon.com/egypt-ar/N11046277A/p',
                                   'item_url_en': 'https://www.noon.com/egypt-en/N11046277A/p',
                                   'item_uid': 'N11046277A', 'item_website': 'noon.com'},
    {'item_url_ar': 'https://www.noon.com/egypt-ar/N11046204A/p',
     'item_url_en': 'https://www.noon.com/egypt-en/N11046204A/p', 'item_uid': 'N11046204A',
     'item_website': 'noon.com'}, {'item_url_ar': 'https://www.noon.com/egypt-ar/N12273254A/p',
                                   'item_url_en': 'https://www.noon.com/egypt-en/N12273254A/p',
                                   'item_uid': 'N12273254A', 'item_website': 'noon.com'},
    {'item_url_ar': 'https://btech.com/ar/screen-protector-ywc98-apple-iphone-x-iphone-10.html',
     'item_url_en': 'https://btech.com/en/screen-protector-ywc98-apple-iphone-x-iphone-10.html', 'item_uid': '12788',
     'item_website': 'btech.com'},
    {'item_url_ar': 'https://btech.com/ar/apple-iphone-11-no-facetime-128gb-black-1617274199.html',
     'item_url_en': 'https://btech.com/en/apple-iphone-11-no-facetime-128gb-black-1617274199.html',
     'item_uid': '36679', 'item_website': 'btech.com'},
    {'item_url_ar': 'https://btech.com/ar/apple-iphone-11-no-facetime-128gb-white-1617276752.html',
     'item_url_en': 'https://btech.com/en/apple-iphone-11-no-facetime-128gb-white-1617276752.html',
     'item_uid': '36683', 'item_website': 'btech.com'},
    {'item_url_ar': 'https://btech.com/ar/apple-iphone-8-plus-128gb-grey-1600703066.html',
     'item_url_en': 'https://btech.com/en/apple-iphone-8-plus-128gb-grey-1600703066.html', 'item_uid': '28641',
     'item_website': 'btech.com'},
    {'item_url_ar': 'https://btech.com/ar/apple-iphone-se-128gb-3gb-red-1600706313.html',
     'item_url_en': 'https://btech.com/en/apple-iphone-se-128gb-3gb-red-1600706313.html', 'item_uid': '28683',
     'item_website': 'btech.com'},
    {'item_url_ar': 'https://btech.com/ar/apple-iphone-xs-max-64gb-space-grey-1573043042.html',
     'item_url_en': 'https://btech.com/en/apple-iphone-xs-max-64gb-space-grey-1573043042.html', 'item_uid': '12963',
     'item_website': 'btech.com'}, {'item_url_ar': 'https://btech.com/ar/apple-iphone-xr-128gb-red-1573728966.html',
                                    'item_url_en': 'https://btech.com/en/apple-iphone-xr-128gb-red-1573728966.html',
                                    'item_uid': '13115', 'item_website': 'btech.com'},
    {'item_url_ar': 'https://btech.com/ar/apple-iphone-12-mini-64gb-blue-1617273310.html',
     'item_url_en': 'https://btech.com/en/apple-iphone-12-mini-64gb-blue-1617273310.html', 'item_uid': '36676',
     'item_website': 'btech.com'}, {'item_url_ar': 'https://btech.com/ar/apple-iphone-xr-128gb-black-1573042168.html',
                                    'item_url_en': 'https://btech.com/en/apple-iphone-xr-128gb-black-1573042168.html',
                                    'item_uid': '12949', 'item_website': 'btech.com'},
    {'item_url_ar': 'https://btech.com/ar/apple-iphone-xr-128gb-white-1573728970.html',
     'item_url_en': 'https://btech.com/en/apple-iphone-xr-128gb-white-1573728970.html', 'item_uid': '13116',
     'item_website': 'btech.com'}, {'item_url_ar': 'https://btech.com/ar/apple-iphone-11-256gb-green-1600703731.html',
                                    'item_url_en': 'https://btech.com/en/apple-iphone-11-256gb-green-1600703731.html',
                                    'item_uid': '28660', 'item_website': 'btech.com'},
    {'item_url_ar': 'https://btech.com/ar/apple-iphone-11-64gb-yellow-1600703256.html',
     'item_url_en': 'https://btech.com/en/apple-iphone-11-64gb-yellow-1600703256.html', 'item_uid': '28646',
     'item_website': 'btech.com'}, {'item_url_ar': 'https://btech.com/ar/apple-iphone-se-64gb-3gb-red-1600705012.html',
                                    'item_url_en': 'https://btech.com/en/apple-iphone-se-64gb-3gb-red-1600705012.html',
                                    'item_uid': '28679', 'item_website': 'btech.com'},
    {'item_url_ar': 'https://btech.com/ar/apple-iphone-11-256gb-purple-1600703681.html',
     'item_url_en': 'https://btech.com/en/apple-iphone-11-256gb-purple-1600703681.html', 'item_uid': '28658',
     'item_website': 'btech.com'}, {'item_url_ar': 'https://btech.com/ar/apple-iphone-xs-256gb-silver-1573042609.html',
                                    'item_url_en': 'https://btech.com/en/apple-iphone-xs-256gb-silver-1573042609.html',
                                    'item_uid': '12956', 'item_website': 'btech.com'},
    {'item_url_ar': 'https://btech.com/ar/apple-iphone-12-pro-max-256gb-gold-1617273188.html',
     'item_url_en': 'https://btech.com/en/apple-iphone-12-pro-max-256gb-gold-1617273188.html', 'item_uid': '36675',
     'item_website': 'btech.com'}, {'item_url_ar': 'https://btech.com/ar/apple-iphone-11-128gb-purple-1588685402.html',
                                    'item_url_en': 'https://btech.com/en/apple-iphone-11-128gb-purple-1588685402.html',
                                    'item_uid': '19816', 'item_website': 'btech.com'},
    {'item_url_ar': 'https://btech.com/ar/apple-iphone-11-256gb-red-1600703651.html',
     'item_url_en': 'https://btech.com/en/apple-iphone-11-256gb-red-1600703651.html', 'item_uid': '28657',
     'item_website': 'btech.com'},
    {'item_url_ar': 'https://btech.com/ar/apple-iphone-se-64gb-3gb-white-1600704990.html',
     'item_url_en': 'https://btech.com/en/apple-iphone-se-64gb-3gb-white-1600704990.html', 'item_uid': '28678',
     'item_website': 'btech.com'},
    {'item_url_ar': 'https://btech.com/ar/apple-iphone-se-128gb-3gb-black-1600706252.html',
     'item_url_en': 'https://btech.com/en/apple-iphone-se-128gb-3gb-black-1600706252.html', 'item_uid': '28681',
     'item_website': 'btech.com'}, {'item_url_ar': 'https://btech.com/ar/apple-iphone-xs-256gb-gold-1573042601.html',
                                    'item_url_en': 'https://btech.com/en/apple-iphone-xs-256gb-gold-1573042601.html',
                                    'item_uid': '12955', 'item_website': 'btech.com'},
    {'item_url_ar': 'https://btech.com/ar/apple-iphone-11-256gb-white-1600703628.html',
     'item_url_en': 'https://btech.com/en/apple-iphone-11-256gb-white-1600703628.html', 'item_uid': '28656',
     'item_website': 'btech.com'},
    {'item_url_ar': 'https://btech.com/ar/apple-iphone-xs-max-64gb-silver-1605694537.html',
     'item_url_en': 'https://btech.com/en/apple-iphone-xs-max-64gb-silver-1605694537.html', 'item_uid': '31626',
     'item_website': 'btech.com'},
    {'item_url_ar': 'https://btech.com/ar/apple-iphone-se-128gb-3gb-white-1600706288.html',
     'item_url_en': 'https://btech.com/en/apple-iphone-se-128gb-3gb-white-1600706288.html', 'item_uid': '28682',
     'item_website': 'btech.com'}, {'item_url_ar': 'https://btech.com/ar/cover-02y48-iphone-x.html',
                                    'item_url_en': 'https://btech.com/en/cover-02y48-iphone-x.html',
                                    'item_uid': '13279', 'item_website': 'btech.com'},
    {'item_url_ar': 'https://btech.com/ar/cover-apple-iphone-7-ywcc-1.html',
     'item_url_en': 'https://btech.com/en/cover-apple-iphone-7-ywcc-1.html', 'item_uid': '12981',
     'item_website': 'btech.com'},
    {'item_url_ar': 'https://btech.com/ar/armor-matte-nano-protector-iphone-11-pro-max-1614026808.html',
     'item_url_en': 'https://btech.com/en/armor-matte-nano-protector-iphone-11-pro-max-1614026808.html',
     'item_uid': '34974', 'item_website': 'btech.com'},
    {'item_url_ar': 'https://btech.com/ar/jetech-rubber-case-82y41-iphone-6-plus.html',
     'item_url_en': 'https://btech.com/en/jetech-rubber-case-82y41-iphone-6-plus.html', 'item_uid': '13272',
     'item_website': 'btech.com'},
    {'item_url_ar': 'https://btech.com/ar/screen-protector-ywc62-apple-iphone-xs-max.html',
     'item_url_en': 'https://btech.com/en/screen-protector-ywc62-apple-iphone-xs-max.html', 'item_uid': '12805',
     'item_website': 'btech.com'}, {'item_url_ar': 'https://btech.com/ar/muzz-cover-74y3-iphone-xs-max.html',
                                    'item_url_en': 'https://btech.com/en/muzz-cover-74y3-iphone-xs-max.html',
                                    'item_uid': '13123', 'item_website': 'btech.com'}]

# @timer(1, 1)
# def test():
#     urls = [
#         'http://www.heroku.com',
#         'http://python-tablib.org',
#         'http://httpbin.org',
#         'http://python-requests.org',
#         'http://fakedomain/',
#         'http://kennethreitz.com'
#     ]
#     rs = (grequests.get(u) for u in urls)
#     # rs = (grequests.get(u) for u in d)
#     r = grequests.map(rs)
#     print(r)


# from concurrent.futures import ThreadPoolExecutor
# import requests
import timeit


#
#
# #
def timer(number, repeat):
    def wrapper(func):
        runs = timeit.repeat(func, number=number, repeat=repeat)
        print(sum(runs) / len(runs))

    return wrapper


#
#
# def get(item_url_en):
#     response_en = requests.get(item_url_en)
#     # response_ar = requests.get(item_url_ar, headers=header)
#
#
# @timer(1, 10)
# def run():
#     urls = [
#         'http://www.heroku.com',
#         'http://python-tablib.org',
#         'http://httpbin.org',
#         'http://python-requests.org',
#         'http://kennethreitz.com',
#         'http://kennethreitz.com'
#     ]
#     with ThreadPoolExecutor(max_workers=20) as executor:
#         results = executor.map(get, urls)


import aiohttp
import asyncio
import os
from aiohttp import ClientSession
import json
import pypeln as pl
from aiohttp import ClientSession, TCPConnector, client_exceptions
import re
from fake_useragent import UserAgent
from requests.exceptions import HTTPError


def extract_fields_from_response(response):
    item = response.get("items", [{}])[0]
    volume_info = item.get("volumeInfo", {})
    title = volume_info.get("title", None)
    subtitle = volume_info.get("subtitle", None)
    description = volume_info.get("description", None)
    published_date = volume_info.get("publishedDate", None)
    return (
        title,
        subtitle,
        description,
        published_date,
    )


def user_agent():
    try:
        return re.search(r'(.*?)\)', UserAgent().random).group(1) + "MSIE 12;)"
    except AttributeError:
        return re.search(r'(.*?)\)', UserAgent().random).group(1) + "MSIE 12;)"


async def get_data(lang, dict_item, session):
    if lang == 'en':
        url = dict_item.get('item_url_en')
    else:
        url = dict_item.get('item_url_ar')

    header = {
        "User-Agent": user_agent(),
        "Accept": "*/*",
        "Accept-Language": "*/*",
        "Accept-Charset": "*/*",
        "Connection": "keep-alive",
        "Keep-Alive": "300"
    }

    try:
        response = await session.request(method='GET', url=url, headers=header)
        response.raise_for_status()
        print(f"Response status en ({url}): {response.status}")
    # except HTTPError as http_err:
    #     print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error ocurred en: {err}")
    # try:
    #     response_ar = await session.request(method='GET', url=url_ar)
    #     response_ar.raise_for_status()
    #     print(f"Response status ar ({url}): {response_ar.status}")

    # except Exception as err:
    #     print(f"An error ocurred ar: {err}")
    response_json = await response.text()
    return response_json


async def main():
    try:
        async with ClientSession() as session:
            print(session)
            group1 = await asyncio.gather(*[get_data('en', dict_item, session) for dict_item in d])
            # group2 = asyncio.gather(*[get_data('ar', dict_item, session) for dict_item in d])
            # await asyncio.gather(group1, group2)
    except Exception as err:
        # await asyncio.gather(group1, group2)
        print(f"An error ocurred in session: {err}")


# limit = 50


@timer(1, 2)
def run_time():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    # pl.task.each(
    #     run_program,
    #     d,
    #     workers=limit,
    #     on_start=lambda: dict(session=ClientSession(connector=TCPConnector(limit=None))),
    #     on_done=lambda session: session.close(),
    #     run=True,
    # )
