from Buttons import main_buttons , namaz_buttons, Namoz_5_buttons_men, Namoz_5_buttons_wmen,namaz_tartib_buttons , WM_buttons, today, tomorrov, dua, mintaqa, namaz, adv1, dasturchi, film, kino_button, fasl
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, CallbackContext,CallbackQueryHandler, ConversationHandler, MessageHandler, Filters
from datetime import date , timedelta
from  Islom_uz_time import region_time , region_time_tomorrow
from get_islom import get_regions , get_region
from database_users import add, get_date
user_region = dict()


state_region = 1
state_command = 2
state_3 = 3
state_4 = 4
state_5 = 5
state_6 = 6
state_7 = 7
state_8 = 8
state_9 = 9
state_10 = 10
state_11 = 11
state_12 = 12
state_13 = 13
state_audio = 14
def region_buttons():
    regions = get_regions()
    buttons = []
    temp_b = []
    for region_name in regions:
        temp_b.append(InlineKeyboardButton(region_name[0], callback_data=region_name[1] ))
        if len(temp_b) == 2:
            buttons.append(temp_b)
            temp_b = []
    return buttons
def command_fasl(update, context):
    query = update.callback_query
    query.message.delete()
    A= query.data
    if A == '1':
        query.message.reply_html('<a>https://www.youtube.com/watch?v=6mTKx36e_0U&list=PLys356tU5j5QG5CAQT7_HJ_B8V3wpgEQb&index=2</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=yXd_d4m_7aQ&list=PLys356tU5j5QG5CAQT7_HJ_B8V3wpgEQb&index=3</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=MAYQ9DAty_Y&list=PLys356tU5j5QG5CAQT7_HJ_B8V3wpgEQb&index=4</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=UV-AU0YtIP8&list=PLys356tU5j5QG5CAQT7_HJ_B8V3wpgEQb&index=5</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=BfsIeNhYElE&list=PLys356tU5j5QG5CAQT7_HJ_B8V3wpgEQb&index=6</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=JTB10DRB7kc&list=PLys356tU5j5QG5CAQT7_HJ_B8V3wpgEQb&index=7</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=TfTz10bbrh0&list=PLys356tU5j5QG5CAQT7_HJ_B8V3wpgEQb&index=8</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=KcguOVh1SD8&list=PLys356tU5j5QG5CAQT7_HJ_B8V3wpgEQb&index=9</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=5lNpV4XJDKI&list=PLys356tU5j5QG5CAQT7_HJ_B8V3wpgEQb&index=10</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=h_W3o3b3vtA&list=PLys356tU5j5QG5CAQT7_HJ_B8V3wpgEQb&index=11</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=mQg6UT8tFvM&list=PLys356tU5j5QG5CAQT7_HJ_B8V3wpgEQb&index=12</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=Da6YrAvVhOk&list=PLys356tU5j5QG5CAQT7_HJ_B8V3wpgEQb&index=13</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=QxNplhpdCzY&list=PLys356tU5j5QG5CAQT7_HJ_B8V3wpgEQb&index=14</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=a6X23HdJ6Lo&list=PLys356tU5j5QG5CAQT7_HJ_B8V3wpgEQb&index=15</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=3TjNVGslYLU&list=PLys356tU5j5QG5CAQT7_HJ_B8V3wpgEQb&index=16</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=ltiT8o-8FH0&list=PLys356tU5j5QG5CAQT7_HJ_B8V3wpgEQb&index=17</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=dj6YjozI4no&list=PLys356tU5j5QG5CAQT7_HJ_B8V3wpgEQb&index=18</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=R22Xyitjjt0&list=PLys356tU5j5QG5CAQT7_HJ_B8V3wpgEQb&index=19</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=Sow9AO2H3h4&list=PLys356tU5j5QG5CAQT7_HJ_B8V3wpgEQb&index=20</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=EZrDFaW8m3c&list=PLys356tU5j5QG5CAQT7_HJ_B8V3wpgEQb&index=21</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=uBhKZ-Ud800&list=PLys356tU5j5QG5CAQT7_HJ_B8V3wpgEQb&index=22</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=9GvNOwYrbXU&list=PLys356tU5j5QG5CAQT7_HJ_B8V3wpgEQb&index=23</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=5Z_S1zr1mOs&list=PLys356tU5j5QG5CAQT7_HJ_B8V3wpgEQb&index=24</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=Zu71wVfIfWk&list=PLys356tU5j5QG5CAQT7_HJ_B8V3wpgEQb&index=25</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=516B-NI1khQ&list=PLys356tU5j5QG5CAQT7_HJ_B8V3wpgEQb&index=26</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=4nvExx6NJeg&list=PLys356tU5j5QG5CAQT7_HJ_B8V3wpgEQb&index=27</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=K-QgOcshoU4&list=PLys356tU5j5QG5CAQT7_HJ_B8V3wpgEQb&index=28</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=xmW5izD82gM&list=PLys356tU5j5QG5CAQT7_HJ_B8V3wpgEQb&index=30</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=wVAp5QivAwI&list=PLys356tU5j5QG5CAQT7_HJ_B8V3wpgEQb&index=31</a>', reply_markup=InlineKeyboardMarkup(kino_button))
    elif A=='2':
        query.message.reply_html('<a>https://www.youtube.com/watch?v=Vb5HT1CGn6M&list=PLys356tU5j5SSwpHO3p-rnFk9Q3x1R1nn&index=2</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=lfJmByxxY-Q&list=PLys356tU5j5SSwpHO3p-rnFk9Q3x1R1nn&index=3</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=sl6h7L9TFAE&list=PLys356tU5j5SSwpHO3p-rnFk9Q3x1R1nn&index=4</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=2ffvF3sMBnM&list=PLys356tU5j5SSwpHO3p-rnFk9Q3x1R1nn&index=5</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=Pua11HTrg2E&list=PLys356tU5j5SSwpHO3p-rnFk9Q3x1R1nn&index=6</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=5FKdjivJ1pU&list=PLys356tU5j5SSwpHO3p-rnFk9Q3x1R1nn&index=7</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=jdEIBwi72So&list=PLys356tU5j5SSwpHO3p-rnFk9Q3x1R1nn&index=8</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=FLSrSP98lH0&list=PLys356tU5j5SSwpHO3p-rnFk9Q3x1R1nn&index=9</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=woo9fW8eBLQ&list=PLys356tU5j5SSwpHO3p-rnFk9Q3x1R1nn&index=10</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=j9ppDOApJC8&list=PLys356tU5j5SSwpHO3p-rnFk9Q3x1R1nn&index=11</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=cExyWTxkUlg&list=PLys356tU5j5SSwpHO3p-rnFk9Q3x1R1nn&index=12</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=qvBRJdCWoh8&list=PLys356tU5j5SSwpHO3p-rnFk9Q3x1R1nn&index=13</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=em3DzeO12oY&list=PLys356tU5j5SSwpHO3p-rnFk9Q3x1R1nn&index=14</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=LqM9WDeai5M&list=PLys356tU5j5SSwpHO3p-rnFk9Q3x1R1nn&index=15</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=qCczpuAP4kI&list=PLys356tU5j5SSwpHO3p-rnFk9Q3x1R1nn&index=16</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=gaLxult8skA&list=PLys356tU5j5SSwpHO3p-rnFk9Q3x1R1nn&index=17</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=wjeoKqD9I5o&list=PLys356tU5j5SSwpHO3p-rnFk9Q3x1R1nn&index=18</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=kaF2VOcl6ec&list=PLys356tU5j5SSwpHO3p-rnFk9Q3x1R1nn&index=19</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=vM3SPcmS1k8&list=PLys356tU5j5SSwpHO3p-rnFk9Q3x1R1nn&index=20</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=qoMkL4q33KU&list=PLys356tU5j5SSwpHO3p-rnFk9Q3x1R1nn&index=21</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=hhETL9tlyuQ&list=PLys356tU5j5SSwpHO3p-rnFk9Q3x1R1nn&index=22</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=z_eViUCTHT4&list=PLys356tU5j5SSwpHO3p-rnFk9Q3x1R1nn&index=23</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=rapHAWtxUfE&list=PLys356tU5j5SSwpHO3p-rnFk9Q3x1R1nn&index=24</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=k1LTTrV-GpM&list=PLys356tU5j5SSwpHO3p-rnFk9Q3x1R1nn&index=25</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=gzVVisgQrgY&list=PLys356tU5j5SSwpHO3p-rnFk9Q3x1R1nn&index=26</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=YB-eVhNaN-E&list=PLys356tU5j5SSwpHO3p-rnFk9Q3x1R1nn&index=27</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=uiP5x_q5rVY&list=PLys356tU5j5SSwpHO3p-rnFk9Q3x1R1nn&index=28</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=NpP-GZbzwa0&list=PLys356tU5j5SSwpHO3p-rnFk9Q3x1R1nn&index=29</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=Nn-y_kJ20Oc&list=PLys356tU5j5SSwpHO3p-rnFk9Q3x1R1nn&index=30</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=fHp6ereWfzM&list=PLys356tU5j5SSwpHO3p-rnFk9Q3x1R1nn&index=31</a>', reply_markup=InlineKeyboardMarkup(kino_button))
    elif A == '3':
        query.message.reply_html('<a>https://www.youtube.com/watch?v=v1GLD9tj7xo&list=PLys356tU5j5SfVim_BxnblS6LlSLq9csQ&index=2</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=OYj38-FAMRI&list=PLys356tU5j5SfVim_BxnblS6LlSLq9csQ&index=3</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=S0MK672DLoY&list=PLys356tU5j5SfVim_BxnblS6LlSLq9csQ&index=4</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=wFv3Ixsgxo8&list=PLys356tU5j5SfVim_BxnblS6LlSLq9csQ&index=5</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=xLXVyAeuTEI&list=PLys356tU5j5SfVim_BxnblS6LlSLq9csQ&index=6</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=DqJnbSpYuLI&list=PLys356tU5j5SfVim_BxnblS6LlSLq9csQ&index=7</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=rHLV--7Y6Oo&list=PLys356tU5j5SfVim_BxnblS6LlSLq9csQ&index=8</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=IzVHrnZ2Klg&list=PLys356tU5j5SfVim_BxnblS6LlSLq9csQ&index=9</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=KiFwBFwx1MQ&list=PLys356tU5j5SfVim_BxnblS6LlSLq9csQ&index=10</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=9mX8LOaLOsI&list=PLys356tU5j5SfVim_BxnblS6LlSLq9csQ&index=11</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=8yMD6lJ9tXw&list=PLys356tU5j5SfVim_BxnblS6LlSLq9csQ&index=12</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=Wd9ZIGManvc&list=PLys356tU5j5SfVim_BxnblS6LlSLq9csQ&index=13</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=rz5SgcgyoaI&list=PLys356tU5j5SfVim_BxnblS6LlSLq9csQ&index=14</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=Z4YSpRl4SyY&list=PLys356tU5j5SfVim_BxnblS6LlSLq9csQ&index=15</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=KpKK0YLuR_M&list=PLys356tU5j5SfVim_BxnblS6LlSLq9csQ&index=16</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=di-PRYrVTug&list=PLys356tU5j5SfVim_BxnblS6LlSLq9csQ&index=17</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=Yv0xrXujC3U&list=PLys356tU5j5SfVim_BxnblS6LlSLq9csQ&index=18</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=K6ZsC1vjKB0&list=PLys356tU5j5SfVim_BxnblS6LlSLq9csQ&index=19</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=H74_8zBCatM&list=PLys356tU5j5SfVim_BxnblS6LlSLq9csQ&index=20</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=Y2wJI9F4BFs&list=PLys356tU5j5SfVim_BxnblS6LlSLq9csQ&index=21</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=YAZXbzPmh6E&list=PLys356tU5j5SfVim_BxnblS6LlSLq9csQ&index=22</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=omF9SllZ94E&list=PLys356tU5j5SfVim_BxnblS6LlSLq9csQ&index=23</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=WRibUdY1Ix0&list=PLys356tU5j5SfVim_BxnblS6LlSLq9csQ&index=24</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=DKFlE5uUmRo&list=PLys356tU5j5SfVim_BxnblS6LlSLq9csQ&index=25</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=8rLSD_-M6UA&list=PLys356tU5j5SfVim_BxnblS6LlSLq9csQ&index=26</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=JZI4tiZ8JGc&list=PLys356tU5j5SfVim_BxnblS6LlSLq9csQ&index=27</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=MYmwfu-dzaE&list=PLys356tU5j5SfVim_BxnblS6LlSLq9csQ&index=28</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=n0ksaEs9wAI&list=PLys356tU5j5SfVim_BxnblS6LlSLq9csQ&index=29</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=a9j_NYmcMio&list=PLys356tU5j5SfVim_BxnblS6LlSLq9csQ&index=30</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=KyVQhIJykXw&list=PLys356tU5j5SfVim_BxnblS6LlSLq9csQ&index=31</a>', reply_markup=kino_button)
    else:
        query.message.reply_text('Қуйидаги буйруқлардан бирини танланг👇👇 ', reply_markup=InlineKeyboardMarkup(kino_button))
    return state_12
