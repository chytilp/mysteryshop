from datetime import date

from django.core.exceptions import ValidationError
from django.test.testcases import TestCase

from germanium.annotations import data_provider
from germanium.tools import assert_equals, assert_raises

from cz_models.fields import CZBirthNumber
from cz_models.validators import CZBirthNumberValidator


class CZModelsTestCase(TestCase):

    def bad_personal_ids(self):
        return (
            ('ahoj',),
            ('89560702991',),
            ('97581148z0',),
            ('9758114851',),
            ('9758114849',),
            ('8958046/823',),
            ('895804//6823',),
            ('9499041101',),
            ('9409441107',),
            ('9679556810',),
            ('9629556810',),
        )

    def good_personal_ids(self):
        return (
            ('9362108173',),
            ('9356063981',),
            ('120623002',),
            ('530623002',),
            ('5406230016',),
            ('540623/0016',)
        )

    def personal_ids_and_dates(self):
        return (
            ('9609156810', date(year=1996, month=9, day=15)),
            ('9659156815', date(year=1996, month=9, day=15)),
            ('300915681', date(year=1930, month=9, day=15)),
            ('1009156819', date(year=2010, month=9, day=15)),
            ('1029156810', date(year=2010, month=9, day=15)),
            ('1059156813', date(year=2010, month=9, day=15)),
            ('1079156815', date(year=2010, month=9, day=15)),
            ('107915/6815', date(year=2010, month=9, day=15)),
            ('300915/681', date(year=1930, month=9, day=15)),
            ('9679556810', None),
            ('9629556816', None),
            ('', None),
        )

    @data_provider(bad_personal_ids)
    def test_bad_personal_id(self, personal_id):
        assert_raises(ValidationError, CZBirthNumberValidator(), personal_id)

    @data_provider(good_personal_ids)
    def test_good_personal_id(self, personal_id):
        assert_equals(CZBirthNumberValidator()(personal_id), None)

    @data_provider(personal_ids_and_dates)
    def test_cz_birth_number(self, personal_id, date):
        assert_equals(CZBirthNumber(personal_id).date(), date)
