file_inputs = open('input.txt')
values = [int(b.rstrip()) if b not in ('','\n') else -1 for b in file_inputs.readlines()]
file_inputs.close()
value_counts = {b:values.count(b) for b in set(values)}
print(value_counts)

input()