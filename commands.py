from bot_config import dp, bot
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.dispatcher.filters import Text
from random import randint

b1 = KeyboardButton('/start')
b2 = KeyboardButton('/go')
rk_client = ReplyKeyboardMarkup(resize_keyboard=True)
rk_client.add(b1,b2)
counter = 0
win = False
board_dict = dict()
disp = []
counter = 1

def check_win(board_win):
    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for each in win_coord:
        if board_win[each[0]] == board_win[each[1]] == board_win[each[2]] and board_win[each[0]] in ['❌', '⭕']:
            print(board_win[each[0]], board_win[each[1]], board_win[each[2]])
            return True
    return False

@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    print(message)
    await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}'
                                                    f', ты написал мне "{message.text}", поиграем в крестики-нолики?'
                                                      f'Напиши команду "/go", если готов начать играть.',
                           reply_markup=rk_client)
    await bot.send_message(658776791, text=f'{message.from_user.first_name}'
                                                    f', ты написал мне "{message.text}"')

@dp.message_handler(commands=['go'])
async def start_bot(message: types.Message):
    global disp, board_dict, counter, win
    counter = 0
    print(message)
    disp = []
    win = False
    board_dict = dict()
    for i in range(0, 9):
        disp.append(' ')
    markup_inline = types.InlineKeyboardMarkup()
    item11 = types.InlineKeyboardButton(text=disp[0], callback_data='like_0')
    item12 = types.InlineKeyboardButton(text=disp[1], callback_data='like_1')
    item13 = types.InlineKeyboardButton(text=disp[2], callback_data='like_2')
    item21 = types.InlineKeyboardButton(text=disp[3], callback_data='like_3')
    item22 = types.InlineKeyboardButton(text=disp[4], callback_data='like_4')
    item23 = types.InlineKeyboardButton(text=disp[5], callback_data='like_5')
    item31 = types.InlineKeyboardButton(text=disp[6], callback_data='like_6')
    item32 = types.InlineKeyboardButton(text=disp[7], callback_data='like_7')
    item33 = types.InlineKeyboardButton(text=disp[8], callback_data='like_8')
    markup_inline.add(item11, item12, item13).add(item21, item22, item23).add(item31, item32, item33)
    await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}'
                                                      f', первый ход твой!', reply_markup=markup_inline)
    # # # # жеребьёвка # # # #
    # global player_action
    # possible_actions = ['компьютер', 'человек']
    # player_action = random.choice(possible_actions)
    # if player_action == 'компьютер':
    #     await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}'
    #                                                       f', первый ход определяется жеребьёвкой, хожу я!',
    #                            reply_markup = markup_inline)
    # else:
    #     await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}'
    #                                                       f', первый ход твой!',
    #                            reply_markup = markup_inline)

