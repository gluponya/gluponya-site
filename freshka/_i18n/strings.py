"""
The landing's texts in every language, keyed by the Ukrainian text exactly as
it stands in freshka/index.html (markup included where the phrase has it).

build.py replaces the keys, longest first, and stops if a key is missing from
the page or if any Cyrillic is left in a translated page, so a new or changed
Ukrainian phrase on the landing cannot slip through untranslated.

Rules for a translation: no ASCII quotes or apostrophes (the phrases also sit
inside HTML attributes and JS strings), so write ’ and “ ”.
"""

LANGS = ("en", "de", "es", "pt", "vi", "tr")

# name in its own language, og:locale, Trustpilot locale
META = {
    "uk": ("Українська", "uk_UA", "uk-UA"),
    "en": ("English", "en_US", "en-US"),
    "de": ("Deutsch", "de_DE", "de-DE"),
    "es": ("Español", "es_ES", "es-ES"),
    "pt": ("Português", "pt_BR", "pt-BR"),
    "vi": ("Tiếng Việt", "vi_VN", "vi-VN"),
    "tr": ("Türkçe", "tr_TR", "tr-TR"),
}

# The link-preview picture's headline, two lines, the accent between asterisks.
OG_HEADLINE = {
    "uk": ["Холодильник,", "*який видно*"],
    "en": ["A fridge", "*you can see*"],
    "de": ["Ein Kühlschrank,", "*den man sieht*"],
    "es": ["Tu nevera,", "*a la vista*"],
    "pt": ["Uma geladeira", "*que dá pra ver*"],
    "vi": ["Tủ lạnh", "*nhìn là thấy*"],
    "tr": ["Göz önünde", "*bir buzdolabı*"],
}

