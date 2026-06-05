import json
import os

def replace_in_notebook(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    changed = False
    for cell in nb.get('cells', []):
        if cell.get('cell_type') == 'code':
            source = cell.get('source', [])
            new_source = []
            for line in source:
                new_line = line
                for old, new in replacements.items():
                    if old in new_line:
                        new_line = new_line.replace(old, new)
                        changed = True
                new_source.append(new_line)
            cell['source'] = new_source
            
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
            # Add a newline at the end of the file to match typical jupyter format
            f.write('\n')

rep_eda = {
    '# Cuántos valores son espacios vacíos en TotalCharges': '# Count empty spaces in TotalCharges',
    'Espacios vacíos en TotalCharges': 'Empty spaces in TotalCharges',
    '# Ver esas filas': '# Display those rows',
    '# Distribución del target': '# Target distribution',
    'Distribución de Churn': 'Churn Distribution'
}

rep_mod = {
    '# Instanciamos el modelo con el peso balanceado': '# Instantiate the model with balanced class weights',
    '# ¡Ojo! Entrenamos con los datos SIN escalar': '# Note: Training on NON-scaled data',
    '# Predicciones': '# Predictions',
    '# Resultados': '# Results'
}

replace_in_notebook('notebooks/01_eda.ipynb', rep_eda)
replace_in_notebook('notebooks/03_modeling.ipynb', rep_mod)
print("Translations applied successfully.")