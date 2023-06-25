def read_data():
    
    with open('da.txt', 'r') as f:

        list = f.read().splitlines()

    length_of_list = len(list)

    for line in range(length_of_list):

        content = list[0].replace('figure - 1.', '')

        list.append(content)

        list.remove(list[0])

        print(content)

    f.close()

    return list

def write_data(data):

        with open('db.txt', 'w') as f:

            length_of_data = len(data)

            for i in range(length_of_data):

                if data[0][1] != '(' :

                    num = str(data[0][0]) + str(data[0][1])

                    line = data[0][2:len(data[0])]

                else:
                    #9("Okay 9")
                    num = str(data[0][0])
                    
                    line = data[0][1:len(data[0])]
                    
                data.append("figure - 1."+ str(i+1) + line + '\n')

                data.remove(data[0])

            f.writelines(data)    

            f.close()

if __name__ == '__main__':

    data = read_data()

    data.remove(data[0])

    write_data(data)