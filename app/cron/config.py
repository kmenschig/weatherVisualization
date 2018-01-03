import os


BASE_URL = 'https://api.wunderground.com/api/{0}/conditions/q/{1}/pws:{2}.json'
WUNDERGROUND_KEY = os.environ["WUNDERGROUND_KEY"]

# Used for the calculation of vapor pressure
# at given temperature.
# TODO: @kmenschig: Please provide more context
# as to what "a0" etc stand for
vapor_pressure = {
  "a0": 6.107799961,
  "a1": 4.436518521E-01,
  "a2": 1.428945805E-02,
  "a3": 2.650648471E-04,
  "a4": 3.031240396E-06,
  "a5": 2.034080948E-08,
  "a6": 6.136820929E-11
}