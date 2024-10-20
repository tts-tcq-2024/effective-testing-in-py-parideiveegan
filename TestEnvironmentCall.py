from alerter import alert_in_celcius, alert_failure_count
def CallMainFunctionFromTestEnv():
  alert_in_celcius(400.5)
  assert (alert_failure_count-1 < 0)
if __name__ == "__main__":
  CallMainFunctionFromTestEnv()

  
