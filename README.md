# Behavioral Cloning Project

[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)

## Shortcuts

* [Writeup Report](writeup_report.md)
* [Python model creation and training](model.py)
* [Sample video](video.mp4)

## Overview

This repository contains files for the Behavioral Cloning Project.

In this project, you will use what you've learned about deep neural networks and convolutional neural networks to clone driving behavior. You will train, validate and test a model using Keras. The model will output a steering angle to an autonomous vehicle.

We have provided a simulator where you can steer a car around a track for data collection. You'll use image data and steering angles to train a neural network and then use this model to drive the car autonomously around the track.

### The Project

The goals / steps of this project are the following:
* Use the simulator to collect data of good driving behavior 
* Design, train and validate a model that predicts a steering angle from image data
* Use the model to drive the vehicle autonomously around the first track in the simulator. The vehicle should remain on the road for an entire loop around the track.
* Summarize the results with a written report

### Data, Model and Training

Please read the [writeup report], were this is explained further.

## Dependencies

This lab requires: [CarND Term1 Starter Kit](https://github.com/udacity/CarND-Term1-Starter-Kit).

The project was developed under Python 3.6. Required python packages can be installed as using the provideded `requirements.txt` file. It is recommended to use a virtual environment.
```bash
pip3 install -r requirements.txt
```

The simulator can be downloaded from GitHub: https://github.com/udacity/self-driving-car-sim

## Execution

### Train
```bash
python3 model.py
```

### Test in simulator

```bash
# Sim
<run simulator>

# Run Model
python3 drive.py model.h5

# Select autonomous mode in the simulator screen.
```
