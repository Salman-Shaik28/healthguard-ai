{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c8e6eb7b-028f-433a-9fa0-d35bc16ce281",
   "metadata": {},
   "outputs": [],
   "source": [
    "import joblib\n",
    "import numpy as np\n",
    "import streamlit as st\n",
    "\n",
    "# LOAD THE OBJECTS\n",
    "model = joblib.load(\"model_rf.joblib\")\n",
    "label_encoder = joblib.load(\"label_encoder.joblib\")\n",
    "selected_features = joblib.load(\"selected_features.joblib\")  # list\n",
    "\n",
    "# Example (Streamlit interface code)\n",
    "st.title(\"Disease Prediction App\")\n",
    "st.write(\"Enter symptoms. All other will be set to zero.\")\n",
    "\n",
    "num_params = st.number_input(\n",
    "    \"Number of symptoms to enter\", min_value=1, max_value=len(selected_features), step=1\n",
    ")\n",
    "chosen_symptoms = st.multiselect(\n",
    "    \"Select symptoms:\", selected_features, max_selections=num_params\n",
    ")\n",
    "\n",
    "input_dict = dict.fromkeys(selected_features, 0)\n",
    "for symptom in chosen_symptoms:\n",
    "    input_dict[symptom] = 1\n",
    "\n",
    "input_array = np.array([input_dict[f] for f in selected_features]).reshape(1, -1)\n",
    "\n",
    "if st.button(\"Predict Disease\"):\n",
    "    prediction = model.predict(input_array)\n",
    "    disease = label_encoder.inverse_transform(prediction)\n",
    "    st.success(f\"Predicted Disease: {disease[0]}\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
