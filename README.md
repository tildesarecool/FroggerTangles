# FroggerTangles

I decided to keep my updates history from one day to the next. Maybe it will show some part of my evolving thought process
I'm upgrading my box-prototype-frogger to its own repo. It's frogger but made of rectangles. 

This is something of an attempt to create a rudimentary version of "Frogger" using nothing but rectangles in pygame. The rectangles aren't even surfaces, in fact. Everything's a rectangle and that's it.

The green square is supposed to be the frog. 

---

I did a bunch of refactoring around the car spawning system: I'm hoping I'm working up to an approach that will allow me to spawn traffic lanes worth of vehicles at a time such that eventually there will be three car lanes - two moving right/left and one moving left/right. Or the other way around. I am also hoping to vary the vehicle type (car or bus) and go through a range of colors.

Right now there's just one car moving right/left but it is smoothly scrolling in and out so that's an improvement. 

Right now I'm having something of an issue with the initial x coordinate of this vehicle. But I think I have solution to that and when there's an endless queue of vehicles going across the position of the first car won't really be noticable. At least that's what I'm going with. Since it does respawn off the screen to the right.


---

I thought about this a little over night. I don't think I want to spawn in multiple vehicles like it is now. 

Keeping in mind I only have 3 vehicles at the moment. In one continuous line of vehicles this wouldn't really be an issue. 

What I'm saying is: right now the three vehicles start on the right and move left. When the last car goes off screen *all three* vehicles pop into existence at the same time at a specific point. Well technically even that is broken at the moment but you get what I'm 
saying. I don't need them all to pop into existence at the same time, I need a never ending loop of vehicles starting off the screen to the right and scrolling to the left.

So what I *really* need is for each individual car to spawn off screen, roll into the screen on the right, scroll off the left and when it disappears off the left get deleted entirely. 

Or each individual car to get reset in a queue to eventually scroll across the screen. 

Either way I think I need to operate on an individual car basis rather than a group of cars at a time. 

I was trying to think of which way would make randomized vehicles eventually a thing that could be implemented. Deleting each vehicle as they disappeared off screen would free up a place in "line" for an entirely new vehicle.

In other words a queue of vehicles consisting of buses and cars initially with one of 3 colors. At the start of the game the queue is filled with random amounts of buses and cars with random colors. 

Then as each car disappears it's replaced with a new random type with a random color. 

Additional vehicle types and more than 3 colors notwithstanding. 

I'm not sure how much refactoring I have to do to implement this new approach.

It also occurred to me I've already implemented pretty much this exact thing in my semi-original game, "UFO invasion", with the way the bullets work. I'd be doing the same thing but without the spacebar to activate the rectangles and some other mechanism to "fire" the rectangles so they move across the screen. But it's all there: spawning into a group and a particular screen location, moving across the screen at a specific speed, and getting deleted from memory after hitting the edge of the screen. I should really just copy that. 

---

With my lanes solution in place it was fortunately easy to re-adjust the height of the main traffic lane: 3 times the vehicle height plus 30. This way I can have 3 lanes of traffic with some space between each row of traffic. 

As for adding the traffic I still can't get it work quite right. This lead to some re-thinking and a mini-refactoring of the appraoch. I was doing too much in the main.py file for instance so I moved a lot of functionality over to a separate py file. 

My initial idea was the seperate instancess of the vehicle class consisting of at least cars and busses with perhaps other types later: the vehicles types would be randomized so there would be a different combination of vehicle types the as the game played. But now I'm re-thinking the approach to just have one long row of vehicles and the whole thing is a loop. That has some issues too. I'll keep thinking about it. The three test vehicles I have now transition smoothly off the side on the left but just kind of pop into place on right. So I'm still kind of thinking about it. 

The script works that far for the one car. The second two vehicles are just stuck in place. So you could say the script is broken.



