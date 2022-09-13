# Electricity Costs Calculator

After a a short period of learning how to code, I've completed the first (and most needed) part of this project: a calculator do find out the costs involved in moving from an old diesel engine to a brand new electric one, given the global skyrocketing in fuel prices.

This calculator inteds to show the current costs, while using the diesel system, the future costs, while relying on electricity, and the costs for switching systems. Things went well and the calculator is up and running.

I wish to make the code cleaner and more concise, but I'm actually very happy with the current result.

You can check out the calculator in this repository.

# Overview

The goal of this project is to create an effective solution to a real-world problem. My father-in-law is a small farmer in the countryside. He works by himself most of the time, without much technological improvement to his work.

Planning crop rotations is surprisingly hard, and most of this planning is done by hand while considering several variables, including the cost and quantity of items such as:

- Type of seed and seed treatment (pesticides)
- Soil correction
- Fertilizers (NPK, KCL, Mo, Zn, Boric Acid, Cobalt, Calcium, Magnesium, etc.)
- Pesticides (herbicides, fungicides, and insecticides)
- Additional workforce during planting and harvest
- Machinery rental (harvesters, trucks, drones)
- Logistics
- Taxes

With these variables sorted, we get an estimated cost-per-hectare of the plantation. By comparing this value to the average productivity of the land, considering the predicted amount of 60 kg sacks yielded by each hectare, along with the average price of the commodity, you get the expected profit.

All of this is done by hand at the moment. 

# Goals

The main goal is to automate all of these calculations, reducing time spent on calculations while also reducing the margin of error. The application is supposed to provide the following information:

- Cost per hectare of a given crop (corn, tomato, potato, soy, beans, etc.)
- Foreseen profits, according to the futures index from the Brazilian Stock Exchange (B3)
- The most profitable plantation to implement at the moment of the calculation, given the variable costs of each crop and commodity prices

It would be nice to bind the application to B3's futures index, so that prices get real-time updates. This will be the most challenging part of the project.

I also intend on hosting this online somehow, so my father-in-law can access it whenever he wants. The website has to be simple by nature, since internet connections in the countryside aren't great (HSDPA, tops).

# Secondary Goals

- Calculator to find out the costs of replacing the old diesel powered pump with an electricity powered pump - DONE!