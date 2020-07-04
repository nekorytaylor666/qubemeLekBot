import telebot
from telebot import types

bot = telebot.TeleBot('1004473184:AAHHSsdSijgcrIiBJ83d4PmXWLu9NpNVNpo')


@bot.message_handler(commands=['start'])
def start(message):
    msg = 'Добрый день! Это бот-помощник для тех, кто болеет Covid-19.\nЗдесь вы можете узнать различную информацию о чатах помощи и каналах для поиска\nЗдесь вы можете узнать различную информацию о чатах помощи и каналах для поиска лекарств. \nСписок команд:\n/indrug - группы в WhatsApp для поиска лекарств по городам.\n/iteka - бот в WhatsApp поможет найти вам необходимые лекарства в аптеках.\n/indrugapp - приложение для поиска лекарств.\n/coviddoc - чат с докторами.'

    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands=['indrug'])
def indrug(message):
    msg = 'inDrug группы в WhatsApp для  поиска лекарств. 💊\nВыбери свой город и общайся с коллегами. 🤝\n1. Нур-Султан, общая группа:\nhttps://chat.whatsapp.com/BQkYuXgyRX6GfGot8NSKla\n2. Нур-Султан, левый берег:\nhttps://chat.whatsapp.com/CxzX1FjRpVR3U4ncDHNoOy\n3. Нур-Султан, правый берег:\nhttps://chat.whatsapp.com/F62jeajGlcCBPbErTd7okL\n4. Алматы, общая группа:\nhttps://chat.whatsapp.com/Hg0UWqjtgjX1vx4HrBFwdF\n5. Алматы 2:\nhttps://chat.whatsapp.com/Be16j5VQr3XB7RwrjRfgtm\n6. Алматы 1:\nhttps://chat.whatsapp.com/LEVWEe1m2KJ1RAgLyfuCZm\n7. Атырау:\nhttps://chat.whatsapp.com/DHERSa10ywF5P3j6PlUDLb\n8. Шымкент:\nhttps://chat.whatsapp.com/JBfVrX7SufkF1AZ5ytr2T2\n9. Караганда:\nhttps://chat.whatsapp.com/BSCDGAcJ1faF7lKOlFD6Oz\n10. Актобе:\nhttps://chat.whatsapp.com/ECf9YhyGQuQ8gDSAytQbkD\n11. Актау:\nhttps://chat.whatsapp.com/FCBmwR18klC4gkpNcJP1Lj\n12. Аякөз:\nhttps://chat.whatsapp.com/Hs1CochDhQsLQbuJBZvAeJ\n13. Уральск:\nhttps://chat.whatsapp.com/CyclnbVQmnGLTMAYvknVUS\n14. Костанай:\nhttps://chat.whatsapp.com/CiQIX7rrFFS12PwzuwX9it\n15. Усть-Каменогорск:\nhttps://chat.whatsapp.com/KwyYa77rlUGD5BRJtUdv4L\n16. Кызылорда:\nhttps://chat.whatsapp.com/CjbgKHdkjV7CAUlfcBJ4fq\n17. Темиртау:\nhttps://chat.whatsapp.com/HMe0RFwGuKSJCWLzGkj4GX\n18. Кокшетау:\nhttps://chat.whatsapp.com/LioHtfC4mfF3gY2TsoDUgX\n19. Экибастуз:\nhttps://chat.whatsapp.com/ENVDKuIo9lYJQ9FCagkYDg\n20. Семей:\nhttps://chat.whatsapp.com/Iq97A6UUEuL0euBNUmakQK\n21. Рудный:\nhttps://chat.whatsapp.com/HAFlzVY8wGP35jalOHbkZn\n22. Талдыкорган:\nhttps://chat.whatsapp.com/Hz4SLi5NEa6DmTCCCjBDP7\n23. Павлодар:\nhttps://chat.whatsapp.com/Eyw5UvGJ81eFmrPfoS3xaB\n24. Петропавловск:\nhttps://chat.whatsapp.com/KiodoNzwqgW3uFJB6OA4ux\n25. Тараз:\nhttps://chat.whatsapp.com/FCeUovkURZWE5PmfzbUNa7\n26. Туркестан:\nhttps://chat.whatsapp.com/CynRQHoO8Lz88IXRZ4F8lf\nЕдиная Telegram группа для всех фармацевтов Казахстана 🇰🇿:\nhttps://t.me/inDrugKZ'



    bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=['iteka'])
def iteka(message):
    bot.send_message(message.chat.id, 'Это контакт I-Teka, сохраните его, и напишите на WhatsApp этого контакта любое сообщение.'
                                      ' Автоответчик поможет последовательно найти нужное лекарство и аптеку.'
                                      '\n+7 707 291 9919')


@bot.message_handler(commands=['indrugapp'])
def indrug(message):
    msg = 'Как альтернатива, установите данное приложение InDrug Покупатель.\nЧтобы соблюдать условия карантина и не бегать по всему городу в поиске лекарств 💊, для вас доступнобесплатное мобильное приложение "inDrug Покупатель".\nЧерез приложение "inDrug Покупатель" можно сидя дома найти лекарства и пойти в нужную аптеку, а внекоторых аптеках есть услуга доставки 🚙.\nСкачайте мобильное приложение 📲 "inDrug Покупатель" для поиска лекарств и аптечных товаров\n💊🔍\nСсылка в App Store:\nhttps://apps.apple.com/us/app/indrug-%D0%BF%D0%BE%D0%BA%D1%83%D0%BF%D0%B0%D1%82%D0%B5%D0%BB%D1%8Cid1497852138?l=ru&ls=1\n💊🔍\nСсылка в Play Market:\nhttps://play.google.com/store/apps/details?id=com.indrug.buyer\n💊🔍\nСтраница в Instagram:\nhttps://www.instagram.com/p/B_fkcLXHRBH/?igshid=pi8ee098lyb5\n💊🔍\nКанал в YouTube:\nhttps://youtu.be/2ocM3UD_n5Q'
    bot.send_message(message.chat.id,msg )


@bot.message_handler(commands=['coviddoc'])
def coviddoc(message):
    bot.send_message(message.chat.id, 'Ссылка на чат, где сидят реальные доктора, '
                                      'которые могут помочь вам дистанционно:'
                                      '\nhttps://t.me/CovidDoctorsKZ')


bot.polling()
