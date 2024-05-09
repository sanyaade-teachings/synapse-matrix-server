from twisted.test.proto_helpers import MemoryReactor

from synapse.server import HomeServer
from synapse.types import JsonDict
from synapse.util import Clock

from tests.rest.client.test_sendtodevice_base import SendToDeviceTestCaseBase
from tests.unittest import HomeserverTestCase


class SendToDeviceTestCase(SendToDeviceTestCaseBase, HomeserverTestCase):
    # See SendToDeviceTestCaseBase for tests
    pass
