# Observant Systems


For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms need to be aware of.

In Lab 5 part 1, we focus on detecting and sense-making.

In Lab 5 part 2, we'll incorporate interactive responses.


## Prep

1.  Pull the new Github Repo.
2.  Read about [OpenCV](https://opencv.org/about/).
3.  Read Belloti, et al's [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf)

### For the lab, you will need:

1. Raspberry Pi
1. Raspberry Pi Camera (2.1)
1. Microphone (if you want speech or sound input)
1. Webcam (if you want to be able to locate the camera more flexibly than the Pi Camera)

### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.


## Overview
Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A
### Play with different sense-making algorithms.

I tested the object detection example. 
I used the noWindow version, and the terminal outputs 'finished a frame'. 

#### Filtering, FFTs, and Time Series data. (beta, optional)
Additional filtering and analysis can be done on the sensors that were provided in the kit. For example, running a Fast Fourier Transform over the IMU data stream could create a simple activity classifier between walking, running, and standing.

Using the set up from the [Lab 3 demo](https://github.com/FAR-Lab/Interactive-Lab-Hub/tree/Spring2021/Lab%203/demo) and the accelerometer, try the following:

**1. Set up threshold detection** Can you identify when a signal goes above certain fixed values?

**2. Set up averaging** Can you average your signal in N-sample blocks? N-sample running average?

**3. Set up peak detection** Can you identify when your signal reaches a peak and then goes down?

Include links to your code here, and put the code for these in your repo--they will come in handy later.

#### Teachable Machines (beta, optional)

### Part B
### Construct a simple interaction.

**Describe and detail the interaction, as well as your experimentation.**
I tried out the OpenCV sample provided. 
My experimentation is a fruit recognizer: it could recognize different fruits through the camera. I have trained the model with four different kinds of fruits - orange, banana, pear and carrots. 

Video of the model: 
https://youtu.be/S4Lv6lRrNtw

### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note your observations**:
For example:
1. When does it what it is supposed to do?

Most of the time, it does what it is supposed to do, I guess it it's because the objects are rather simple and distinct from each other. 

3. When does it fail?

It fails when 

5. When it fails, why does it fail?


S

4. Based on the behavior you have seen, what other scenarios could cause problems?

**Think about someone using the system. Describe how you think this will work.**
1. Are they aware of the uncertainties in the system?

Maybe not. People might want the model to work at 100% accuracy and would feel frustrated when it is not. 

2. How bad would they be impacted by a miss classification?



3. How could change your interactive system to address this?


4. Are there optimizations you can try to do on your sense-making algorithm.



### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for?

The fruit recognizer can be used in a smart fridge, where it detects what is in the fridge and tells you, or even generates recipes for you to let you know what you could make out of the food in your fridge. 

* What is a good environment for X?

An ideal environment would have enough lightning, and nothing is blocking the fruit from being recognized by the camera. 

* What is a bad environment for X?

Dim, Dark environment; shaky camera; blocking of the fruit. 

* When will X break?

It will likely break when put in a bad enironmnent. 

* When it breaks how will X break?

It will output wrong label of the recognized fruit. 

* What are other properties/behaviors of X?



* How does X feel?

X should include a screen on the fridge, and a in-built camera (or cameras) that is hidden but also takes in all the things in the fridge perfectly. 

### Part 2.

**Include a short video demonstrating the finished result.**

1. Are they aware of the uncertainties in the system?

Maybe not. People might want the model to work at 100% accuracy and would feel frustrated when it is not. 

2. How bad would they be impacted by a miss classification?

The user would be frustrated and disappointed by the system, to say the least. They might get wrong labels of the fruit, which result in wrong generations of the recipe for the smart fridge. People might decide to make something out of the stuff in the fridge only to open the fridge and find out they don't have that ingredient. 

3. How could change your interactive system to address this?

One of the main changes that could be made would be to improve the model accuracy. 

4. Are there optimizations you can try to do on your sense-making algorithm.

I could use more training data in different light conditions and angles - currently I have only ~100 images per class, with pictures taking at day & night. I should try different light sources and light intensity and record more models for training. 
