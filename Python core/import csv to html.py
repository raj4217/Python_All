import csv

html_output = ''
names = []

with open('patron.csv', 'r') as readfile:
    # readf = csv.reader(readfile)
    readf = csv.DictReader(readfile)

    # to remove headers and first line of the data (while using list)
    # next(readf)
    # next(readf)

    # for line in readf:
    #     if line[0] == 'No Reward':
    #         break
    #     names.append(f"{line[0]} {line[1]}")

    # to remove first line of the data (while using dict)

    next(readf)

    for line in readf:
        if line['FirstName'] == 'No Reward':
            break
        names.append(f"{line['FirstName']} {line['LastName']}")

html_output += f'<p>There are current {len(names)} contributer. Thanks!</p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'

print(html_output)
