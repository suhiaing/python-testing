if __name__ == '__main__':
    try:

        l = []

        for i in range(1,11):

            l.append('figure - 1.' + str(i) +'\n')

            print(l)

        with open('db.txt', 'w') as f:

            f.writelines(l)    

            f.close()

    except Exception as e:

        print(e)