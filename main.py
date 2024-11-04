import streamlit as st
import tensorflow as tf
import numpy as np
# tensorflow model prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model('plant_train.keras')
    image = tf.keras.preprocessing.image.load_img(test_image,target_size=(128,128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) 
    prediction  = model.predict(input_arr)
    res = np.argmax(prediction)
    return res
#sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("select page",["home","about","Disease Recognition"])
#home page
if(app_mode == "home"):
    st.header("Plant Disease Recognitio System")
    st.markdown("""
    Welcome to the Plant Disease Recognition System! 🌿🔍
    
    Our mission is to help in identifying plant diseases efficiently. Upload an image of a plant, and our system will analyze it to detect any signs of diseases. Together, let's protect our crops and ensure a healthier harvest!

    ### How It Works
    1. *Upload Image:* Go to the *Disease Recognition* page and upload an image of a plant with suspected diseases.
    2. *Analysis:* Our system will process the image using advanced algorithms to identify potential diseases.
    3. *Results:* View the results and recommendations for further action.

    ### Why Choose Us?
    - *Accuracy:* Our system utilizes state-of-the-art machine learning techniques for accurate disease detection.
    - *User-Friendly:* Simple and intuitive interface for seamless user experience.
    - *Fast and Efficient:* Receive results in seconds, allowing for quick decision-making.

    ### Get Started
    Click on the *Disease Recognition* page in the sidebar to upload an image and experience the power of our Plant Disease Recognition System!

    ### About Us
    Learn more about the project, our team, and our goals on the *About* page.
    """)
#about page
elif(app_mode == "about"):
    st.header("about")
    st.markdown("""
    #### About Dataset
    This dataset is recreated using offline augmentation from the original dataset. 
    The original dataset can be found on this github repo. This dataset consists of 
    about 87K rgb images of healthy and diseased crop leaves which is categorized 
    into 38 different classes. The total dataset is divided into 80/20 ratio of 
    training and validation set preserving the directory structure. A new directory 
    containing 33 test images is created later for prediction purpose.
    #### content
    1. train (70295 images)   
    2. valid (17572 images)   
    3. test  (33 images)
    #### our team
    Dana Mowafak
    Abeer Mohamed     
             
                """)
#predection page
elif(app_mode== "Disease Recognition"):
    st.header("Disease Recognition")
    test_image = st.file_uploader("choose an image")
    print("#")
    print(test_image)
    if(st.button("show image")):
       st.image(test_image)
    if(st.button("predict")):
       result_index =  model_prediction(test_image)
       #define class
       class_name = ['Apple___Apple_scab',
 'Apple___Black_rot',
 'Apple___Cedar_apple_rust',
 'Apple___healthy',
 'Blueberry___healthy',
 'Cherry_(including_sour)_Powdery_mildew',
 'Cherry_(including_sour)_healthy',
 'Corn_(maize)_Cercospora_leaf_spot Gray_leaf_spot',
 'Corn_(maize)Common_rust',
 'Corn_(maize)_Northern_Leaf_Blight',
 'Corn_(maize)_healthy',
 'Grape___Black_rot',
 'Grape__Esca(Black_Measles)',
 'Grape__Leaf_blight(Isariopsis_Leaf_Spot)',
 'Grape___healthy',
 'Orange__Haunglongbing(Citrus_greening)',
 'Peach___Bacterial_spot',
 'Peach___healthy',
 'Pepper,bell__Bacterial_spot',
 'Pepper,bell__healthy',
 'Potato___Early_blight',
 'Potato___Late_blight',
 'Potato___healthy',
 'Raspberry___healthy',
 'Soybean___healthy',
 'Squash___Powdery_mildew',
 'Strawberry___Leaf_scorch',
 'Strawberry___healthy',
 'Tomato___Bacterial_spot',
 'Tomato___Early_blight',
 'Tomato___Late_blight',
 'Tomato___Leaf_Mold',
 'Tomato___Septoria_leaf_spot',
 'Tomato___Spider_mites Two-spotted_spider_mite',
 'Tomato___Target_Spot',
 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
 'Tomato___Tomato_mosaic_virus',
 'Tomato___healthy']
       st.success("model is predicting it`s a {}".format(class_name[result_index]))


