# Fixed version: ensure Y arrays are column vectors consistently.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import Matern, ConstantKernel as C, WhiteKernel
from scipy.stats import norm

def f(x):
    x = np.array(x)
    return (np.sin(3 * x) * (1 - x) + 0.5 * x**2).ravel()

bounds = np.array([[0.0, 1.0]])
rng = np.random.RandomState(42)
n_init = 5
X_init = rng.uniform(bounds[0,0], bounds[0,1], size=(n_init, 1))
y_init = f(X_init).reshape(-1,1)  # column vector

kernel = C(1.0, (1e-3, 1e3)) * Matern(length_scale=0.2, nu=2.5) + WhiteKernel(noise_level=1e-6, noise_level_bounds=(1e-8,1e-1))
gp = GaussianProcessRegressor(kernel=kernel, normalize_y=True, n_restarts_optimizer=5, random_state=0)

def expected_improvement(X, X_sample, Y_sample, gp, xi=0.01):
    mu, sigma = gp.predict(X, return_std=True)
    sigma = sigma.reshape(-1, 1)
    mu = mu.reshape(-1, 1)
    Y_sample = Y_sample.reshape(-1, 1)
    mu_sample_opt = np.max(Y_sample)
    with np.errstate(divide='warn'):
        imp = mu - mu_sample_opt - xi
        Z = imp / sigma
        ei = imp * norm.cdf(Z) + sigma * norm.pdf(Z)
        ei[sigma == 0.0] = 0.0
    return ei.ravel()

def propose_location(acq_func, X_sample, Y_sample, gp, bounds, grid_size=1000):
    x_grid = np.linspace(bounds[0,0], bounds[0,1], grid_size).reshape(-1,1)
    ei = acq_func(x_grid, X_sample, Y_sample, gp)
    ind_best = np.argmax(ei)
    return x_grid[ind_best].reshape(1,1), x_grid, ei

max_iter = 8
X_sample = X_init.copy()
Y_sample = y_init.copy()

history_best = [np.max(Y_sample)]

for i in range(max_iter):
    gp.fit(X_sample, Y_sample)
    x_next, x_grid, ei_vals = propose_location(expected_improvement, X_sample, Y_sample, gp, bounds)
    y_next = f(x_next).reshape(-1,1)
    X_sample = np.vstack((X_sample, x_next))
    Y_sample = np.vstack((Y_sample, y_next))
    history_best.append(np.max(Y_sample))

gp.fit(X_sample, Y_sample)

X_plot = np.linspace(bounds[0,0], bounds[0,1], 1000).reshape(-1,1)
y_true = f(X_plot)
mu, sigma = gp.predict(X_plot, return_std=True)

plt.figure(figsize=(10, 5))
plt.plot(X_plot, y_true, linewidth=1, label="True function")
plt.plot(X_plot, mu, linewidth=1, label="GP mean")
plt.fill_between(X_plot.ravel(), mu - 1.96*sigma, mu + 1.96*sigma, alpha=0.3, label="GP 95% CI")
plt.scatter(X_sample, Y_sample, marker='x', s=80, label="Sampled points")
plt.title("Bayesian Optimization (1D) — GP posterior and samples")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 4))
iters = np.arange(0, len(history_best))
plt.plot(iters, history_best, marker='o')
plt.title("Convergence: Best observed value vs iteration")
plt.xlabel("Iteration")
plt.ylabel("Best observed f(x)")
plt.grid(True)
plt.tight_layout()
plt.show()

best_index = int(np.argmax(Y_sample))
best_x = X_sample[best_index, 0]
best_y = Y_sample[best_index, 0]

print(f"Best found x = {best_x:.6f}, f(x) = {best_y:.6f} after {max_iter} BO iterations (plus {n_init} initial samples).")