# uk: (en, de, es, pt, vi, tr)
T = {
    # head
    "Фрешка показує холодильник як картинку: полиці, продукти на них і те, що скоро зіпсується": (
        "Freshka shows your fridge as a picture: the shelves, the food on them and what is about to go off",
        "Freshka zeigt deinen Kühlschrank als Bild: die Fächer, die Lebensmittel darin und was bald verdirbt",
        "Freshka muestra tu nevera como un dibujo: los estantes, la comida que hay en ellos y lo que está a punto de estropearse",
        "O Freshka mostra sua geladeira como um desenho: as prateleiras, a comida nelas e o que está prestes a estragar",
        "Freshka vẽ tủ lạnh của bạn thành một bức tranh: các ngăn, đồ ăn trên đó và món nào sắp hỏng",
        "Freshka buzdolabını bir resim olarak gösterir: raflar, üstündeki yiyecekler ve yakında bozulacak olanlar",
    ),
    "Холодильник, який видно. Полиці й продукти намальовані, що ось-ось зіпсується, видно одразу": (
        "A fridge you can see. The shelves and the food are drawn, so what is about to go off shows at a glance",
        "Ein Kühlschrank, den man sieht. Fächer und Lebensmittel sind gezeichnet, und was bald verdirbt, siehst du sofort",
        "Tu nevera, a la vista. Los estantes y la comida están dibujados, y lo que está a punto de estropearse se ve al instante",
        "Uma geladeira que dá pra ver. As prateleiras e a comida são desenhadas, e o que está prestes a estragar aparece na hora",
        "Tủ lạnh nhìn là thấy. Các ngăn và đồ ăn đều được vẽ ra, món nào sắp hỏng là thấy ngay",
        "Göz önünde bir buzdolabı. Raflar ve yiyecekler çizilmiş, yakında bozulacak olan hemen görünür",
    ),
    "Фрешка. Холодильник, який видно: екран застосунку з намальованим холодильником і продуктами на полицях": (
        "Freshka. A fridge you can see: the app screen with a drawn fridge and food on its shelves",
        "Freshka. Ein Kühlschrank, den man sieht: der Bildschirm der App mit einem gezeichneten Kühlschrank und Lebensmitteln in den Fächern",
        "Freshka. Tu nevera, a la vista: la pantalla de la app con una nevera dibujada y comida en los estantes",
        "Freshka. Uma geladeira que dá pra ver: a tela do app com uma geladeira desenhada e comida nas prateleiras",
        "Freshka. Tủ lạnh nhìn là thấy: màn hình ứng dụng với chiếc tủ lạnh được vẽ và đồ ăn trên các ngăn",
        "Freshka. Göz önünde bir buzdolabı: çizilmiş bir buzdolabı ve raflarındaki yiyeceklerle uygulama ekranı",
    ),
    "Холодильник як картинка: сфотографуй чек, і покупки зʼявляться на полицях. Видно, що є вдома і що скоро зіпсується, а спільний холодильник бачить уся сімʼя": (
        "Your fridge as a picture: snap the receipt and the groceries appear on the shelves. See what you have at home and what is about to go off, and share one fridge with the whole family",
        "Dein Kühlschrank als Bild: Fotografiere den Kassenbon, und der Einkauf erscheint in den Fächern. Du siehst, was zu Hause ist und was bald verdirbt, und die ganze Familie teilt sich einen Kühlschrank",
        "Tu nevera como un dibujo: haz una foto al tique y la compra aparece en los estantes. Se ve qué hay en casa y qué está a punto de estropearse, y toda la familia comparte la misma nevera",
        "Sua geladeira como um desenho: fotografe o cupom e as compras aparecem nas prateleiras. Dá pra ver o que tem em casa e o que está prestes a estragar, e a família toda divide a mesma geladeira",
        "Tủ lạnh của bạn thành một bức tranh: chụp hóa đơn là đồ vừa mua hiện lên các ngăn. Thấy ngay trong nhà còn gì, món nào sắp hỏng, và cả nhà dùng chung một tủ lạnh",
        "Buzdolabın bir resim olarak: fişin fotoğrafını çek, aldıkların raflarda belirsin. Evde ne var, ne yakında bozulacak görünür ve bütün aile aynı buzdolabını paylaşır",
    ),
    "Фрешка": ("Freshka",) * 6,
    "Глупоня": ("Gluponya",) * 6,

    # header
    "Як це працює": ("How it works", "So funktioniert’s", "Cómo funciona", "Como funciona", "Cách hoạt động", "Nasıl çalışır"),
    "Спробувати": ("Try it", "Ausprobieren", "Pruébalo", "Experimente", "Dùng thử", "Dene"),
    "Підтримка": ("Support", "Support", "Soporte", "Suporte", "Hỗ trợ", "Destek"),
    "Завантажити": ("Download", "Laden", "Descargar", "Baixar", "Tải về", "İndir"),

    # hero
    "Холодильник, <em>який видно</em>": (
        "A fridge <em>you can see</em>",
        "Ein Kühlschrank, <em>den man sieht</em>",
        "Tu nevera, <em>a la vista</em>",
        "Uma geladeira <em>que dá pra ver</em>",
        "Tủ lạnh <em>nhìn là thấy</em>",
        "Göz önünde <em>bir buzdolabı</em>",
    ),
    "Намалюй свій холодильник у телефоні. Що скоро зіпсується, видно одразу.": (
        "Draw your own fridge on your phone. What is about to go off shows at a glance.",
        "Zeichne deinen Kühlschrank im Handy nach. Was bald verdirbt, siehst du sofort.",
        "Dibuja tu nevera en el móvil. Lo que está a punto de estropearse se ve al instante.",
        "Desenhe sua geladeira no celular. O que está prestes a estragar aparece na hora.",
        "Vẽ chiếc tủ lạnh của bạn ngay trên điện thoại. Món nào sắp hỏng là thấy ngay.",
        "Buzdolabını telefonunda çiz. Yakında bozulacak olan hemen görünür.",
    ),
    "Завантажити в": ("Download on the", "Laden im", "Consíguelo en el", "Baixar na", "Tải về trên", "Hemen indir"),
    "Спробувати в Telegram": ("Try in Telegram", "In Telegram testen", "Probar en Telegram", "Testar no Telegram", "Thử trên Telegram", "Telegram’da dene"),
    "Екран Фрешки з намальованим холодильником": (
        "Freshka screen with a drawn fridge",
        "Freshka-Bildschirm mit einem gezeichneten Kühlschrank",
        "Pantalla de Freshka con una nevera dibujada",
        "Tela do Freshka com uma geladeira desenhada",
        "Màn hình Freshka với chiếc tủ lạnh được vẽ",
        "Çizilmiş buzdolabıyla Freshka ekranı",
    ),

    # not a list
    "Не список, <em>а картинка</em>": (
        "Not a list, <em>a picture</em>",
        "Keine Liste, <em>ein Bild</em>",
        "No una lista, <em>un dibujo</em>",
        "Não é lista, <em>é desenho</em>",
        "Không phải danh sách, <em>mà là bức tranh</em>",
        "Liste değil, <em>resim</em>",
    ),
    "Їжу ми пам'ятаємо очима. Тому у Фрешці полиці, а не рядки.": (
        "We remember food with our eyes. So Freshka has shelves, not rows.",
        "Essen merken wir uns mit den Augen. Darum hat Freshka Fächer statt Zeilen.",
        "La comida la recordamos con los ojos. Por eso en Freshka hay estantes, no filas.",
        "A gente lembra da comida com os olhos. Por isso o Freshka tem prateleiras, não linhas.",
        "Ta nhớ đồ ăn bằng mắt. Vì thế Freshka có các ngăn tủ, chứ không phải những dòng chữ.",
        "Yiyecekleri gözümüzle hatırlarız. Bu yüzden Freshka’da satırlar değil, raflar var.",
    ),
    "Звичайний застосунок": ("A regular app", "Eine normale App", "Una app cualquiera", "Um app comum", "Ứng dụng thông thường", "Sıradan bir uygulama"),
    "Молоко 1 л, до 12.11": ("Milk 1 L, use by Nov 12", "Milch 1 l, bis 12.11.", "Leche 1 L, hasta el 12/11", "Leite 1 L, até 12/11", "Sữa 1 lít, hạn 12/11", "Süt 1 L, son 12.11"),
    "Помідори 500 г": ("Tomatoes 500 g", "Tomaten 500 g", "Tomates 500 g", "Tomates 500 g", "Cà chua 500 g", "Domates 500 g"),
    "Сир чеддер, до 20.11": ("Cheddar, use by Nov 20", "Cheddar, bis 20.11.", "Queso cheddar, hasta el 20/11", "Queijo cheddar, até 20/11", "Phô mai cheddar, hạn 20/11", "Çedar peyniri, son 20.11"),
    "Яйця 10 шт": ("Eggs, 10", "Eier, 10 Stück", "Huevos, 10 uds.", "Ovos, 10 un.", "Trứng 10 quả", "Yumurta 10 adet"),
    "Кефір, до 14.11": ("Kefir, use by Nov 14", "Kefir, bis 14.11.", "Kéfir, hasta el 14/11", "Kefir, até 14/11", "Kefir, hạn 14/11", "Kefir, son 14.11"),
    "Намальований холодильник з продуктами на полицях": (
        "A drawn fridge with food on its shelves",
        "Ein gezeichneter Kühlschrank mit Lebensmitteln in den Fächern",
        "Una nevera dibujada con comida en los estantes",
        "Uma geladeira desenhada com comida nas prateleiras",
        "Chiếc tủ lạnh được vẽ với đồ ăn trên các ngăn",
        "Raflarında yiyecekler olan çizilmiş bir buzdolabı",
    ),

    # ways to add
    "Додати <em>за секунду</em>": (
        "Add it <em>in a second</em>",
        "In einer Sekunde <em>hinzugefügt</em>",
        "Añádelo <em>en un segundo</em>",
        "Adicione <em>em um segundo</em>",
        "Thêm món <em>trong một giây</em>",
        "Bir saniyede <em>ekle</em>",
    ),
    "Сфотографуй покупки": ("Snap your groceries", "Fotografiere deinen Einkauf", "Haz una foto a la compra", "Fotografe as compras", "Chụp ảnh đồ vừa mua", "Aldıklarının fotoğrafını çek"),
    "ШІ знайде на фото всі продукти й розкладе по полицях.": (
        "AI finds every item in the photo and puts it on the shelves.",
        "Die KI findet alle Lebensmittel auf dem Foto und räumt sie in die Fächer.",
        "La IA encuentra todos los productos de la foto y los coloca en los estantes.",
        "A IA encontra todos os itens da foto e coloca nas prateleiras.",
        "AI tìm mọi món trong ảnh và xếp lên các ngăn.",
        "Yapay zekâ fotoğraftaki tüm ürünleri bulur ve raflara yerleştirir.",
    ),
    "Екран додавання з фото": ("Adding food from a photo", "Hinzufügen per Foto", "Añadir productos desde una foto", "Adicionar itens por foto", "Thêm món từ ảnh chụp", "Fotoğraftan ürün ekleme"),
    "Вибери з каталогу": ("Pick from the catalogue", "Aus dem Katalog wählen", "Elige del catálogo", "Escolha no catálogo", "Chọn từ danh mục", "Katalogdan seç"),
    "Торкнись малюнка, і продукт уже на полиці.": (
        "Tap a picture and the item is on the shelf.",
        "Tippe auf ein Bild, und schon liegt es im Fach.",
        "Toca un dibujo y el producto ya está en el estante.",
        "Toque num desenho e o item já está na prateleira.",
        "Chạm vào hình vẽ là món đã nằm trên ngăn.",
        "Resme dokun, ürün rafta.",
    ),
    "Каталог продуктів": ("Food catalogue", "Lebensmittelkatalog", "Catálogo de productos", "Catálogo de alimentos", "Danh mục thực phẩm", "Ürün kataloğu"),
    "Штрихкод": ("Barcode", "Barcode", "Código de barras", "Código de barras", "Mã vạch", "Barkod"),
    "Разом з родиною": ("Together with family", "Mit der ganzen Familie", "Con toda la familia", "Com a família toda", "Cùng cả nhà", "Ailece"),

    # try it
    "Розклади <em>покупки</em>": (
        "Put away <em>the groceries</em>",
        "Räum den <em>Einkauf ein</em>",
        "Guarda <em>la compra</em>",
        "Guarde <em>as compras</em>",
        "Xếp <em>đồ vừa mua</em>",
        "Aldıklarını <em>yerleştir</em>",
    ),
    "Перетягни зі столу в холодильник. Куди поклала, там і побачиш.": (
        "Drag things from the table into the fridge. Where you put them is where you will see them.",
        "Zieh die Sachen vom Tisch in den Kühlschrank. Wo du sie hinlegst, siehst du sie auch.",
        "Arrastra de la mesa a la nevera. Donde lo dejes, ahí lo verás.",
        "Arraste da mesa para a geladeira. Onde você colocar, é lá que vai ver.",
        "Kéo đồ từ bàn vào tủ lạnh. Đặt ở đâu thì thấy ở đó.",
        "Masadan buzdolabına sürükle. Nereye koyduysan orada görürsün.",
    ),
    "Відкритий холодильник": ("Open fridge", "Offener Kühlschrank", "Nevera abierta", "Geladeira aberta", "Tủ lạnh đang mở", "Açık buzdolabı"),
    "Молоко": ("Milk", "Milch", "Leche", "Leite", "Sữa", "Süt"),
    "Кефір": ("Kefir", "Kefir", "Kéfir", "Kefir", "Kefir", "Kefir"),
    "Кетчуп": ("Ketchup", "Ketchup", "Kétchup", "Ketchup", "Tương cà", "Ketçap"),
    "Вода": ("Water", "Wasser", "Agua", "Água", "Nước", "Su"),
    "Чеддер": ("Cheddar", "Cheddar", "Cheddar", "Cheddar", "Phô mai cheddar", "Çedar"),
    "Яйця": ("Eggs", "Eier", "Huevos", "Ovos", "Trứng", "Yumurta"),
    "Йогурт": ("Yoghurt", "Joghurt", "Yogur", "Iogurte", "Sữa chua", "Yoğurt"),
    "Ковбаса": ("Sausage", "Wurst", "Salchichón", "Salame", "Xúc xích", "Salam"),
    "Борщ": ("Borscht", "Borschtsch", "Borsch", "Borscht", "Súp borscht", "Borş"),
    "Помідори": ("Tomatoes", "Tomaten", "Tomates", "Tomates", "Cà chua", "Domates"),
    "Огірки": ("Cucumbers", "Gurken", "Pepinos", "Pepinos", "Dưa chuột", "Salatalık"),
    "Морква": ("Carrots", "Möhren", "Zanahorias", "Cenouras", "Cà rốt", "Havuç"),
    "Яблука": ("Apples", "Äpfel", "Manzanas", "Maçãs", "Táo", "Elma"),
    "Полуниця": ("Strawberries", "Erdbeeren", "Fresas", "Morangos", "Dâu tây", "Çilek"),
    "Камамбер": ("Camembert", "Camembert", "Camembert", "Camembert", "Phô mai camembert", "Kamamber"),
    "Масло": ("Butter", "Butter", "Mantequilla", "Manteiga", "Bơ", "Tereyağı"),
    "М'ятний": ("Mint", "Mint", "Menta", "Menta", "Xanh bạc hà", "Nane yeşili"),
    "Червоний": ("Red", "Rot", "Rojo", "Vermelho", "Đỏ", "Kırmızı"),
    "Рожевий": ("Pink", "Rosa", "Rosa", "Rosa", "Hồng", "Pembe"),
    "Жовтий": ("Yellow", "Gelb", "Amarillo", "Amarelo", "Vàng", "Sarı"),
    "Блакитний": ("Light blue", "Hellblau", "Azul claro", "Azul-claro", "Xanh da trời", "Açık mavi"),
    "Лавандовий": ("Lavender", "Lavendel", "Lavanda", "Lavanda", "Tím oải hương", "Lavanta"),
    "Білий": ("White", "Weiß", "Blanco", "Branco", "Trắng", "Beyaz"),

    # spoiling
    "Псується <em>на очах</em>": (
        "Going off <em>before your eyes</em>",
        "Verdirbt <em>vor deinen Augen</em>",
        "Se estropea <em>ante tus ojos</em>",
        "Estraga <em>diante dos olhos</em>",
        "Hỏng dần <em>ngay trước mắt</em>",
        "Gözünün önünde <em>bozuluyor</em>",
    ),
    "Продукт в'яне й темніє разом зі справжнім. Не треба читати дати.": (
        "The picture wilts and darkens along with the real thing. No dates to read.",
        "Das Bild welkt und dunkelt zusammen mit dem echten Lebensmittel. Kein Datum zu lesen.",
        "El dibujo se marchita y oscurece a la vez que el producto real. Sin leer fechas.",
        "O desenho murcha e escurece junto com o alimento de verdade. Sem precisar ler datas.",
        "Hình vẽ héo và sẫm lại cùng lúc với món thật. Không cần đọc hạn sử dụng.",
        "Resim, gerçeğiyle birlikte solar ve kararır. Tarih okumana gerek yok.",
    ),
    "Свіжа полуниця": ("Fresh strawberry", "Frische Erdbeere", "Fresa fresca", "Morango fresco", "Dâu tây tươi", "Taze çilek"),
    "Полуниця в'яне": ("Wilting strawberry", "Welkende Erdbeere", "Fresa marchitándose", "Morango murchando", "Dâu tây đang héo", "Solan çilek"),
    "Зіпсована полуниця": ("Spoiled strawberry", "Verdorbene Erdbeere", "Fresa estropeada", "Morango estragado", "Dâu tây đã hỏng", "Bozulmuş çilek"),
    "Свіже": ("Fresh", "Frisch", "Fresco", "Fresco", "Tươi", "Taze"),
    "Скоро": ("Soon", "Bald", "Pronto", "Em breve", "Sắp hỏng", "Yakında"),
    "Зіпсоване": ("Gone off", "Verdorben", "Estropeado", "Estragado", "Đã hỏng", "Bozulmuş"),
    "Сьогодні": ("Today", "Heute", "Hoy", "Hoje", "Hôm nay", "Bugün"),
    "3 дні": ("3 days", "3 Tage", "3 días", "3 dias", "3 ngày", "3 gün"),
    "5 днів": ("5 days", "5 Tage", "5 días", "5 dias", "5 ngày", "5 gün"),
    "Тиждень": ("A week", "Eine Woche", "Una semana", "Uma semana", "Một tuần", "Bir hafta"),

    # catalogue
    "малюнків для продуктів, <em>банок і каструль</em>": (
        "pictures of food, <em>jars and pots</em>",
        "Bilder für Lebensmittel, <em>Gläser und Töpfe</em>",
        "dibujos de alimentos, <em>tarros y ollas</em>",
        "desenhos de alimentos, <em>potes e panelas</em>",
        "hình vẽ thực phẩm, <em>hũ lọ và nồi</em>",
        "yiyecek, <em>kavanoz ve tencere çizimi</em>",
    ),
    "Овочі й фрукти": ("Fruit and veg", "Obst und Gemüse", "Frutas y verduras", "Frutas e legumes", "Rau củ và trái cây", "Sebze ve meyve"),
    "Молочне й м'ясо": ("Dairy and meat", "Milch und Fleisch", "Lácteos y carne", "Laticínios e carne", "Sữa và thịt", "Süt ürünleri ve et"),
    "Готова їжа": ("Ready meals", "Fertige Gerichte", "Platos preparados", "Comida pronta", "Món nấu sẵn", "Hazır yemek"),
    "Тара": ("Containers", "Behälter", "Envases", "Recipientes", "Hộp đựng", "Kaplar"),

    # reviews
    "Що кажуть <em>про Фрешку</em>": (
        "What people say <em>about Freshka</em>",
        "Was man <em>über Freshka sagt</em>",
        "Qué dicen <em>de Freshka</em>",
        "O que dizem <em>do Freshka</em>",
        "Mọi người nói gì <em>về Freshka</em>",
        "Freshka hakkında <em>ne diyorlar</em>",
    ),
    "Відгуки живуть на Trustpilot, ми їх не редагуємо і не відбираємо.": (
        "Reviews live on Trustpilot. We do not edit or pick them.",
        "Die Bewertungen stehen auf Trustpilot. Wir bearbeiten sie nicht und wählen sie nicht aus.",
        "Las reseñas están en Trustpilot. No las editamos ni las seleccionamos.",
        "As avaliações ficam no Trustpilot. Não editamos nem selecionamos.",
        "Đánh giá nằm trên Trustpilot. Chúng tôi không chỉnh sửa hay chọn lọc.",
        "Yorumlar Trustpilot’ta durur. Onları düzenlemiyor, seçmiyoruz.",
    ),
    "Відгуків ще немає. <em>Напиши перший</em>": (
        "No reviews yet. <em>Write the first one</em>",
        "Noch keine Bewertungen. <em>Schreib die erste</em>",
        "Aún no hay reseñas. <em>Escribe la primera</em>",
        "Ainda não há avaliações. <em>Escreva a primeira</em>",
        "Chưa có đánh giá nào. <em>Hãy viết đánh giá đầu tiên</em>",
        "Henüz yorum yok. <em>İlkini sen yaz</em>",
    ),
    "Залишити відгук на Trustpilot": (
        "Leave a review on Trustpilot", "Auf Trustpilot bewerten", "Dejar una reseña en Trustpilot",
        "Avaliar no Trustpilot", "Viết đánh giá trên Trustpilot", "Trustpilot’ta yorum yaz",
    ),

    # final and footer
    "Почни з <em>одного продукту</em>": (
        "Start with <em>one item</em>",
        "Fang mit <em>einem Lebensmittel an</em>",
        "Empieza con <em>un solo producto</em>",
        "Comece com <em>um item só</em>",
        "Bắt đầu từ <em>một món</em>",
        "Tek bir <em>ürünle başla</em>",
    ),
    "Холодильник у телефоні, намальований від руки.": (
        "A fridge on your phone, drawn by hand.",
        "Ein Kühlschrank im Handy, von Hand gezeichnet.",
        "Una nevera en tu móvil, dibujada a mano.",
        "Uma geladeira no celular, desenhada à mão.",
        "Tủ lạnh trong điện thoại, được vẽ tay.",
        "Telefonunda, elle çizilmiş bir buzdolabı.",
    ),
    "Застосунок": ("App", "App", "App", "App", "Ứng dụng", "Uygulama"),
    "Допомога": ("Help", "Hilfe", "Ayuda", "Ajuda", "Trợ giúp", "Yardım"),
    "Документи": ("Legal", "Rechtliches", "Legal", "Documentos", "Pháp lý", "Yasal"),
    "Конфіденційність": ("Privacy", "Datenschutz", "Privacidad", "Privacidade", "Quyền riêng tư", "Gizlilik"),
    "Умови": ("Terms", "Bedingungen", "Términos", "Termos", "Điều khoản", "Koşullar"),
    "Зроблено в Глупоні": ("Made by Gluponya", "Gemacht von Gluponya", "Hecho por Gluponya", "Feito pela Gluponya", "Do Gluponya thực hiện", "Gluponya yapımı"),
}
