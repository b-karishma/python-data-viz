import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
study_hours = [2, 3, 1, 4, 2, 5, 1]

plt.bar(days, study_hours)
plt.xlabel('Days')
plt.ylabel('Hours Studied')
plt.title('Weekly Study Hours')

plt.savefig("study_hours.png")
plt.show()

