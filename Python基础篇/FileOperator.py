
"""
r_file = open("a.txt","r")      #只读

content = r_file.read(20)
print(content)

content_line = r_file.readline()
print(content_line)

content_lines = r_file.readlines()
print(content_lines[1])

for line in content_lines:
    print(line)

a_file = open("a.txt","a")      #追加
#a_file.write("\nyiduo")
#a_file.write("\nerduo")

w_file = open("a.txt","w")
w_file.write("siduo")
"""

w_file = open("b.txt","w")

w_file.close()