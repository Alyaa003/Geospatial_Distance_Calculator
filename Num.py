import numpy as np

coords_riyadh = np.array([24.7136, 46.6753])
coords_mecca = np.array([21.4225, 39.8262])

coords_riyadh_rad = np.radians(coords_riyadh)
coords_mecca_rad = np.radians(coords_mecca)

R = 6371
dlat = coords_mecca_rad[0] - coords_riyadh_rad[0]
dlon = coords_mecca_rad[1] - coords_riyadh_rad[1]

a = np.sin(dlat / 2)**2 + np.cos(coords_riyadh_rad[0]) * np.cos(coords_mecca_rad[0]) * np.sin(dlon / 2)**2
c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

distance = R * c

print(f"The distance between Riyadh and Mecca is: {distance:.2f} km")
