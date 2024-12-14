import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
revenue = [100, 200, 300, 400, 500]

plt.plot(months, revenue, marker="o", label="Revenue")
plt.title("Company Revenue")
plt.xlabel("Months")
plt.ylabel("Revenue")
plt.legend()
plt.show()