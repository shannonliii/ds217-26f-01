measurements = [18, 21, 24, 19]
review_threshold_text = "20"

review_threshold = int(review_threshold_text)
total = 0
review_count = 0

for measurement in measurements:
    total = total + measurement
    if measurement >= review_threshold:
        label = "review"
        review_count = review_count + 1
    else:
        label = "within range"
    print("Measurement:", measurement, label)

mean = total / len(measurements)
print("Count:", len(measurements))
print("Total:", total)
print("Mean:", mean)
print("Review count:", review_count)
