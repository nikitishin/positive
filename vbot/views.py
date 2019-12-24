from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import TextMessage, PictureMessage, KeyboardMessage, ContactMessage
from .models import ViberUser
from .utils import viber, registration, botton_menu, botton_main_disp, botton_back, botton_languages

from viberbot.api.viber_requests import *

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.translation import activate, gettext as _
from urllib.parse import urljoin


class ViberUserCreate(CreateView):
    model = ViberUser
    fields = ['name', 'language']

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('users_all')


class ViberUserListView(ListView):
    model = ViberUser

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['my_var']='test'
        return context


class ViberUserView(View):

    def get(self, request):
        return HttpResponse('Hi')


@method_decorator(csrf_exempt, name="dispatch")
class Callback(View):

    def post(self, request):
        viber_request = viber.parse_request(request.body)
        handler = None
        if viber_request.event_type == "webhook":
            return HttpResponse(status=200)
        if isinstance(viber_request, ViberConversationStartedRequest):
            handler = ConversationHandler(request=request)
        # print('TEST!!!!!!!!!request===', request)
        # print('TEST!!!!!!!!!viber_request===', viber_request)
        try:
            id = viber_request.user.id
            try:
                lang_id = ViberUser.objects.get(viber_id=id)
                language = lang_id.language
            except:
                language = viber_request.user.language
            activate(language)
            # language = viber_request.user.language
        except AttributeError:
            pass
        try:
            id = viber_request.sender.id
            lang_id = ViberUser.objects.get(viber_id=id)
            language = lang_id.language
            activate(language)
            # language = viber_request.sender.language
        except AttributeError:
            pass

        if isinstance(viber_request, ViberMessageRequest):
            handler = MessageHandler(request=request)
        elif isinstance(viber_request, ViberSubscribedRequest):
            handler = SubscribedHandler(request=request)

        elif isinstance(viber_request, ViberUnsubscribedRequest):
            handler = UnsubscribedHandler(request=request)

        handler.handle(viber_request)
        return HttpResponse(status=200)


