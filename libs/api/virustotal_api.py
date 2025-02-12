import os
from libs.api.base_api import BaseApi



class VirustotalApi(BaseApi):
  """
  Virustotal API integration

  """



  def __init__(self):
    headers = {
      "accept": "application/json",
      "x-apikey": os.getenv("API_KEY_VIRUSTOTAL", ""),
    }
    request_delay = 1000/4
    super().__init__(headers=headers, request_delay=request_delay)



  def upload_file(self):
    """
    Upload a file
    https://docs.virustotal.com/reference/files-scan

    :returns: id
    """
    files = { "file": ("protected_archive.zip", open(f"{os.getcwd()}/protected/protected_archive.zip", "rb"), "application/zip") }
    data = { "password": os.getenv("ZIP_PASSWORD") }
    url = "https://www.virustotal.com/api/v3/files"

    res = self.do_post(url, data=data, files=files)

    id = res["data"]["id"]
    file_id = None
    if "file_info" in res["meta"]:
      file_id = res["meta"]["file_info"]["sha256"]

    return (id, file_id)



  def get_file_analyses(self, id):
    """
    Get file analyses

    :param int id: file id analyses id, ex NjEyYjU3ZTJhZmU3MDY1ZWJlOTIxMzM3MTcwZGY3ZDQ6MTczODE4Mjg5Mg==
    :returns: report file
    """
    url = f"https://www.virustotal.com/api/v3/analyses/{id}"
    return self.do_get(url)



  def get_file_info(self, id):
    """
    Get a file report 
    https://docs.virustotal.com/reference/file-info

    :param str id: file id

    https://docs.virustotal.com/reference/files
    :returns: File object
    """

    url = f"https://www.virustotal.com/api/v3/files/{id}"
    return self.do_get(url)



  def get_all_behaviors_summary(self, id):
    """
    Get all behaviours summary
    https://docs.virustotal.com/reference/file-all-behaviours-summary

    :param id: file id, ex f4dc2e1abf2de55b455c7dfc0bbe66a9d12f7e857cd12f8408dadd7129946ae3
    :returns: response
    """
    url = f"https://www.virustotal.com/api/v3/files/{id}/behaviour_summary"
    return self.do_get(url)



  def get_all_behavior_reports(self, id):
    """Get all behavior reports for a file
    https://docs.virustotal.com/reference/get-all-behavior-reports-for-a-file

    :param id: file id, ex f4dc2e1abf2de55b455c7dfc0bbe66a9d12f7e857cd12f8408dadd7129946ae3
    :returns: response
    """
    url = f"https://www.virustotal.com/api/v3/files/{id}/behaviours"
    return self.do_get(url)


  
  def get_file_behavior_report(self, id):
    """
    !! POSSIBLY DEPRECATED !!
    Get a file behavior report from a sandbox
    https://docs.virustotal.com/reference/get-file-behaviour-id

    :param id: file id
    :returns: response
    """
    url = f"https://www.virustotal.com/api/v3/file_behaviours/{id}"
    return self.do_get(url)

