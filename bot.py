import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
import threading
import time

# ========== ВАШИ ДАННЫЕ ==========
TOKEN = "8652785746:AAHW7CufljQULtzWv4MyOdY9Mpkmqgqlghg"
ADMIN_ID = 5310441458
# =================================

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

# Хранилище данных
user_links = {}
users_db = set()
pending_ads = {}  # { message_id: {"text": "текст", "chat_id": chat_id} }

def get_random_unused_link(user_id):
    global user_links
    if str(user_id) in user_links and user_links[str(user_id)].get("valid", False):
        return None, "❌ У вас уже есть активная ссылка! Сначала нажмите 'Сделать недействительной'."
    
    used_links = [data["link"] for data in user_links.values() if data.get("valid", False)]
    available = [link for link in LINKS if link not in used_links]
    
    if not available:
        return None, "❌ Все ссылки закончились!"
    
    link = random.choice(available)
    user_links[str(user_id)] = {"link": link, "valid": True}
    return link, None

def invalidate_link(user_id):
    global user_links
    if str(user_id) in user_links and user_links[str(user_id)].get("valid", False):
        user_links[str(user_id)]["valid"] = False
        return True
    return False

def get_remaining():
    used = [data["link"] for data in user_links.values() if data.get("valid", False)]
    return len(LINKS) - len(used)

def broadcast_message(admin_id, text):
    success = 0
    fail = 0
    for uid in users_db:
        try:
            bot.send_message(int(uid), text)
            success += 1
            time.sleep(0.05)
        except:
            fail += 1
    bot.send_message(admin_id, f"📊 ОТЧЁТ О РАССЫЛКЕ:\n\n✅ Успешно: {success}\n❌ Не доставлено: {fail}\n👥 Всего: {len(users_db)}")

# ========== КОМАНДЫ ==========

@bot.message_handler(commands=['start'])
def start(message):
    users_db.add(str(message.chat.id))
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("🔗 ПОЛУЧИТЬ СЛУЧАЙНУЮ ССЫЛКУ", callback_data="get_link"),
        InlineKeyboardButton("❌ СДЕЛАТЬ ССЫЛКУ НЕДЕЙСТВИТЕЛЬНОЙ", callback_data="invalidate")
    )
    bot.send_message(
        message.chat.id,
        f"👋 Привет, {message.from_user.first_name}!\n\n"
        f"🤖 Я бот для выдачи реферальных ссылок VACBAN\n\n"
        f"📋 Нажми кнопку, чтобы получить случайную ссылку.\n"
        f"⚠️ Каждая ссылка выдается ТОЛЬКО ОДНОМУ пользователю!",
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
        
        remaining = get_remaining()
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(InlineKeyboardButton("❌ СДЕЛАТЬ НЕДЕЙСТВИТЕЛЬНОЙ", callback_data="invalidate"))
        
        bot.edit_message_text(
            f"✅ {user_name}, ВАША ССЫЛКА:\n\n"
            f"🔗 `{link}`\n\n"
            f"📊 Осталось ссылок: {remaining}\n\n"
            f"⚠️ Если ссылка не подойдёт — нажмите кнопку ниже и получите НОВУЮ!",
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            parse_mode="Markdown",
            reply_markup=markup
        )
    
    elif call.data == "invalidate":
        if invalidate_link(user_id):
            remaining = get_remaining()
            markup = InlineKeyboardMarkup(row_width=1)
            markup.add(InlineKeyboardButton("🔗 ПОЛУЧИТЬ НОВУЮ ССЫЛКУ", callback_data="get_link"))
            
            bot.edit_message_text(
                f"✅ Ссылка АННУЛИРОВАНА!\n\n"
                f"🔁 Нажмите кнопку, чтобы получить НОВУЮ ссылку.\n"
                f"📊 Осталось ссылок: {remaining}",
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                reply_markup=markup
            )
        else:
            bot.answer_callback_query(call.id, "❌ Нет активной ссылки!", show_alert=True)

# ========== /ads - ИСПРАВЛЕННАЯ ВЕРСИЯ ==========

@bot.message_handler(commands=['ads'])
def ads_command(message):
    if message.from_user.id != ADMIN_ID:
        bot.send_message(message.chat.id, "⛔ Доступ запрещён!")
        return
    
    text = message.text.replace('/ads', '').strip()
    
    if not text:
        bot.send_message(
            message.chat.id,
            f"📢 *ИНСТРУКЦИЯ*\n\n"
            f"`/ads [текст сообщения]`\n\n"
            f"👥 *Пользователей:* {len(users_db)}\n\n"
            f"📌 Пример:\n`/ads Всем привет! Новые ссылки!`",
            parse_mode="Markdown"
        )
        return
    
    # Сохраняем текст рассылки
    pending_ads[message.message_id] = {
        "text": text,
        "chat_id": message.chat.id
    }
    
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("✅ ДА, ОТПРАВИТЬ", callback_data=f"ads_confirm_{message.message_id}"),
        InlineKeyboardButton("❌ ОТМЕНА", callback_data=f"ads_cancel_{message.message_id}")
    )
    
    bot.send_message(
        message.chat.id,
        f"📢 *ПОДТВЕРЖДЕНИЕ РАССЫЛКИ*\n\n"
        f"📝 Текст:\n`{text[:200]}`\n\n"
        f"👥 Получателей: {len(users_db)}\n\n"
        f"Отправить?",
        parse_mode="Markdown",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data.startswith('ads_'))
