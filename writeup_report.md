# Writeup: Behavioral Cloning 

The goals / steps of this project are the following:
* Use the simulator to collect data of good driving behavior
* Build, a convolution neural network in Keras that predicts steering angles from images
* Train and validate the model with a training and validation set
* Test that the model successfully drives around track one without leaving the road
* Summarize the results with a written report

## Rubric Points

Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/432/view) individually and describe how I addressed each point in my implementation.

### Model Architecture and Training Strategy

#### 1. An appropriate model architecture has been employed

The model constist of the NVIDIA architecture which was provided as an example for the project. Also the _LeNet_ architecture was tested, but dismissed as if did not perform as well as the NVIDIA one. (model.py lines 27-57)

#### 2. Attempts to reduce overfitting in the model

Two strategies were used to address this:
* Recording data on both tracks and doing clock and counter-clockwise runs for the circuits.
* Augmenting the data by using the 3 cameras and also flipping the images horizontaly.

The model was tested by running it through the simulator and ensuring that the vehicle could stay on the track.

#### 3. Model parameter tuning

The model used an adam optimizer, so the learning rate was not tuned manually. Also, the number of epochs was kept small to reduce the training time.

#### 4. Appropriate training data

The complete dataset is composed of 6 diferent recording scenarios:
* (4681 samples) Driving on the center lane on track 1.
* (2605 samples) Driving on the center lane on track 2. 
* (4050 samples) Driving on the center lane on track 1, on the opposite direction.
* (3094 samples) Driving on the center lane on track 2, on the opposite direction.
* (2015 samples) Recordings of properly executed maneuvers on track 1 curves.
* (1380 samples) Recordings of recovery situations, starting from the sides of the road.

Considering each recording sample provides 3 images, the dataset provides ~49000 images. However some of them were manually blacklisted, as they provide wrong use cases.


### Model Architecture and Training Strategy

#### Data

The ~49000 sample images were further augmented to ~98000, by flipping each one horizontaly.
Each image was preprocessed by cropping the top and bottom portions, to ensure the input data only consist of road pixels.


#### Model

The design approach was the same discussed on the lectures. First, a very network was used, just to validate the loading and automated simulation are working. Then, the model was updated to consider the LeNet architecture. As recommended in the lectures, the NVIDIA model was used as a final approach.


#### Training

The dataset was shuffled and split into 80% training data and 20% validation data. The loss for both sets was similar, implying the model was not overfitting: 0.0326 for training and 0.0255 for validation.

The model was verified by running the simulator and driving autonomously the car around track one. This was tested under different velocities: 10 mph, 20 mph, and 30 mph. The car performed well on each case.

