from transformers import pipeline

summarizer = pipeline('summarization', model="t5-base", tokenizer="t5-base", framework="tf")

text = '''
Suzlon Press Release | Suzlon Energy LTD
Toggle navigation
Media Room
|
Contact Us
|
About
Overview
Group Profile
Vision & Values
History
Awards
Leadership
Call Of The Wind
The Wind Man
Spotlight
CSR
Sustainability
Products
Overview
S144 Wind Turbine Generator
S133 Wind Turbine Generator
S120 Wind Turbine Generator
Classic Fleet
Services
Overview
Operations & Maintenance Services
Leadership
Optimisation & Digitalisation
Value Added Services & Products
Multi Brand O&M Services
End-To-End Solutions
Overview
Research and Development
SUPPLY CHAIN MANAGEMENT & MANUFACTURING
Turnkey Project Services
Solar Energy Solutions
QUALITY MANAGEMENT
Health, Safety & Environment
Investors
Overview
Financial Reports & Presentations
Shareholders Information
Other Disclosures
Investors Helpdesk
Offer Documents
Financials – Subsidiary Companies
Careers
Overview
LIFE at SUZLON
ONE EARTH
Job Opportunities
Recruitment fraud Alert
Global
Overview
ASIA
EUROPE, AFRICA & LATAM
AUSTRALIA
About
Overview
Group Profile
Vision & Values
History
Awards
Leadership
Call Of The Wind
The Wind Man
Spotlight
Sustainability & CSR
Products
Overview
S120 Wind Turbine Generator
Classic Fleet
Services
Overview
Operations & Maintenance Services
Optimisation & Digitalisation
Value Added Services & Products
End-To-End Solutions
Overview
Research and Development
SUPPLY CHAIN MANAGEMENT & MANUFACTURING
Turnkey Project Services
Solar Energy Solutions
QUALITY MANAGEMENT
Health, Safety & Environment
Investors
Overview
Financial Reports
Notices & Announcements
Shareholding Pattern
Investors Helpdesk
Offer Documents
Financials – Subsidiary Companies
Careers
Overview
LIFE AT SUZLON
ONE EARTH
Job Opportunities
Recruitment fraud Alert
GLOBAL
Overview
ASIA
EUROPE
AUSTRALIA
Media Room
Contact Us
Overview
Press Releases
Suzlon in the News
Media Kit
Photo Gallery
Video Gallery
Home
Media Room
Press Release
September 29, 2023
Suzlon Receives the 'Best Construction and Infrastructure Brands - Renewable Energy Suppliers' Award by The Times Group
Pune, India: Suzlon Group,
India's largest renewable energy solutions provider, has been chosen as one of the 'Best Construction and Infrastructure Brands in Renewable Energy Suppliers' category at the 8th Infra Focus Summit and Awards by The Times Group. This honour serves as a testament to Suzlon's unwavering commitment to driving the energy transition and pioneering innovative wind energy technologies.
The award as part of the 8th Infra Focus Summit and Awards 2023 was received by Mr. Rohit Chauhan, Head Business Development India, Suzlon Energy Limited.
Commenting on the recognition, J P Chalasani, Chief Executive Officer, Suzlon Group,
stated, "Every
award is a validation of our commitment to excellence. It is an honour to be recognized as a top renewable energy brand by the esteemed Times Group. This accolade reaffirms our dedication to sustainable energy solutions and our mission to driving a cleaner, greener future. At Suzlon Energy, we continue to innovate and lead the way in renewable energy, ensuring a sustainable and thriving environment for generations to come"
Suzlon Energy strives to drive energy transition with reliable and efficient wind energy solutions. The Company is committed to innovation and revolutionizing the Indian renewable sector focusing on decreasing CO2 emissions and accelerating the national target of 500 GW renewable energy by 2030. Being at the forefront of the industry, pioneering the way for cleaner electricity, reduced carbon footprint, and the growth of green technologies, Suzlon Energy continues its journey towards renewable and cleaner energy sources.
About The Suzlon Group
The Suzlon Group is one of the leading renewable energy solutions providers in the world with more than 20 GW* of wind energy capacity installed across 17 countries. Headquartered at Suzlon One Earth in Pune, India; the Group comprises of Suzlon Energy Limited (NSE: SUZLON & BSE: 532667) and its subsidiaries. A
vertically integrated organisation, with in-house research and development (R&D) centers in Germany, the Netherlands, Denmark and India, Suzlon's world-class manufacturing facilities are spread across 14 locations in India. With over 28 years of operational track record, the Group has a diverse workforce of
nearly 6,000 employees. Suzlon is also India's No. 1 wind energy service Company with the largest service portfolio of over 14 GW of wind energy assets. The Group has ~6 GW of installed capacity outside India. The 3 MW Series wind turbine technology platform is the latest addition to its comprehensive product
portfolio.
*Global installations of Suzlon manufactured wind turbine generators. Data as on 30th June 2023.
Suzlon corporate website: www.suzlon.com
Download
Contact Us
Dharini Mishra
Tel: +91 (20) 67025000
E-mail: ccp@suzlon.com
Share This
Facebook
Twitter
Linked in
E Mail
About Suzlon
Group Profile
Vision & Values
History
Awards
Leadership
Call Of The Wind
The Wind Man
Spotlight
CSR
Sustainability
PRODUCTS
S144 Wind Turbine Generator
S133 Wind Turbine Generator
S120 Wind Turbine Generator
Classic Fleet
Services
Operations & Maintenance Services
Leadership
Optimisation & Digitalisation
Value Added Services & Products
Multi Brand O&M Services
End To End Solutions
Research and Development
Supply Chain Management & Manufacturing
Turnkey Project Services
Solar Energy Solutions
Quality Management
HSE
Investors
Financial Reports & Presentations
Shareholders Information
Other Disclosures
Investors Helpdesk
Offer Documents
Financials – Subsidiary Companies
Careers
Life at Suzlon
One Earth
Job Opportunities
Recruitment fraud Alert
Media Room
Press Releases
Suzlon In The News
Media Kit
Photo Gallery
Video Gallery
Global
Asia
|
Europe, Africa and Latam
|
Australia
© Suzlon Energy Limited 2021
Webmail | Disclaimer | Privacy Policy | Terms of Use | GSTN & Statutory Details |
Contact Us
'''

summary = summarizer(text, max_length=100, min_length=30, do_sample=False)

print(summary)