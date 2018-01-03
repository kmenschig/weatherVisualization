import os
import sys
import datetime
import requests
import logging
import config
import utilities
import pymysql.cursors
from dateutil import parser

# TODO: place this in separate module so other functions can access
# Checks if log directory exists
utilities.does_directory_exist('/app/cron/logs')

# Sets up logging
logging.basicConfig(
  filename='app/cron/logs/log.log',
  # TODO: change time format
  format='%(asctime)s [%(levelname)s] %(message)s',
  level=logging.DEBUG)


# Instantiating connection to MySQL db
connection = pymysql.connect(
  host="localhost",
  user="root",
  password="administrator",
  db="weather")

try:
  with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM weather_stations")
    stations = cursor.fetchall()

    # If there are no weather stations
    if len(stations) == 0:
      # TODO: log this to log file as well
      logging.info("No stations exist! Exiting..")
      print("No stations exist! Exiting gracefully..")
      sys.exit(0)

finally:
  connection.close()

for station in stations:
  res = utilities.fetch_data(station)

  logging.info(("Fetching data for '{0}' with station id '{1}'").format(station[1], station[3]))
  # logging.info(("Wunderground API responded with: {0}").format(utilities.fetch_data(station))) # Potentially too verbose
  print(res)