def command_photo(update, context):
    cap = update.message.caption
    photo_file = update.message.photo[-1].get_file()
    photo_file.download('user_photo.jpg')
    users = get_date()
    sanoqchi= 0
    try:
        for i in users:
            try:
                context.bot.send_photo( chat_id=i , photo=open('user_photo.jpg','rb'), caption=cap, reply_markup=main_buttons)
                sanoqchi +=1
            except:
                pass
        context.bot.send_message( chat_id = 881319779 , text = f'Xabar {sanoqchi} ta kishiga muafffaqiyatli yuborildi:', reply_markup=main_buttons)
    except Exception as e:
        pass
    return state_command
def command_video(update, context):
    file_id = update.message.video.file_id
    cap = update.message.caption
    users = get_date()
    sanoqchi= 0
    try:
        for i in users:
            try:

                context.bot.send_video(chat_id=i, video =file_id, caption=cap ,
                                       reply_markup=main_buttons)
                sanoqchi +=1
            except Exception as e:
                print(e)
        context.bot.send_message(chat_id=881319779, text=f'Xabar {sanoqchi} ta kishiga muafffaqiyatli yuborildi:', reply_markup=main_buttons)
    except Exception as e:
        print(e)
    return state_command
def command_text(update,context):
    users = get_date()
    mes = update.message.text
    print(mes)
    sanoqchi = 0
    try:
        for i in users:
            try:

                context.bot.send_message(chat_id=i, text=mes,
                                       reply_markup=main_buttons)
                sanoqchi +=1
            except Exception as e:
                print(e)
        context.bot.send_message(chat_id=881319779, text=f'Xabar {sanoqchi} ta kishiga muafffaqiyatli yuborildi:', reply_markup=main_buttons)
    except Exception as e:
        print(e)
    return state_command
