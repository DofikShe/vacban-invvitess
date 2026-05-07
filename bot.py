import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
import os
import threading
import time

# ========== НАСТРОЙКИ ==========
TOKEN = "8652785746:AAHW7CufljQULtzWv4MyOdY9Mpkmqgqlghg"  # ← ЗАМЕНИТЕ НА ВАШ ТОКЕН!
ADMIN_ID = 5310441458  # ← ЗАМЕНИТЕ НА ВАШ TELEGRAM ID
# ================================

bot = telebot.TeleBot(TOKEN)

# ==== ВАШИ ССЫЛКИ ====
LINKS = [
    "https://vacban.wtf/?vacinvite=WTF-6BFf68AP5qNS1d1fc0ig7wYvWyOpR92Lr0U6",
    "https://vacban.wtf/?vacinvite=WTF-7cGdAcmblaF9bQ0Lt3i9aaO8z32ffZ0Xc91r",
    "https://vacban.wtf/?vacinvite=WTF-1PDF42VOfZ4fBthfn0Jb4v9c5f7cWgsre67f",
    "https://vacban.wtf/?vacinvite=WTF-KYcn8901XUayxcaJ0kgP7HzW23rlbwc4B5pe",
    "https://vacban.wtf/?vacinvite=WTF-9Ir4g5fCqTp2utd16dJLsR2e8Sf7fa4fNMiB",
    "https://vacban.wtf/?vacinvite=WTF-5ez8ecKeCB2b2XNi48bfJocRl45fwua2fc1e",
    "https://vacban.wtf/?vacinvite=WTF-8NTgOoIjYqdDEV1kCMs56676aJdnWfe21bUK",
    "https://vacban.wtf/?vacinvite=WTF-aZx7kaWIr0gezbmc1Y6747645QBqd3ydHEPN",
    "https://vacban.wtf/?vacinvite=WTF-9afQzZ18CtksXe7Ff9J36jcx6cyg88O5DB2Y",
    "https://vacban.wtf/?vacinvite=WTF-7mQgfD1HeNK43aLe1deJaV8F7jsafq5Pw4hr",
    "https://vacban.wtf/?vacinvite=WTF-y2ncYtuR38P1WfEfQ2e756kL5SwMfbAcxGU9",
    "https://vacban.wtf/?vacinvite=WTF-20KmI56Td2hdXA851PL2UOlR6Vksdv74CcG6",
    "https://vacban.wtf/?vacinvite=WTF-WapED98PFl9f2JdiXe81z54cS2whxYfnBNTd",
    "https://vacban.wtf/?vacinvite=WTF-r8h65PY5oT7camUfcFSzbe49vayKipa02qJ2",
    "https://vacban.wtf/?vacinvite=WTF-MYl9e927UjL0SGC5hckD7sfcecixcHOFdZ3P",
    "https://vacban.wtf/?vacinvite=WTF-1Q0FdameM982Zcacfn38bB2082dH248c7lb7",
    "https://vacban.wtf/?vacinvite=WTF-71a1nQ53H2a0J4S88IPM2713TdC72fKX6fZ4",
    "https://vacban.wtf/?vacinvite=WTF-C1hExbHaeP3O8BUSqAQzgdKo9ly152fRi0bk",
    "https://vacban.wtf/?vacinvite=WTF-zeEFc1s0Hgi981v22MbS5f5NPTucay0b306b",
    "https://vacban.wtf/?vacinvite=WTF-9AepJ4NXWu2tP3Fb1aQqgd8R3Cc5aj7O1UYB",
    "https://vacban.wtf/?vacinvite=WTF-OgcVMQfF3Wad0bhq9dYz09r9870f5uneN2S9",
    "https://vacban.wtf/?vacinvite=WTF-1WI6m1422sc4cdjuDS5aEZhpMq5eLcwnf5ao",
    "https://vacban.wtf/?vacinvite=WTF-qsfWd27dd6eP0u5foft9h6cSHdxOX5pEJNMm",
    "https://vacban.wtf/?vacinvite=WTF-xQ3a2HS2bdzCUK8guRcf8Xj7yh305cWvF9Ar",
    "https://vacban.wtf/?vacinvite=WTF-yXv4i48nJw8ejga0UOD9GYFdfkH89fVoqtcC",
    "https://vacban.wtf/?vacinvite=WTF-8bebDrfgR7O25GWlvob7fFcX5ewbcYS02ex3",
    "https://vacban.wtf/?vacinvite=WTF-tH6LPRu2J9cOV8XfKC32AUyq5EN97Zb1TB0m",
    "https://vacban.wtf/?vacinvite=WTF-h62V4e32Jbgi7t4w2N8e3DddcdUkl47xrS7E",
    "https://vacban.wtf/?vacinvite=WTF-8bems0badEAq1168zNe9akQta2cGY6JL0B1e",
    "https://vacban.wtf/?vacinvite=WTF-71ru2bRsyBMadof5I3gePKx6l6ka3Fa1a6pE",
    "https://vacban.wtf/?vacinvite=WTF-8X2gxbjAfJe9yYG9bh5bL8rdHafKIf0TvCik",
    "https://vacban.wtf/?vacinvite=WTF-4nfDscowrE5bfifXJV29g5l424cxdqUYcIee",
    "https://vacban.wtf/?vacinvite=WTF-99W5I782mXHa766beSgifs0Rw58vfff6l5G2",
    "https://vacban.wtf/?vacinvite=WTF-8Fkn5Wc4chQ7Ly5b5V43rEdg2qaIu2a9cKef",
    "https://vacban.wtf/?vacinvite=WTF-fV2Rl7xN3f4cX4ZAIndDeHiu17dr88f68cKo",
    "https://vacban.wtf/?vacinvite=WTF-5U3f225mdGY70Xb9CB9aFQTHNJftaz2pLK4o",
    "https://vacban.wtf/?vacinvite=WTF-H281epRGfBAhvd1yFa4a7OUaP1Cq86JZife2",
    "https://vacban.wtf/?vacinvite=WTF-3VbHhee68NoB94RGsdd4bDcAf2i7lp7Kv1nE",
    "https://vacban.wtf/?vacinvite=WTF-fa9D1abkoYh5OWS8bBfc00lQc8JexC4X95d8",
    "https://vacban.wtf/?vacinvite=WTF-edvpca3RSAed5f910ie4VYfMa4ITU8kxdOod",
    "https://vacban.wtf/?vacinvite=WTF-99b89786Qcz08kaVf2ZdBPu5teH2i03MJ7cf",
    "https://vacban.wtf/?vacinvite=WTF-IbM4dEcFaH2KW9qOa4QsdVNod7cLXl874ffd",
    "https://vacban.wtf/?vacinvite=WTF-fyfeVMleW0Oq6r6B9d8do7UGXwR4si76EuJc",
    "https://vacban.wtf/?vacinvite=WTF-GcV99I6e4vy089h53R5cdfok4ZxA0YbrU85N",
    "https://vacban.wtf/?vacinvite=WTF-WqZ3z8dSGOdfsB1YUkLve4yCp2eKM9g8f91n",
    "https://vacban.wtf/?vacinvite=WTF-cwCAprScx5jmK5fz0f0R2ycnOb1tBseq7boY",
    "https://vacban.wtf/?vacinvite=WTF-N3bgaVf6977Xkd1dcR65qrP1v0LaBH19eaxu",
    "https://vacban.wtf/?vacinvite=WTF-5ZbdG4Vabo4i7Ym4E67O4CdbqWfegd6cPvp2",
    "https://vacban.wtf/?vacinvite=WTF-c6rYq1A78fHUijafkh7byNM271FJ3geo54lp",
    "https://vacban.wtf/?vacinvite=WTF-13O64l5csYSVeE4dJ45Mv4eTdba1tR53e69y",
    "https://vacban.wtf/?vacinvite=WTF-JvWObt069ff18RNEQj5MXd6ce9S5xw15kf93",
    "https://vacban.wtf/?vacinvite=WTF-1PjfrnLH6McSY6pAyNdei5aFa6xw2eec59qf",
    "https://vacban.wtf/?vacinvite=WTF-75WdX6qEmLH7cCalfdxuAt54e8Tc0DOrSnUf",
    "https://vacban.wtf/?vacinvite=WTF-Lb082302ybK4V39468jCQ9vNfcAwkf8i8WZT",
    "https://vacban.wtf/?vacinvite=WTF-0g2ciJP8Q14qLc63KfH1Afd9aIOezx8ycfd8",
    "https://vacban.wtf/?vacinvite=WTF-acDbe92qoi0dxz5T73ws4lLYPbjZacMrWuA4",
    "https://vacban.wtf/?vacinvite=WTF-O1P7bSaM5DW1fdvd3Jj1U06Vh4boB721RcYw",
    "https://vacban.wtf/?vacinvite=WTF-dxj235lFO5egBbsE6860LdoC3MHac1rV73bv",
    "https://vacban.wtf/?vacinvite=WTF-8Se171efKbaisy7V6Nb3uELjW055288Cpf8a",
    "https://vacban.wtf/?vacinvite=WTF-PeWEIqf3KpD71hed4e5R5kGeyxS6Qa5d6B16",
    "https://vacban.wtf/?vacinvite=WTF-11eiMJSKf9hd6lEwd5LcAG5o7D70d9Ftf6c3",
    "https://vacban.wtf/?vacinvite=WTF-m6kED0Cb1d5NqAoOKecaU7fH3a4d75bcjg21",
    "https://vacban.wtf/?vacinvite=WTF-De1KRdP9U606idc5f47eoWqm5afSTd60fQ47",
    "https://vacban.wtf/?vacinvite=WTF-cm2hgdaPdCE7fo3JA89Yb02jBI49HcZcsaSa",
    "https://vacban.wtf/?vacinvite=WTF-U8wfKGdg2cdWxdm2Rp616u1c6SiT5O40c0BN",
    "https://vacban.wtf/?vacinvite=WTF-Bwdc8taEpb6T1oh5r2j0de3afe0737GLeMec",
    "https://vacban.wtf/?vacinvite=WTF-Wqg6j7vy8f9MoVOwxhA1ub32Z2F5Gc994HU8",
    "https://vacban.wtf/?vacinvite=WTF-lfLesa58Kfcu70737z26EdqdMWbwbiexo52r",
    "https://vacban.wtf/?vacinvite=WTF-ec2T5715NaEIvs8kM5e0w9h073YuBa6O9GbQ",
    "https://vacban.wtf/?vacinvite=WTF-ela1sd43e5te72gePcfhd8kCmxu3fZ4XcQnJ",
    "https://vacban.wtf/?vacinvite=WTF-n99We2Bp7f090cCl56gvZcfwd4K18T13hj5k",
    "https://vacban.wtf/?vacinvite=WTF-z8h4Aead912qtN7iVacJoCccdf4BpRcb520a"
]

