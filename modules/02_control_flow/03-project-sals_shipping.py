weight = 41.5

# Ground Shipping
flat_rate_ground = 20.00
if weight <= 2:
  cost_ground = flat_rate_ground + 1.5 * weight
elif weight > 2 and weight <= 6:
  cost_ground = flat_rate_ground + 3 * weight
elif weight > 6 and weight <= 10:
  cost_ground = flat_rate_ground + 4 * weight
else:
  cost_ground = flat_rate_ground + 4.75 * weight

print("Ground Shipping cost: ${0}".format(cost_ground))

# Ground Shipping Premium
cost_ground_premium = 125

print("Ground Shipping Premium cost: ${0}".format(cost_ground_premium))

# Drone Shipping
if weight <= 2:
  cost_drone = 4.5 * weight
elif weight > 2 and weight <= 6:
  cost_drone = 9 * weight
elif weight > 6 and weight <= 10:
  cost_drone = 12 * weight
else:
  cost_drone = 14.25 * weight

print("Drone Shipping cost: ${0}".format(cost_drone))
