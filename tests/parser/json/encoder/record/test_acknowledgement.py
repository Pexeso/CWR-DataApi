# -*- coding: utf-8 -*-

import unittest
import datetime
import json

from cwr.parser.cwrjson import JSONEncoder
from cwr.acknowledgement import AcknowledgementRecord


"""
Acknowledgement to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestAcknowledgementRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = JSONEncoder()

    def test_encoded(self):
        data = AcknowledgementRecord(record_type='ACK',
                                     transaction_sequence_n=3,
                                     record_sequence_n=15,
                                     original_group_id=4,
                                     original_transaction_sequence_n=5,
                                     original_transaction_type='AGR',
                                     transaction_status='AS',
                                     creation_date_time=datetime.datetime.strptime('20030215', '%Y%m%d').date(),
                                     processing_date=datetime.datetime.strptime('20030216', '%Y%m%d').date(),
                                     creation_title='TITLE',
                                     submitter_creation_n='A123',
                                     recipient_creation_n='B124')

        encoded = self._encoder.encode(data)

        encoded = json.loads(encoded)

        self.assertEqual('ACK', encoded['record_type'])
        self.assertEqual(3, encoded['transaction_sequence_n'])
        self.assertEqual(15, encoded['record_sequence_n'])
        self.assertEqual(4, encoded['original_group_id'])
        self.assertEqual(5, encoded['original_transaction_sequence_n'])
        self.assertEqual('AGR', encoded['original_transaction_type'])
        self.assertEqual('AS', encoded['transaction_status'])
        self.assertEqual('2003-02-15', encoded['creation_date_time'])
        self.assertEqual('2003-02-16', encoded['processing_date'])
        self.assertEqual('TITLE', encoded['creation_title'])
        self.assertEqual('A123', encoded['submitter_creation_n'])
        self.assertEqual('B124', encoded['recipient_creation_n'])