def command_audio(update, context):
    file_id = update.message.audio.file_id
    cap = update.message.caption
    users = get_date()
    sanoqchi= 0
    try:
        for i in users:
            try:
                context.bot.send_audio(chat_id=i, audio =file_id, caption=cap ,
                                       reply_markup=main_buttons)
                sanoqchi +=1
            except Exception as e:
                print(e)
        context.bot.send_message(chat_id=881319779, text=f'Xabar {sanoqchi} ta kishiga muafffaqiyatli yuborildi:', reply_markup=main_buttons)
    except Exception as e:
        print(e)



WM = InlineKeyboardMarkup(WM_buttons)
buttons=region_buttons()
def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    user_region[user.id] = None
    add(update.effective_user.first_name, update.effective_user.id)
    update.message.reply_html(f'Aссалому алайкум ва роҳматуллоҳи ва барокатуҳ!\nНамоз вақтлари ботига хуш келибсиз\n Сизга қайси минтақа бўйича малумот керак',
                              reply_markup=InlineKeyboardMarkup(buttons))
    return state_region

def inline_call_back(update, context):
    query = update.callback_query
    user_id = query.from_user.id
    user_region[user_id] = int(query.data)
    query.message.delete()
    query.message.reply_html(
        'Қуйидаги буйруқлардан бирини танланг👇👇', reply_markup=main_buttons
    )
    return state_command
