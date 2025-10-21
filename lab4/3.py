from matplotlib import pyplot as plt

trains = ['ДР1Б', 'ДРБ1', 'ДР1А', 'ЭР9Е', 'ДДБ1', 'ЭР9Т']

data = [23, 17, 35, 29, 12, 41]

fig = plt.figure(figsize=(10, 7))
plt.pie(data, labels=trains)
plt.title('Пригородные поезда')

plt.show()