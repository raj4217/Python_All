import requests
import csv
from bs4 import BeautifulSoup as bs

# csv_file = open('scrp.csv', 'w', newline='')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['Tutorials', 'Description', 'Links'])


def scrapp(url):
    source = requests.get(url).text
    soup = bs(source, 'lxml')
    title1 = []
    data1 = []
    link1 = []
    title2 = []
    data2 = []
    link2 = []
    for content in soup.find_all('div', class_='card-panel hoverable'):
        while 'container-fluid' not in soup:
            title1.append(content.find('span', class_='card-title').strong.text)
            data1.append(content.find('div', class_='card-content').p.text)
            ln = content.find('div', class_='card-action').a['href']
            link1.append(f'https://pythonprogramming.net{ln}')

    return title1, data1, link1,


# scrapp('https://pythonprogramming.net')

main_t, main_d, main_l = scrapp('https://pythonprogramming.net')
temp = main_l.copy()
while len(temp) != 0:
    for url in temp:
        t, d, l = scrapp(url)
    main_t = main_t + t
    main_d = main_d + d
    main_l = main_l + l
    temp = l.copy()

print(main_t, main_d, main_l)


# print(f'{t}\n\n{d}\n\n{l}\n\n{temp_t}\n\n{temp_d}\n\n{temp_l}')

# csv_writer.writerow([title, data, link])


# csv_file.close()
