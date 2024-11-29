import requests
from bs4 import BeautifulSoup

# Making a GET request
r = requests.get('https://connect2concepts.com/connect2/?type=circle&key=2A2BE0D8-DF10-4A48-BEDD-B3BC0CD628E7', headers={"User-Agent": "XY"})

# check status code for response received
# success code - 200
print(r.status_code)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
text = soup.get_text().splitlines()
clean = []
for s in text:
    if len(s) > 30 and (s[0] == 'M' or s[0] == 'S'):
        clean.append(s)
for i in clean:
    print(i)


# def main(data, context):
#     try:
#         # Making a GET request
#         r = requests.get('https://connect2concepts.com/connect2/?type=circle&key=2A2BE0D8-DF10-4A48-BEDD-B3BC0CD628E7', headers={"User-Agent": "XY"})

#         # check status code for response received
#         # success code - 200
#         print(r.status_code)

#         # Parsing the HTML
#         soup = BeautifulSoup(r.content, 'html.parser')
#         text = soup.get_text().splitlines()
#         clean = []
#         for s in text:
#             if len(s) > 30 and (s[0] == 'M' or s[0] == 'S'):
#                 clean.append(s)
#     except Exception as error:
#         log_message = Template('$error').substitute(error=error)
#         logging.error(log_message)
# if