"""
The support page's texts, keyed by the Ukrainian text exactly as it stands in
freshka/support/index.html. Same rules as strings.py; phrases the two pages
share (Фрешка, Підтримка, the footer links) come from strings.py.

The app itself speaks Ukrainian and English only, so the names of its screens
and buttons are given in English in every language.
The app is on the App Store only, so the translations do not mention Google Play.
"""

# uk: (en, de, es, pt, vi, tr)
S = {
    "Підтримка Фрешки: як написати нам, що робити, якщо щось не працює, як видалити акаунт": (
        "Freshka support: how to write to us, what to do if something does not work, how to delete your account",
        "Freshka-Support: wie du uns schreibst, was du tun kannst, wenn etwas nicht funktioniert, und wie du dein Konto löschst",
        "Soporte de Freshka: cómo escribirnos, qué hacer si algo no funciona y cómo eliminar tu cuenta",
        "Suporte do Freshka: como escrever para nós, o que fazer se algo não funcionar e como excluir sua conta",
        "Hỗ trợ Freshka: cách viết cho chúng tôi, làm gì khi có trục trặc, cách xóa tài khoản",
        "Freshka desteği: bize nasıl yazılır, bir şey çalışmazsa ne yapılır, hesap nasıl silinir",
    ),
    "Як написати нам, що робити, якщо щось не працює, як видалити акаунт": (
        "How to write to us, what to do if something does not work, how to delete your account",
        "Wie du uns schreibst, was du tun kannst, wenn etwas nicht funktioniert, und wie du dein Konto löschst",
        "Cómo escribirnos, qué hacer si algo no funciona y cómo eliminar tu cuenta",
        "Como escrever para nós, o que fazer se algo não funcionar e como excluir sua conta",
        "Cách viết cho chúng tôi, làm gì khi có trục trặc, cách xóa tài khoản",
        "Bize nasıl yazılır, bir şey çalışmazsa ne yapılır, hesap nasıl silinir",
    ),
    "Підтримка Фрешки": ("Freshka support", "Freshka-Support", "Soporte de Freshka", "Suporte do Freshka", "Hỗ trợ Freshka", "Freshka desteği"),
    "Про Фрешку": ("About Freshka", "Über Freshka", "Sobre Freshka", "Sobre", "Về Freshka", "Hakkında"),
    "Щось не так? Напиши нам": (
        "Something wrong? Write to us",
        "Etwas stimmt nicht? Schreib uns",
        "¿Algo va mal? Escríbenos",
        "Algo errado? Escreva para nós",
        "Có gì không ổn? Hãy viết cho chúng tôi",
        "Bir sorun mu var? Bize yaz",
    ),
    "Не працює, незрозуміло або хочеться, щоб було інакше. Відповідаємо на пошту, зазвичай протягом двох днів.": (
        "It does not work, it is unclear, or you wish it were different. We reply by email, usually within two days.",
        "Es funktioniert nicht, ist unklar oder du hättest es gern anders. Wir antworten per E-Mail, meist innerhalb von zwei Tagen.",
        "No funciona, no se entiende o te gustaría que fuera distinto. Respondemos por correo, normalmente en dos días.",
        "Não funciona, não ficou claro ou você queria que fosse diferente. Respondemos por e-mail, geralmente em até dois dias.",
        "Không chạy, khó hiểu hoặc bạn muốn nó khác đi. Chúng tôi trả lời qua email, thường trong vòng hai ngày.",
        "Çalışmıyor, anlaşılmıyor ya da başka türlü olsun istiyorsun. E-postayla, genellikle iki gün içinde yanıtlıyoruz.",
    ),
    "Написати на пошту": ("Send an email", "E-Mail schreiben", "Escribir un correo", "Enviar e-mail", "Gửi email", "E-posta gönder"),
    "Як написати нам": ("How to write to us", "So schreibst du uns", "Cómo escribirnos", "Como escrever para nós", "Cách viết cho chúng tôi", "Bize nasıl yazılır"),
    "<b>Налаштування</b>": ("<b>Settings</b>",) * 6,
    "<b>Я</b>": ("<b>Me</b>",) * 6,
    "<b>Написати нам</b>": ("<b>Write to us</b>",) * 6,
    "<b>Повторити</b>": ("<b>Try again</b>",) * 6,
    "<b>Видалити акаунт</b>": ("<b>Delete the account</b>",) * 6,
    "Там можна додати скриншот і, якщо хочеш, дані телефона, вони допомагають знайти причину. Відповідь прийде на пошту акаунта або на ту, яку ти вкажеш.": (
        "There you can add a screenshot and, if you like, your phone details, which help us find the cause. The reply comes to your account email or to the one you give.",
        "Dort kannst du einen Screenshot und, wenn du magst, die Daten deines Handys anhängen, sie helfen bei der Suche nach der Ursache. Die Antwort kommt an die E-Mail-Adresse deines Kontos oder an die, die du angibst.",
        "Ahí puedes añadir una captura y, si quieres, los datos del teléfono, que ayudan a encontrar la causa. La respuesta llega al correo de la cuenta o al que indiques.",
        "Lá você pode anexar uma captura de tela e, se quiser, os dados do celular, que ajudam a encontrar a causa. A resposta chega no e-mail da conta ou no que você informar.",
        "Ở đó bạn có thể đính kèm ảnh chụp màn hình và, nếu muốn, thông tin điện thoại để giúp tìm ra nguyên nhân. Câu trả lời sẽ gửi về email của tài khoản hoặc email bạn ghi.",
        "Orada ekran görüntüsü ve istersen telefon bilgilerini ekleyebilirsin, nedeni bulmamıza yardım eder. Yanıt, hesabının e-postasına ya da belirttiğin adrese gelir.",
    ),
    "Або просто листом на hello@gluponya.tv. Напиши, що саме сталося і на якому телефоні. Скриншот дуже допомагає.": (
        "Or simply email hello@gluponya.tv. Tell us what exactly happened and on which phone. A screenshot helps a lot.",
        "Oder einfach per E-Mail an hello@gluponya.tv. Schreib, was genau passiert ist und auf welchem Handy. Ein Screenshot hilft sehr.",
        "O simplemente por correo a hello@gluponya.tv. Cuenta qué pasó exactamente y en qué teléfono. Una captura ayuda mucho.",
        "Ou simplesmente por e-mail para hello@gluponya.tv. Conte o que aconteceu e em qual celular. Uma captura de tela ajuda muito.",
        "Hoặc đơn giản là gửi email tới hello@gluponya.tv. Hãy kể chính xác chuyện gì xảy ra và trên điện thoại nào. Ảnh chụp màn hình giúp rất nhiều.",
        "Ya da doğrudan hello@gluponya.tv adresine yaz. Tam olarak ne olduğunu ve hangi telefonda olduğunu anlat. Ekran görüntüsü çok yardımcı olur.",
    ),
    "Якщо щось не синхронізується": (
        "If something does not sync",
        "Wenn etwas nicht synchronisiert",
        "Si algo no se sincroniza",
        "Se algo não sincronizar",
        "Nếu có gì đó không đồng bộ",
        "Bir şey eşitlenmiyorsa",
    ),
    "Фрешка працює без інтернету, а зміни надсилає, коли звʼязок повертається. Якщо на аватарці зʼявився знак, що частина змін не надіслана:": (
        "Freshka works without the internet and sends changes when the connection is back. If your avatar shows a mark that some changes were not sent:",
        "Freshka funktioniert ohne Internet und sendet Änderungen, sobald die Verbindung zurück ist. Wenn an deinem Avatar ein Zeichen erscheint, dass ein Teil der Änderungen nicht gesendet wurde:",
        "Freshka funciona sin internet y envía los cambios cuando vuelve la conexión. Si en tu avatar aparece una señal de que parte de los cambios no se envió:",
        "O Freshka funciona sem internet e envia as mudanças quando a conexão volta. Se no seu avatar aparecer um sinal de que parte das mudanças não foi enviada:",
        "Freshka chạy được khi không có mạng và gửi các thay đổi khi có kết nối trở lại. Nếu trên ảnh đại diện hiện dấu báo một số thay đổi chưa được gửi:",
        "Freshka internetsiz çalışır ve bağlantı geri gelince değişiklikleri gönderir. Avatarında bazı değişikliklerin gönderilmediğini gösteren bir işaret çıktıysa:",
    ),
    "Якщо не допомогло, напиши нам.": (
        "If that did not help, write to us.",
        "Wenn das nicht hilft, schreib uns.",
        "Si no sirve, escríbenos.",
        "Se não resolver, escreva para nós.",
        "Nếu vẫn không được, hãy viết cho chúng tôi.",
        "İşe yaramadıysa bize yaz.",
    ),
    "<h2>Підписка</h2>": (
        "<h2>Subscription</h2>", "<h2>Abo</h2>", "<h2>Suscripción</h2>", "<h2>Assinatura</h2>", "<h2>Gói đăng ký</h2>", "<h2>Abonelik</h2>",
    ),
    "Підписку продає магазин додатків, тож скасовується вона там же: у налаштуваннях Apple ID або Google Play, розділ «Підписки». У Фрешці це рядок «Підписка» у вкладці «Я», він веде на ту саму сторінку магазину.": (
        "The App Store sells the subscription, so it is cancelled there too: in your Apple ID settings, under Subscriptions. In Freshka it is the “Subscription” row in the “Me” tab, which leads to the same store page.",
        "Das Abo verkauft der App Store, also wird es auch dort gekündigt: in den Einstellungen deiner Apple-ID unter „Abonnements“. In Freshka ist es die Zeile “Subscription” im Tab “Me”, sie führt auf dieselbe Seite im Store.",
        "La suscripción la vende el App Store, así que se cancela ahí mismo: en los ajustes de tu Apple ID, en «Suscripciones». En Freshka es la fila “Subscription” de la pestaña “Me”, que lleva a esa misma página de la tienda.",
        "A assinatura é vendida pela App Store, então é lá que se cancela: nos ajustes do seu Apple ID, em “Assinaturas”. No Freshka é a linha “Subscription” na aba “Me”, que leva à mesma página da loja.",
        "Gói đăng ký do App Store bán nên cũng hủy ở đó: trong phần cài đặt Apple ID, mục “Đăng ký”. Trong Freshka, đó là dòng “Subscription” ở thẻ “Me”, dẫn tới chính trang đó của cửa hàng.",
        "Aboneliği App Store satar, bu yüzden iptali de oradan yapılır: Apple Kimliği ayarlarında, “Abonelikler” bölümünde. Freshka’da bu, “Me” sekmesindeki “Subscription” satırıdır ve mağazadaki aynı sayfaya götürür.",
    ),
    "Куплене привʼязане до акаунта Фрешки і переходить на новий телефон разом з ним.": (
        "What you bought is tied to your Freshka account and moves to a new phone along with it.",
        "Was du gekauft hast, hängt an deinem Freshka-Konto und zieht mit ihm auf ein neues Handy um.",
        "Lo que compras queda ligado a tu cuenta de Freshka y pasa con ella a un teléfono nuevo.",
        "O que você comprou fica ligado à sua conta do Freshka e vai junto com ela para um celular novo.",
        "Những gì đã mua gắn với tài khoản Freshka và chuyển sang điện thoại mới cùng tài khoản.",
        "Satın aldıkların Freshka hesabına bağlıdır ve hesapla birlikte yeni telefona geçer.",
    ),
    "Як видалити акаунт": (
        "How to delete your account", "So löschst du dein Konto", "Cómo eliminar la cuenta", "Como excluir a conta", "Cách xóa tài khoản", "Hesap nasıl silinir",
    ),
    "Разом з акаунтом видаляються твої листи до нас, скриншоти й те, що лежало лише на сервері. Холодильник на телефоні теж очищається, і Фрешка починає з чистого аркуша.": (
        "Along with the account we delete your messages to us, the screenshots and whatever was kept only on the server. The fridge on your phone is cleared too, and Freshka starts from a clean sheet.",
        "Mit dem Konto werden auch deine Nachrichten an uns, die Screenshots und alles gelöscht, was nur auf dem Server lag. Der Kühlschrank auf dem Handy wird ebenfalls geleert, und Freshka beginnt von vorn.",
        "Junto con la cuenta se eliminan tus mensajes para nosotros, las capturas y lo que solo estaba en el servidor. La nevera del teléfono también se vacía y Freshka empieza de cero.",
        "Junto com a conta são excluídas suas mensagens para nós, as capturas de tela e o que ficava só no servidor. A geladeira no celular também é esvaziada, e o Freshka começa do zero.",
        "Cùng với tài khoản, thư bạn gửi cho chúng tôi, ảnh chụp màn hình và những gì chỉ lưu trên máy chủ cũng bị xóa. Tủ lạnh trên điện thoại cũng được dọn sạch, và Freshka bắt đầu lại từ đầu.",
        "Hesapla birlikte bize yazdıkların, ekran görüntüleri ve yalnızca sunucuda duranlar da silinir. Telefondaki buzdolabı da temizlenir ve Freshka sıfırdan başlar.",
    ),
    "Якщо не виходить зайти в додаток, напиши на пошту з адреси акаунта, і ми видалимо його вручну.": (
        "If you cannot get into the app, email us from the account address and we will delete it by hand.",
        "Wenn du nicht in die App kommst, schreib uns von der E-Mail-Adresse des Kontos, und wir löschen es von Hand.",
        "Si no puedes entrar en la app, escríbenos desde el correo de la cuenta y la eliminaremos a mano.",
        "Se não conseguir entrar no app, escreva do e-mail da conta e nós a excluímos manualmente.",
        "Nếu không vào được ứng dụng, hãy gửi email từ địa chỉ của tài khoản, chúng tôi sẽ xóa thủ công.",
        "Uygulamaya giremiyorsan hesabın e-posta adresinden yaz, hesabı elle sileriz.",
    ),
}
