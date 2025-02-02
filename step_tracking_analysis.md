# My Weekly Step Tracking Analysis

## Introduction
Welcome to my personal step tracking analysis! This document explores my walking activity over the past week and compares it with my friends' data. I used my *smartwatch* to collect this data and analyzed it using **Python**.

## Methodology
The data was collected using the following methods:
1. Continuous step tracking via smartwatch
2. Daily synchronization with phone app
3. Data export to CSV format
4. Analysis using Python pandas

## Data Overview

Here's my daily step count for the week:

| Day       | Steps  | Goal Met |
|-----------|--------|----------|
| Monday    | 8,542  | Yes      |
| Tuesday   | 7,891  | No       |
| Wednesday | 12,405 | Yes      |
| Thursday  | 9,876  | Yes      |
| Friday    | 6,543  | No       |
| Saturday  | 15,234 | Yes      |
| Sunday    | 4,567  | No       |

## Key Findings

### Personal Achievement
- Highest step count: 15,234 (Saturday)
- Lowest step count: 4,567 (Sunday)
- Average daily steps: 9,294

### Comparison with Friends
> "Walking with friends is the best motivation!" - Sarah, top stepper

My friends' performance:
- Sarah: 12,000 avg. steps/day
- Mike: 8,500 avg. steps/day
- Lisa: 9,800 avg. steps/day

## Data Analysis Code

Here's the Python code used for the analysis:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Sample data analysis
def analyze_steps(data):
    avg_steps = data['steps'].mean()
    max_steps = data['steps'].max()
    return avg_steps, max_steps
```

## Visualization
![Weekly Step Count Graph](step_graph.png)

## Resources
For more information about step tracking and health benefits, visit [World Health Organization](https://www.who.int/news-room/fact-sheets/detail/physical-activity)

## Future Goals
To improve my step count, I plan to:
1. Take the stairs instead of elevator
2. Walk during phone calls
3. Join weekend hiking groups

## Tools Used
The analysis was performed using `pandas` and `matplotlib` in Python.
