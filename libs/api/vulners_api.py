import os
from libs.api.base_api import BaseApi



class VulnersApi(BaseApi):
  """
  Vulners API integration

  """

  __api_key = os.getenv("API_KEY_VULNERS", "")

  __api_url = os.getenv("API_URL_VULNERS", "")



  def __init__(self):
    headers = {
      "accept": "application/json",
    }
    super().__init__(headers)



  def do_search(self):
    url = f"{self.__api_url}/api/v3/search/lucene/"

    query = "Cisco"

    data = {
      "query": query,
      "apiKey": self.__api_key,
    }

    return self.do_post(url, json_data=data)



  def do_search_by_name(self, software, version):
    """
    https://vulners.com/docs/api_reference/search_strategies/#get-vulnerabilitiesexploits-by-software-name-and-version
    """
    url = f"{self.__api_url}/api/v3/burp/softwareapi/"
  
    data = {
      "software": software, 
      "version": version, 
      "type": "software", 
      "maxVulnerabilities": 5000,
      "only_ids": True,
      "apiKey": self.__api_key,
    }

    return self.do_post(url, json_data=data)


