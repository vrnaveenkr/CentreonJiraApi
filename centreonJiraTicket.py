import requests
import sys

def ticketcreate(id,summary,desc):

    url = "http://10.10.100.108:8085/rest/api/2/issue/"

    payload = "{\r\n    \"fields\": {\r\n       \"project\":\r\n       {\r\n          \"id\": \""+id+"\"\r\n       },\r\n       \"summary\":\""+summary+"\",\r\n       \"description\":\""+desc+"\",\r\n       \"issuetype\": {\r\n          \"id\": \""+id+"\"\r\n       }\r\n   }\r\n}"

    headers = {
    'Authorization': 'Basic dnJuYXZlZW5rcjpXZWxjb21lQDE=',
    'Content-Type': 'application/json',
    'Cookie': 'JSESSIONID=1FB69227EAFB08832449C11941491A0E; atlassian.xsrf.token=B48Y-IYW6-CN2L-TJXQ_72a4dc92a01eb34b8086accd892be987455cf0f5_lin'
    }

    response = requests.request("POST", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))

if __name__ == '__main__':
    id = str(sys.argv[1])
    summary = str(sys.argv[2])
    desc = str(sys.argv[3])
    ticketcreate(id,summary,desc)
