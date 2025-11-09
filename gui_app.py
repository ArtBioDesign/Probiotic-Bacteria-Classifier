# gui_inference.py (English version)
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import joblib
import os

def run_inference(input_path, output_path):
    try:
        df = pd.read_csv(input_path)
        categorical_features = ['Form/Shape', 'colony Color', 'Colony margin', 'Gram’s Staining', 'Cell shape']
        
        # Ensure all required columns exist
        missing_cols = [col for col in categorical_features if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Input CSV is missing required columns: {missing_cols}")

        df_onehot = df[categorical_features].astype(str)
        X = pd.get_dummies(df_onehot, prefix=categorical_features, drop_first=False)

        # Load model
        model_path = 'model/autosklearn_model.pkl'
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found: {model_path}")
        automl_loaded = joblib.load(model_path)

        # Predict
        df['label'] = automl_loaded.predict(X)

        # Save result
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False)
        return True, output_path
    except Exception as e:
        return False, str(e)

def select_input_file():
    filepath = filedialog.askopenfilename(
        title="Select Input CSV File",
        filetypes=[("CSV files", "*.csv")]
    )
    if filepath:
        input_var.set(filepath)

def select_output_file():
    filepath = filedialog.asksaveasfilename(
        title="Save Result As",
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv")]
    )
    if filepath:
        output_var.set(filepath)

def on_run():
    input_file = input_var.get()
    output_file = output_var.get() or "Result.csv"
    
    if not input_file:
        messagebox.showwarning("Warning", "Please select an input file first!")
        return

    success, msg = run_inference(input_file, output_file)
    if success:
        messagebox.showinfo("Success", f"✅ Prediction completed!\nResults saved to:\n{msg}")
    else:
        messagebox.showerror("Error", f"❌ Inference failed:\n{msg}")

# GUI Setup
root = tk.Tk()
root.title("Probiotic Classifier")
root.geometry("500x250")

input_var = tk.StringVar()
output_var = tk.StringVar(value="Result.csv")

tk.Label(root, text="Input CSV File:", font=("Arial", 10)).pack(pady=(10, 0))
tk.Entry(root, textvariable=input_var, width=60).pack(pady=5)
tk.Button(root, text="Browse...", command=select_input_file).pack()

tk.Label(root, text="Output File Path:", font=("Arial", 10)).pack(pady=(10, 0))
tk.Entry(root, textvariable=output_var, width=60).pack(pady=5)
tk.Button(root, text="Save As...", command=select_output_file).pack()

tk.Button(root, text="Run Prediction", command=on_run, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=20)

root.mainloop()