# dz-final-module-3


## Demo video

[![Watch](https://raw.githubusercontent.com/sr9yar/dz-final-module-3/main/demo.jpg)](https://raw.githubusercontent.com/sr9yar/dz-final-module-3/main/demo.mp4)


https://raw.githubusercontent.com/sr9yar/dz-final-module-3/main/demo.mp4



## Installation


Чтобы произвести установку необходимо выполнить команды

```
source venv/bin/activate
pip install -r requirements.txt

```

Далее создать файла .env в корне проекта и установить необхожимые переменные окружения. 
Можно использовать файл .env.example как шаблон.

Файл с вредоносным кодом для анализа должен быть расположен в 

```
./protected/protected_archive.zip
```



## Start local server

Запустить приложние локально можно используюя команду 

```

python app.py

```

Приложение будет доступно по адресу http://localhost:8080/

Отчеты доступны по адресам

http://localhost:8080/virustotal
http://localhost:8080/vulners

ПДФ версии по адресам 

http://localhost:8080/virustotal.pdf
http://localhost:8080/vulners.pdf


## Notes 

### Installing packages from scratch

```
pip uninstall xhtml2pdf
pip freeze | xargs pip uninstall -y  
    
pip install requests python-dotenv bottle
pip install -e  git+https://github.com/xhtml2pdf/xhtml2pdf@master#egg=xhtml2pdf
pip freeze > requirements.txt
```