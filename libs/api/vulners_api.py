import os
from libs.api.base_api import BaseApi



class VulnersApi(BaseApi):
  """
  Vulners API integration

  """

  __apiKey = os.getenv("API_KEY_VULNERS", "")



  def __init__(self):
    headers = {
      "accept": "application/json",
    }
    super().__init__(headers)



  def do_search(self):
    url = "https://vulners.com/api/v3/search/lucene/"

    query = "Cisco"

    data = {
      "query": query,
      "apiKey": self.__apiKey,
    }

    return self.do_post(url, json_data=data)



  def do_search_by_name(self, software, version):
    """
    https://vulners.com/docs/api_reference/search_strategies/#get-vulnerabilitiesexploits-by-software-name-and-version
    """
    url = "https://vulners.com/api/v3/burp/softwareapi/"
    # url = "https://api-mock-1.0x100.ru/vulners.com/api/v3/burp/softwareapi/"
  
    data = {
      "software": software, 
      "version": version, 
      "type": "software", 
      "maxVulnerabilities": 5000,
      "only_ids": True,
      "apiKey": self.__apiKey,
    }

    return self.do_post(url, json_data=data)


