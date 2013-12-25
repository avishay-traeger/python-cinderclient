# Copyright 2013 IBM Corp.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from cinderclient.tests import utils
from cinderclient.tests.v2 import fakes


cs = fakes.FakeClient()


class VolumeReplicationTest(utils.TestCase):

    def test_get(self):
        relationship_id = '1234'
        cs.relationships.get(relationship_id)
        cs.assert_called('GET', '/os-volume-replication/%s' % relationship_id)

    def test_list(self):
        cs.relationships.list()
        cs.assert_called('GET', '/os-volume-replication/detail')

    def test_list_filter_primary(self):
        cs.relationships.list(search_opts={'primary_id': '1234'})
        cs.assert_called('GET',
                         '/os-volume-replication/detail?primary_id=1234')

    def test_list_filter_secondary(self):
        cs.relationships.list(search_opts={'secondary_id': '1234'})
        cs.assert_called('GET',
                         '/os-volume-replication/detail?secondary_id=1234')

    def test_list_filter_status(self):
        cs.relationships.list(search_opts={'status': 'error'})
        cs.assert_called('GET', '/os-volume-replication/detail?status=error')

    def test_list_swap(self):
        cs.relationships.swap(1234)
        expected = {'relationship': {'swap': None}}
        cs.assert_called('PUT', '/os-volume-replication/1234', expected)