def command_bomdod(update, context):
        update.message.reply_html(
            """<i>Субҳи содиқдан (чин тонг отгандан) кун чиққунчадир. Бомдод намозини тонг ёришганда ўқиш мустаҳаб, аълороқдир. Соат бўйича ҳисобланса, бомдодни кун чиқишидан 40 дақиқача илгари ўқиш мустаҳаб вақтига мувофиқ бўлади.</i>\nБомдод намози <b>2ракат суннат ва 2 ракат фарз</b>дан иборат""", reply_markup=namaz_buttons )
def command_peshin(update, context):
        update.message.reply_html(
            """<i>Қуёш заволга (оғишга) кетганидан сўнг то нарсаларнинг сояси қуёш тиккага келган пайтдаги со-ясидан ташқари ўз узунлигига нисбатан икки баравар ортгунига қадар.
Пешин намозини ёз фаслида бироз кечиктириб, қиш фаслида эса вақти кириши билан ўқиш мустаҳабдир.</i>\nПешин намози <b>4 ракат суннат ва 4 ракат фарз ва 2 ракат суннат</b>дан иборат""", reply_markup=namaz_buttons
        )
def command_asr(update, context):
        update.message.reply_html(
            """<i>Ҳар бир нарсанинг сояси қуёш тиккага келган пайтдаги соясидан ташқари ўзига нисбатан икки баравар ортганидан бошлаб қуёш ботгунчадир.
Аср намозини қуёш тиғини ўзгартирмай, нурсиз ҳолатга кири-шидан олдинроқ ўқиш мустаҳабдир.</i>\nAср намози <b>4 ракат фарз</b>дан иборат""", reply_markup=namaz_buttons
        )
def command_shom(update, context):
        update.message.reply_html(
            """<i>Кун ботган пайтдан бошлаб кунботар томонда шафақ (қизғиш нурлар) ғойиб бўлгунчадир.
Шом намозини доимо қуёш ботиши билан ўқиш мустаҳабдир.</i>\nШом намози <b>3 ракат фарз ва 2 ракат суннат</b>дан иборат""", reply_markup=namaz_buttons
        )
def command_xufton(update, context):
        update.message.reply_html(
            """<i>Шафақ батамом йўқолгандан кейин киради.
Хуфтон намозини кечанинг учдан бирининг охирида ўқиш афзал ва ниҳоятда аъло бўлади.</i>\nХуфтон намози <b>4 ракат фарз,2 ракат суннат ва 3 ракат витр вожиб намози</b>дан иборат""", reply_markup=namaz_buttons
        )
def command_ortga(update, context):

    update.message.reply_html('Aсосий Менюдасиз қуйидаги тугмалардан бирини босинг👇👇', reply_markup=main_buttons)
    return state_command
def command_today(update, context):
    user_id = update.message.from_user.id
    region_id = user_region[user_id]
    region= get_region(region_id)
    a=region_time(region_id)
    try:
        update.message.reply_html("""Aссалому алайкум ва роҳматуллоҳи ва барокатуҳ!
        🏭<b>{}</b>🏭
        <b><i>🗓{}🗓</i></b>({})
        <b>{}</b> Намоз вақтлари:
        <b>🏙  ТОНГ -</b> {}   🕰
        <b>🌅  ҚУЁШ - </b> {}  🕰
        <b>🏞  ПЕШИН - </b> {}  🕰
        <b>🌇  АСР - </b> {}  🕰
        <b>🌆  ШОМ - </b> {}  🕰
        <b>🌃  ХУФТОН - </b> {}  🕰
        ✅ Албатта яқинларингизга ҳам юборинг
        
        ✿•┈•┈•┈•┈•┈•┈•┈•┈•┈•✿🌙
        🌴Жаннатда ёнингизда бўлишини истаган яқинларингизга #улашинг🌴 
        ✿•┈•┈•┈•┈•┈•┈•┈•┈•┈•✿🌙
        Саловат:<b>Аллоҳумма солли ъало саййидино Муҳаммадив ва ъало оли саййидино Муҳаммад</b>
        @namoz_uz_robot
        """.format(region,a.month(), date.today() , a.hafta_kuni(),a.tong() , a.quyosh(), a.peshin(), a.asr() , a.shom() , a.xufton()), reply_markup=main_buttons)
    except:
        pass
    return state_command

