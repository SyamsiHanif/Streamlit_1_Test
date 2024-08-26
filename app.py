import streamlit as st

# Title of the app
st.title('Car Price Estimator')

# Input form
with st.form(key='car_price_form'):
    st.header('Enter Car Details')

    levy = st.number_input('Levy', min_value=0, step=1)
    manufacturer = st.selectbox('Manufacturer', ['Toyota', 'Honda', 'Ford', 'BMW', 'Other'])
    model = st.text_input('Model')
    category = st.selectbox('Category', ['Sedan', 'SUV', 'Truck', 'Coupe', 'Convertible'])
    leather_interior = st.selectbox('Leather Interior', ['Yes', 'No'])
    fuel_type = st.selectbox('Fuel Type', ['Petrol', 'Diesel', 'Electric', 'Hybrid'])
    engine_volume = st.number_input('Engine Volume (L)', min_value=0.0, step=0.1)
    mileage = st.number_input('Mileage (km)', min_value=0, step=100)
    cylinders = st.number_input('Cylinders', min_value=1, step=1)
    gearbox_type = st.selectbox('Gearbox Type', ['Manual', 'Automatic'])
    drive_wheels = st.selectbox('Drive Wheels', ['Front', 'Rear', 'All'])
    wheel = st.number_input('Wheel Size (inches)', min_value=10, step=1)
    color = st.selectbox('Color', ['Red', 'Blue', 'Black', 'White', 'Silver', 'Other'])
    airbags = st.number_input('Airbags', min_value=0, step=1)
    age = st.number_input('Age (years)', min_value=0, step=1)

    # Submit button
    submit_button = st.form_submit_button(label='Estimate Price')

# Placeholder for price estimation logic
if submit_button:
    # Here, you can implement the price estimation logic
    # For demonstration, we use a simple placeholder formula
    estimated_price = (
        10000 - (age * 500) +
        (engine_volume * 1000) -
        (mileage * 0.05) +
        (cylinders * 200) +
        (airbags * 300)
    )

    st.subheader('Estimated Car Price')
    st.write(f'Estimated Price: ${estimated_price:,.2f}')
