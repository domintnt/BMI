import tkinter as tk
from tkinter import messagebox


def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    return weight / (height_m ** 2)


def calculate_difference(current_bmi, target_bmi, height_cm, weight):
    target_weight = target_bmi * (height_cm / 100) ** 2
    return abs(target_weight - weight)


def calculate_button_clicked():
    try:
        weight = float(weight_entry.get())
        height_cm = float(height_entry.get())
    except ValueError:
        messagebox.showerror("Błąd", "Waga i wzrost muszą być liczbami.")
        return

    bmi = calculate_bmi(weight, height_cm)
    bmi_label.config(text=f"Twoje BMI wynosi: {bmi:.2f}")

    if bmi < 18.5:
        target_bmi = 18.5
        message = f"Aby osiągnąć prawidłową wagę, musisz przytyć o {calculate_difference(bmi, target_bmi, height_cm, weight):.2f} kg."
    elif bmi < 24.9:
        message = "Twoja waga jest prawidłowa."
    else:
        target_bmi = 24.9
        message = f"Aby osiągnąć prawidłową wagę, musisz schudnąć {calculate_difference(bmi, target_bmi, height_cm, weight):.2f} kg."

    result_label.config(text=message)


app = tk.Tk()
app.title("Kalkulator BMI")

weight_label = tk.Label(app, text="Waga (kg):")
weight_label.pack()

weight_entry = tk.Entry(app)
weight_entry.pack()

height_label = tk.Label(app, text="Wzrost (cm):")
height_label.pack()

height_entry = tk.Entry(app)
height_entry.pack()

calculate_button = tk.Button(app, text="Oblicz BMI", command=calculate_button_clicked)
calculate_button.pack()

bmi_label = tk.Label(app, text="")
bmi_label.pack()

result_label = tk.Label(app, text="")
result_label.pack()

made_by_label = tk.Label(app, text="Made by czarnaMamba")
made_by_label.pack(side="bottom")

app.mainloop()
