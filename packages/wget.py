import urllib.request

url = input()

try:
  with urllib.request.urlopen(url) as response:
      # Read and decode bytes to text string
      content = response.read().decode('utf-8')
except Exception as e:
  print("Error: " + str(e))

print(content)
