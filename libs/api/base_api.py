import datetime
import time 
import json
import datetime
import requests
import os



class BaseApi:
  """
  Base API integration

  """
  # Next valid request time (when using rate limiting)
  __next_time = datetime.datetime.now()
  # Headers
  __headers = {}
  # Rate limiting delay (in milliseconds)
  __request_delay = 0 
  # log requests
  __log = int(os.getenv("LOG_REQUESTS", 0))


  def __init__(self, headers={}, request_delay=0):
    self.__headers = headers
    self.__request_delay = request_delay



  def do_get(self, url) -> dict:
    """
    do get request 
    :returns: response
    """
    self.__sleep_until_next()
    response = requests.get(url, headers=self.__headers)
    self.__update_next_time()
    if self.__log == 1: print(f"\nGET {url}\n")
    res = self.__parse_response(response.text)
    if self.__log == 1: print(res)
    if self.__log == 1: print("\n")
    return res



  def do_post(self, url, json_data=None, files=None, data=None) -> dict:
    """
    do post request 
    
    :returns: response
    """

    self.__sleep_until_next()
    response = requests.post(url, json=json_data, data=data, files=files, headers=self.__headers)
    self.__update_next_time()
    if self.__log == 1: print(f"\nPOST {url}\n")
    res = self.__parse_response(response.text)
    if self.__log == 1: print(res)
    if self.__log == 1: print("\n")
    return res



  def __parse_response(self, response_text):
    """
    Parse response json text

    :returns: dict
    """

    text = json.loads(response_text)

    if "result" in text and text["result"] == "error":
      return text["data"]

    # print(json.dumps(text, indent=2))
    return text
  


  def __update_next_time(self):
    """
    Set next call deplay 
    4 req/sec is the rate limit of the virus total API

    """
    if self.__request_delay == 0:
      return

    self.__next_time = datetime.datetime.now() + datetime.timedelta(0, 0, 0, self.__request_delay)
    return



  def __sleep_until_next(self):
    """
    Sleep until next request is allowed 
    4 req/sec is the rate limit of the virus total API

    """
    if self.__request_delay == 0:
      return

    if self.__next_time > datetime.datetime.now():
      diff = self.__next_time - datetime.datetime.now()
      time.sleep(diff.total_seconds())

    return