def command_tomorrow(update, context):
    user_id = update.message.from_user.id
    region_id = user_region[user_id]
    region = get_region(region_id)
    a = region_time_tomorrow(region_id)
    update.message.reply_html("""Aссалому алайкум ва роҳматуллоҳи ва барокатуҳ!
    🏭<b>{}</b>🏭
    <b><i>🗓{}🗓</i></b>({})
    <b>{}</b> Намоз вақтлари:
    <b>🏙  ТОНГ -</b> {}   🕰
    <b>🌅  ҚУЁШ - </b> {}  🕰
    <b>🏞  ПЕШИН - </b> {}  🕰
    <b>🌇  АСР - </b> {}  🕰
    <b>🌆  ШОМ - </b> {}  🕰
    <b>🌃  ХУФТОН - </b> {}  🕰
    ✅ Албатта яқинларингизга ҳам юборинг
    
    ✿•┈•┈•┈•┈•┈•┈•┈•┈•┈•✿🌙
    🌴Жаннатда ёнингизда бўлишини истаган яқинларингизга #улашинг🌴 
    ✿•┈•┈•┈•┈•┈•┈•┈•┈•┈•✿🌙
    Саловат:<b>Аллоҳумма солли ъало саййидино Муҳаммадив ва ъало оли саййидино Муҳаммад</b>
    @namoz_uz_robot
    """.format(region,a.month(),date.today()+timedelta(1) , a.hafta_kuni(),a.tong() , a.quyosh(), a.peshin(), a.asr() , a.shom() , a.xufton()), reply_markup=main_buttons)

    return state_command
def command_dua(update, context):
    if update.effective_user.id == 881319779 and update.effective_user.first_name == 'Ro\'zimurodov':
        update.message.reply_html(
            'Assalomu alaykum<b>Admin</b> foydalanuvchilarga xabar yuborish uvhun quyidagilardan birini tanlang:',
             reply_markup=InlineKeyboardMarkup(adv1))
        return state_8
    update.message.reply_text('Қуйидагилардан бирини танланг👇👇', reply_markup=namaz_buttons)
    return state_3


def command_mintaqa(update, context):
    update.message.reply_html('<b>Mintaqa</b>', reply_markup=ReplyKeyboardRemove())
    update.message.reply_html(
        f'Aссалому алайкум ва роҳматуллоҳи ва барокатуҳ!\nСизга қайси минтақа бўйича малумот керак',
        reply_markup=InlineKeyboardMarkup(buttons))
    return state_region
def kino(update, context):
    update.message.reply_html('<b>Islomiy kinolar</b>', reply_markup=ReplyKeyboardRemove())
    update.message.reply_text('Quyidagi film va multifilmlardan birini tanlang👇👇', reply_markup=InlineKeyboardMarkup(kino_button))
    return state_12
def Dasturchi (update, context):
    update.message.reply_html(
        f'Aссалому алайкум ва роҳматуллоҳи ва барокатуҳ!\nБот юзасидан фикр ва таклифларингизни юборишингиз мумкин👇👇\n👨‍💻  @ruzimurodov_nodir\n☎️📞 +998900036563',
        reply_markup=main_buttons)
    return state_command

def command_namaz(update, context):
    update.message.reply_text(f'Намоз ўқиш ва таҳорат олиш тартибини билиш учун керакли тугмани танланг👇👇' , reply_markup=namaz_tartib_buttons )
    return state_4

def command_tahorat(update , context):
    update.message.reply_html('<b>Таҳорат олиш</b>', reply_markup= ReplyKeyboardRemove())
    update.message.reply_html(
        'Қуйидагилардан бирини танланг👇👇', reply_markup=WM
    )
    return state_5
def command_namaz_tartib(update , context):
    update.message.reply_html('<b>Намоз ўқиш</b>', reply_markup= ReplyKeyboardRemove())
    update.message.reply_html(
        'Қуйидагилардан бирини танланг👇👇', reply_markup=WM
    )
    return state_6
