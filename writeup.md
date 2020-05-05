# Writeup

## Data Collection

### Training data

- `/home/workspace` has a small number of inodes and only 3GB available!.
- Data must be saved under `/opt`.
- Data under `/opt` will be

### Considerations
- the car should stay in the center of the road as much as possible
- if the car veers off to the side, it should recover back to center
- driving counter-clockwise can help the model generalize
- flipping the images is a quick way to augment the data
- collecting data from the second track can also help generalize the model
- we want to avoid overfitting or underfitting when training the model
- knowing when to stop collecting more data

### Test Scenarios

- Data from multiple tracks
- Drive counterclockwise
- 2-3 laps of center lane driving
- 1 lap of recovery driving from the sides
- 1 lap on driving smoothly around curves
