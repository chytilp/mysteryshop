from decimal import Decimal
from datetime import datetime, date, timedelta

from django.contrib.auth import models as auth_models

from project.models import Region, District, Client, Project, Wave, Shop
from account.models import Candidate, Interviewer, InterviewerStatus, InterviewerDistrict
from visit.models import Test, Attachment, Wage, Bonus, Visit
from message.models import Message, MessageContext

#  project


def fill_region():
    # name slug
    create_region(**{'name': 'Středočeský kraj', 'slug': 'st'})
    create_region(**{'name': 'Jihočeský kraj', 'slug': 'jc'})
    create_region(**{'name': 'Plzeňský kraj', 'slug': 'pl'})
    create_region(**{'name': 'Karlovarský kraj', 'slug': 'kv'})
    create_region(**{'name': 'Ústecký kraj', 'slug': 'ut'})
    create_region(**{'name': 'Liberecký kraj', 'slug': 'li'})
    create_region(**{'name': 'Královéhradecký kraj', 'slug': 'kh'})
    create_region(**{'name': 'Pardubický kraj', 'slug': 'pa'})
    create_region(**{'name': 'Kraj Vysočina', 'slug': 'vy'})
    create_region(**{'name': 'Jihomoravský kraj', 'slug': 'jm'})
    create_region(**{'name': 'Olomoucký kraj', 'slug': 'ol'})
    create_region(**{'name': 'Moravskoslezský kraj', 'slug': 'ms'})
    create_region(**{'name': 'Zlínský kraj', 'slug': 'zl'})
    create_region(**{'name': 'Praha', 'slug': 'pha'})


def create_region(**kwargs):
    Region.objects.create(**kwargs)


def create_district(region_slug, **kwargs):
    region = Region.objects.get(slug=region_slug)
    kwargs.update({'region': region})
    District.objects.create(**kwargs)


