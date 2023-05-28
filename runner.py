__author__ = "AminHZDEV"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = ""
__email__ = "amin.hasan.zarei@gmail.com"
__status__ = "Production"

import eel
from utils.my_log import MyLog

log = MyLog()

try:
    if __name__ == "__main__":
        from behave import __main__ as behave_executable

        behave_executable.main(None)

    eel.init(log.mdotenv["EEL_INIT"])

    @eel.expose
    def load_behave():
        """
        this method display stdout and stderr of behave
        :return:
        """
        with open(log.mdotenv["LOG_FILE"]) as flog:
            return [str(item) for item in flog.readlines()]

    eel.start(
        log.mdotenv["EEL_START"],
        size=(int(log.mdotenv["MAIN_VERTICAL"]), int(log.mdotenv["MAIN_HORIZONTAL"])),
    )
except Exception as e:
    log.mdotenv.error(e)
