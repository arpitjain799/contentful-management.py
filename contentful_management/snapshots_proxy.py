from .client_proxy import ClientProxy
from .snapshot import Snapshot


class SnapshotsProxy(ClientProxy):
    def __init__(self, client, space_id, parent_resource_id, resource_kind='entries'):
        super(SnapshotsProxy, self).__init__(client, space_id)
        self.parent_resource_id = parent_resource_id
        self.resource_kind = resource_kind

    @property
    def _resource_class(self):
        return Snapshot

    def create(*args, **kwargs):
        """Not Supported"""

        raise Exception("Not Supported")

    def delete(*args, **kwargs):
        """Not Supported"""

        raise Exception("Not Supported")

    def _url(self, resource_id='', **kwargs):
        return self._resource_class.base_url(
            self.space_id,
            self.parent_resource_id,
            resource_url=self.resource_kind,
            resource_id=resource_id
        )

    def __repr__(self):
        return "<{0}[{1}] space_id='{2}' parent_resource_id='{3}'>".format(
            self.__class__.__name__,
            self.resource_kind,
            self.space_id,
            self.parent_resource_id
        )
