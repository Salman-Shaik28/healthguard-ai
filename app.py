import gradio as gr
import joblib
import numpy as np
import pandas as pd

# Load the model package
try:
    loaded_package = joblib.load('disease_prediction_model.pkl')
    model = loaded_package['model']
    label_encoder = loaded_package['label_encoder']
    selected_features = loaded_package['selected_features']
    
    print(f"✅ Model loaded successfully")
    print(f"📋 Features: {len(selected_features)}")
    print(f"🎯 Diseases: {len(label_encoder.classes_)}")
    
except Exception as e:
    print(f"❌ Error loading model: {e}")
    raise e

def predict_disease(selected_symptoms):
    """
    Predict disease based on selected symptoms
    """
    try:
        # Create input array with all features
        input_array = np.array([[1 if feature in selected_symptoms else 0 for feature in selected_features]])
        
        # Make prediction
        prediction = model.predict(input_array)
        prediction_proba = model.predict_proba(input_array)
        
        # Decode prediction
        disease = label_encoder.inverse_transform(prediction)
        confidence = np.max(prediction_proba[0])
        
        # Get top 3 probabilities
        top_3_indices = np.argsort(prediction_proba[0])[-3:][::-1]
        top_3_diseases = label_encoder.inverse_transform(top_3_indices)
        top_3_probs = prediction_proba[0][top_3_indices]
        
        # Format output
        result = f"🔍 PREDICTED DISEASE: {disease[0]}\n"
        result += f"📊 CONFIDENCE: {confidence:.1%}\n\n"
        result += "🏥 TOP 3 POSSIBLE DISEASES:\n"
        
        for i, (disease_name, prob) in enumerate(zip(top_3_diseases, top_3_probs)):
            result += f"{i+1}. {disease_name}: {prob:.1%}\n"
        
        result += f"\n📝 Symptoms selected: {len(selected_symptoms)}/{len(selected_features)}"
        
        return result
        
    except Exception as e:
        return f"❌ Error in prediction: {str(e)}"

# Create examples (first 6 symptoms in groups of 2-3)
example_symptoms = []
if len(selected_features) >= 6:
    example_symptoms = [
        selected_features[0:2],
        selected_features[2:4],
        selected_features[4:6]
    ]

# Create the interface
demo = gr.Interface(
    fn=predict_disease,
    inputs=gr.CheckboxGroup(
        choices=selected_features,
        label="Select Your Symptoms",
        info=f"Choose from {len(selected_features)} possible symptoms"
    ),
    outputs=gr.Textbox(
        label="Prediction Result",
        lines=10,
        show_copy_button=True
    ),
    title="🏥 HealthGuard AI - Disease Prediction",
    description="Select your symptoms and get AI-powered disease predictions with confidence scores.",
    examples=example_symptoms,
    theme="soft"
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)