class MessageHandler:
    def __init__(self, request):
        self.request = request

    def handle_text(self, viber_request):
        print('Test_2')
        botton_main_disp(viber_request)

    def handle_contact(self, viber_request):
        vuser = ViberUser.objects.get(viber_id=viber_request.sender.id)
        vuser.phone_number = viber_request.message.contact.phone_number
        vuser.save()
        viber.send_messages(viber_request.sender.id, [TextMessage(text=_('Номер записан. Смотрите что я умею'))])
        botton_main_disp(viber_request)

    def menu(self, viber_request):
        # viber.send_messages(viber_request.sender.id, [TextMessage(text='Кнопка меню')])
        botton_menu(viber_request)

    def balances(self, viber_request):
        viber.send_messages(viber_request.sender.id, [TextMessage(text='Это твои балансы')])
        botton_back(viber_request)

    def transactions(self, viber_request):
        viber.send_messages(viber_request.sender.id, [TextMessage(text='Это твои транзакции')])
        botton_back(viber_request)

    def points(self, viber_request):
        viber.send_messages(viber_request.sender.id, [TextMessage(text='Это твои точки')])
        botton_back(viber_request)

    def change_positive(self, viber_request):
        viber.send_messages(viber_request.sender.id, [TextMessage(text='Это твои изменить позитив')])
        botton_back(viber_request)

    def promo(self, viber_request):
        viber.send_messages(viber_request.sender.id, [TextMessage(text='Кнопка изменить промо-код')])
        botton_back(viber_request)

    def set_language(self, viber_request):
        hostname = "%s://%s" % (self.request.scheme, self.request.get_host())
        botton_languages(viber_request, hostname)

    def set_timezone(self, viber_request):
        viber.send_messages(viber_request.sender.id, [TextMessage(text='Кнопка Изменить часовой пояс')])
        botton_back(viber_request)

    def share(self, viber_request):
        hostname = "%s://%s" % (self.request.scheme, self.request.get_host())
        photo = urljoin(hostname, 'media/qr-code1.jpg')
        viber.send_messages(viber_request.sender.id, [PictureMessage(
            media=photo, text="Viber bot", thumbnail=photo,
        )])
        botton_back(viber_request)

    def pin(self, viber_request):
        viber.send_messages(viber_request.sender.id, [TextMessage(text='Кнопка Ввести код авторизации')])
        botton_back(viber_request)

    def review(self, viber_request):
        viber.send_messages(viber_request.sender.id, [TextMessage(text='Кнопка написать разработчикам')])
        botton_back(viber_request)

    def help_me(self, viber_request):
        viber.send_messages(viber_request.sender.id, [TextMessage(text=_('HELP_TEXT'))])
        botton_main_disp(viber_request)

    def back(self, viber_request):
        botton_main_disp(viber_request)

    def language_uk(self, viber_request):
        vuser = ViberUser.objects.get(viber_id=viber_request.sender.id)
        vuser.language = "uk"
        vuser.save()
        viber.send_messages(viber_request.sender.id, [TextMessage(text='Мову змінено на Українську')])
        activate(vuser.language)
        botton_main_disp(viber_request)

    def language_en(self, viber_request):
        vuser = ViberUser.objects.get(viber_id=viber_request.sender.id)
        vuser.language = "en"
        vuser.save()
        viber.send_messages(viber_request.sender.id, [TextMessage(text='Language changed to English')])
        activate(vuser.language)
        botton_main_disp(viber_request)

    def language_ru(self, viber_request):
        vuser = ViberUser.objects.get(viber_id=viber_request.sender.id)
        vuser.language = "ru"
        vuser.save()
        viber.send_messages(viber_request.sender.id, [TextMessage(text='Язык изменен на Русский')])
        activate(vuser.language)
        botton_main_disp(viber_request)

    def command_not_found(self, viber_request):
        viber.send_messages(viber_request.sender.id, [TextMessage(text=_('Команда не найдена, выберите пункт меню'))])
        botton_main_disp(viber_request)

    def handle(self, viber_request):
        if isinstance(viber_request.message, TextMessage):
            getattr(self, viber_request.message.text, self.command_not_found)(viber_request)

        elif isinstance(viber_request.message, ContactMessage):
            self.handle_contact(viber_request)


class SubscribedHandler:
    def __init__(self, request):
        self.request = request

    def handle(self, viber_request):
        registration(viber_request)


class UnsubscribedHandler:
    def __init__(self, request):
        self.request = request

    def handle(self, viber_request):
        ViberUser.objects.update_or_create(
            viber_id=viber_request.user_id, defaults={'is_active': False}
        )


class ConversationHandler:
    def __init__(self, request):
        self.request = request

    def handle(self, viber_request):
        registration(viber_request)


@csrf_exempt
def set_webhook(request):
    event_types = ["subscribed", "unsubscribed", "conversation_started", "failed", "message"]
    url = f'https://{settings.ALLOWED_HOSTS[0]}/viber/callback/'
    viber.set_webhook(url=url, webhook_events=event_types)
    return HttpResponse('OK')


@csrf_exempt
def unset_webhook(request):
    viber.unset_webhook()
    return HttpResponse('Webhook_drop')


@csrf_exempt
def send_message_for_user(request):
    # SAMPLE_KEYBOARD = {
    #     "Type": "keyboard",
    #     "Buttons": [
    #         {
    #             "Columns": 3,
    #             "Rows": 2,
    #             "BgColor": "#e6f5ff",
    #             "BgMedia": "http://link.to.button.image",
    #             "BgMediaType": "picture",
    #             "BgLoop": True,
    #             "ActionType": "share-phone",
    #             "ActionBody": "This will be sent to your bot in a callback",
    #             "ReplyType": "message",
    #             "Text": "Push me!"
    #         }
    #     ]
    # }
    # vuser = ViberUser.objects.get(id=request.GET.get('user'))
    # viber.send_messages(vuser.viber_id,
    #                     [KeyboardMessage(tracking_data='tracking_data', keyboard=SAMPLE_KEYBOARD, min_api_version=3)])
    # print(request.GET.get('user'))
    return HttpResponse('Привет')
