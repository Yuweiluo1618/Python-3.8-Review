class Person():
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")



with Person() as p_enter:
    print(p_enter)