def fill_district():
    # name slug region
    # st
    create_district('st', **{'name': 'Benešov', 'slug': 'ben'})
    create_district('st', **{'name': 'Beroun', 'slug': 'ber'})
    create_district('st', **{'name': 'Kladno', 'slug': 'kla'})
    create_district('st', **{'name': 'Kolín', 'slug': 'kol'})
    create_district('st', **{'name': 'Kutná Hora', 'slug': 'kut'})
    create_district('st', **{'name': 'Mělník', 'slug': 'mel'})
    create_district('st', **{'name': 'Mladá Boleslav', 'slug': 'mlabo'})
    create_district('st', **{'name': 'Nymburk', 'slug': 'nym'})
    create_district('st', **{'name': 'Praha-východ', 'slug': 'phavy'})
    create_district('st', **{'name': 'Praha-západ', 'slug': 'phaza'})
    create_district('st', **{'name': 'Příbram', 'slug': 'pri'})
    create_district('st', **{'name': 'Rakovník', 'slug': 'rak'})
    # jc
    create_district('jc', **{'name': 'České Budějovice', 'slug': 'cesbu'})
    create_district('jc', **{'name': 'Český Krumlov', 'slug': 'ceskr'})
    create_district('jc', **{'name': 'Jindřichův Hradec', 'slug': 'jinhr'})
    create_district('jc', **{'name': 'Písek', 'slug': 'pis'})
    create_district('jc', **{'name': 'Prachatice', 'slug': 'prach'})
    create_district('jc', **{'name': 'Strakonice', 'slug': 'stra'})
    create_district('jc', **{'name': 'Tábor', 'slug': 'tab'})
    # pl
    create_district('pl', **{'name': 'Domažlice', 'slug': 'dom'})
    create_district('pl', **{'name': 'Klatovy', 'slug': 'kla'})
    create_district('pl', **{'name': 'Plzeň-jih', 'slug': 'plzj'})
    create_district('pl', **{'name': 'Plzeň-město', 'slug': 'plzm'})
    create_district('pl', **{'name': 'Plzeň-sever', 'slug': 'plzs'})
    create_district('pl', **{'name': 'Rokycany', 'slug': 'roky'})
    create_district('pl', **{'name': 'Tachov', 'slug': 'tach'})
    # kv
    create_district('kv', **{'name': 'Cheb', 'slug': 'cheb'})
    create_district('kv', **{'name': 'Karlovy Vary', 'slug': 'karv'})
    create_district('kv', **{'name': 'Sokolov', 'slug': 'soko'})
    # ut
    create_district('ut', **{'name': 'Děčín', 'slug': 'deci'})
    create_district('ut', **{'name': 'Chomutov', 'slug': 'chom'})
    create_district('ut', **{'name': 'Litoměřice', 'slug': 'lito'})
    create_district('ut', **{'name': 'Louny', 'slug': 'loun'})
    create_district('ut', **{'name': 'Most', 'slug': 'most'})
    create_district('ut', **{'name': 'Teplice', 'slug': 'tepl'})
    create_district('ut', **{'name': 'Ústí nad Labem', 'slug': 'utnl'})
    # li
    create_district('li', **{'name': 'Česká Lípa', 'slug': 'cesli'})
    create_district('li', **{'name': 'Jablonec nad Nisou', 'slug': 'jabl'})
    create_district('li', **{'name': 'Liberec', 'slug': 'libe'})
    create_district('li', **{'name': 'Semily', 'slug': 'semi'})
    # kh
    create_district('kh', **{'name': 'Hradec Králové', 'slug': 'hrak'})
    create_district('kh', **{'name': 'Jičín', 'slug': 'jici'})
    create_district('kh', **{'name': 'Náchod', 'slug': 'nach'})
    create_district('kh', **{'name': 'Rychnov nad Kněžnou', 'slug': 'rychn'})
    create_district('kh', **{'name': 'Trutnov', 'slug': 'trut'})
    # pa
    create_district('pa', **{'name': 'Chrudim', 'slug': 'chru'})
    create_district('pa', **{'name': 'Pardubice', 'slug': 'pard'})
    create_district('pa', **{'name': 'Svitavy', 'slug': 'svit'})
    create_district('pa', **{'name': 'Ústí nad Orlicí', 'slug': 'utno'})
    # vy
    create_district('vy', **{'name': 'Havlíčkův Brod', 'slug': 'havb'})
    create_district('vy', **{'name': 'Jihlava', 'slug': 'jihl'})
    create_district('vy', **{'name': 'Pelhřimov', 'slug': 'pelh'})
    create_district('vy', **{'name': 'Třebíč', 'slug': 'treb'})
    create_district('vy', **{'name': 'Žďár nad Sázavou', 'slug': 'zdar'})
    # jm
    create_district('jm', **{'name': 'Blansko', 'slug': 'blan'})
    create_district('jm', **{'name': 'Brno-město', 'slug': 'brnm'})
    create_district('jm', **{'name': 'Brno-venkov', 'slug': 'brnv'})
    create_district('jm', **{'name': 'Břeclav', 'slug': 'brec'})
    create_district('jm', **{'name': 'Hodonín', 'slug': 'hodo'})
    create_district('jm', **{'name': 'Vyškov', 'slug': 'vysk'})
    create_district('jm', **{'name': 'Znojmo', 'slug': 'znoj'})
    # ol
    create_district('ol', **{'name': 'Jeseník', 'slug': 'jese'})
    create_district('ol', **{'name': 'Olomouc', 'slug': 'olom'})
    create_district('ol', **{'name': 'Prostějov', 'slug': 'prost'})
    create_district('ol', **{'name': 'Přerov', 'slug': 'prer'})
    create_district('ol', **{'name': 'Šumperk', 'slug': 'sump'})
    # ms
    create_district('ms', **{'name': 'Bruntál', 'slug': 'brun'})
    create_district('ms', **{'name': 'Frýdek-Místek', 'slug': 'frydm'})
    create_district('ms', **{'name': 'Karviná', 'slug': 'karv'})
    create_district('ms', **{'name': 'Nový Jičín', 'slug': 'noji'})
    create_district('ms', **{'name': 'Opava', 'slug': 'opav'})
    create_district('ms', **{'name': 'Ostrava-město', 'slug': 'ostrm'})
    # zl
    create_district('zl', **{'name': 'Kroměříž', 'slug': 'krom'})
    create_district('zl', **{'name': 'Uherské Hradiště', 'slug': 'uhehr'})
    create_district('zl', **{'name': 'Vsetín', 'slug': 'vset'})
    create_district('zl', **{'name': 'Zlín', 'slug': 'zlin'})
    # pha
    for i in range(1, 11):
        create_district('pha', **{'name': 'Praha {}'.format(i), 'slug': 'pha{}'.format(i)})


def fill_client():
    # name description slug
    create_client(**{'name': 'Ahold', 'description': '', 'slug': 'ahold'})
    create_client(**{'name': 'Česká pošta', 'description': '', 'slug': 'posta'})


def create_client(**kwargs):
    Client.objects.create(**kwargs)


def fill_project():
    # name number client date_from date_to test_cluster limit_for_test
    create_project('ahold', **{'name': 'Mystery shop pro ahold 2017', 'number': 2017001, 'date_from': date(2017, 1, 1),
                               'date_to': date(2017, 1, 1) + timedelta(days=100), 'test_cluster': 100,
                               'limit_for_test': 85})
    create_project('posta', **{'name': 'Mystery pro českou poštu 2017', 'number': 2017002,
                                'date_from': date(2017, 5, 1), 'date_to': date(2017, 5, 1) + timedelta(days=100),
                                'test_cluster': 200, 'limit_for_test': 75})


