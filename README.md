# Credit Card Fraud Detection Project

A comprehensive machine learning project for detecting fraudulent credit card transactions using various classification algorithms and an interactive Streamlit dashboard for monitoring and analysis.

## 📋 Project Overview

This project implements a fraud detection system that:
- Analyzes credit card transaction data for fraudulent patterns
- Trains multiple machine learning models (Logistic Regression, Random Forest)
- Provides an interactive dashboard for real-time monitoring
- Generates reports for further analysis in tools like Tableau

## 🚀 Features

### Machine Learning Models
- **Logistic Regression**: Baseline model for fraud detection
- **Random Forest Classifier**: Ensemble method for improved accuracy
- **Model Evaluation**: Comprehensive metrics including confusion matrix, F1 score, and AUC-ROC

### Interactive Dashboard
- **Real-time Monitoring**: Live tracking of transaction patterns
- **Visual Analytics**: Interactive charts and graphs
- **Alert System**: Detection of unusual transaction patterns
- **Investigation Panel**: Tools for ongoing fraud investigations

### Data Processing
- **Data Cleaning**: Handling of missing values and outliers
- **Feature Scaling**: Standardization of Amount and Time features
- **Class Imbalance Handling**: Techniques for dealing with rare fraud cases

## 📁 Project Structure

```
credit_card_fraud_project/
├── data/
│   └── creditcard.csv              # Original dataset (excluded from git due to size)
├── notebooks/
│   └── 01_fraud_detection.ipynb    # Jupyter notebook for model development
├── reports/
│   └── model_predictions_for_tableau.csv  # Processed data for visualization
├── .streamlit/
│   └── config.toml                 # Streamlit configuration
├── app.py                          # Main Streamlit dashboard application
└── README.md                       # Project documentation
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/ADITYAJAY09/Credit-Card-Fraud-Detection.git
   cd credit_card_fraud_project
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

   If requirements.txt doesn't exist, install packages manually:
   ```bash
   pip install streamlit pandas numpy matplotlib seaborn plotly scikit-learn jupyter
   ```

4. **Download the dataset**
   - The original creditcard.csv file is not included in the repository due to GitHub's file size limitations
   - Download the dataset from [Kaggle Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
   - Place the creditcard.csv file in the `data/` directory

## 🎯 Usage

### Running the Jupyter Notebook
```bash
jupyter notebook notebooks/01_fraud_detection.ipynb
```

### Running the Streamlit Dashboard
```bash
streamlit run app.py
```

The dashboard will open in your default web browser at `http://localhost:8501`

### Notebook Workflow
1. **Data Exploration**: Analyze dataset characteristics and class distribution
2. **Data Preprocessing**: Scale features and handle class imbalance
3. **Model Training**: Train Logistic Regression and Random Forest models
4. **Model Evaluation**: Compare performance metrics and select best model
5. **Data Export**: Generate reports for Tableau visualization

## 📊 Dashboard Features

### Main Sections
- **Recent Activity**: Total transactions and unusual transaction counts
- **Daily Fraud Trends**: Time-based analysis of fraudulent activities
- **Unusual Transaction Alerts**: Real-time detection of suspicious patterns
- **Ongoing Investigations**: Tracking of current fraud cases
- **Verification Metrics**: Performance metrics and confusion matrix visualization

### Visualizations
- Stacked bar charts for time-based analysis
- Donut charts for verification status
- Confusion matrix heatmaps
- ROC curves for model evaluation

## 🔧 Configuration

### Streamlit Theme
The dashboard uses a custom dark theme defined in `.streamlit/config.toml`:
- Primary Color: #F9A31A (Orange)
- Background: #373A3F (Dark Gray)
- Text Color: #FFFFFF (White)

### Model Parameters
- **Random Forest**: 100 estimators with random state 42
- **Test Split**: 20% of data for testing with stratified sampling
- **Evaluation Metrics**: F1 Score, AUC-ROC, Precision, Recall

## 📈 Performance Metrics

The models are evaluated using:
- Confusion Matrix**: True/False Positive/Negative rates
- Classification Report**: Precision, Recall, F1-Score
- ROC-AUC Score**: Area under the Receiver Operating Characteristic curve
- F1 Score**: Harmonic mean of precision and recall

 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Dataset provided by [Machine Learning Group - ULB](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- Built with Streamlit, Scikit-learn, Pandas, and other open-source libraries

## 📞 Support

For questions or support, please open an issue in the GitHub repository or contact the project maintainer.

---

**Note**: This project is for educational and demonstration purposes. Always follow proper security protocols when working with financial data.
