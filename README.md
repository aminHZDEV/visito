# visito
A local app to visit doctor
*******************************
#### how to run ?
* create a .env file in  root directory 
* add these lines to .env file
  * MONGO_URL="mongodb://localhost:27017/"
  * DB_NAME="mydatabase"
  * LOG_FILE="app.log"
  * LOG_MODE="w"
  * LOG_FORMAT="%(name)s - %(levelname)s - %(message)s
  * MAIN_VERTICAL="720"
  * MAIN_HORIZONTAL="480"
  * EEL_INIT="statics"
  * EEL_START="/html/main.html"
* install libs in requirements.txt file 
* make app.log file in root directory 
* just run the runner.py file and enjoy