import dotenv
import eel

de = dotenv.dotenv_values()

eel.init(de.get("EEL_INIT"))



@eel.expose
def load_behave():
    """
    this method display stdout and stderr of behave
    :return:
    """
    return "TEST"


eel.start(
    de.get("EEL_START"),
    size=(int(de.get("MAIN_VERTICAL")), int(de.get("MAIN_HORIZONTAL"))),
)



if __name__ == "__main__":
    from behave import __main__ as behave_executable

    behave_executable.main(None)
