from libs.api.virustotal_api import VirustotalApi
from libs.api.vulners_api import VulnersApi

from xhtml2pdf import pisa
from programs import programs



class AppService:

  __virustotalApi = VirustotalApi()
  __vulnersApi =  VulnersApi()



  def do_file_scan(self):
    """
    Perform file scan
    https://docs.virustotal.com/reference/files-scan

    :returns: report
    """
    id, file_id = self.__virustotalApi.upload_file()

    # file_id = "f4dc2e1abf2de55b455c7dfc0bbe66a9d12f7e857cd12f8408dadd7129946ae3"
    # id = "NjEyYjU3ZTJhZmU3MDY1ZWJlOTIxMzM3MTcwZGY3ZDQ6MTczOTMwNjI5NA=="

    output = {}

    analyses = self.__virustotalApi.get_file_analyses(id)
    output["detected"] = self.parse_virustotal_analyses(analyses)

    summary = self.get_all_behaviors_summary_parsed(file_id)
    output = {**output, **summary}

    behaviors = self.get_all_behavior_reports_parsed(file_id)
    output = {**output, **behaviors}

    return output



  def do_search_by_name(self):

    prepared_data = {
      "programs": [],
      "report": [],
    }

    for p in programs:
      result = self.__vulnersApi.do_search_by_name(p["Program"], p["Version"])

      cve = []

      if "data" in result:
        if "result" in result and result["result"] == "error":
          vulnerability_report["error"] = result["data"]["error"]

        if result["data"].get("search", False):
          for s in result["data"]["search"]:
            cve.append({
              "id": s["id"],
              "title": s["_source"]["title"],
            })

      vulnerability_report = {
        "error": "",
        "name": p["Program"],
        "version": p["Version"],
        "cve": cve,
      }

      prepared_data["programs"].append(vulnerability_report)
      prepared_data["report"].append(result)

    return prepared_data



  def get_file_analyses(self, id):
    result = self.__virustotalApi.get_file_analyses(id)
    return result



  def upload_file(self):
    result = self.__virustotalApi.upload_file()
    return result



  def get_all_behaviors_summary_parsed(self, fileId):
    result = self.__virustotalApi.get_all_behaviors_summary(fileId)

    output = {
      "data": result,
      "attack_techniques": [],
      "dns_lookups": [],
    }

    for item in result["data"]["mitre_attack_techniques"]:
      output["attack_techniques"].append(item["id"])
    for item in result["data"]["dns_lookups"]:
      output["dns_lookups"].append({
          "hostname": item["hostname"],
          "resolved_ips": item.get("resolved_ips", []),
        })
      
    return output



  def get_all_behavior_reports_parsed(self, fileId):
    result = self.__virustotalApi.get_all_behavior_reports(fileId)

    output = {
      "data": result,
      "sandbox_names": [],
    }

    for item in result["data"]:
      output["sandbox_names"].append(item["attributes"]["sandbox_name"])

    return output



  def html_to_pdf(self, content, output):
    """
    Generate a PDF from html template
    https://xhtml2pdf.readthedocs.io/en/latest/quickstart.html

    """
    result_file = open(output, "w+b")

    pisa_status = pisa.CreatePDF(
      content,
      dest=result_file
    )           

    result_file.close()

    if pisa_status.err:
      raise Exception("ERROR: failed to create PDF")

    return



  def parse_virustotal_analyses(self, res):
    """
    https://docs.virustotal.com/reference/analyses-object

    """
    results = res["data"]["attributes"]["results"]
    if results is None or len(results.keys()) == 0:
      print("WARN: no analyses has been received")
      return []

    detected = {}
    for key in results.keys():
      result = results[key]

      if result["category"] == "malicious":
        detected[key] = result["result"]

    return detected


