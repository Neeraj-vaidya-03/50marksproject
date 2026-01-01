
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

disease_data = pd.read_csv("Heart_Disease_Prediction.csv")

def main_menu():
    print("\n------ Welcome to Heart Disease Prediction Project ------")
    print("1. View the dataset")
    print("2. Analyze the dataset")
    print("3. Show patients with Chest pain > 3")
    print("4. Show patients with high Cholesterol (> 150)")
    print("5. Data visualization (Matplotlib)")
    print("6. Data visualization (Seaborn)")
    print("Type 'exit' to quit")

def view_dataset():
    x = input("Do you want to view the dataset? (yes/no): ").lower()
    if x == 'yes':
        print(disease_data)
    else:
        print("Dataset view skipped.")

def analyze_dataset():
    print("\nDataset Analysis:")
    print(disease_data.describe())

def show_chest_pain_detail():
    print("\nPatients with Chest pain type > 3")

    if "Chest pain type" not in disease_data.columns:
        print("Chest pain column not found!")
        return

    result = disease_data[disease_data["Chest pain type"] > 3]

    if result.empty:
        print("No patients found.")
    else:
        print(f"Found {len(result)} patients")
        print(result)

def show_high_cholesterol_detail():
    print("\nPatients with Cholesterol > 150")

    if "Cholesterol" not in disease_data.columns:
        print("Cholesterol column not found!")
        return

    result = disease_data[disease_data["Cholesterol"] > 150]

    if result.empty:
        print("No patients found.")
    else:
        print(f"Found {len(result)} patients")
        print(result[["Age", "Sex", "Cholesterol"]])
        print("Highest Cholesterol:", result["Cholesterol"].max())
        print("Average Cholesterol:", result["Cholesterol"].mean())


def data_visualization():
    print("\nMatplotlib Visualization")
    print("1. Histogram of Cholesterol")
    print("2. Scatter plot (Age vs Cholesterol)")

    choice = input("Enter choice (1-2): ")

    if choice == '1':
        plt.figure(figsize=(8,5))
        plt.hist(disease_data["Cholesterol"], bins=10, edgecolor="black")
        plt.title("Cholesterol Distribution")
        plt.xlabel("Cholesterol")
        plt.ylabel("Count")
        plt.show()

    elif choice == '2':
        plt.figure(figsize=(8,5))
        plt.scatter(disease_data["Age"], disease_data["Cholesterol"], alpha=0.7)
        plt.title("Age vs Cholesterol")
        plt.xlabel("Age")
        plt.ylabel("Cholesterol")
        plt.show()
    else:
        print("Invalid choice")

def seaborn_graph():
    print("\nSeaborn Visualization")
    print("1. Relationship plot (Age vs Cholesterol)")
    print("2. Distribution plot (Cholesterol)")

    disease_data["Risk"] = disease_data["Cholesterol"] > 200
    choice = input("Enter choice (1-2): ")

    if choice == '1':
        plt.figure(figsize=(8,5))
        sns.scatterplot(
            data=disease_data,
            x="Age",
            y="Cholesterol",
            hue="Risk",
            palette={True: "red", False: "green"}
        )
        plt.title("Age vs Cholesterol (Red = High Risk)")
        plt.show()

    elif choice == '2':
        plt.figure(figsize=(8,5))
        sns.histplot(disease_data["Cholesterol"], kde=True, color="purple")
        plt.title("Cholesterol Distribution")
        plt.show()
    else:
        print("Invalid choice")

while True:
    main_menu()
    choice = input("Enter choice: ").lower()

    if choice == '1':
        view_dataset()
    elif choice == '2':
        analyze_dataset()
    elif choice == '3':
        show_chest_pain_detail()
    elif choice == '4':
        show_high_cholesterol_detail()
    elif choice == '5':
        data_visualization()
    elif choice == '6':
        seaborn_graph()
    elif choice == 'exit':
        print("Program exited successfully.")
        break
    else:
        print("Invalid choice!")
