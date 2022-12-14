def super_care_func(item_type_arg):
    super_care_dict = {"Music CDs": "Media@أفلام و موسيقى",
                       "Video Games": "Video Games@العاب الكترونية",
                       "Lifestyle Books": "Books@كتب",
                       "Game Consoles": "Video Games@العاب الكترونية",
                       "Games Gadgets & Accessories": "Video Games@العاب الكترونية",
                       "Software": "Media@أفلام و موسيقى",
                       "DVD and Blu-ray Players": "Electronics@إلكترونيات",
                       "Televisions": "Home Appliances@الأجهزة المنزلية",
                       "Home Theater Systems": "Home Appliances@الأجهزة المنزلية",
                       "Projectors": "Electronics@إلكترونيات",
                       "Digital Cameras": "Cameras & Optics@كاميرات وبصريات",
                       "Camcorders": "Cameras & Optics@كاميرات وبصريات",
                       "GPS Navigators": "Vehicle Parts & Accessories@قطع ولوازم سيارات",
                       "PDAs": "Other@آخرى",
                       "Media Players": "Electronics@إلكترونيات",
                       "CD Players & Recorders": "Electronics@إلكترونيات",
                       "Stereo Systems and Equalizers": "Electronics@إلكترونيات",
                       "Amplifiers and Receivers": "Electronics@إلكترونيات",
                       "Speakers": "Electronics@إلكترونيات",
                       "MP3 & MP4 players": "Electronics@إلكترونيات",
                       "Toys": "Toys & Games@لعب الاطفال",
                       "Camera and camcorder Accessories": "Cameras & Optics@كاميرات وبصريات",
                       "Mobile Phone Accessories": "Mobile Phone Accessories@ملحقات الهاتف المحمول",
                       "Projectors Accessories": "Electronics@إلكترونيات",
                       "TV and Satellite Accessories": "Electronics@إلكترونيات",
                       "Cable": "Electronics@إلكترونيات",
                       "Audio Accessories": "Electronics@إلكترونيات",
                       "Webcams": "Computers@أجهزة الكمبيوتر",
                       "Digital Photo Frames": "Cameras & Optics@كاميرات وبصريات",
                       "Mobile Phones": "Mobile Phones & Tablets@الهواتف المحمولة والاجهزة لوحية",
                       "Telephones": "Electronics@إلكترونيات",
                       "Car Audio": "Vehicle Parts & Accessories@قطع ولوازم سيارات",
                       "Specialty Bags & Carry Cases": "Computers@أجهزة الكمبيوتر",
                       "Barcode reader": "Computers@أجهزة الكمبيوتر",
                       "Blank CDs": "Computers@أجهزة الكمبيوتر",
                       "Blank DVDs": "Computers@أجهزة الكمبيوتر",
                       "Mouse": "Computers@أجهزة الكمبيوتر",
                       "PCs": "Computers@أجهزة الكمبيوتر",
                       "Photo Copiers": "Media@أفلام و موسيقى",
                       "CPUs & Processors": "Computers@أجهزة الكمبيوتر",
                       "Docking Station": "Computers@أجهزة الكمبيوتر",
                       "Fax Machines and Shredders": "Office Supplies@اللوازم المكتبية",
                       "Uninterruptible Power Supply UPS": "Computers@أجهزة الكمبيوتر",
                       "Hard Drives": "Computers@أجهزة الكمبيوتر",
                       "Hardware components": "Electronics@إلكترونيات",
                       "Specialty Kitchen Appliances": "Kitchen Appliances@أدوات المطبخ",
                       "Ink Cartridges": "Office Supplies@اللوازم المكتبية",
                       "IT Security": "IT & Network@شبكات و برامج",
                       "Keyboards": "Computers@أجهزة الكمبيوتر",
                       "Memory Modules": "Computers@أجهزة الكمبيوتر",
                       "Motherboards": "Computers@أجهزة الكمبيوتر",
                       "Multifunctional Printers": "Office Supplies@اللوازم المكتبية",
                       "Network cards & adapters": "Computers@أجهزة الكمبيوتر",
                       "Networking Tools": "IT & Network@شبكات و برامج",
                       "Network switches": "IT & Network@شبكات و برامج",
                       "Laptops & Notebooks": "Computers@أجهزة الكمبيوتر",
                       "Office equipment": "Office Supplies@اللوازم المكتبية",
                       "Office Furniture": "Furniture@أثاث المنزل",
                       "Office Supplies": "Office Supplies@اللوازم المكتبية",
                       "Health and Personal Care": "Health & Personal care@الصحة والعناية الشخصية",
                       "Work Safety Equipment & Gear": "Business & Industrial@تجارة و صناعة",
                       "Power supplies": "Computers@أجهزة الكمبيوتر",
                       "Printer and Scanner Accessories": "Office Supplies@اللوازم المكتبية",
                       "Batteries": "Electronics@إلكترونيات",
                       "Router": "IT & Network@شبكات و برامج",
                       "Scanners": "Office Supplies@اللوازم المكتبية",
                       "Server": "IT & Network@شبكات و برامج",
                       "Surge Protection": "Electronics@إلكترونيات",
                       "Tablets": "Mobile Phones & Tablets@الهواتف المحمولة والاجهزة لوحية",
                       "Thin Clients": "Other@آخرى",
                       "Power Tools": "Hardware & Improvements Tools@قطع الغيار و تحسينات أدوات",
                       "Video Cards": "Computers@أجهزة الكمبيوتر",
                       "Other": "Other@آخرى",
                       "Garden decoration": "Garden@الحديقة",
                       "Gardening and Watering equipments": "Garden@الحديقة",
                       "Barbecue Grills & Smokers": "Kitchen Appliances@أدوات المطبخ",
                       "Tables": "Furniture@أثاث المنزل",
                       "Chairs and benches": "Furniture@أثاث المنزل",
                       "Sofas, Bean bags & Ottomans": "Furniture@أثاث المنزل",
                       "Storage & Organization": "Furniture@أثاث المنزل",
                       "Light Bulbs": "Electronics@إلكترونيات",
                       "Bedding Sets & Components": "Home Supplies@اللوازم المنزلية",
                       "Home Decor": "Furniture@أثاث المنزل",
                       "Bathroom Accessories": "Bath Supplies@لوازم الحمام",
                       "Sports Equipments": "Sporting Goods & Fitness@مستلزمات الرياضية واللياقة البدنية",
                       "Sports Nutrition": "Health & Personal care@الصحة والعناية الشخصية",
                       "Prepaid cards": "Digital Products@المنتجات الرقمية",
                       "Lines and Numbers": "Other@آخرى",
                       "Tablet Accessories": "Mobile Phone Accessories@ملحقات الهاتف المحمول",
                       "Microphones": "Computers@أجهزة الكمبيوتر",
                       "domain names": "Digital Products@المنتجات الرقمية",
                       "Computers Fans": "Computers@أجهزة الكمبيوتر",
                       "Cooling Pads": "Computers@أجهزة الكمبيوتر",
                       "Computer & Laptop Accessories": "Computers@أجهزة الكمبيوتر",
                       "Computer Monitors": "Computers@أجهزة الكمبيوتر",
                       "Printers": "Office Supplies@اللوازم المكتبية",
                       "Women's Sleepwear": "Apparel & Accessories@ملابس واكسسوارات",
                       "MP3,MP4 Players Accessories": "Electronics@إلكترونيات",
                       "Satellite Receivers": "Electronics@إلكترونيات",
                       "DVD- VCR Combos": "Computers@أجهزة الكمبيوتر",
                       "Home Video Accessories": "Electronics@إلكترونيات",
                       "Recording and Studio Equipment": "Electronics@إلكترونيات",
                       "Vacuums & Floor Care Accessories": "Home Appliances@الأجهزة المنزلية",
                       "Ironing Accessories": "Home Supplies@اللوازم المنزلية",
                       "Sewing and Accessories": "Home Appliances@الأجهزة المنزلية",
                       "E-book Readers": "Books@كتب",
                       "Air Conditioners & Coolers": "Home Appliances@الأجهزة المنزلية",
                       "Heaters": "Home Appliances@الأجهزة المنزلية",
                       "Security & Surveillance Systems": "Electronics@إلكترونيات",
                       "Fans": "Home Appliances@الأجهزة المنزلية",
                       "Car Video": "Vehicle Parts & Accessories@قطع ولوازم سيارات",
                       "Smart Watches & Watches Accessories": "Electronics@إلكترونيات",
                       "Rings": "Jewelry@المجوهرات",
                       "Necklaces": "Jewelry@المجوهرات",
                       "Earrings": "Jewelry@المجوهرات",
                       "Bracelets": "Jewelry@المجوهرات",
                       "loose gemstones & diamonds": "Jewelry@المجوهرات",
                       "Jewelry sets": "Jewelry@المجوهرات",
                       "Jewelry Accessories": "Jewelry@المجوهرات",
                       "Men's Jewelry": "Jewelry@المجوهرات",
                       "Car speakers, Sub-woofers and Amplifiers": "Vehicle Parts & Accessories@قطع ولوازم سيارات",
                       "Makeup": "Beauty@الجمال",
                       "Skin Care": "Beauty@الجمال",
                       "Hair Care": "Beauty@الجمال",
                       "Bath & Body": "Health & Personal care@الصحة والعناية الشخصية",
                       "Men's Grooming": "Health & Personal care@الصحة والعناية الشخصية",
                       "Beauty Tools and Accessories": "Beauty@الجمال",
                       "Beauty Gifts and Sets": "Beauty@الجمال",
                       "Hair Extensions Wigs & Accessories": "Beauty@الجمال",
                       "Small Medical Equipment": "Personal Care Appliances@أجهزة العناية الشخصية",
                       "Drawings & Paintings": "Arts & Entertainment@فنون وترفيه",
                       "handcrafts, sculpture & carvings": "Furniture@أثاث المنزل",
                       "maps, atlases & globes": "Arts & Entertainment@فنون وترفيه",
                       "Antiques": "Furniture@أثاث المنزل",
                       "tourism packages": "Other@آخرى",
                       "Travel Tickets": "Other@آخرى",
                       "Vouchers": "Arts & Entertainment@فنون وترفيه",
                       "Prints, Posters & Photographs": "Arts & Entertainment@فنون وترفيه",
                       "Kitchen Accessories": "Kitchen Supplies@لوازم المطبخ",
                       "Bedroom Furniture Sets": "Furniture@أثاث المنزل",
                       "Barbecue Tools and Grill Accessories": "Kitchen Supplies@لوازم المطبخ",
                       "Hand Tools": "Hardware & Improvements Tools@قطع الغيار و تحسينات أدوات",
                       "Musical Instruments": "Arts & Entertainment@فنون وترفيه",
                       "Movies, Plays and Series": "Media@أفلام و موسيقى",
                       "Sporting Goods": "Sporting Goods & Fitness@مستلزمات الرياضية واللياقة البدنية",
                       "Camping Goods": "Outdoor Recreation products@المنتجات الترفيه خارج المنزل",
                       "Coins": "Arts & Entertainment@فنون وترفيه",
                       "Paper Money": "Arts & Entertainment@فنون وترفيه",
                       "Stamps": "Arts & Entertainment@فنون وترفيه",
                       "Magazines": "Media@أفلام و موسيقى",
                       "GPS accessories": "Vehicle Parts & Accessories@قطع ولوازم سيارات",
                       "Car Audio and Video Accessories": "Vehicle Parts & Accessories@قطع ولوازم سيارات",
                       "Baby Gears": "Baby & Toddler@لوازم الاطفال",
                       "Baby Safety and Health": "Baby & Toddler@لوازم الاطفال",
                       "Feeding": "Baby & Toddler@لوازم الاطفال",
                       "Nursery Furniture & Décor": "Furniture@أثاث المنزل",
                       "Baby Toys and Accessories": "Baby & Toddler@لوازم الاطفال",
                       "Stationery": "Office Supplies@اللوازم المكتبية",
                       "Home Supplies": "Home Supplies@اللوازم المنزلية",
                       "Data Storage devices": "Computers@أجهزة الكمبيوتر",
                       "Clocks": "Furniture@أثاث المنزل",
                       "Baby Bags": "Baby & Toddler@لوازم الاطفال",
                       "Baby Clothes & Shoes": "Baby & Toddler@لوازم الاطفال",
                       "closed items": "Other@آخرى",
                       "E-books": "Books@كتب",
                       "Womens Lingerie": "Apparel & Accessories@ملابس واكسسوارات",
                       "Electrical Personal Care": "Personal Care Appliances@أجهزة العناية الشخصية",
                       "Chargers": "Mobile Phone Accessories@ملحقات الهاتف المحمول",
                       "Children's Books": "Books@كتب",
                       "Business & Trade Books": "Books@كتب",
                       "Education, Learning & Self Help Books": "Books@كتب",
                       "Pet & Animals Supplies": "Animals & Pet Supplies@مستلزمات الحيوانات الأليفة",
                       "Car Care Products": "Vehicle Parts & Accessories@قطع ولوازم سيارات",
                       "Telephone Accessories": "Electronics@إلكترونيات",
                       "GPS Receiver": "Vehicle Parts & Accessories@قطع ولوازم سيارات",
                       "USB Flash Drives": "Computers@أجهزة الكمبيوتر",
                       "Card Readers / Writers": "Electronics@إلكترونيات",
                       "Optical Drives": "Computers@أجهزة الكمبيوتر",
                       "Headphones & Headsets": "Computers@أجهزة الكمبيوتر",
                       "TV Mounts": "Home Supplies@اللوازم المنزلية",
                       "Interchangeable Lenses": "Cameras & Optics@كاميرات وبصريات",
                       "Binoculars and Telescopes": "Electronics@إلكترونيات",
                       "CD Recording Media": "Electronics@إلكترونيات",
                       "Sandwich & Waffle Makers": "Kitchen Appliances@أدوات المطبخ",
                       "Personal Draught Systems": "Other@آخرى",
                       "Juicers & Presses": "Kitchen Appliances@أدوات المطبخ",
                       "Oral Care": "Health & Personal care@الصحة والعناية الشخصية",
                       "Rice Cooker": "Kitchen Appliances@أدوات المطبخ",
                       "Fryers": "Kitchen Appliances@أدوات المطبخ",
                       "Toasters": "Kitchen Appliances@أدوات المطبخ",
                       "Kettles": "Home Appliances@الأجهزة المنزلية",
                       "Kitchen Scales": "Kitchen Appliances@أدوات المطبخ",
                       "Electric Slicers": "Kitchen Appliances@أدوات المطبخ",
                       "Food Preparation": "Kitchen Appliances@أدوات المطبخ",
                       "Irons": "Home Appliances@الأجهزة المنزلية",
                       "Thermometers": "Personal Care Appliances@أجهزة العناية الشخصية",
                       "Analogue Cameras": "Cameras & Optics@كاميرات وبصريات",
                       "Electronic Flashes": "Cameras & Optics@كاميرات وبصريات",
                       "Memory Cards": "Mobile Phone Accessories@ملحقات الهاتف المحمول",
                       "Portable Radios": "Electronics@إلكترونيات",
                       "Clock Radios": "Electronics@إلكترونيات",
                       "Communication Devices": "Electronics@إلكترونيات",
                       "Media Gateways": "Computers@أجهزة الكمبيوتر",
                       "Universal Remote Controls": "Electronics@إلكترونيات",
                       "Tuners": "Electronics@إلكترونيات",
                       "Steam Cleaners": "Home Appliances@الأجهزة المنزلية",
                       "Vacuum Cleaners": "Home Appliances@الأجهزة المنزلية",
                       "Personal Scales": "Personal Care Appliances@أجهزة العناية الشخصية",
                       "Coffee & Espresso Makers": "Home Appliances@الأجهزة المنزلية",
                       "Still Films": "Cameras & Optics@كاميرات وبصريات",
                       "Car Vision": "Vehicle Parts & Accessories@قطع ولوازم سيارات",
                       "Air Treatment": "Home Supplies@اللوازم المنزلية",
                       "Video Tapes": "Media@أفلام و موسيقى",
                       "Cookware": "Kitchen Supplies@لوازم المطبخ",
                       "Portable Cassette & CD Players": "Electronics@إلكترونيات",
                       "Islamic, Ethnic and Digital Art": "Religious & Ceremonial@اسلاميات",
                       "Baby Gift Sets": "Baby & Toddler@لوازم الاطفال",
                       "Baby Accessories": "Baby & Toddler@لوازم الاطفال",
                       "Comics & Graphic Novels": "books@كتب",
                       "Literature & Fiction": "Books@كتب",
                       "Eyewear": "Apparel & Accessories@ملابس واكسسوارات",
                       "Shoes Accessories": "Shoes@الأحذية",
                       "Smoking Accessories": "Home & Garden - Outdoor@المنزل والحديقة",
                       "Maternity Wear": "Apparel & Accessories@ملابس واكسسوارات",
                       "Uniform": "Apparel & Accessories@ملابس واكسسوارات",
                       "Coins & Stamps Accessories": "Arts & Entertainment@فنون وترفيه",
                       "Sound Cards": "Computers@أجهزة الكمبيوتر",
                       "Computer Casing": "Computers@أجهزة الكمبيوتر",
                       "Microwaves": "Kitchen Appliances@أدوات المطبخ",
                       "VCD, VCP and VCR Players": "Electronics@إلكترونيات",
                       "Dietary Supplements": "Health & Personal care@الصحة والعناية الشخصية",
                       "Vitamins & Minerals": "Health & Personal care@الصحة والعناية الشخصية",
                       "Rugs & Carpets": "Home Supplies@اللوازم المنزلية",
                       "Aquariums & Indoor Fountains": "Furniture@أثاث المنزل",
                       "Services": "Other@آخرى",
                       "Musical Instruments Parts": "Arts & Entertainment@فنون وترفيه",
                       "Large Musical Instruments": "Arts & Entertainment@فنون وترفيه",
                       "Plates Numbers": "Other@آخرى",
                       "Boats Parts & Accessories": "Outdoor Recreation products@المنتجات الترفيه خارج المنزل",
                       "Keys & key chains": "Hardware & Improvements Tools@قطع الغيار و تحسينات أدوات",
                       "Tires & Wheels": "Vehicle Parts & Accessories@قطع ولوازم سيارات",
                       "Concerts & Events": "Arts & Entertainment@فنون وترفيه",
                       "Dresses": "Apparel & Accessories@ملابس واكسسوارات",
                       "Accessories": "Apparel & Accessories@ملابس واكسسوارات",
                       "Sportswear": "Apparel & Accessories@ملابس واكسسوارات",
                       "Backpacks": "Luggage@حقائب السفر",
                       "Boots": "Shoes@الأحذية",
                       "Costumes & Accessories": "Apparel & Accessories@ملابس واكسسوارات",
                       "Handbags": "Apparel & Accessories@ملابس واكسسوارات",
                       "Jackets & Coats": "Apparel & Accessories@ملابس واكسسوارات",
                       "Trolley Suitcases & Bags": "Luggage@حقائب السفر",
                       "Pants": "Apparel & Accessories@ملابس واكسسوارات",
                       "Perfumes & Fragrances": "Beauty@الجمال",
                       "Sandals": "Shoes@الأحذية",
                       "Casual & Dress Shoes": "Shoes@الأحذية",
                       "Shorts": "Apparel & Accessories@ملابس واكسسوارات",
                       "Skirts": "Apparel & Accessories@ملابس واكسسوارات",
                       "Sleepwear": "Apparel & Accessories@ملابس واكسسوارات",
                       "Slippers": "Shoes@الأحذية",
                       "Suits": "Apparel & Accessories@ملابس واكسسوارات",
                       "Swimwear": "Apparel & Accessories@ملابس واكسسوارات",
                       "Tops": "Apparel & Accessories@ملابس واكسسوارات",
                       "Underwear": "Apparel & Accessories@ملابس واكسسوارات",
                       "Watches": "Watches@الساعات",
                       "Hair Styling Electronics": "Beauty@الجمال",
                       "Garden Furniture": "Garden@الحديقة",
                       "Pet Food & Supplements": "Animals & Pet Supplies@مستلزمات الحيوانات الأليفة",
                       "Pendants & Charms": "Jewelry@المجوهرات",
                       "Diapers": "Baby & Toddler@لوازم الاطفال",
                       "Baby Bath & Skin Care": "Baby & Toddler@لوازم الاطفال",
                       "Fitness Technology": "Sporting Goods & Fitness@مستلزمات الرياضية واللياقة البدنية",
                       "Outdoor Play": "Toys & Games@لعب الاطفال",
                       "Party Supplies": "Arts & Entertainment@فنون وترفيه",
                       "Scooters & Ride-Ons": "Toys & Games@لعب الاطفال",
                       "Combos": "Other@آخرى",
                       "Lamps & Lightings": "Electronics@إلكترونيات",
                       "Blenders & Mixers": "Home Appliances@الأجهزة المنزلية",
                       "Food Processors": "Kitchen Appliances@أدوات المطبخ",
                       "Paint & Supplies": "Hardware & Improvements Tools@قطع الغيار و تحسينات أدوات",
                       "Drinkware": "Kitchen Supplies@لوازم المطبخ",
                       "Nails, Screws & Fixings": "Hardware & Improvements Tools@قطع الغيار و تحسينات أدوات",
                       "Smart Watches": "Electronics@إلكترونيات",
                       "Bed Pillows": "Home Supplies@اللوازم المنزلية",
                       "3D Glasses": "Electronics@إلكترونيات",
                       "Screen Protectors": "Mobile Phone Accessories@ملحقات الهاتف المحمول",
                       "USB Hubs": "Computers@أجهزة الكمبيوتر",
                       "Decorative Pillows & Cushions": "Home Supplies@اللوازم المنزلية",
                       "Skins & Decals": "Mobile Phone Accessories@ملحقات الهاتف المحمول",
                       "Ethnic & Traditional Wear": "Religious & Ceremonial@اسلاميات",
                       "Washing Machines": "Kitchen Appliances@أدوات المطبخ",
                       "Dishwashers": "Kitchen Appliances@أدوات المطبخ",
                       "Cutlery & Flatware Sets": "Kitchen Supplies@لوازم المطبخ",
                       "Table Linens": "Home Supplies@اللوازم المنزلية",
                       "Measuring & Layout Tools": "Hardware & Improvements Tools@قطع الغيار و تحسينات أدوات",
                       "Mattresses": "Home Supplies@اللوازم المنزلية",
                       "Towels": "Home Supplies@اللوازم المنزلية",
                       "Bakeware & Accessories": "Kitchen Supplies@لوازم المطبخ",
                       "Kitchen Measuring Tools": "Kitchen Supplies@لوازم المطبخ",
                       "Curtains & Accessories": "Home Supplies@اللوازم المنزلية",
                       "Showers & Showerheads": "Bath Supplies@لوازم الحمام",
                       "Refrigerators & Freezers": "Kitchen Appliances@أدوات المطبخ",
                       "Hair Tools & Accessories": "Beauty@الجمال",
                       "Wallets": "Luggage@حقائب السفر",
                       "Athletic Shoes": "Sporting Goods & Fitness@مستلزمات الرياضية واللياقة البدنية",
                       "Body Massagers": "Personal Care Appliances@أجهزة العناية الشخصية",
                       "Baby Food": "Baby & Toddler@لوازم الاطفال",
                       "Electric Shavers & Removal": "Personal Care Appliances@أجهزة العناية الشخصية",
                       "Blankets & Throws": "Home Supplies@اللوازم المنزلية",
                       "3D Printers": "Office Supplies@اللوازم المكتبية",
                       "Internet Packages": "Computers@أجهزة الكمبيوتر",
                       "Label Printers": "Office Supplies@اللوازم المكتبية",
                       "Dinnerware & Serveware": "Kitchen Supplies@لوازم المطبخ",
                       "Cooking Utensils": "Kitchen Supplies@لوازم المطبخ",
                       "Power & Hand Tools Accessories": "Hardware & Improvements Tools@قطع الغيار و تحسينات أدوات",
                       "Pest Control": "Garden@الحديقة",
                       "Electric Meat Grinders": "Kitchen Appliances@أدوات المطبخ",
                       "Mirrors": "Furniture@أثاث المنزل",
                       "Frames": "Furniture@أثاث المنزل",
                       "Wallpaper & Decals": "Furniture@أثاث المنزل",
                       "Dryers": "Home Appliances@الأجهزة المنزلية",
                       "Ovens, Ranges & Stoves": "Kitchen Appliances@أدوات المطبخ",
                       "Washers Dryers 2 in 1": "Kitchen Appliances@أدوات المطبخ",
                       "Range Hoods": "Kitchen Appliances@أدوات المطبخ",
                       "Kitchen & Dining Rooms Furniture Sets": "Furniture@أثاث المنزل",
                       "Beds, Bed Frames & Accessories": "Furniture@أثاث المنزل",
                       "Living Room sets": "Furniture@أثاث المنزل",
                       "Belts": "Apparel & Accessories@ملابس واكسسوارات",
                       "Electrical & Electronic Accessories": "Electronics@إلكترونيات",
                       "Duffle Bags": "Luggage@حقائب السفر",
                       "Contact Lenses": "Apparel & Accessories@ملابس واكسسوارات",
                       "Fragrance Gift Sets": "Beauty@الجمال",
                       "Power Banks": "Electronics@إلكترونيات",
                       "Jumpsuits, Rompers & Overalls": "Apparel & Accessories@ملابس واكسسوارات",
                       "Packing & Bags Accessories": "Luggage@حقائب السفر",
                       "Hats & Caps": "Apparel & Accessories@ملابس واكسسوارات",
                       "Scarves & Wraps": "Apparel & Accessories@ملابس واكسسوارات",
                       "Coffee": "Food & Beverages@المواد الغذائية والمشروبات",
                       "Dairy Products": "Food & Beverages@المواد الغذائية والمشروبات",
                       "Cereals & Grains": "Grocery@البقالة والخضروات و الفواكه",
                       "Seasoning, Spices & Preservatives": "Grocery@البقالة والخضروات و الفواكه",
                       "Guitars": "Media@أفلام و موسيقى",
                       "Beverages": "Food & Beverages@المواد الغذائية والمشروبات",
                       "Treadmills": "Sporting Goods & Fitness@مستلزمات الرياضية واللياقة البدنية",
                       "Balls": "Sporting Goods & Fitness@مستلزمات الرياضية واللياقة البدنية",
                       "Water Coolers & Dispensers": "Kitchen Appliances@أدوات المطبخ",
                       "Eyewear Accessories": "Apparel & Accessories@ملابس واكسسوارات",
                       "Appliances Parts & Accessories": "Kitchen Supplies@لوازم المطبخ",
                       "Plastic & Paper Products": "Grocery@البقالة والخضروات و الفواكه",
                       "Laundry": "Kitchen Supplies@لوازم المطبخ",
                       "Cleaning Products": "Home Supplies@اللوازم المنزلية",
                       "Snacks": "Food & Beverages@المواد الغذائية والمشروبات",
                       "Flowers": "Home & Garden - Outdoor@المنزل والحديقة",
                       "Motorcycle Parts": "Vehicle Parts & Accessories@قطع ولوازم سيارات",
                       "Car Parts": "Vehicle Parts & Accessories@قطع ولوازم سيارات",
                       "Vehicle Fluids": "Vehicle Parts & Accessories@قطع ولوازم سيارات",
                       "Water Heaters": "Home Appliances@الأجهزة المنزلية",
                       "Music Keyboards": "Electronics@إلكترونيات",
                       "Bikes & Bicycles": "Sporting Goods & Fitness@مستلزمات الرياضية واللياقة البدنية",
                       "Tea": "Food & Beverages@المواد الغذائية والمشروبات",
                       "Pasta & Noodles": "Grocery@البقالة والخضروات و الفواكه",
                       "VR Gadgets": "Video Games@العاب الكترونية",
                       "Shampoos & Conditioners": "Health & Personal care@الصحة والعناية الشخصية",
                       "Glasses Frames": "Apparel & Accessories@ملابس واكسسوارات",
                       "Deodorants & Antiperspirants": "Beauty@الجمال",
                       "Hair Dyes": "Personal Care Appliances@أجهزة العناية الشخصية",
                       "Soap & Shower Gel": "Health & Personal care@الصحة والعناية الشخصية",
                       "Candles": "Home Supplies@اللوازم المنزلية",
                       "Air Fresheners": "Home Supplies@اللوازم المنزلية",
                       "Drills": "Hardware & Improvements Tools@قطع الغيار و تحسينات أدوات",
                       "Electric Toothbrushes": "Personal Care Appliances@أجهزة العناية الشخصية",
                       "Fine Jewellery": "Jewelry@المجوهرات",
                       "Rackets": "Sporting Goods & Fitness@مستلزمات الرياضية واللياقة البدنية",
                       "Bakery": "Grocery@البقالة والخضروات و الفواكه",
                       "Confectionery": "Food & Beverages@المواد الغذائية والمشروبات",
                       "Weights & Dumbbells": "Sporting Goods & Fitness@مستلزمات الرياضية واللياقة البدنية",
                       "Sport Gloves": "Sporting Goods & Fitness@مستلزمات الرياضية واللياقة البدنية",
                       "Juices": "Food & Beverages@المواد الغذائية والمشروبات",
                       "Vehicles Lights & Bulbs": "Vehicle Parts & Accessories@قطع ولوازم سيارات",
                       "Fruits & Vegetables": "Grocery@البقالة والخضروات و الفواكه",
                       "Exercise bikes": "Sporting Goods & Fitness@مستلزمات الرياضية واللياقة البدنية",
                       "Cheese": "Dairy Product@منتجات الألبان",
                       "Flashlights": "Electronics@إلكترونيات",
                       "Eggs": "Food & Beverages@المواد الغذائية والمشروبات",
                       "Meats & Chicken": "Food & Beverages@المواد الغذائية والمشروبات",
                       "Sea Food": "Food & Beverages@المواد الغذائية والمشروبات",
                       "Protective Gear": "T-Shirts@مستلزمات الرياضية واللياقة البدنية"}
    return super_care_dict.get(item_type_arg)


# ff = str(super_care_func("Jackets &Coats")).split('@')
# print(ff)
#
# if ''.join(ff) == 'None':
#     print('gg')
