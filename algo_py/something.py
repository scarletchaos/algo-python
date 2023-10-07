from algo_py import q

st = q.Queue()

for i in range(10):
    st.push(i)
print(st)

while not st.isEmpty():
    print(st.pop())

