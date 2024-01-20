def process_csv(file_path):
    print(file_path)
    class_counts = {}
    total_rows = 0

    with open(file_path, 'r') as file:
        next(file)
        for line in file:
            total_rows += 1
            class_value = line.strip().split(',')[-1]
            class_counts[class_value] = class_counts.get(class_value, 0) + 1

    return class_counts, total_rows

diabetes_path = "C:/Users/aakarsh/Desktop/ASE_HW/w3/diabetes.csv"
soybean_path = "C:/Users/aakarsh/Desktop/ASE_HW/w3/soybean.csv"

diabetes_class_counts, diabetes_total_rows = process_csv(diabetes_path)

soybean_class_counts, soybean_total_rows = process_csv(soybean_path)

diabetes_percentage = {cls: (count / diabetes_total_rows) * 100 for cls, count in diabetes_class_counts.items()}
soybean_percentage = {cls: (count / soybean_total_rows) * 100 for cls, count in soybean_class_counts.items()}

print("Diabetes Classes:\n")
for cls, count in diabetes_class_counts.items():
    print(f"{cls}: {count} rows ({diabetes_percentage[cls]:.2f}%)")

print("\nSoybean Classes:\n")
for cls, count in soybean_class_counts.items():
    print(f"{cls}: {count} rows ({soybean_percentage[cls]:.2f}%)")
