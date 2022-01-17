import csv

with open("top_cities.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["rank, city, population"])
    writer.writerows(
        [
            ["1", "Shanhai", "2415000"],
            ["2", "Karachi", "415000"],
            ["3", "Beigin", "115000"],
            ["4", "tenshin", "2415000"],
        ]
    )
