def read_data():
    with open('db.txt', 'r') as f:

        content = f.read().splitlines()

    f.close()

    return content

# def ass_data(to_remove):
    
#     for i in range(len(to_remove)):

#         num = to_remove[i][len(to_remove[i])-1]

#         print(num)

def ass_data(to_remove):
    
    for i in to_remove:

        num = 1

        length = len(i)

        for j in i:

            if ord(i[length - num]) >= 48 and ord(i[length - num]) <= 57:

                print(i[length - num])

                num = num + 1

            else:

                break
            


if __name__ == '__main__':

    data = read_data()

    ass_data(data)

    # okay = True
    # while okay == True:

    #     try:

    #         remove_item = int(input("Enter data to pop:"))

    #         okay = False

    #     except Exception as error:

    #         print(error)