def create_project(client_slug, **kwargs):
    client = Client.objects.get(slug=client_slug)
    kwargs.update({'client': client})
    Project.objects.create(**kwargs)


def fill_wave():
    # number project date_from date_to status fee_full fee_part max_delay_for_full_fee
    create_wave(2017001, **{'number': 1, 'date_from': date(2017, 1, 1), 'date_to': date(2017, 1, 31),
                            'fee_full': Decimal('100.0'), 'fee_part': Decimal('75.0'), 'max_delay_for_full_fee': 1})
    create_wave(2017001, **{'number': 2, 'date_from': date(2017, 2, 1), 'date_to': date(2017, 2, 28),
                            'fee_full': Decimal('150.0'), 'fee_part': Decimal('100.0'), 'max_delay_for_full_fee': 2})
    create_wave(2017002, **{'number': 1, 'date_from': date(2017, 5, 1), 'date_to': date(2017, 5, 31),
                            'fee_full': Decimal('200.0'), 'fee_part': Decimal('100.0'), 'max_delay_for_full_fee': 1})


def create_wave(project_number, **kwargs):
    project = Project.objects.get(number=project_number)
    kwargs.update({'project': project})
    Wave.objects.create(**kwargs)


def fill_shop():
    # name client client_shop_id district category city address zip_code
    create_shop('', '', **{'name': '', 'client_shop_id': '', 'category': '', 'city': '', 'address': '', 'zip_code': ''})


def create_shop(client_slug, district_slug, **kwargs):
    kwargs.update({'client': Client.objects.get(slug=client_slug)})
    kwargs.update({'district': District.objects.get(slug=district_slug)})
    Shop.objects.create(**kwargs)


# account

def fill_candidate():
    # first_name last_name email personal_id phone is_man districts city address zip_code status education
    Candidate.objects.create(**{'first_name': '', 'last_name': '', 'email': '', 'personal_id': '', 'phone': '',
                                'is_man': True, 'districts': 'PR,OL', 'city': '', 'address': '',
                                'zip_code': '', 'status': None, 'education': None})


def fill_group():
    # name
    auth_models.Group.objects.create(name='interviewer')
    auth_models.Group.objects.create(name='business')
    auth_models.Group.objects.create(name='admin')


def fill_user():
    # first_name last_name email username password is_active is_supervisor group
    # user.groups.add
    create_user(['interviewer', 'admin'], **{'first_name': '', 'last_name': '', 'email': '', 'username': '',
                                             'is_active': True, 'is_supervisor': False, 'password': ''})


def create_user(group_names, **kwargs):
    user = auth_models.User.objects.create(**kwargs)
    for group_name in group_names:
        user.groups.add(auth_models.Group.objects.get(name=group_name))
    user.set_password(kwargs.get('password'))
    user.save()


def fill_interviewer():
    # user phone bank_account visit_districts
    create_interviewer('username', **{'phone': '', 'bank_account': '', 'districts': ['*ol', 'pre', 'sum']})


def create_interviewer(username, **kwargs):
    districts = kwargs.pop('districts')
    kwargs.update({'user': auth_models.User.objects.get(username=username)})
    interviewer = Interviewer.objects.create(**kwargs)
    for district in districts:
        InterviewerDistrict.objects.create(**{'interviewer': interviewer, 'is_home': district.startswith('*'),
                                              'district': district if not district.startswith('*') else district[1:]})


def fill_interviewer_status():
    # interviewer status begin
    create_interviewer_status('username', **{'status': None, 'begin': '2015-05-06 11:34:01'})


def create_interviewer_status(username, **kwargs):
    kwargs.update({'interviewer': Interviewer.objects.get(user__username=username)})
    InterviewerStatus.objects.create(**kwargs)


# visit

def fill_test():
    # project interviewer score passed
    Test.objects.create(**{
        'project': Project.objects.get(slug='project slug'),
        'interviewer': Interviewer.objects.get(user__username='username'),
        'score': Decimal('86.0'),
        'passed': datetime.now()
    })


def fill_attachment():
    # wave shop interviewer file_name type data
    pass


def fill_wage():
    # interviewer billing_period amount description paid
    pass


def fill_bonus():
    # wave interviewer amount wage description
    pass


def fill_visit():
    # wave shop interviewer group date_from date_to visit_day is_pm
    pass


def create_visit(project_number, wave_number, client_shop_id, **kwargs):
    wave = Wave.objects.get(project__number=project_number, number=wave_number)
    shop = Shop.objects.get(client_shop_id=client_shop_id)
    kwargs.update({'wave': wave, 'shop': shop})

# message


def fill_message():
    # context from_user to_user content title solver status
    pass


def fill_message_context():
    # project or wave content_object author
    pass

