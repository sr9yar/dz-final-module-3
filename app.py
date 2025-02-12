import os 
import json

from bottle import response, run, route, static_file, template
from dotenv import load_dotenv

from libs.service.app_service import AppService



load_dotenv()

PORT = os.getenv("PORT") or 8080

app_service = AppService()



@route("/")
def index():

  dic = {
    "links": [
      {
        "anchor": "Отчет Virustotal",
        "url": "/virustotal",
        "target": "_self",
      },
      {
        "anchor": "Virustotal (PDF)",
        "url": "/virustotal.pdf",
        "target": "_blank",
      },
      {
        "anchor": "Отчет Vulners",
        "url": "/vulners",
        "target": "_self",
      },
      {
        "anchor": "Vulners (PDF)",
        "url": "/vulners.pdf",
        "target": "_blank",
      },
    ],
    "title": "Главная",
  }

  return template("index", **dic)



@route("/virustotal")
def virustotal():
  dic = {
    "title": "Отчет Virustotal",
  }

  result = app_service.do_file_scan()

  dic = {**dic, **result}
  dic["report"] = json.dumps(result["data"], indent=2) 

  return template("report_virustotal", **dic)



@route("/virustotal.pdf")
def create_pdf():

  filename = "report_virustotal.pdf"
  dic = {
    "title": "Отчет Virustotal PDF",
  }

  response.headers["Content-Type"] = "application/pdf; charset=UTF-8"
  response.headers["Content-Disposition"] = f"attachment; filename=\"{filename}\""

  result = app_service.do_file_scan()

  dic = {**dic, **result}
  dic["report"] = json.dumps(result["data"], indent=2) 

  html = template("report_virustotal", **dic)
  app_service.html_to_pdf(html, filename)
  return static_file(filename, root=os.getcwd())



@route("/vulners")
def vulners():
  dic = {
    "title": "Отчет Vulners",
  }
  data = app_service.do_search_by_name()
  dic["data"] = data
  dic["report"] = json.dumps(data, indent=2)

  return template("report_vulners", **dic)



@route("/vulners.pdf")
def create_pdf():

  filename = "report_vulners.pdf"
  dic = {
    "title": "Отчет Vulners PDF",
  }

  response.headers["Content-Type"] = "application/pdf; charset=UTF-8"
  response.headers["Content-Disposition"] = f"attachment; filename=\"{filename}\""

  data = app_service.do_search_by_name()
  dic["data"] = data
  dic["report"] = json.dumps(data, indent=2)

  html = template("report_vulners", **dic)
  app_service.html_to_pdf(html, filename)
  return static_file(filename, root=os.getcwd())



@route("/favicon.ico")
def favicon():
  return static_file("favicon.ico", root=os.getcwd())

if __name__ == "__main__":
  run(host="localhost", port=PORT, debug=True, reloader=True)


