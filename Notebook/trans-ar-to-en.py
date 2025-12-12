# Import library dan load dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')
pd.set_option('display.max_columns', None)

from transformers import MarianMTModel, MarianTokenizer
import pandas as pd
from tqdm import tqdm

# Load dataset
data_path = '../Dataset/UsedCarsSA_Unclean_Ar.xlsx'
df = pd.read_excel(data_path)

# Load model & tokenizer
model_name = 'Helsinki-NLP/opus-mt-ar-en'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Kolom yang ingin diterjemahkan
cols_to_translate = ['Make', 'Type', 'Origin', 'Color', 'Options', 'Fuel_Type', 'Gear_Type', 'Condition', 'Region', 'Price']

# Fungsi translate batch
def translate_batch(texts):
    inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True)
    translated = model.generate(**inputs)
    return [tokenizer.decode(t, skip_special_tokens=True) for t in translated]

# Loop tiap kolom
for col in cols_to_translate:
    print(f"Translating column: {col}")
    translated = []
    batch_size = 64

    for i in tqdm(range(0, len(df), batch_size)):
        batch_texts = df[col].astype(str).iloc[i:i+batch_size].tolist()
        translated.extend(translate_batch(batch_texts))
    
    df[col + '_en'] = translated

# Simpan hasil
output_path = '../Dataset/UsedCarsSA_Translated.xlsx'
df.to_excel(output_path, index=False)
print(f"✅ Translation completed and saved to {output_path}")