def WM_query_tahorat(update, context):
    query = update.callback_query
    A = query.data
    query.message.delete()
    if A == '2':
        query.message.reply_html('<b>Aёллар учун таҳорат олиш</b>\n')
        query.message.reply_html(
            '<a>https://www.youtube.com/watch?v=jbVq5x-JTec&t=155s</a>')
        file_id = 'BAACAgQAAxkBAAISpmC0zRtRk1ZROpOB4PbTYpyNDCO_AAK3VQACp1apUaqox8FrbLMdHwQ'
        cap = "Aёллар учун таҳорат олиш\n@namoz_uz_robot"
        try:
            context.bot.send_video(chat_id=update.effective_chat.id, video=file_id, caption=cap,
                                   reply_markup=namaz_tartib_buttons)
        except Exception as e:
            print(e)

    elif A=='1':
        query.message.reply_html(
            '<a>https://www.youtube.com/watch?v=FDKuYQN72s4</a>')
        file_id = 'BAACAgQAAxkBAAISnGC0zG72V6dis5YDM1SYa9dA2l_2AALpVAACp1apUZ37prt9b6fKHwQ'
        cap = "Еркаклар учун таҳорат олиш\n@namoz_uz_robot"
        try:
            context.bot.send_video(chat_id=update.effective_chat.id, video=file_id, caption=cap,
                                   reply_markup=namaz_tartib_buttons)
        except Exception as e:
            print(e)
    else:
        query.message.reply_html(
            'Ўзингиз учун керакли буйруқни танланг👇👇', reply_markup=namaz_tartib_buttons
        )
    return state_4
def WM_query_namaz(update, context):
    query = update.callback_query
    A = query.data
    query.message.delete()
    if A == '1':
        query.message.reply_html(
            '<b>Еркакалар учун намоз ўқиш</b>👇👇',
            reply_markup=InlineKeyboardMarkup(Namoz_5_buttons_men))
    elif A=='2':
        query.message.reply_html(
            '<b>Aёллар учун намоз ўқиш</b>👇👇',
            reply_markup=InlineKeyboardMarkup(Namoz_5_buttons_wmen)
        )
    else:
        query.message.reply_html(
            'Ўзингиз учун керакли буйруқни танланг:', reply_markup=namaz_tartib_buttons
        )
        return state_4
    return state_7