# Хранилище в памяти
user_links = {}  # { user_id: {"link": "ссылка", "valid": True/False} }
users_db = set()  # Множество для хранения всех пользователей, кто написал боту

# ========== ФУНКЦИИ БОТА ==========

def get_random_unused_link(user_id):
    """Выдаёт случайную неиспользованную ссылку пользователю"""
    global user_links
    
    if str(user_id) in user_links and user_links[str(user_id)].get("valid", False):
        return None, "❌ У вас уже есть активная ссылка! Сначала нажмите 'Сделать недействительной'."
    
    used_links = []
    for uid, data in user_links.items():
        if data.get("valid", False):
            used_links.append(data["link"])
    
    available_links = [link for link in LINKS if link not in used_links]
    
    if not available_links:
        return None, "❌ Все ссылки закончились! Обратитесь к администратору."
    
    selected_link = random.choice(available_links)
    
    user_links[str(user_id)] = {
        "link": selected_link,
        "valid": True
    }
    
    return selected_link, None

def invalidate_link(user_id):
    """Делает ссылку пользователя недействительной"""
    global user_links
    
    if str(user_id) in user_links and user_links[str(user_id)].get("valid", False):
        user_links[str(user_id)]["valid"] = False
        return True
    return False

def broadcast_message(admin_id, message_text):
    """Отправляет сообщение всем пользователям"""
    success_count = 0
    fail_count = 0
    
    for user_id in users_db:
        try:
            bot.send_message(int(user_id), message_text)
            success_count += 1
            time.sleep(0.05)  # Небольшая задержка, чтобы не превысить лимиты Telegram
        except Exception as e:
            fail_count += 1
            print(f"Не удалось отправить пользователю {user_id}: {e}")
    
    # Отправляем отчет админу
    bot.send_message(
        admin_id,
        f"📊 Отчёт о рассылке:\n\n"
        f"✅ Успешно отправлено: {success_count}\n"
        f"❌ Не доставлено: {fail_count}\n"
        f"👥 Всего пользователей: {len(users_db)}"
    )

