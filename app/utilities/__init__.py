from .vms import set_vm_state, extract_vm_state
from .log import log_vm_event
from .azure import get_subscriptions
from .settings import get_setting, set_setting, CURRENCIES
from .cache import get_price
from .update import copy_url_to_blob, DEPLOYMENT_URL

STARTSCHEDULETAG = "vm-start-schedule"
STOPSCHEDULETAG = "vm-stop-schedule"

daysMapping = {1: "Mon", 2: "Tue", 3: "Wed", 4: "Thu", 5: "Fri", 6: "Sat", 7: "Sun"}
