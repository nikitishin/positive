from .models import ViberUser
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import TextMessage, PictureMessage, KeyboardMessage, ContactMessage
from viberbot.api.viber_requests import *
from django.utils.translation import activate, gettext as _
from urllib.parse import urljoin




viber = Api(BotConfiguration(
    name='PythonSampleBot',
    avatar='http://viber.com/avatar.jpg',
    auth_token='4a886870fc67d50c-1286fc8b377e5f59-38d063b54f7d0e6a'
))


def registration(viber_request):
    vuser, created = ViberUser.objects.update_or_create(
        viber_id=viber_request.user.id,
        defaults={
            'is_active': True,
            'name': viber_request.user.name,
            'country': viber_request.user.country,
            'language': viber_request.user.language}
    )
    if vuser.phone_number is None:
        simple_keyboard = {
            "Type": "keyboard",
            "Buttons": [
                {
                    "Columns": 6,
                    "Rows": 1,
                    "BgColor": "#e6f5ff",
                    "BgMedia": "http://link.to.button.image",
                    "BgMediaType": "picture",
                    "BgLoop": True,
                    "ActionType": "share-phone",
                    "ActionBody": "This will be sent to your bot in a callback",
                    "ReplyType": "message",
                    "Text": "Для начала давай знакомиться. Что-бы дать номер телефона нажми сюда"
                }
            ]
        }

        keyboard_message = KeyboardMessage(
            tracking_data='tracking_data',
            keyboard=simple_keyboard, min_api_version=3
        )
        viber.send_messages(vuser.viber_id, [keyboard_message])
    else:
        print(viber_request)
        botton_main_disp(viber_request)


def botton_main_disp(viber_request):
    simple_keyboard = {
        "Type": "keyboard",
        "Buttons": [
            {
                "Columns": 3,
                "Rows": 1,
                "BgColor": "#e6f5ff",
                "BgMedia": "http://link.to.button.image",
                "BgMediaType": "picture",
                "BgLoop": True,
                "ActionType": "reply",
                "ActionBody": "menu",
                "ReplyType": "message",
                "Text": _("Меню")
            },{
                "Columns": 3,
                "Rows": 1,
                "BgColor": "#e6f5ff",
                "BgMedia": "http://link.to.button.image",
                "BgMediaType": "picture",
                "BgLoop": True,
                "ActionType": "reply",
                "ActionBody": "promo",
                "ReplyType": "message",
                "Text": _("Промо-код")
            },{
                "Columns": 3,
                "Rows": 1,
                "BgColor": "#e6f5ff",
                "BgMedia": "http://link.to.button.image",
                "BgMediaType": "picture",
                "BgLoop": True,
                "ActionType": "reply",
                "ActionBody": "set_language",
                "ReplyType": "message",
                "Text": _("Изменить язык")
            },{
                "Columns": 3,
                "Rows": 1,
                "BgColor": "#e6f5ff",
                "BgMedia": "http://link.to.button.image",
                "BgMediaType": "picture",
                "BgLoop": True,
                "ActionType": "reply",
                "ActionBody": "set_timezone",
                "ReplyType": "message",
                "Text": _("Изменить часовой пояс")
            },{
                "Columns": 3,
                "Rows": 1,
                "BgColor": "#e6f5ff",
                "BgMedia": "http://link.to.button.image",
                "BgMediaType": "picture",
                "BgLoop": True,
                "ActionType": "reply",
                "ActionBody": "share",
                "ReplyType": "message",
                "Text": _("Рассказать про меня")
            },{
                "Columns": 3,
                "Rows": 1,
                "BgColor": "#e6f5ff",
                "BgMedia": "http://link.to.button.image",
                "BgMediaType": "picture",
                "BgLoop": True,
                "ActionType": "reply",
                "ActionBody": "pin",
                "ReplyType": "message",
                "Text": _("Ввести код авторизации")
            },{
                "Columns": 3,
                "Rows": 1,
                "BgColor": "#e6f5ff",
                "BgMedia": "http://link.to.button.image",
                "BgMediaType": "picture",
                "BgLoop": True,
                "ActionType": "reply",
                "ActionBody": "review",
                "ReplyType": "message",
                "Text": _("Отправить отзыв разработчикам")
            },{
                "Columns": 3,
                "Rows": 1,
                "BgColor": "#e6f5ff",
                "BgMedia": "http://link.to.button.image",
                "BgMediaType": "picture",
                "BgLoop": True,
                "ActionType": "reply",
                "ActionBody": "help_me",
                "ReplyType": "message",
                "Text": _("Помощь")
            }
        ]
    }
    # reply_address = None
    try:
        reply_address = viber_request.user.id
    except AttributeError:
        reply_address = viber_request.sender.id
    keyboard_message = KeyboardMessage(tracking_data='tracking_data', keyboard=simple_keyboard, min_api_version=3)
    viber.send_messages(reply_address, [keyboard_message])


