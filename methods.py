hello_world = ['Hello, World!']
sample_list = [1, '2', 5, 5, 'jeronimo', hello_world]

print(sample_list)  # [1, '2', 5, 5, 'jeronimo', ['Hello, World!']]
sample_list.pop(4)  # [1, '2', 5, 5, 'jeronimo']
sample_list.append(hello_world)  # [1, '2', 5, 5, 'jeronimo', ['Hello, World!']]
sample_list.remove(5)  # [1, '2', 5, 'jeronimo', ['Hello, World!']]
sample_list.count(hello_world)  # 1
sample_list.count('hello_world')  # 0
