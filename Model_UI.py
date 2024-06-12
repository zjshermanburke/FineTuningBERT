# Python Imports
import matplotlib.pyplot as plt

# Scikit-Learn Imports
from sklearn.metrics import ConfusionMatrixDisplay, f1_score, accuracy_score, confusion_matrix

# Transformer Imports
from transformers import pipeline


def get_model(prompt):
    while True:
        try:
            model_input = str(input(prompt))
            model_input = model_input.strip().lower().replace(" ", "")
        except ValueError:
            print("Value entered not a string")
            continue
        
        if model_input not in ('distilbert', 'bert', 'largebert'):
            print("Model Not Recognized\n")
            continue
        else:
            break
    
    return model_input
    
    
def get_input(prompt):
    while True:
        try:
            string = str(input(prompt))
        except ValueError:
            print("Value entered not a string")
            continue
        
        if len(string) > 512:
            print("String too long")
            continue
        
        else:
            break
    
    return string
    
    
def pipeline_generator(selected_model):
    model = None
    selected_model = selected_model.strip().lower().replace(" ", "")
    
    if selected_model == 'distilbert':
        model = './Models/BERTModel'
        
    elif selected_model == 'bert':
        model = './Models/BERTModel'
        
    elif selected_model == 'largebert':
        model = './Models/LargeBERT'
        
    else:
        print("While this is awkward")
        
    model_pipeline = pipeline('text-classification',
                      model=model,
                      device=0)
        
    return model_pipeline




def response_parser(user_input, model_pipeline):
    prediction = None
    
    analysis = model_pipeline(user_input)[0]
    
    label = analysis['label']
    confidence = analysis['score']
    
    # 'negative': 0, 'neutral': 1, 'positive': 2
    pred_int = int(label.split('_')[1])
    
    if pred_int == 0:
        prediction = 'Negative'
    elif pred_int == 1:
        prediction = 'Neutral'
    elif pred_int == 2:
        prediction = 'Positive'
    else:
        print("Prediction not recognized")
    
    return prediction, confidence


if __name__ =="__main__":
    
    model_input = get_model("Enter model to use (BERT, DistilBERT, LargeBERT): ")
    print(f"\nThe model selected is: {model_input}")
    
    generated_pipeline = pipeline_generator(model_input)
    
    user_input = get_input("\nPlease enter sentence regarding financial sentiment: ")
    
    prediction, confidence = response_parser(user_input, generated_pipeline)
    
    print('-------------------------------------------------------------------------------------------')
    print(f"The sentiment towards the user input is: {prediction} \nWith a confidence of: {confidence}")
    
        
        