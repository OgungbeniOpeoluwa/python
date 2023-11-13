with open('demo.txt', mode='w') as files:
    files.write('ope is a good girl\n')
    files.write('uye is a fine girl\n')
    files.write('tobi is a wife beater\n')
    files.write('welcome to c18\n')

with open('demo.txt', mode='r') as files:
    for result in files:
        record, records, results, *value = result.split()
        print(f'{record} {records} {results}  {value} ')

