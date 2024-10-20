from alerter import *
def CallMainFunctionFromTestEnv():
  alert_in_celcius(400.5)
  assert (alert_failure_count-1 < 0)
