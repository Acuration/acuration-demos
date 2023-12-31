import json
from crawl import crawl
from summarize_text import summarize

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
  'what are the business models of the company SunSource Energy', # partially done
  'What are the revenue streams of the company SunSource Energy?', # not done
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

# company_file = open(r'C:\Users\admin\Desktop\ACURATION FINAL FOLDER\task-2 serp\SunSourceEnergy.txt', 'a', encoding='utf-8')

folder_path = r'C:\Users\admin\Desktop\ACURATION FINAL FOLDER\task-2 serp\json_resps'
for i in range(18, len(queries)):
    print(queries[i])
    with open(r'C:\Users\admin\Desktop\ACURATION FINAL FOLDER\task-2 serp\SunSourceEnergy.txt', 'a', encoding='utf-8') as company_file:
        with open(r'{}\{}.json'.format(folder_path, i+1)) as json_file:
            data = json.load(json_file)
            print('loaded json file')
        # print(data)
        
        question = data['search_parameters']['q']
        # print(f'{i+1}: ', question)

        company_file.write(question+'\n')

        if 'answer_box' in data:

            company_file.write(f'\tAnswer Box:\n')
            if 'answer' in data['answer_box']:
                company_file.write(f'\t\t\Answer: {data["answer_box"]["answer"]}\n')

            if 'title' in data['answer_box']:
                company_file.write(f'\t\tTitle: {data["answer_box"]["title"]}\n')

            if 'snippet' in data['answer_box']:
                company_file.write(f'\t\tSnippet: {data["answer_box"]["snippet"]}\n')

            if 'link' in data['answer_box']:
                #crawl link
                text, extension = crawl(data['answer_box']['link'])
                summary = summarize(text)
                company_file.write(f'\t\tLink: {data["answer_box"]["link"]}\n')
                company_file.write(f'\t\tSummary of Link: {summary}\n')

            elif 'displayed_link' in data['answer_box']:
                #crawl link
                text, extension = crawl(data['answer_box']['displayed_link'])
                summary = summarize(text)
                company_file.write(f'\t\tLink: {data["answer_box"]["displayed_link"]}\n')
                company_file.write(f'\t\tSummary of Link: {summary}\n')

            company_file.write('\n')

        print('answer box done')
        
        company_file.write(f'\tOrganic results:\n')
        for i in range(len(data['organic_results'])):

            if 'title' in data["organic_results"][i]:
                company_file.write(f'\t\tTitle: {data["organic_results"][i]["title"]}\n')

            if 'snippet' in data["organic_results"][i]:
                company_file.write(f'\t\tSnippet: {data["organic_results"][i]["snippet"]}\n')

            if 'link' in data["organic_results"][i]:
                #crawl link
                text, extension = crawl(data['organic_results'][i]['link'])
                summary = summarize(text)
                company_file.write(f'\t\tLink: {data["organic_results"][i]["link"]}\n')
                company_file.write(f'\t\tSummary of Link: {summary}\n')

            company_file.write('\n')

        print('organic results done')

        company_file.write(f'\tRelated Questions:\n')
        for i in range(len(data['related_questions'])):

            if 'question' in data["related_questions"][i]:
                company_file.write(f'\t\tQuestion: {data["related_questions"][i]["question"]}\n')

            if 'title' in data["related_questions"][i]:
                company_file.write(f'\t\tTitle: {data["related_questions"][i]["title"]}\n')

            if 'snippet' in data["related_questions"][i]:
                company_file.write(f'\t\tSnippet: {data["related_questions"][i]["snippet"]}\n')

            if 'link' in data["related_questions"][i]:
                #crawl link
                text, extension = crawl(data['related_questions'][i]['link'])
                summary = summarize(text)
                company_file.write(f'\t\tLink: {data["related_questions"][i]["link"]}\n')
                company_file.write(f'\t\tSummary of Link: {summary}\n')

            company_file.write('\n')

        print('related results done')

        company_file.write('\n\n')
        print(f'Done json file no {i+1}')
    

