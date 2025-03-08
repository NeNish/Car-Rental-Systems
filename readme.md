# 🚗 AI-Based Dynamic Pricing for Car Rental System

## 📖 Overview
This project implements **AI-driven dynamic pricing** for a car rental system, adjusting rental prices based on **demand, weather conditions, and competitor pricing**. The system predicts optimal rental rates using **machine learning models** trained on historical data.

## ✨ Features
- ✅ Predicts optimal rental prices using **AI models**  
- ✅ Considers **demand, competitor prices, weather conditions**  
- ✅ **Real-time API integration** for weather data  
- ✅ **Flask API** for easy integration into any car rental system  

---

## 💽 Project Structure
```
💾 AI_Car_Rental_Pricing/
│── 📂 data/                     # Dataset folder
│   ├── car_rental_data.csv      # Sample dataset
│── 📂 models/                   # ML Model storage
│── 📂 api/                      # Flask API folder
│── 📑 README.md                 # Project documentation
│── 📚 requirements.txt          # Required dependencies
│── 🚀 train_model.py            # ML model training script
│── 🌎 app.py                    # Flask API to serve predictions
```

---

## 🔧 Installation & Setup
### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/your-username/AI_Car_Rental_Pricing.git
cd AI_Car_Rental_Pricing
```

### 2️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 3️⃣ **Run the Model Training**
```bash
python train_model.py
```

### 4️⃣ **Start the Flask API**
```bash
python app.py
```
The API will start on **http://127.0.0.1:5000**

---

## 📊 Dataset (`car_rental_data.csv`)
This dataset includes **rental demand, competitor pricing, and weather conditions** to help train the model.  
| date       | car_type | location  | demand_level | competitor_price | temperature | rainfall | price |
|------------|---------|-----------|--------------|------------------|-------------|----------|-------|
| 2024-01-01 | Economy | New York  | 0.85         | 45.0             | 5.0         | 10.2     | 50.0  |
| 2024-01-02 | SUV     | Los Angeles | 0.70       | 80.0             | 20.0        | 0.0      | 85.0  |
| 2024-01-03 | Luxury  | Miami     | 0.60         | 120.0            | 30.0        | 0.0      | 130.0 |

---

## 🚀 Endpoints (Flask API)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/predict` | POST | Predicts rental price based on input data |

Example API Request:
```json
{
  "car_type": "SUV",
  "location": "New York",
  "demand_level": 0.7,
  "competitor_price": 80,
  "temperature": 3,
  "rainfall": 15.1
}
```

---

## 🎯 Future Enhancements
- ✅ Integrate **real-time weather API**  
- ✅ Implement **customer behavior analysis**  
- ✅ Add **location-based pricing variations**  

---

## 👨‍💻 Contributors
- **Your Name** – [GitHub Profile](https://github.com/your-username)

---

## 📜 License
This project is licensed under the **MIT License**.

