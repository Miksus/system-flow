
# System Flow

> System Dynamics package for Python!

> Syntatically clean and simple Python package for modelling complex multidomain dynamic systems.

> Simulation, System Dynamics, Modelling


---

## Example

```python
import systemflow as sf

# Define Stocks 
clouds = sf.Stock("clouds", initial_value=500)
lake = sf.Stock("lake", initial_value=50)

# Link the stocks
rain = clouds >> lake

# Create flow logic to the links
condensation = clouds * 0.2

# Set the logic to the flow's 
rain.valve = condensation

# Simulate and display results
system = sf.System(rain, stop=20)
system.simulate()
system.plot()
```
![Example](docs/img/readme_fig.png "Rain Simulation")

System Flow uses extensively the Python's magic methods. Even though magic method "```>>```"  is a bitwise operation, it also resembles a transition and for this reason it was chosen to resemble a flow when used between stocks. The core idea of System Flow is to make the making system dynamics models as easy as writing it down on a paper. Of course there is extensive GUI for it in MATLAB but this package is for those who prefer open source over commercial products.

---
## Terminology
- Stock: A container for value
- Flow: A link from one Stock to another
    - Valve: attribute of a Flow that controls how much value is passed through per time step. Can be constant or varying using computators.
- Computator: computation class for computing the values of valves or used for analytical purposes. Do not affect the stocks directly and produces values on demand.
- System: collection stocks, flows and computators that form a system. Used for the actual simulation.

### Analogy: Water treatment plant
- Stock can be thought as a water container.
- Flow can be thought as a pipe that transport water from one container (stock) to another.
    - valve is like a valve in this pipe: controls the amount of water flowing per second through the pipe.
- Computator is kind of the wirings and sensors of the plant: does not directly affect the amount of water in each container but can be used to control how much the valve is open in each moment. It also can be used to show things like how much water is in the plant in total.
- System is all the components in the plant.

---
## Alchemy
> Creating Flows from Stocks
```python
a = sf.Stock("a", initial_value=5)
b = sf.Stock("b", initial_value=5)
a >> b
# Same as Flow(a, b)
```

> Creating Computator from Stocks
```python
a = sf.Stock("a", initial_value=5)
b = sf.Stock("b", initial_value=5)
a + b
# Computator for a.value + b.value 
```
