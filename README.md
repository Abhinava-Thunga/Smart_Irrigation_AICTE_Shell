# Smart_Irrigation_AICTE_Shell_Edunet
AICTE Internship Cycle 2
---
### 💡 Project Description

The **Smart Irrigation System using Machine Learning** is designed to automate and optimize the process of agricultural watering by leveraging real-time sensor data and intelligent predictions. Traditional irrigation methods often rely on manual control or fixed schedules, which leads to problems such as overwatering, water wastage, soil erosion, and long-term fertility loss. This project addresses those challenges by introducing a data-driven solution that adapts to the farm's changing environmental conditions.

The system uses **19 sensor inputs** (scaled between 0 and 1) that simulate various environmental and soil parameters. These inputs are fed into a trained **Random Forest Classifier** that predicts whether each of the **3 sprinkler pumps** should be turned ON or OFF. The model is trained using scikit-learn and serialized with joblib for deployment.

To make the system user-friendly, a **Streamlit web application** is developed. The app allows users to input real-time or test sensor values and get instant predictions about the sprinkler status. The interface is enhanced using **HTML and CSS**, making it visually intuitive and informative.

This smart irrigation solution can significantly improve water efficiency, crop health, and soil sustainability, especially in water-scarce and agriculture-dependent regions. It also lays a foundation for future integration with IoT systems, weather APIs, and large-scale automation platforms.

----
