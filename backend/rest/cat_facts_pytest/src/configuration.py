from backend.rest.common.configuration import ConfReader
from backend.rest.cat_facts_pytest.src.data.constants import CONF_FILE_PATH

configuration = ConfReader(CONF_FILE_PATH)
base_url = configuration.get_base_url()


