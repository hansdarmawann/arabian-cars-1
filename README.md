# Used Cars Price Prediction – Saudi Arabia

by Hans Darmawan

---

| Path                                                    | Type   | Description                               |
| ------------------------------------------------------- | ------ | ----------------------------------------- |
| `Datasets/`                                             | Folder | Saudi Arabia used car dataset             |
| `Datasets/UsedCarsSA_Unclean_Ar.xlsx`                   | File   | Raw dataset (Arabic)                      |
| `Datasets/UsedCarsSA_Unclean_EN.csv`                    | File   | Raw dataset (English translation)         |
| `Datasets/UsedCarsSA_Clean.csv`                         | File   | Clean dataset for modeling                |
| `Datasets/UsedCarsSA_Clean_EN.csv`                      | File   | Clean dataset (English version)           |
| `Environments/`                                         | Folder | Environment & dependency management       |
| `Environments/environment.yml`                          | File   | Conda/Mamba environment (reproducible)    |
| `Models/`                                               | Folder | Machine learning model artifacts          |
| `Models/xgb_tuned_mae11198_20251222.joblib`             | File   | Best XGBoost model from tuning            |
| `Notebooks/`                                            | Folder | End-to-end workflow notebooks             |
| `Notebooks/01_Business Understanding.ipynb`             | File   | Business problem & objectives             |
| `Notebooks/02_Data Acquisition And Understanding.ipynb` | File   | EDA & data understanding                  |
| `Notebooks/03_Modeling.ipynb`                           | File   | Modeling, evaluation, tuning              |
| `Notebooks/04_Deployment.ipynb`                         | File   | Inference & deployment preparation        |
| `Notebooks/05_Customer or Stakeholder Acceptance.ipynb` | File   | Acceptance, limitations & recommendations |
| `README.md`                                             | File   | Main project documentation                |

---

This project aims to build a **machine learning regression model** to predict the **fair price of used cars in Saudi Arabia** using the *Saudi Arabia Used Cars* dataset (±8,000 records) from Kaggle. The model is designed to help **sellers, buyers, and platforms** make objective pricing decisions, using key features such as brand, type, production year, engine size, mileage, region, and vehicle options. Model success is measured using **MAE**, with an accuracy target that is meaningful from a business perspective.

The data was processed through **EDA, cleaning, imputation, outlier handling (IQR), data type conversion, and feature engineering** such as *Car_Age* and *Mileage_per_Year*. The modeling process was performed end-to-end using a **preprocessing pipeline** to prevent data leakage, with evaluation across multiple regression algorithms. **XGBoost** was selected as the best model after **cross-validation and hyperparameter tuning**, delivering the most stable and accurate performance. **SHAP analysis** indicates that *Engine_Size, Year, Mileage,* and *Car_Age* are the dominant factors influencing price.

The final model is implemented as an **integrated pipeline** ready for operational use, capable of receiving new vehicle inputs and consistently producing **fair market price estimates**. The model artifact is saved and can be used for system integration or further deployment.

---

Special thanks to my friends Kirana, Adrian, and Satrio for making this project highly valuable for my learning journey in ML regression! You can refer to the original source here:
https://github.com/PurwadhikaDev/BetaGroup_JC_DS_FT_BSD_26_FinalProject
