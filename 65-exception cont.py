import  time
try:
    print(1)
except Exception as e:
    print(e)
else:
    print("no exception run else block")


try:
    f1 = open("finally.txt", 'r')

except Exception as e:

    f1 = open("finally.txt", 'w')

finally:
    f1.close()

try:
    f = open('test.txt')
    try:
        while True:
            con = f.readline()
            if len(con) == 0:
                break
            time.sleep(3)
            print(con)
    except:
        print("accident jump out")

    finally:
        f.close()

except:
    print("file does not exist")