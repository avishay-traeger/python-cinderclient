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

"""
Volume replication interface.
"""

import six

from cinderclient import base


class VolumeReplication(base.Resource):
    def __repr__(self):
        return "<VolumeReplication: %s>" % self.id

#    def swap(self):
#        """Swap roles in this replication relationshp."""
#        return self.manager.delete(self)


class VolumeReplicationManager(base.ManagerWithFind):
    """Manage :class:`VolumeReplication` resources."""
    resource_class = VolumeReplication

    def get(self, relationship_id):
        """Show details of a replication relationship.

        :param relationship_id: ID of the replication relationship to display.
        :rtype: :class:`VolumeReplication`
        """
        return self._get("/os-volume-replication/%s" % relationship_id,
                         "relationship")

    def list(self, detailed=True, search_opts=None):
        """Get a list of all replication relationships.

        :rtype: list of :class:`VolumeReplication`
        """
        if search_opts is None:
            search_opts = {}

        qparams = {}

        for opt, val in six.iteritems(search_opts):
            if val:
                qparams[opt] = val

        query_string = "?%s" % urlencode(qparams) if qparams else ""

        detail = ""
        if detailed:
            detail = "/detail"

        return self._list("/os-volume-replication%s%s" % (detail, query_string),
                          "relationships")

    def _action(self, action, volume, info=None, **kwargs):
        """Perform a replication "action."
        """
        body = {action: info}
        self.run_hooks('modify_body_for_action', body, **kwargs)
        url = '/os-volume-replication/%s/action' % base.getid(volume)
        return self.api.client.post(url, body=body)

#    def swap(self, relationship_id):
#        """Swap roles in this replication relationshp.
#
#        :param relationship_id: The :class:`VolumeReplication` to swap.
#        """
#        self._action('os-swap' % base.getid(relationship_id))
