import requests

def get(endpoint, params, clientcert, cacert, timeout):
  res = requests.get(endpoint, params=params, cert=clientcert, verify=cacert, timeout=timeout)
  return res
