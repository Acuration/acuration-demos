import serpapi
import json
import os

def store_jsons(query, folder_path, json_filename):
  if not os.path.exists(r'{}\{}'.format(folder_path, json_filename)):
    params = {
      "engine": "google",
      "q": query,
      "api_key": "a9304fd53f1001b20d55b12afdee1beb0b711fcac98bf3f48b4d100938bc3751"
    }

    search_ans = serpapi.search(params)
    # results = search_ans.as_dict()

    with open(r'{}\{}'.format(folder_path, json_filename), 'w') as f:
      json.dump(search_ans.as_dict(), f, indent=4)
  else:
    print('Json file already exists!')


queries = [
  'What is the official website of the company SunSource Energy?',
  'key people in the company sunsource energy',
  "Where is the Headquarters' location of SunSource Energy?",
  'What are the products and services of the company SunSource Energy?',
  'What is the unique selling point (USP) of the company SunSource Energy?',
  'What is the value proposition of the company SunSource Energy?',
  'Who is the target market of the company SunSource Energy?',
  'What is the market size of the company SunSource Energy?',
  'What is the competitive landscape in which SunSource Energy is working?',
  'what are the business models of the company SunSource Energy',
  'What are the revenue streams of the company SunSource Energy?',
  'What is the pricing model of the company SunSource Energy?',
  'What is the share price of the company SunSource Energy?',
  'What is the profit margin of the company SunSource Energy?',
  'What is the total user base of the company SunSource Energy?',
  'How many paying customers does the company SunSource Energy have?',
  'What are the social media platforms links of the company SunSource Energy?',
  'How many followers does the company SunSource Energy have on all social media platforms?',
  'What is the funding info of the company SunSource Energy?',
  'What is the vision and mission of the company SunSource Energy?',
  'What are the key capabilities of the company SunSource Energy?',
  'What is the marketing strategy of the company SunSource Energy?',
  'What is the business strategy of the company SunSource Energy?',
  'Does the company SunSource Energy have any collaborations or partnerships?',
  'What is the cash flow of the company SunSource Energy?'
]

for i in range(25):
  print(f'{i+1}: {queries[i]}')
  store_jsons(queries[i], r'C:\Users\admin\Desktop\ACURATION FINAL FOLDER\task-2 serp\json_resps', f'{i+1}.json')

