from telegram import InlineKeyboardMarkup, InlineKeyboardButton

keyboards = {
    'ru': {
        'start': InlineKeyboardMarkup([
            [InlineKeyboardButton('👨‍🏫 Стать ментором', callback_data=str('become_a_mentee'))],
            [InlineKeyboardButton('🔍 Найти ментора', callback_data=str('find_a_mentee'))],
            [InlineKeyboardButton('ℹ️ О нас', callback_data=str('about'))]
        ]),
        'about': InlineKeyboardMarkup([
            [InlineKeyboardButton('🔙 Назад', callback_data=str('about_back'))],
        ])
    },
    'en': {
        'start': InlineKeyboardMarkup([
            [InlineKeyboardButton('👨‍🏫 Become a mentee', callback_data=str('become_a_mentee'))],
            [InlineKeyboardButton('🔍 Find me a mentee', callback_data=str('find_a_mentee'))],
            [InlineKeyboardButton('ℹ️ About us', callback_data=str('about'))]
        ]),
        'about': InlineKeyboardMarkup([
            [InlineKeyboardButton('🔙 Back', callback_data=str('about_back'))],
        ])
    }
}
