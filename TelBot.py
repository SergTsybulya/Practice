# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# import sqlite3
# import numpy as np
#
#
# updater = Updater(token='628013145:AAFbLjHNJ-LeHEDKe8d0Vbe8Yqi4D-k9tZg')
# dispatcher = updater.dispatcher
#
#
# def start_command(bot, update):
#     bot.send_message(chat_id=update.message.chat_id, text="Hi! Let's chat")
#
# def fbs(bot, update):
#
#
#     plt = np.array([900,
#                     1200,
#                     2400])
#
#     rsl = lambda a: np.array([a % 10, a % 100 // 10, a // 100])
#     # cnv = lambda a, b: rsl(a).dot(b)
#     cn2 = lambda a, b: rsl(a).T.dot(b)
#     # klc = lambda a: sum(rsl(a))
#
#     st1 = lambda a: str(a[0]) + ' x ' + str(a[1])
#     st2 = lambda a: st1(a[0]) + ' + ' + st1(a[1]) + ' + ' + st1(a[2])
#     st3 = lambda a, b: list(zip(list(a), list(b)))
#     st = lambda a, b: st2(st3(rsl(a), b))
#     sf = lambda a, b: st(a, b) + ' = ' + str(cn2(a, b))
#
#     n1 = lambda a, b, n: n if (a * n % b == 0) else n1(a, b, n + 1)
#     n2 = lambda a: n1(a[0], a[1], 1)  # (a,b,1)
#     # n3 = lambda a: tuple(map(n2, zip(a[a != max(a)], [max(a)] * (len(a) - 1))))
#
#     b = np.array(list(range(10 ** len(plt))))
#
#     l = int(update.message.text.split(' ')[1])
#
#     nl = b[(cn2(b, plt) <= l) * (cn2(b, plt) > (l - min(plt)))]
#     rres = nl[cn2(nl, plt) == max(cn2(nl, plt))]
#     dres = list(map(lambda x: sf(x, plt), rres))
#
#
#     bot.send_message(chat_id=update.message.chat_id, text='\n'.join(dres))
#
#
# def stears(bot, update):
#
#     x = int(update.message.text.split(' ')[1])
#
#     l = x + 60
#
#     bot.send_message(chat_id=update.message.chat_id, text=l)
#
#
# def text_message(bot, update):
#     if update.message.forward_from or update.message.forward_from_chat:
#         response = update.message.text
#         response = response.upper()
#         fi = response.find('BUY')
#         li = response.find('SELL')
#         response = response[fi:li]
#         response = response.rstrip()
#         response = response.split(' ')
#         for item in response:
#             if not item.isalnum():
#                 for char in ['/','-','_',':']:
#                     if char in item:
#                         response = item.split(char)
#
#         bot.send_message(chat_id=update.message.chat_id, text=response)
#     else:
#         bot.send_message(chat_id=update.message.chat_id, text="Lo}{")
#
#
#
# start_command_handler = CommandHandler('start', start_command)
# fbs_command_handler = CommandHandler('fbs',fbs)
# stears_command_handler = CommandHandler('stears', stears)
# text_massage_handler = MessageHandler(Filters.text, text_message)
#
# dispatcher.add_handler(start_command_handler)
# dispatcher.add_handler(fbs_command_handler)
# dispatcher.add_handler(stears_command_handler)
# dispatcher.add_handler(text_massage_handler)
#
#
#
# updater.start_polling(clean=True)
#
# updater.idle()


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import numpy as np

updater = Updater(token='628013145:AAFbLjHNJ-LeHEDKe8d0Vbe8Yqi4D-k9tZg')
dispatcher = updater.dispatcher


