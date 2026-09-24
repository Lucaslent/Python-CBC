import numpy as np
import matplotlib.pyplot as plt

ada_lovelance_np = 0.0028
alan_turing_np = 0.002264

aceleracion_ada = 100 / ada_lovelance_np
aceleracion_alan = 100 / alan_turing_np

fig, ax = plt.subplots()
ax.bar(["Aceleracion Alan", "Aceleracion Ada"],[aceleracion_alan,aceleracion_ada])
ax.grid()
ax.set_title("Aceleracion")
ax.legend()
plt.show()
