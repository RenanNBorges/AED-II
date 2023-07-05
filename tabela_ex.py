from tabela import Table


test_table = Table(10)

test_table.insert("ABC1234", ("VW", "GOL", 2010, "Anderson"))
test_table.insert("DFG6789", ('FIAT', 'UNO', '2001', 'Maria'))
test_table.insert("JKL0077", ('FIAT', 'UNO', '2001', 'Maria'))
test_table.insert("UTY2345", ('FIAT', 'UNO', '2001', 'Maria'))
test_table.insert("XYZ4567", ('FIAT', 'UNO', '2001', 'Maria'))
print(test_table)
test_table.insert("XYZ4567", ('FORD', 'FOCUS', '2007', 'Carlos'))
print(test_table)

test_table.insert("DFG6789", ('FIAT', 'UNO', '2001', 'Maria'))
test_table.insertion_sort()
print(test_table)
print(test_table.binary_search('XYZ4567'))
