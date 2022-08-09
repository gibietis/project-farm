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

I've created this section for smaller, but important projects that may appear. 

I was talking to my father-in-law about fuel costs and alternatives to diesel, which is skyrocketing worldwide. He told me he has interest in installing solar power systems and replacing his diesel operated irrigation system with a electricity powered one, which would be very expensive at first, but given the current fuel prices, would pay for itself soon enough.

This smaller, yet very important task, comprises calculating: 

- Monthly amount of power needed to mantain the new system.
- The costs of switching from diesel to electricity.
- If installing a solar power system is worth the investment.
