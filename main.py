import telebot
import time

TOKEN = "5233008083:AAEydL8Cfw8WTY_Fsdgb5EqnJ6Dwmvq2b3w"


bot = telebot.TeleBot(TOKEN)



first_post_text = """
Магазин расходников: @ToxicKingsShop_bot
Всем оптовикам при закупке от 100шт. скидка оговаривается. Пишите - @ToxicKings_Support

🔥Магазин качественных расходников Toxic Kings Shop !🔥

🔥Мы команда специалистов своего дела, которая выполняет свою работу качественно, что подтверждено отзывами.🔥
✅Наш магазин предоставляет качественные расходники для Facebook | Google, которые служат долго и надежно.
Если у вас есть необходимость в аккаунтах, картах и других расходников для FB | Google хорошего качества — вы оказались в нужное время — в нужном месте.
✅Мы всегда готовы к сотрудничеству на постоянной основе в качестве поставщика оптом для арбитражных команд и не только…😈

Менеджер магазина - @ToxicKings_Support
"""


second_post_text = """
Рекомендуем проводить все сделки через гаранта чата.
Гарант: @Victor_ZzzakaZzzak
Гарант: @cpamix
10% за сделку

МАГАЗИН РАСХОДНИКОВ: @ToxicKingsShop_bot
Всем оптовикам при закупке от 100шт. скидка оговаривается. Пишите - @ToxicKings_Support

ДОСТУП В ПРИВАТ: Временно закрыт.
Приватный магазин: Временно закрыт.
Только тут приватные возможности для аудитории нашего чата!

❗️ПРАВИЛА ЧАТА: https://t.me/c/1253104153/1643

Чат, где только ваши пост-объявления👇
⚠️ Чат специально создан при поддержке чата «#ПЕРВОБИЛЬЩИКИ ЧАТ | TOXIC KINGS» для Ваших объявлений и предложений! 

🔥 @TXBOARD — куплю
🔥 @TXBOARD — продам
🔥 @TXBOARD — отолью
🔥 @TXBOARD — ищу
🔥 @TXBOARD — найду

Проверенные продавцы | селлеры: @sellerverif

SKAM, Кидалы, Скамеры, Арбитраж police | Black list: @SkamTraffic

Все сделки среди участников чата проводятся исключительно с гарантом!

❌Любая реклама без предварительного согласования: каналов, чатов, ботов даже без размещения ссылки карается баном‼️

"""

@bot.message_handler(commands=['start'])
def start(message):
    while True:
        first_post_gif = open('gif.gif', 'rb')
        bot.send_animation("@ToxicKings_chat", first_post_gif, None, caption=first_post_text)
        first_post_gif.close()
        time.sleep(15)
        second_post_image = open('image.jpg', 'rb')
        bot.send_photo("@ToxicKings_chat", second_post_image, caption=second_post_text)
        second_post_image.close()
        time.sleep(10800)

            
        
    
bot.polling(none_stop=True, interval=0)

    
