from io import StringIO,BytesIO

s_io = StringIO()
print("hello", file=s_io)
print("world", file=s_io)
s_io.write("hello")

print(s_io.getvalue())
s_io.close()

b_io = BytesIO()
b_io.write("hello".encode('utf-8'))
print(b_io.getvalue().decode('utf-8'))
b_io.close()