# ========== КОМАНДЫ БОТА ==========

@bot.message_handler(commands=['start'])
def start(message):
    # Добавляем пользователя в базу
    users_db.add(str(message.chat.id))
    
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("🔗 Рабочая", callback_data="get_link"),
        InlineKeyboardButton("❌ Не рабочая", callback_data="invalidate")
    )
    
    user_name = message.from_user.first_name or "Пользователь"
    
    bot.send_message(
        message.chat.id,
        f"👋 Привет, {user_name}!\n\n"
        f"🤖 Я бот для выдачи реферальных ссылок VACBAN\n\n"
        f"📋 Как я работаю:\n"
        f"• При нажатии на кнопку выдаю инвайт доступ к форуму vacban.wtf\n"
        f"• Можешь получть ссылку для себя и друзей\n"
        f"• ОБРАЩАЙТЕ ВНИМАНИЕ НА ПОСЛЕДНИЙ АПДЕЙТ ИНВАЙТОВ И СКОЛЬКО ДОСТУПНО\n"
        f"• Последнее обновление бота/инвайтов :08.05.2026\n\n"
        f"⚠️ Если ссылка не действительна то нажмите НЕ РАБОЧАЯ\n\n"
        f"👉 Нажмите кнопку ниже, чтобы получить случайную ссылку:"
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: True)
def handle_buttons(call):
    user_id = call.from_user.id
    user_name = call.from_user.first_name or "Пользователь"
    
    if call.data == "get_link":
        link, error = get_random_unused_link(user_id)
        
        if error:
            bot.answer_callback_query(call.id, error, show_alert=True)
            return
        
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(
            InlineKeyboardButton("📋 СКОПИРОВАТЬ ССЫЛКУ", callback_data="copy"),
            InlineKeyboardButton("❌ СДЕЛАТЬ НЕДЕЙСТВИТЕЛЬНОЙ", callback_data="invalidate")
        )
        
        used_links = []
        for uid, data in user_links.items():
            if data.get("valid", False):
                used_links.append(data["link"])
        remaining = len(LINKS) - len(used_links)
        
        bot.edit_message_text(
            f"✅ {user_name}, ВАШ ИНВАЙТ :\n\n"
            f"🔗 `{link}`\n\n"
            f"📌 Используйте ее\n"
            f"📊 Осталось свободных инвайтов: {remaining}\n\n"
            f"💡 Нажмите на ссылку, чтобы выделить, затем скопируйте.",
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            parse_mode="Markdown",
            reply_markup=markup
        )
        
        try:
            bot.send_message(
                ADMIN_ID,
                f"📢 Выдана ссылка!\n\n👤 Пользователь: {user_name}\n🆔 ID: {user_id}\n📊 Осталось: {remaining}"
            )
        except:
            pass
    
    elif call.data == "invalidate":
        if invalidate_link(user_id):
            markup = InlineKeyboardMarkup(row_width=1)
            markup.add(InlineKeyboardButton("🔗 ПОЛУЧИТЬ НОВУЮ ССЫЛКУ", callback_data="get_link"))
            
            bot.edit_message_text(
                f"✅ {user_name}, ваша ссылка АННУЛИРОВАНА!\n\n"
                f"🔁 Вы можете получить НОВУЮ случайную ссылку, нажав на кнопку ниже.",
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                reply_markup=markup
            )
            
            try:
                bot.send_message(ADMIN_ID, f"⚠️ Пользователь {user_name} (ID: {user_id}) аннулировал ссылку и может получить новую")
            except:
                pass
        else:
            bot.answer_callback_query(call.id, "❌ У вас нет активной ссылки для аннулирования!", show_alert=True)
    
    elif call.data == "copy":
        bot.answer_callback_query(call.id, "📋 Нажмите и удерживайте ссылку, чтобы скопировать", show_alert=False)