def handle_ads_callback(call):
    if call.from_user.id != ADMIN_ID:
        bot.answer_callback_query(call.id, "⛔ Доступ запрещён!", show_alert=True)
        return
    
    action, msg_id = call.data.split('_')[1], call.data.split('_')[2]
    msg_id = int(msg_id)
    
    if action == "cancel":
        bot.edit_message_text(
            "❌ Рассылка ОТМЕНЕНА.",
            chat_id=call.message.chat.id,
            message_id=call.message.message_id
        )
        if msg_id in pending_ads:
            del pending_ads[msg_id]
        bot.answer_callback_query(call.id, "Отменено")
        return
    
    if action == "confirm":
        if msg_id not in pending_ads:
            bot.edit_message_text(
                "❌ Ошибка! Данные не найдены. Попробуйте снова.",
                chat_id=call.message.chat.id,
                message_id=call.message.message_id
            )
            bot.answer_callback_query(call.id, "Ошибка!")
            return
        
        ads_text = pending_ads[msg_id]["text"]
        
        bot.edit_message_text(
            f"📢 РАССЫЛКА НАЧАТА!\n\n"
            f"👥 Получателей: {len(users_db)}\n"
            f"⏳ Пожалуйста, подождите...",
            chat_id=call.message.chat.id,
            message_id=call.message.message_id
        )
        
        bot.answer_callback_query(call.id, "Рассылка начата!")
        
        # Запускаем рассылку
        threading.Thread(target=broadcast_message, args=(call.from_user.id, ads_text)).start()
        
        # Удаляем из pending
        del pending_ads[msg_id]

# ========== ОСТАЛЬНЫЕ АДМИН-КОМАНДЫ ==========

@bot.message_handler(commands=['stats'])
def stats(message):
    if message.from_user.id != ADMIN_ID:
        return
    total = len(LINKS)
    active = sum(1 for d in user_links.values() if d.get("valid"))
    bot.send_message(
        message.chat.id,
        f"📊 *СТАТИСТИКА*\n\n"
        f"📝 Всего: {total}\n"
        f"✅ Выдано: {active}\n"
        f"📭 Осталось: {total - active}\n"
        f"👥 Пользователей: {len(users_db)}",
        parse_mode="Markdown"
    )

@bot.message_handler(commands=['users'])
def users_list(message):
    if message.from_user.id != ADMIN_ID:
        return
    if not users_db:
        bot.send_message(message.chat.id, "📭 Нет пользователей")
        return
    text = f"👥 ПОЛЬЗОВАТЕЛИ ({len(users_db)}):\n\n"
    for i, uid in enumerate(list(users_db), 1):
        text += f"{i}. `{uid}`\n"
        if len(text) > 3500:
            text += "\n⚠️ ..."
            break
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

@bot.message_handler(commands=['reset_user'])
def reset_user(message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        target = str(int(message.text.split()[1]))
        if target in user_links:
            del user_links[target]
            bot.send_message(message.chat.id, f"✅ Сброшено: {target}")
        else:
            bot.send_message(message.chat.id, f"❌ Не найден: {target}")
    except:
        bot.send_message(message.chat.id, "❌ Использование: /reset_user [ID]")

@bot.message_handler(commands=['reset_all'])
def reset_all(message):
    if message.from_user.id != ADMIN_ID:
        return
    global user_links
    user_links = {}
    bot.send_message(message.chat.id, "✅ ВСЁ СБРОШЕНО!")

print("=" * 50)
print("🤖 БОТ ЗАПУЩЕН!")
print(f"👨‍💻 Админ: {ADMIN_ID}")
print(f"📊 Ссылок: {len(LINKS)}")
print("=" * 50)
print("✅ Команда /ads [текст] - для рассылки")
print("=" * 50)

bot.infinity_polling()
