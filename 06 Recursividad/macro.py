import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import pandas as pd
import uuid

def generate_lpn():
    return "SU-" + uuid.uuid4().hex[:12].upper()

def load_pmf():
    pmf_path = filedialog.askopenfilename(title="Seleccionar Part Master File", filetypes=[("Excel files", "*.xlsx")])
    if not pmf_path:
        return None
    return pd.read_excel(pmf_path)

def load_lpns():
    lpn_path = filedialog.askopenfilename(title="Seleccionar archivo con LPNs", filetypes=[("Excel files", "*.xlsx")])
    if not lpn_path:
        return []
    df_lpn = pd.read_excel(lpn_path)
    return df_lpn.iloc[:, 0].dropna().tolist()

def save_to_excel(data):
    df = pd.DataFrame(data)
    output_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    if output_path:
        df.to_excel(output_path, index=False, header=False)
        messagebox.showinfo("Éxito", f"Archivo guardado: {output_path}")

def get_input(prompt):
    return simpledialog.askstring("Input", prompt)

def main():
    root = tk.Tk()
    root.withdraw()

    messagebox.showinfo("Ingreso de Mercadería", "Cargar Part Master File")
    pmf_df = load_pmf()
    if pmf_df is None:
        messagebox.showerror("Error", "No se cargó el PMF.")
        return

    messagebox.showinfo("Ingreso de Mercadería", "Cargar archivo con LPNs")
    lpn_list = load_lpns()
    if not lpn_list:
        messagebox.showerror("Error", "No se cargaron LPNs.")
        return

    output_data = []

    while True:
        part = get_input("Ingresar Part Number (ITEM_ID) (o dejar vacío para salir):")
        if not part:
            break

        cantidad = int(get_input("Cantidad a ingresar:"))
        batch = get_input("Batch:")
        lote = get_input("Lote:")

        pmf_row = pmf_df[pmf_df["ITEM_ID"] == part]
        if pmf_row.empty:
            messagebox.showerror("Error", f"El Part Number '{part}' no está en el PMF.")
            continue

        row_data = pmf_row.iloc[0]

        revision = get_input("Revisión:") if row_data.get("REVISION_NO_CONTROL") == "Y" else ""
        vencimiento = get_input("Fecha de Vencimiento (DD/MM/YYYY):") if row_data.get("EXPIRY_CONTROL") == "Y" else ""
        requiere_serial = row_data.get("IS_SERIAL_TRACKED") == "Y"

        for i in range(cantidad):
            lpn = lpn_list.pop(0) if lpn_list else generate_lpn()

            if requiere_serial:
                tipo_serial = get_input("¿Ingresar serial físico o ficticio? (físico/ficticio):")
                if tipo_serial.lower() == "ficticio":
                    serial = "SNS" + lpn
                else:
                    serial = get_input(f"Ingresar Serial para LPN {lpn}:")
                row = [lpn, part, "NA", batch, lote, vencimiento, serial, "NA"]
            else:
                row = [lpn, part, "NA", revision, batch, lote, 1]

            output_data.append(row)

    if output_data:
        save_to_excel(output_data)
    else:
        messagebox.showinfo("Sin datos", "No se ingresaron datos.")

if __name__ == "__main__":
    main()