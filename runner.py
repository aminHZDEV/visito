__author__ = "AminHZDEV"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "amin.hasan.zarei@gmail.com"
__status__ = "Production"

import dotenv
import eel
from utils.my_log import MyLog

de = dotenv.dotenv_values()


log = MyLog()
if __name__ == "__main__":
    from behave import __main__ as behave_executable

    behave_executable.main(None)

eel.init(de.get("EEL_INIT"))


@eel.expose
def load_behave():
    """
    this method display stdout and stderr of behave
    :return:
    """
    with open(de.get("LOG_FILE")) as flog:
        return [str(item) for item in flog.readlines()]


eel.start(
    de.get("EEL_START"),
    size=(int(de.get("MAIN_VERTICAL")), int(de.get("MAIN_HORIZONTAL"))),
)
