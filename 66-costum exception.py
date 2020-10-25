class Len_Error(Exception):
    def __init__(self, len, min_len):
        self.len = len
        self.min_len = min_len

    def __str__(self):
        return f"you enter length is {self.len} require length is{self.min_len}"


def main():
    try:
        password = input("enter the password")
        if len(password) < 3:
            raise Len_Error(len(password), 3)
    except Exception as e:
            print(e)
    else:
        print("password ok")

main()