import urllib.request

url = input("URL: ")
destination = input("Destination path: ")

try:
  with urllib.request.urlopen(url) as response:
      # Read and decode bytes to text string
      content = response.read().decode('utf-8')
  rashFS.write(destination, content)
except Exception as e:
  print("Error: " + str(e))