def start_command(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hi! Let's chat")


"""
def fbs(bot, update):

    #=====================================================================
    plt = np.array([900,
                    1200,
                    2400])
    rsl = lambda a: np.array([a % 10, a % 100 // 10, a // 100])
    cn2 = lambda a, b: rsl(a).T.dot(b)
    st1 = lambda a: str(a[0]) + ' x ' + str(a[1])
    st2 = lambda a: st1(a[0]) + ' + ' + st1(a[1]) + ' + ' + st1(a[2])
    st3 = lambda a, b: list(zip(list(a), list(b)))
    st = lambda a, b: st2(st3(rsl(a), b))
    sf = lambda a, b: st(a, b) + ' = ' + str(cn2(a, b))
    n1 = lambda a, b, n: n if (a * n % b == 0) else n1(a, b, n + 1)
    n2 = lambda a: n1(a[0], a[1], 1)  # (a,b,1)
    b = np.array(list(range(10 ** len(plt))))
    #=====================================================================

    l = int(update.message.text.split(' ')[1])

    nl = b[(cn2(b, plt) <= l) * (cn2(b, plt) > (l - min(plt)))]
    rres = nl[cn2(nl, plt) == max(cn2(nl, plt))]
    dres = list(map(lambda x: sf(x, plt), rres))


    bot.send_message(chat_id=update.message.chat_id, text='\n'.join(dres))
"""


def rasklad(l, lst):
    """
    Раскладываем сборные элементы по указанной длине
    :param l: длина участка на котором производится раскладка, int
    :param lst: перечень длин укладываемых элементов, ndarray
    """
    cn2 = lambda a, b: np.array([a % 10, a % 100 // 10, a // 100]).T.dot(b)
    b = np.arange(10 ** len(lst))
    c = cn2(b, lst)
    x = (c <= l) * (c > l - min(lst))
    b = b[x]
    c = c[x]
    b = b[c == max(c)]
    t = []

    for i in b:
        s = ''
        s = s + ' + '.join(['{0} x {1}'.format(x[0], x[1]) for x in zip([i % 10, i % 100 // 10, i // 100], list(lst))])
        s = s + ' = {0};\t(+{1} = {2})'.format(cn2(i, lst), (l - cn2(i, lst)), l)
        t += [s]

    res = '\n'.join(t)
    return res


def decorated_print(l, msg):
    s = 'l = {0} мм\n{1}\n'.format(l, msg)
    return s


def fbs(bot, update):
    """
    Раскладываем ФБСки
    """
    fbs = np.array([900,
                    1200,
                    2400])

    lens = [int(x) for x in update.message.text.split()[1:]]
    msg = [decorated_print(l, rasklad(l, fbs)) for l in lens]

    bot.send_message(chat_id=update.message.chat_id, text='\n'.join(msg))


def plt(l):
    """
    Раскладываем плиты
    """
    plt = np.array([1000,
                    1200,
                    1500])

    lens = [int(x) for x in update.message.text.split()[1:]]
    msg = [decorated_print(l, rasklad(l, plt)) for l in lens]

    bot.send_message(chat_id=update.message.chat_id, text='\n'.join(msg))


def stears(bot, update):
    x = int(update.message.text.split(' ')[1])

    l = x + 60

    bot.send_message(chat_id=update.message.chat_id, text=l)


def text_message(bot, update):
    if update.message.forward_from or update.message.forward_from_chat:
        response = update.message.text
        response = response.upper()
        fi = response.find('BUY')
        li = response.find('SELL')
        response = response[fi:li]
        response = response.rstrip()
        response = response.split(' ')
        for item in response:
            if not item.isalnum():
                for char in ['/', '-', '_', ':']:
                    if char in item:
                        response = item.split(char)

        bot.send_message(chat_id=update.message.chat_id, text=response)
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Lo}{")


start_command_handler = CommandHandler('start', start_command)
fbs_command_handler = CommandHandler('fbs', fbs)
plt_command_handler = CommandHandler('plt', plt)
stears_command_handler = CommandHandler('stears', stears)
text_massage_handler = MessageHandler(Filters.text, text_message)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(fbs_command_handler)
dispatcher.add_handler(plt_command_handler)
dispatcher.add_handler(stears_command_handler)
dispatcher.add_handler(text_massage_handler)

updater.start_polling(clean=True)

updater.idle()
