"""
  Author: Marian Menschig
  Date: 2018-01-02

  This module contains helper functions for the retrieval, verification and
  storage of data from Wunderground.
"""
import os
import config
import requests


def fetch_data(url):

  station_country = url[1]
  country_short = url[3]

  QRY_URL = config.BASE_URL.format(config.WUNDERGROUND_KEY, station_country, country_short)
  print("GET Request: " + QRY_URL)
  # TODO: Log this as well

  r = requests.get(QRY_URL)
  
  if r.status_code == 200:
    res = r.json()["current_observation"]
    return res

def does_directory_exist(directory):
    """
    @param {directory}
    """
    cwd = os.getcwd()
    if not os.path.isdir(cwd + directory):
      # Log this
      print(directory + " directory does not exist. Creating it..")
      os.mkdir(cwd + directory)
      print("Created directory!")

def is_valid_data(data):
  pass


def date_to_ISO(date):
  pass
