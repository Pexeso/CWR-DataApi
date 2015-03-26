# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import PrefixBuilder, RecordFactory
from cwr.parser.dictionary import AgreementTerritoryDictionaryDecoder


"""
CWR Territory in Agreement grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

_data = _config.load_field_config('table')
_data.update(_config.load_field_config('common'))

_factory_field = DefaultFieldFactory(_data, CWRTables())

_prefixer = PrefixBuilder(_config.record_types())
_factory_record = RecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)

"""
Territory in Agreement patterns.
"""

territory_in_agreement = _factory_record.get_transaction_record('territory_in_agreement')

"""
Parsing actions for the patterns.
"""

territory_in_agreement.setParseAction(lambda p: _to_agreementterritory(p))

"""
Parsing actions for the patterns.
"""


def _to_agreementterritory(parsed):
    """
    Transforms the final parsing result into a AgreementTerritoryRecord instance.

    :param parsed: result of parsing a Territory in Agreement transaction header
    :return: a AgreementTerritoryRecord created from the parsed record
    """
    decoder = AgreementTerritoryDictionaryDecoder()
    return decoder.decode(parsed)