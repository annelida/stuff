import csv
with open('list_of_urls.txt', 'w') as file:
    writer = csv.writer(file, delimiter='\t', lineterminator='\n',)
    handle = open('infile.txt')
    for urls in handle:
        url = 'http://www.apercite.fr/api/apercite/320x240/yes/' + urls.strip()
        writer.writerow([url])
