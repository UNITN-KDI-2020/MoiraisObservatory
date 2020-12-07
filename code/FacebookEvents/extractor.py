import facebook_events_scraper as sc
import json
import time 

driver = sc.driver('./chromedriver')

event_urls = [
    "https://www.facebook.com/events/442646183573774",
    "https://www.facebook.com/events/119061183165620/",
    "https://www.facebook.com/events/367546061252509/",
    "https://www.facebook.com/events/802522200323292/",
    "https://www.facebook.com/events/781389142591365/",
    "https://www.facebook.com/events/279219430101617/",
    "https://www.facebook.com/events/183993549943591/",
    "https://www.facebook.com/events/3021076944663769/",
    "https://www.facebook.com/events/581245542747775/",
    "https://www.facebook.com/events/756326468432319/",
    "https://www.facebook.com/events/147690982536063/",
    "https://www.facebook.com/events/355864681668421/",
    "https://www.facebook.com/events/1821151754701683/",
    "https://www.facebook.com/events/1262094610521833/",
    "https://www.facebook.com/events/232678604034073/",
    "https://www.facebook.com/events/375869966960695/",
    "https://www.facebook.com/events/1243399506045392/",
    "https://www.facebook.com/events/667724533948337/",
    "https://www.facebook.com/events/165082432004468/",
    "https://www.facebook.com/events/401666710962331/",
    "https://www.facebook.com/events/726574938275467/"
]

events = []
for event_uri in event_urls:
    response_data = sc.event_info(driver, link = event_uri)
    events.append(response_data)

with open('data.json', 'w') as outfile:
    json.dump(events, outfile)