# dz-final-module-3


## Demo video

[![Watch](https://raw.githubusercontent.com/sr9yar/dz-final-module-3/main/demo.jpg)](https://raw.githubusercontent.com/sr9yar/dz-final-module-3/main/demo.mp4)


https://raw.githubusercontent.com/sr9yar/dz-final-module-3/main/demo.mp4



## Installation

```
source venv/bin/activate
pip install -r requirements.txt

```



## Start local server

```

python app.py

```




## Notes 

### Installing packages from scratch

```
pip uninstall xhtml2pdf
pip freeze | xargs pip uninstall -y  
    
pip install requests python-dotenv bottle
pip install -e  git+https://github.com/xhtml2pdf/xhtml2pdf@master#egg=xhtml2pdf
pip freeze > requirements.txt
```