# ========== НОВАЯ КОМАНДА /ads ДЛЯ РАССЫЛКИ ==========

@bot.message_handler(commands=['ads'])
def ads_command(message):
    """Команда для массовой рассылки (только для админа)"""
    if message.from_user.id != ADMIN_ID:
        bot.send_message(message.chat.id, "⛔ Доступ запрещён. Эта команда только для администратора.")
        return
    
    # Проверяем, есть ли текст после команды
    text = message.text.replace('/ads', '').strip()
    
    if not text:
        bot.send_message(
            message.chat.id,
            "📢 *Как сделать рассылку:*\n\n"
            "Напишите команду и текст сообщения:\n"
            "`/ads Ваше рекламное сообщение здесь`\n\n"
            "📌 *Пример:*\n"
            "`/ads Внимание! У нас новые реферальные ссылки!`\n\n"
            f"👥 *Всего пользователей:* {len(users_db)}\n\n"
            "⚠️ Рассылку нельзя отменить. Убедитесь, что сообщение готово!",
            parse_mode="Markdown"
        )
        return
    
    # Подтверждение перед отправкой
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("✅ ДА, ОТПРАВИТЬ", callback_data=f"confirm_ads_{message.message_id}"),
        InlineKeyboardButton("❌ ОТМЕНА", callback_data="cancel_ads")
    )
    
    # Сохраняем текст рассылки во временную переменную (через атрибут бота)
    bot.temp_ads_text = text
    bot.temp_ads_msg_id = message.message_id
    
    bot.send_message(
        message.chat.id,
        f"📢 *ПОДТВЕРЖДЕНИЕ РАССЫЛКИ*\n\n"
        f"📝 Текст сообщения:\n"
        f"`{text[:200]}{'...' if len(text) > 200 else ''}`\n\n"
        f"👥 Будет отправлено: {len(users_db)} пользователям\n\n"
        f"⚠️ Это действие нельзя отменить!\n\n"
        f"Отправить?",
        parse_mode="Markdown",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data.startswith('confirm_ads_') or call.data == 'cancel_ads')
