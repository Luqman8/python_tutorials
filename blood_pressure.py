# Blood Pressure Analyzer and Plotter

import re
import os
import matplotlib.pyplot as plt

def load_bp_readings(filename="bp_readings.txt"):
    #### Return (systolic_list, diastolic_list) parsed from filename.
    systolic_list = []
    diastolic_list = []

    if not os.path.exists(filename):
        # file doesn't exist yet
        return systolic_list, diastolic_list

    with open(filename, "r", encoding="utf-8") as fh:
        for lineno, raw_line in enumerate(fh, start=1):
            line = raw_line.strip()
            if not line:
                continue
            m = re.search(r'(\d{2,3})\s*/\s*(\d{2,3})', line)
            if m:
                systolic_list.append(int(m.group(1)))
                diastolic_list.append(int(m.group(2)))
            else:
                print(f"Skipping line {lineno} (can't parse): {line}")

    return systolic_list, diastolic_list


def plot_bp(systolic_list, diastolic_list, save_as=None):
    #Plot systolic and diastolic lists over measurement index.
    if not systolic_list or not diastolic_list:
        print("No readings to plot.")
        return

    x = list(range(1, len(systolic_list) + 1))

    plt.figure(figsize=(10, 5))
    plt.plot(x, systolic_list, marker='o', label='Systolic (mmHg)')
    plt.plot(x, diastolic_list, marker='o', label='Diastolic (mmHg)')

    # clinical cutoff lines
    plt.axhline(120, linestyle='--', linewidth=0.9, label='Systolic 120 (elevated cutoff)')
    plt.axhline(140, linestyle=':', linewidth=0.9, label='Systolic 140 (Stage 2 cutoff)')
    plt.axhline(80, linestyle='--', linewidth=0.9, label='Diastolic 80 (normal cutoff)')
    plt.axhline(90, linestyle=':', linewidth=0.9, label='Diastolic 90 (Stage 2 cutoff)')

    plt.title("Blood Pressure Readings Over Time")
    plt.xlabel("Measurement # (chronological)")
    plt.ylabel("Pressure (mmHg)")
    plt.xticks(x)
    plt.grid(True, alpha=0.3)
    plt.legend(loc='best')
    plt.tight_layout()

    if save_as:
        plt.savefig(save_as, dpi=150)
        print(f"Saved plot to {save_as}")

    plt.show()


def blood_pressure_analyzer():
    print("========= Blood Pressure Analyzer =========")
    while True:
        try:
            systolic = int(input("What is your systolic reading (top number)?\n").strip())
            diastolic = int(input("What is your diastolic reading (bottom number)?\n").strip())

            if systolic <= 0 or diastolic <= 0:
                print("Values must be positive numbers. Try again.")
                continue  # go back to top of while True
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue  # ask again

        # Categorization (order matters: check most severe first)
        if systolic > 180 or diastolic > 120:
            category = "Hypertensive Crisis (Seek medical attention!)"
        elif systolic >= 140 or diastolic >= 90:
            category = "Hypertension Stage 2"
        elif systolic >= 130 or diastolic >= 80:
            category = "Hypertension Stage 1"
        elif systolic >= 120 and diastolic < 80:
            category = "Elevated"
        else:
            category = "Normal"

        print(f"Your blood pressure is {systolic}/{diastolic} mmHg -> {category}")

        # Save to file (append). using UTF-8 is safe on most systems.
        with open("bp_readings.txt", "a", encoding="utf-8") as file:
            file.write(f"{systolic}/{diastolic} -> {category}\n")

        q = input("Do you want to continue? (y/n): ").strip().lower()
        if q == "n":
            # ask if user wants to see plot now
            show = input("Show plot of saved readings now? (y/n): ").strip().lower()
            if show == "y":
                s_list, d_list = load_bp_readings("bp_readings.txt")
                plot_bp(s_list, d_list, save_as="bp_plot.png")
            print("Goodbye! Stay healthy")
            break


if __name__ == "__main__":
    blood_pressure_analyzer()