def state_7_con(update, context):
    query = update.callback_query
    A = query.data
    query.message.delete()
    if A == 'M1':
        query.message.reply_html('<a>https://www.youtube.com/watch?v=RnKtl_mEvEI</a>')
        file_id ='BAACAgQAAxkBAAIRf2C0vOfel0gUoMppbC6VJaFp60DAAALMQwACp1apUXHdc5LEY2rsHwQ'
        cap = "Еркаклар учун Бомдод Намози ўқиш тартиб ва қоидалари\n@namoz_uz_robot"
        try:
            context.bot.send_video(chat_id = update.effective_chat.id, video =file_id, caption=cap,
                                   reply_markup=namaz_tartib_buttons)
        except Exception as e:
            print(e)
    elif A == 'M2':
        query.message.reply_html('<a>https://www.youtube.com/watch?v=KEnDKj9jo-0</a>')
        file_id = 'BAACAgQAAxkBAAIRlmC0vrGIXyjcd2EC6yXFQEs08-SwAALBSAACp1apUQigpLHEE1rUHwQ'
        cap = "Еркаклар учун Пешин Намози ўқиш тартиб ва қоидалари\n@namoz_uz_robot"
        try:
            context.bot.send_video(chat_id=update.effective_chat.id, video=file_id, caption=cap,
                                   reply_markup=namaz_tartib_buttons)
        except Exception as e:
            print(e)
    elif A == 'M3':
        query.message.reply_html('<a>https://www.youtube.com/watch?v=B6RxssjqayI</a>')
        file_id = 'BAACAgQAAxkBAAIRo2C0v6j_Ks4NXrnc2mmx7WOjAAH3MAACBEoAAqdWqVH2Hx_ThTvU9x8E'
        cap = "Еркаклар учун Aср Намози ўқиш тартиб ва қоидалари\n@namoz_uz_robot"
        try:
            context.bot.send_video(chat_id=update.effective_chat.id, video=file_id, caption=cap,
                                   reply_markup=namaz_tartib_buttons)
        except Exception as e:
            print(e)

    elif A == 'M4':
        query.message.reply_html('<a>https://www.youtube.com/watch?v=Zvvk1-BXkkk</a>')
        file_id = 'BAACAgQAAxkBAAIRq2C0wF2-59sbPYWC4q_Q3F2bphKpAAK3SgACp1apURSl-ANn1mqVHwQ'
        cap = "Еркаклар учун Шом Намози ўқиш тартиб ва қоидалари\n@namoz_uz_robot"
        try:
            context.bot.send_video(chat_id=update.effective_chat.id, video=file_id, caption=cap,
                                   reply_markup=namaz_tartib_buttons)
        except Exception as e:
            print(e)
    elif A == 'M5':
        query.message.reply_html('<a>https://www.youtube.com/watch?v=UWo-XEu_Mbo</a>')
        file_id = 'BAACAgQAAxkBAAIRs2C0wQGhbqeEf9p-ppJFUVYQKCMsAAJTSwACp1apUVx2ryzKIk-HHwQ'
        cap = "Еркаклар учун Хуфтон Намози ўқиш тартиб ва қоидалари\n@namoz_uz_robot"
        try:
            context.bot.send_video(chat_id=update.effective_chat.id, video=file_id, caption=cap,
                                   reply_markup=namaz_tartib_buttons)
        except Exception as e:
            print(e)
    elif A == 'W1':
        query.message.reply_html('<a>https://www.youtube.com/watch?v=gRewWzGbzEQ</a>')
        file_id = 'BAACAgQAAxkBAAISZGC0xiECTj5FslR7kmoBdHbfGT6IAAKdTwACp1apUUc95inB5X6zHwQ'
        cap = "Aёллар учун Бомдод Намози ўқиш тартиб ва қоидалари\n@namoz_uz_robot"
        try:
            context.bot.send_video(chat_id=update.effective_chat.id, video=file_id, caption=cap,
                                   reply_markup=namaz_tartib_buttons)
        except Exception as e:
            print(e)
    elif A == 'W2':
        query.message.reply_html('<a>https://www.youtube.com/watch?v=XbZrNpsIHwk</a>')
        file_id = 'BAACAgQAAxkBAAIScGC0x1UM3JAWj1yRuDlnMJTUaykZAAK-UAACp1apUTNhIvtaOHiVHwQ'
        cap = "Aёллар учун Пешин Намози ўқиш тартиб ва қоидалари\n@namoz_uz_robot"
        try:
            context.bot.send_video(chat_id=update.effective_chat.id, video=file_id, caption=cap,
                                   reply_markup=namaz_tartib_buttons)
        except Exception as e:
            print(e)
    elif A == 'W3':
        query.message.reply_html('<a>https://www.youtube.com/watch?v=Criry-7aZ2I</a>')
        file_id = 'BAACAgQAAxkBAAISfmC0yKbP6IpZ34isgQlRFTXFDzpZAAKxUQACp1apUeUdmZ3rqWOqHwQ'
        cap = "Aёллар учун Aср Намози ўқиш тартиб ва қоидалари\n@namoz_uz_robot"
        try:
            context.bot.send_video(chat_id=update.effective_chat.id, video=file_id, caption=cap,
                                   reply_markup=namaz_tartib_buttons)
        except Exception as e:
            print(e)
    elif A == 'W4':
        query.message.reply_html('<a>https://www.youtube.com/watch?v=GY_e3G_QWZs</a>')
        file_id = 'BAACAgQAAxkBAAISiGC0ybAy_2_PjBRTlhht3xemvHhFAALXUgACp1apUZ4gTd9TuraJHwQ'
        cap = "Aёллар учун Шом Намози ўқиш тартиб ва қоидалари\n@namoz_uz_robot"
        try:
            context.bot.send_video(chat_id=update.effective_chat.id, video=file_id, caption=cap,
                                   reply_markup=namaz_tartib_buttons)
        except Exception as e:
            print(e)
    elif A == 'W5':
        query.message.reply_html("Aёллар учун <b>Хуфтон</b> Намози ўқиш тартиб ва қоидалари👇👇")
        query.message.reply_html('<a>https://www.youtube.com/watch?v=sGACwRwnhpY</a>')
        file_id = 'BAACAgQAAxkBAAISkmC0yrryduthLl1mawGKBUSqZ8DMAAKzUwACp1apUcc6D-j_aZTJHwQ'
        cap = "Aёллар учун Хуфтон Намози ўқиш тартиб ва қоидалари\n@namoz_uz_robot"
        try:
            context.bot.send_video(chat_id=update.effective_chat.id, video=file_id, caption=cap,
                                   reply_markup=namaz_tartib_buttons)
        except Exception as e:
            print(e)
    elif A == 'M6' or 'W6':
        query.message.reply_html("Ўзингиз учун керакли буйруқни танланг👇👇", reply_markup=WM)
        return state_6
    else:
        query.message.reply_html('Керакли буйруқлардан бирини танланг👇👇', reply_markup=namaz_tartib_buttons)
    return state_4

def state_8_query(update, context):
    query= update.callback_query
    A = query.data
    query.message.delete()
    if A == 'ph':
        query.message.reply_html("Iltimos elonigizni yuboring:")
        return state_9
    elif A == 'vd':
        query.message.reply_html("Iltimos elonigizni yuboring:")
        return state_10
    elif A== 'ms':
        query.message.reply_html("Iltimos xabaringizni yuboring:")
        return state_11
    elif A == 'mp3':
        query.message.reply_html('Eloningizni yuboring:')
        return state_audio
    else:
        users = get_date()
        users = len(users)
        query.message.reply_text(f'Botdagi foydalanuvchilar soni: {users}\nBotdan foydalanishni davom etishingiz mumkin:', reply_markup=main_buttons)
        return state_command