def handle_ads_confirmation(call):
    if call.from_user.id != ADMIN_ID:
        bot.answer_callback_query(call.id, "⛔ Доступ запрещён!", show_alert=True)
        return
    
    if call.data == 'cancel_ads':
        bot.edit_message_text(
            "❌ Рассылка отменена.",
            chat_id=call.message.chat.id,
            message_id=call.message.message_id
        )
        bot.answer_callback_query(call.id, "Рассылка отменена")
        return
    
    if call.data.startswith('confirm_ads_'):
        # Получаем текст рассылки
        ads_text = getattr(bot, 'temp_ads_text', None)
        
        if not ads_text:
            bot.edit_message_text(
                "❌ Ошибка: текст рассылки не найден. Попробуйте снова.",
                chat_id=call.message.chat.id,
                message_id=call.message.message_id
            )
            bot.answer_callback_query(call.id, "Ошибка!")
            return
        
        # Уведомляем о начале рассылки
        bot.edit_message_text(
            f"📢 Начинаю рассылку...\n\n👥 Всего пользователей: {len(users_db)}\n⏳ Пожалуйста, подождите...",
            chat_id=call.message.chat.id,
            message_id=call.message.message_id
        )
        
        bot.answer_callback_query(call.id, "Рассылка начата!")
        
        # Запускаем рассылку в отдельном потоке, чтобы не блокировать бота
        threading.Thread(target=broadcast_message, args=(call.from_user.id, ads_text)).start()

# ========== ОСТАЛЬНЫЕ КОМАНДЫ АДМИНА ==========

