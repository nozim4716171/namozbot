from telegram import ReplyKeyboardMarkup , InlineKeyboardButton
today = '⌛️Бугун'
tomorrov = '⌛️Эртага'
dua = '🤲Ўқиладиган Дуолар'
mintaqa = '🇺🇿Минтақа'
namaz = 'Намоз ўқиш тартиби'
dasturchi = '💬 Фикр билдириш 📝'
film = '🕋Islomiy filmlar'

main_buttons =ReplyKeyboardMarkup( [
    [
         today
    ],
    [
        tomorrov,
        dua
    ],
    [
        mintaqa,
        namaz
    ],
    [
        film
    ],
    [
        dasturchi
    ]
], resize_keyboard=True)

namaz_buttons = ReplyKeyboardMarkup([
        [
         'Бомдод',
         'Пешин'
        ],
        [
        "Aср",
        "Шом",
         ],
        [
            "Хуфтон"
        ],
       [
       'Ортга'
       ]
    ], resize_keyboard=True)

Namoz_5_buttons_men = [
    [
        InlineKeyboardButton('Бомдод', callback_data='M1'),
        InlineKeyboardButton('Пешин', callback_data='M2')
    ],
    [
        InlineKeyboardButton('Aср', callback_data='M3'),
        InlineKeyboardButton('Шом', callback_data='M4')
    ],
    [
        InlineKeyboardButton('Хуфтон', callback_data='M5'),
        InlineKeyboardButton('Ортга', callback_data='M6')
    ]
]

Namoz_5_buttons_wmen = [
    [
        InlineKeyboardButton('Бомдод', callback_data='W1'),
        InlineKeyboardButton('Пешин', callback_data='W2')
    ],
    [
        InlineKeyboardButton('Aср', callback_data='W3'),
        InlineKeyboardButton('Шом', callback_data='W4')
    ],
    [
        InlineKeyboardButton('Хуфтон', callback_data='W5'),
        InlineKeyboardButton('Ортга', callback_data='W6')
    ]
]
namaz_tartib_buttons = ReplyKeyboardMarkup(
    [
        [
            'Таҳорат'
        ],
        [
            'Намоз'
        ],
        [
            'Ортга'
        ]
    ],
    resize_keyboard=True
)
WM_buttons = [
    [
        InlineKeyboardButton('Еркаклар учун', callback_data= '1')
    ] ,
    [
        InlineKeyboardButton('Aёллар учун' , callback_data= '2')
    ],
    [
        InlineKeyboardButton('Ортга', callback_data= '3')
    ]
]

adv1 = [
       [
           InlineKeyboardButton('Photo', callback_data='ph')
       ],
    [
        InlineKeyboardButton('Video', callback_data='vd')
    ],
    [
        InlineKeyboardButton('message', callback_data='ms')
    ],
    [
       InlineKeyboardButton('Audio', callback_data='mp3')
    ],
    [
        InlineKeyboardButton('Main', callback_data='0')
    ]
]
kino_button = [
    [
        InlineKeyboardButton('Рисолат Ислом тарихи', callback_data='1')
    ],
    [
        InlineKeyboardButton('Дунёнинг яратилиши Пайғамбарлар қиссаси',callback_data= '2' )
    ],
    [
        InlineKeyboardButton('Аллоҳнинг Ҳабиби Муҳаммад', callback_data='3')
    ],
    [
        InlineKeyboardButton('Қуръонда зикри келган ажойиботлар', callback_data= '4')
    ],
    [
        InlineKeyboardButton('Ортга', callback_data= '5')
    ]
]

fasl = [
    [
        InlineKeyboardButton('1-fasl', callback_data= '1')
    ],
    [
       InlineKeyboardButton('2-fasl', callback_data= '2')
    ],
    [
        InlineKeyboardButton('3-fasl', callback_data='3')
    ],
    [
        InlineKeyboardButton('Ortga', callback_data= '4')
    ]
]