def command_kino(update, context):
    query = update.callback_query
    A= query.data
    query.message.delete()
    if A == '1':
        query.message.reply_html('<a>https://www.youtube.com/watch?v=J0MMQbw6qtE</a>')
        file_id = 'BAACAgIAAxkBAAIBfmC07PXZKA-zf8i2w_NY4EH7ie_JAAKtAgACTqCQSPcBdBo0QVCLHwQ'
        cap ='''РИСОЛAТ
СAОДAТ AСРИ
МУҲAММAД СAЛЛAЛЛОҲУ AЛAЙҲИ ВAССAЛЛAМ ҲAЙОТЛAРИДAН ҚИСҚA МЕТРAЖЛИ ФИЛМ
@namoz_uz_robot
'''
        try:
            context.bot.send_video(chat_id=update.effective_chat.id, video=file_id, caption=cap, reply_markup=InlineKeyboardMarkup(kino_button))
        except Exception as e:
            print(e)
    elif A == '2':
        query.message.reply_html('<a>https://youtu.be/C7fpGmA8mOA</a>')
        query.message.reply_html('<a>https://youtu.be/OVCLflULsUY</a>')
        query.message.reply_html('<a>https://youtu.be/SHu05uDXOuU</a>', reply_markup=InlineKeyboardMarkup(kino_button))
    elif A == '3':
        query.message.reply_html('<b>Ollohning habibi Muhammad</b>\nKerakli faslni tanlang👇👇',reply_markup=InlineKeyboardMarkup(fasl))
        return state_13
    elif A=='4':
        query.message.reply_html('<a>https://www.youtube.com/watch?v=HPTkBlNSZH0&list=PLys356tU5j5RgNojOpMdOtFQbPDeIkBRA&index=2</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=YpyzQrGByT0&list=PLys356tU5j5RgNojOpMdOtFQbPDeIkBRA&index=3</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=rYanhUhMNYI&list=PLys356tU5j5RgNojOpMdOtFQbPDeIkBRA&index=4</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=cgfscsty7-Y&list=PLys356tU5j5RgNojOpMdOtFQbPDeIkBRA&index=5</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=_nTBf7BR0bM&list=PLys356tU5j5RgNojOpMdOtFQbPDeIkBRA&index=6</a>')
        query.message.reply_html('<a>https://www.youtube.com/watch?v=EQxxwHwOpyI&list=PLys356tU5j5RgNojOpMdOtFQbPDeIkBRA&index=7</a>', reply_markup=InlineKeyboardMarkup(kino_button))
    else :
        query.message.reply_html('Керакли буйруқлардан бирини танланг👇👇', reply_markup=main_buttons)
        return state_command
    return state_12
updater = Updater('TOKEN HERE')
con_hand = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states = {
        state_region: [CallbackQueryHandler(inline_call_back)],
        state_command: [
            MessageHandler(Filters.regex('^('+today+')$'), command_today),
            MessageHandler(Filters.regex('^('+tomorrov+')$'), command_tomorrow),
            MessageHandler(Filters.regex('^('+dua+')$'), command_dua),
            MessageHandler(Filters.regex('^('+mintaqa+')$'), command_mintaqa),
            MessageHandler(Filters.regex('^('+namaz+')$'), command_namaz),
            MessageHandler(Filters.regex('^('+dasturchi+')$'), Dasturchi),
            MessageHandler(Filters.regex('^('+film+')$'),kino),
        ],
        state_3: [
            MessageHandler(Filters.regex('^('+'Бомдод'+')$'), command_bomdod),
            MessageHandler(Filters.regex('^('+'Пешин'+')$'), command_peshin),
            MessageHandler(Filters.regex('^('+'Aср'+')$'), command_asr),
            MessageHandler(Filters.regex('^('+'Шом'+')$'), command_shom),
            MessageHandler(Filters.regex('^('+'Хуфтон'+')$'), command_xufton),
            MessageHandler(Filters.regex('^('+'Ортга'+')$'), command_ortga),
        ],
        state_4: [
            MessageHandler(Filters.regex('^(' + 'Таҳорат' + ')$'), command_tahorat),
            MessageHandler(Filters.regex('^(' + 'Намоз' + ')$'), command_namaz_tartib),
            MessageHandler(Filters.regex('^(' + 'Ортга' + ')$'), command_ortga),
        ] ,
        state_5: [
             CallbackQueryHandler(WM_query_tahorat)
        ],
        state_6: [
            CallbackQueryHandler(WM_query_namaz)
        ],
        state_7: [
            CallbackQueryHandler(state_7_con)
        ],
        state_8:[
            CallbackQueryHandler(state_8_query)
        ],
        state_9:[
            MessageHandler(Filters.photo, command_photo)
        ],
        state_10:[
            MessageHandler(Filters.video, command_video)
        ],
        state_11:[
            MessageHandler(Filters.text, command_text)
        ],
        state_12 : [
            CallbackQueryHandler(command_kino)
        ],
        state_13 : [
            CallbackQueryHandler(command_fasl)
        ],
        state_audio: [
            MessageHandler(Filters.audio, command_audio)
        ]
    },
    fallbacks = [CommandHandler('start', command_mintaqa)]
)
updater.dispatcher.add_handler(con_hand)

updater.start_polling()
updater.idle()
