N = 50
x = np.linspace(0, N, N)
y = np.abs(np.random.randn(N))

factor = 0.7
n = round(N * factor)
x_train, x_test = x[:n], x[n:]
y_train, y_test = y[:n], y[n:]


def metric_mae(y, y_fit):
    return np.mean(np.abs(y - y_fit))

def metric_rmse(y, y_fit):
    return np.sqrt(np.mean((y - y_fit)**2))

fig, axes = plt.subplots(1,2, figsize=(10, 6))
axes[0].plot(x, y, "ro", label="real")
errors = {x: [] for x in ("degree", "train", "test")}
for deg in (0, 1, 2, 3, 5, 8, 12):
    coefs = polyfit(x_train, y_train, deg, full=False)
    y_hat = np.sum(np.array([c * x ** (n) for n, c in enumerate(coefs)]), axis=0)
    errors["degree"].append(deg)
    errors["train"].append(metric_rmse(y_train, y_hat[:n]))
    errors["test"].append(metric_rmse(y_test, y_hat[n:]))
    axes[0].plot(x, y_hat, label=f"n = {deg}")
axes[0].legend()
axes[0].axvline(n, ls="--", color="b")
axes[0].set_yscale("log")
axes[1].set_yscale("log")
axes[1].bar([x - 0.25 for x in errors["degree"]], errors["train"], width=0.4, color='b', align='center', label="train")
axes[1].bar([x + 0.25 for x in errors["degree"]], errors["test"],  width=0.4, color='g', align='center', label="test")
axes[1].legend()
axes[1].set_xlabel("Degree")
axes[1].set_ylabel("Root Mean Squared Error")
fig.suptitle("Runge's Phenomenon")
plt.show()
