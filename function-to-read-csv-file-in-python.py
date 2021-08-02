# Open comma separated value files
def open_csv_file(path):
    with open(path, 'r') as f:
        body3 = []
        file_content3 = f.readlines()
        for i in range(len(file_content3)):
            if i == 0:
                headers3 = file_content3[i].strip().split(',')
            else:
                sub_body = []
                for item in file_content3[i].strip().split(','):
                    if item == '':
                        sub_body.append(0.0)
                    else:
                        sub_body.append(float(item))
                body3.append(sub_body)
        data3 = [headers3,body3]
        return data3


# Calling function
data = open_csv_file('./directoryDummy/loan3.txt')


# create dictionary
def dictionary(headers,bodys):
    result = {}
    for head,body in zip(headers,bodys):
        result[head] = body
    return result

------------------------------------------------------------------------------------------------------------------

def read_csv_file(path):
    with open(path, 'r') as f:
        bodyNew = []
        file_contentNew = f.readlines()
        for i in range(len(file_contentNew)):
            if i == 0:
                headersNew = file_contentNew[i].strip().split(',')
            else:
                sub_body = []
                for item in file_contentNew[i].strip().split(','):
                    if item == '':
                        sub_body.append(0.0)
                    else:
                        sub_body.append(float(item))
                bodyNew.append(sub_body)
        
        def create_as_dictionary(headers,bodys):
            result = {}
            for head,body in zip(headers,bodys):
                result[head] = body
            return result
        
        totalNew = []
        for i in range(len(bodyNew)):
            totalNew.append(create_as_dictionary(headersNew,bodyNew[i]))
        
        return totalNew

data = read_csv_file('./directoryDummy/loan3.txt')
print(data)



# Appending element to header
total = []
for i in range(len(body)):
    total.append(dictionary(headers3,body3[i]))


