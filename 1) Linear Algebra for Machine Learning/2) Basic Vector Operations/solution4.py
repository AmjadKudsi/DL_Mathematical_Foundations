# use vector addition to find their average scores in each subject

import numpy as np

# Vectors representing scores of two students in three subjects
student1_scores = np.array([75, 80, 85])
student2_scores = np.array([90, 78, 88])

# TODO: Find combined scores using vector addition
combined = student1_scores + student2_scores

# TODO: Find the average scores by multiplying the combined scores by 1/2
avg = combined / 2

# TODO: Display the average scores
print("Average Scores: ", avg)