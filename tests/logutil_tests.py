import sys
from test_testing import LoggingTest
from test_dictconfig import ConfigDictTest
from test_queue import QueueTest
from test_formatter import FormatterTest
from test_messages import MessageTest
try:
    from test_redis import RedisQueueTest
except ImportError:
    pass

# The adapter won't work in < 2.5 because the "extra" parameter used by it
# only appeared in 2.5 :-(
if sys.version_info[:2] >= (2, 5):
    from test_adapter import AdapterTest
else:
    print("LoggerAdapter won't work in Python < 2.5, so its tests are being "
          "skipped.")