def botton_menu(viber_request):
    simple_keyboard = {
        "Type": "keyboard",
        "Buttons": [
            {
                "Columns": 3,
                "Rows": 1,
                "BgColor": "#e6f5ff",
                "BgMedia": "http://link.to.button.image",
                "BgMediaType": "picture",
                "BgLoop": True,
                "ActionType": "reply",
                "ActionBody": "balances",
                "ReplyType": "message",
                "Text": _("Балансы")
            },{
                "Columns": 3,
                "Rows": 1,
                "BgColor": "#e6f5ff",
                "BgMedia": "http://link.to.button.image",
                "BgMediaType": "picture",
                "BgLoop": True,
                "ActionType": "reply",
                "ActionBody": "transactions",
                "ReplyType": "message",
                "Text": _("Транзакции")
            },{
                "Columns": 6,
                "Rows": 1,
                "BgColor": "#e6f5ff",
                "BgMedia": "http://link.to.button.image",
                "BgMediaType": "picture",
                "BgLoop": True,
                "ActionType": "reply",
                "ActionBody": "points",
                "ReplyType": "message",
                "Text": _("Точки")
            },{
                "Columns": 6,
                "Rows": 1,
                "BgColor": "#e6f5ff",
                "BgMedia": "http://link.to.button.image",
                "BgMediaType": "picture",
                "BgLoop": True,
                "ActionType": "reply",
                "ActionBody": "change_positive",
                "ReplyType": "message",
                "Text": _("Изменить позитив")
            }
        ]
    }
    keyboard_message = KeyboardMessage(tracking_data='tracking_data', keyboard=simple_keyboard, min_api_version=3)
    viber.send_messages(viber_request.sender.id, [keyboard_message])


def botton_back(viber_request):
    # text = _("Вернуться в предыдущее меню")
    simple_keyboard = {
        "Type": "keyboard",
        "Buttons": [
            {
                "Columns": 6,
                "Rows": 1,
                "BgColor": "#e6f5ff",
                "BgMedia": "http://link.to.button.image",
                "BgMediaType": "picture",
                "BgLoop": True,
                "ActionType": "reply",
                "ActionBody": "back",
                "ReplyType": "message",
                "Text": _("Вернуться в предыдущее меню")
            }
        ]
    }
    keyboard_message = KeyboardMessage(tracking_data='tracking_data', keyboard=simple_keyboard, min_api_version=3)
    viber.send_messages(viber_request.sender.id, [keyboard_message])


def botton_languages(viber_request, hostname):
    # hostname = "%s://%s" % (request.scheme, request.scheme.get_host())
    photo_ua = urljoin(hostname, 'media/ua4.jpg')
    photo_en = urljoin(hostname, 'media/en4.jpg')
    photo_ru = urljoin(hostname, 'media/ru4.jpg')
    simple_keyboard = {
        "Type": "keyboard",
        "Buttons": [
            {
                "Columns": 2,
                "Rows": 1,
                "BgColor": "#e6f5ff",
                "Image": photo_ua,
                "ActionType": "reply",
                "ActionBody": "language_uk",
                "ReplyType": "message"
            },{
                "Columns": 2,
                "Rows": 1,
                "BgColor": "#e6f5ff",
                "Image": photo_en,
                "ActionType": "reply",
                "ActionBody": "language_en",
                "ReplyType": "message"
            },{
                "Columns": 2,
                "Rows": 1,
                "BgColor": "#e6f5ff",
                "Image": photo_ru,
                "ActionType": "reply",
                "ActionBody": "language_ru",
                "ReplyType": "message"
            }
        ]
    }
    keyboard_message = KeyboardMessage(tracking_data='tracking_data', keyboard=simple_keyboard, min_api_version=3)
    viber.send_messages(viber_request.sender.id, [keyboard_message])