@dp.callback_query_handler(Text(startswith='like_'))
async def www_call(call: types.CallbackQuery):
    global board_dict, disp, counter, win
    res = int(call.data.split('_')[1])
    if res not in board_dict and win == False:
        board_dict[res] = '❌'
        for i in range(0, 9):
            if i in board_dict.keys():
                disp[i] = board_dict[i]
        win = check_win(disp)
        if win != False:
            # await call.message.delete()
            markup_inline = types.InlineKeyboardMarkup()
            item11 = types.InlineKeyboardButton(text=disp[0], callback_data='like_0')
            item12 = types.InlineKeyboardButton(text=disp[1], callback_data='like_1')
            item13 = types.InlineKeyboardButton(text=disp[2], callback_data='like_2')
            item21 = types.InlineKeyboardButton(text=disp[3], callback_data='like_3')
            item22 = types.InlineKeyboardButton(text=disp[4], callback_data='like_4')
            item23 = types.InlineKeyboardButton(text=disp[5], callback_data='like_5')
            item31 = types.InlineKeyboardButton(text=disp[6], callback_data='like_6')
            item32 = types.InlineKeyboardButton(text=disp[7], callback_data='like_7')
            item33 = types.InlineKeyboardButton(text=disp[8], callback_data='like_8')
            markup_inline.add(item11, item12, item13).add(item21, item22, item23).add(item31, item32, item33)
            await bot.send_message(call.from_user.id, text=f'{call.from_user.first_name}'
                                                              f', ты выиграл!!!',
                                   reply_markup=markup_inline)
            counter = 8
            await call.message.delete()
        counter += 1
        #await bot.send_message(658776791, text=f'counter после хода человека ={counter}')
        if win == False and counter < 9:
            res_bot = True
            while res_bot != False: # Выполняю, пока не найду пустую клетку
                i = randint(0, 8)
                if i not in board_dict: # Если не занята клетка, то ставим 0
                    board_dict[i] = '⭕'
                    disp[i] = board_dict[i]
                    await call.message.delete()
                    markup_inline = types.InlineKeyboardMarkup()
                    item11 = types.InlineKeyboardButton(text=disp[0], callback_data='like_0')
                    item12 = types.InlineKeyboardButton(text=disp[1], callback_data='like_1')
                    item13 = types.InlineKeyboardButton(text=disp[2], callback_data='like_2')
                    item21 = types.InlineKeyboardButton(text=disp[3], callback_data='like_3')
                    item22 = types.InlineKeyboardButton(text=disp[4], callback_data='like_4')
                    item23 = types.InlineKeyboardButton(text=disp[5], callback_data='like_5')
                    item31 = types.InlineKeyboardButton(text=disp[6], callback_data='like_6')
                    item32 = types.InlineKeyboardButton(text=disp[7], callback_data='like_7')
                    item33 = types.InlineKeyboardButton(text=disp[8], callback_data='like_8')
                    markup_inline.add(item11, item12, item13).add(item21, item22, item23).add(item31, item32, item33)
                    if counter < 4:
                        await bot.send_message(call.from_user.id, text=f'{call.from_user.first_name}'
                                                                       f', я пошел, твой ход: ❌',
                                               reply_markup=markup_inline)
                        counter += 1
                        await call.answer()
                        res_bot = False
                    elif counter > 3:
                        win = check_win(disp)
                        if win != False:
                            await bot.send_message(call.from_user.id, text=f'{call.from_user.first_name}'
                                                                           f', ну все! Выиграл я!',
                                                   reply_markup=markup_inline)
                            win = True
                            await call.answer()
                            counter = 9
                            res_bot = False
                        else:
                            await bot.send_message(call.from_user.id, text=f'{call.from_user.first_name}'
                                                                           f', я пошел, твой ход: ❌',
                                                   reply_markup=markup_inline)
                            counter += 1
                            await call.answer()
                            res_bot = False
                    elif counter == 7:
                        await bot.send_message(call.from_user.id, text=f'{call.from_user.first_name}'
                                                                       f', ничья!',
                                               reply_markup=markup_inline)
                        counter += 1
                        await call.answer()
                        res_bot = False
                    else:
                        await call.answer('Что-то не так')
                        res_bot = True
                else:
                    res_bot = True
        elif  win != True and counter == 9:
            markup_inline = types.InlineKeyboardMarkup()
            item11 = types.InlineKeyboardButton(text=disp[0], callback_data='like_0')
            item12 = types.InlineKeyboardButton(text=disp[1], callback_data='like_1')
            item13 = types.InlineKeyboardButton(text=disp[2], callback_data='like_2')
            item21 = types.InlineKeyboardButton(text=disp[3], callback_data='like_3')
            item22 = types.InlineKeyboardButton(text=disp[4], callback_data='like_4')
            item23 = types.InlineKeyboardButton(text=disp[5], callback_data='like_5')
            item31 = types.InlineKeyboardButton(text=disp[6], callback_data='like_6')
            item32 = types.InlineKeyboardButton(text=disp[7], callback_data='like_7')
            item33 = types.InlineKeyboardButton(text=disp[8], callback_data='like_8')
            markup_inline.add(item11, item12, item13).add(item21, item22, item23).add(item31, item32, item33)
            await bot.send_message(call.from_user.id, text=f'{call.from_user.first_name}'
                                                       f', ничья!',
                                               reply_markup=markup_inline)
            await call.answer()
        else:
            await call.answer('Что-то не так')
    elif res not in board_dict and win == True or counter == 9:
        await call.answer(f'Если хочешь поигать, нажми "go"!')
    else:
        await call.answer(f'Клетка занята!')
