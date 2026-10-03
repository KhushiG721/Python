"""
While loop with a condition.

This example demonstrates how a loop continues
until a target condition is reached.
"""

# Initial temperature
temperature = 30

# Target temperature
target_temperature = 25

# Reduce the temperature gradually
while temperature > target_temperature:
    print(f"Current temperature: {temperature}°C")
    temperature -= 1

print(f"Target temperature reached: {temperature}°C")