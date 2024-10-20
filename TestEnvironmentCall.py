from alerter import alert_in_celcius, alert_failure_count
def CallMainFunctionFromTestEnv():
  previous_alert_failure_count = alert_failure_count  
  alert_in_celcius(400.5)  
  assert (alert_failure_count > previous_alert_failure_count)
if __name__ == "__main__":
  CallMainFunctionFromTestEnv()

  
