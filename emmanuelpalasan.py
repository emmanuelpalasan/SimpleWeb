import requests

url = "https://pixabay.com/api/?key=30096817-8a042463bc564ca36e8a85070&q=landscape&image_type=vector&orientation=horizontal&editors_choice=true&per_page=3"

payload={}
headers = {
  'Cookie': '__cf_bm=x0GhgzT7t38TRjZYa5oU9OK107vndD8nT9Gr7K7JVZY-1668666364-0-ARo3Yll/Qvi/WkuueTiPsDfdffByUFS7Mc98Yi5a7ODp17xv3wWpc3/oGRFK8IBI4U6biRrcyC81k7Mc/Rs5HZA=; anonymous_user_id=None; csrftoken=ppAsvhgo3eTNN2cMbWyncXEsxHl4IN3YzO5Y7QoIU6IvQdjdwtp8LyOhc1Wd4D45'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