@bot.message_handler(commands=['stats'])
def stats(message):
    """Статистика для админа"""
    if message.from_user.id != ADMIN_ID:
        bot.send_message(message.chat.id, "⛔ Доступ запрещён. Эта команда только для администратора.")
        return
    
    global user_links
    
    total_links = len(LINKS)
    active_users = len(user_links)
    active_links = sum(1 for data in user_links.values() if data.get("valid", False))
    used_links_ids = [data["link"] for data in user_links.values() if data.get("valid", False)]
    used_count = len(used_links_ids)
    
    stats_text = f"📊 СТАТИСТИКА БОТА\n\n"
    stats_text += f"📝 Всего ссылок в базе: {total_links}\n"
    stats_text += f"👥 Пользователей в боте: {len(users_db)}\n"
    stats_text += f"✅ Активных ссылок выдано: {active_links}\n"
    stats_text += f"📭 Свободных ссылок осталось: {total_links - used_count}\n"
    stats_text += f"🔒 Аннулированных: {active_users - active_links}\n\n"
    
    if active_links > 0:
        stats_text += "🆔 Активные ссылки:\n"
        for uid, data in user_links.items():
            if data.get("valid"):
                stats_text += f"• User {uid}: {data['link'][:50]}...\n"
    
    if len(stats_text) > 4000:
        stats_text = stats_text[:4000] + "..."
    
    bot.send_message(message.chat.id, stats_text)

@bot.message_handler(commands=['reset_user'])
def reset_user(message):
    """Сброс ссылки конкретного пользователя (только админ)"""
    if message.from_user.id != ADMIN_ID:
        bot.send_message(message.chat.id, "⛔ Доступ запрещён.")
        return
    
    try:
        target_id = str(int(message.text.split()[1]))
        global user_links
        
        if target_id in user_links:
            del user_links[target_id]
            bot.send_message(message.chat.id, f"✅ Ссылка пользователя {target_id} сброшена!")
        else:
            bot.send_message(message.chat.id, f"❌ Пользователь {target_id} не найден в базе.")
    except:
        bot.send_message(message.chat.id, "❌ Использование: /reset_user [ID пользователя]")

@bot.message_handler(commands=['reset_all'])
def reset_all(message):
    """Полный сброс всех данных (только админ)"""
    if message.from_user.id != ADMIN_ID:
        bot.send_message(message.chat.id, "⛔ Доступ запрещён.")
        return
    
    global user_links
    user_links = {}
    bot.send_message(message.chat.id, "✅ ВСЕ ДАННЫЕ СБРОШЕНЫ! Все ссылки снова доступны.")

@bot.message_handler(commands=['users'])
def list_users(message):
    """Список всех пользователей бота (только админ)"""
    if message.from_user.id != ADMIN_ID:
        bot.send_message(message.chat.id, "⛔ Доступ запрещён.")
        return
    
    if not users_db:
        bot.send_message(message.chat.id, "📭 Нет пользователей в базе.")
        return
    
    users_list = list(users_db)
    text = f"👥 СПИСОК ПОЛЬЗОВАТЕЛЕЙ ({len(users_db)}):\n\n"
    
    for i, uid in enumerate(users_list, 1):
        text += f"{i}. `{uid}`\n"
        if len(text) > 3500:
            text += "\n⚠️ Список слишком длинный, показаны не все..."
            break
    
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = (
        "🤖 *Команды бота:*\n\n"
        "👤 *Для всех:*\n"
        "/start - Начать работу\n\n"
        "👑 *Админ-команды:*\n"
        "/stats - Статистика\n"
        "/users - Список всех пользователей\n"
        "/ads [текст] - Массовая рассылка\n"
        "/reset_user [ID] - Сбросить ссылку пользователя\n"
        "/reset_all - Полный сброс всех данных\n\n"
        "*Как пользоваться:*\n"
        "1️⃣ Нажмите 'Получить случайную ссылку'\n"
        "2️⃣ Бот выдаст РАНДОМНУЮ ссылку из списка\n"
        "3️⃣ Эта ссылка больше НИКОМУ не выдастся\n"
        "4️⃣ Если ссылка не подходит - аннулируйте её и получите новую\n\n"
        "⚠️ Каждая ссылка выдается ТОЛЬКО ОДНОМУ пользователю!"
    )
    bot.send_message(message.chat.id, help_text, parse_mode="Markdown")

# Запуск бота
print("=" * 50)
print("🤖 БОТ ЗАПУЩЕН!")
print("=" * 50)
print(f"📊 Всего загружено ссылок: {len(LINKS)}")
print(f"👨‍💻 Админ ID: {ADMIN_ID}")
print(f"👥 База пользователей: {len(users_db)}")
print("=" * 50)
print("✅ Бот готов к работе!")
print("📌 Команда /ads [текст] - для массовой рассылки")
print("=" * 50)
print("Нажмите Ctrl+C для остановки")
print("=" * 50)

bot.infinity_polling()
