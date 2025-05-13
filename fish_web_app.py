import streamlit as st
import numpy as np
from PIL import Image
import os

# Dashboard title and intro
st.title("🐟 Fish Price Prediction Dashboard")
st.markdown("Welcome to the **Fish Price Prediction Dashboard**. Enter the fish details in the sidebar to predict its price.")

# Display image if exists
image_path = "Fresh Fish Price_remix.png"
if os.path.exists(image_path):
    st.image(image_path, caption="Fish Price Prediction", use_container_width=True)
else:
    st.warning("⚠️ Image 'Fresh_Fish_Price_remix.png' not found in directory.")

# Sidebar inputs
st.header("Input Fish Features")
weight = st.number_input("Weight (grams)", min_value=0.0, step=0.1)
length = st.number_input("Length (cm)", min_value=0.0, step=0.1)
height = st.number_input("Height (cm)", min_value=0.0, step=0.1)
cost_tl = st.number_input("Cost (TL)", min_value=0.0, step=0.1)

# Prediction logic
if st.button("Predict"):
    if weight <= 0 or length <= 0 or height <= 0 or cost_tl <= 0:
        st.error("⚠️ Please enter valid positive values for all inputs.")
    else:
        st.info("Calculating the fish price...")

        # Dummy prediction logic (replace with actual model prediction)
        # Example: prediction = model.predict(input_data)
        # Here we use a simple sum for demonstration
        input_data = np.array([[weight * 72.70544102, 19.48175649 * length, 5.98011468 * height, 14.77860333 * cost_tl]])
        prediction = 415.71559715057083 + input_data.sum()

    # st.balloons()
        st.snow()
        st.success(f"🎉 Predicted Fish Price: {prediction:.2f} TL")
# Footer
st.markdown("---")  
st.markdown("### About")
st.markdown("This dashboard uses a machine learning model to predict fish prices based on various features. The model was trained on a dataset of fish prices and their corresponding features.")
st.markdown("### Contact")
st.markdown("For any inquiries, please contact us at: muhammadali0302770@gmail.com ")
