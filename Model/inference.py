import torch
import torchaudio
from Model.model import VEModel
from transformers import WhisperProcessor

label_mapping ={
    0:'angry',
    1:'disgust', 
    2:'Fear', 
    3:'happy',
    4:'neutral',
    5:'surprised',
    6:'Sad', 
    7:'angry', 
    8:'disgust',
    9:'fear',
    10:'happy',
    11:'neutral',
    12:'surprised',
    13:'sad'
    }

def load_model(checkpoint_path):
    model = VEModel(num_classes=len(label_mapping)) 
    checkpoint = torch.load(checkpoint_path)
    model.load_state_dict(checkpoint['model_state_dict'])
    model.eval()  
    return model

def preprocess_audio(audio_file):
    processor=WhisperProcessor.from_pretrained("openai/whisper-base")
    waveform, sample_rate = torchaudio.load(audio_file)
    waveform = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)(waveform)
    inputs = processor(waveform.squeeze(0), return_tensors="pt", sampling_rate=16000)
    return inputs.input_features.squeeze(0)

def predict_emotion(model, audio_tensor):
    with torch.no_grad():
        output = model(audio_tensor.unsqueeze(0))  
        _, predicted = torch.max(output, 1) 
    return predicted.item() 

def Inference(audio_file):
    checkpoint_path = "Checkpoint/checkpoint.pt" 
    model = load_model(checkpoint_path)
    audio_tensor = preprocess_audio(audio_file)
    predicted_index = predict_emotion(model, audio_tensor)
    emotion_labels = list(label_mapping.values())  
    predicted_label = emotion_labels[predicted_index]
    return predicted_label
 

