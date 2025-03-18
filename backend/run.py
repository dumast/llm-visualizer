from app.app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)



import torch
from transformers import BertTokenizer, BertModel
import matplotlib.pyplot as plt
import seaborn as sns

# # Load pre-trained BERT model and tokenizer
# tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
# model = BertModel.from_pretrained('bert-base-uncased', output_attentions=True)

# # Sample input text
# text = "The quick brown fox jumps over the lazy dog."

# # Tokenize the input text
# inputs = tokenizer(text, return_tensors='pt', add_special_tokens=True)

# # Forward pass through the model
# with torch.no_grad():
#     outputs = model(**inputs)

# # Extract attention weights (last layer attention weights)
# attentions = outputs.attentions  # List of attention weights for each layer

# # Choose the layer to visualize (e.g., last layer, or choose another layer)
# layer_index = -1  # Use the last layer
# attention_matrix = attentions[layer_index][0]  # Shape: [num_heads, seq_len, seq_len]

# # To better visualize, let's average over all attention heads
# avg_attention = attention_matrix.mean(dim=0)  # Shape: [seq_len, seq_len]

# # Convert token indices back to words
# tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])

# # Plot the attention matrix
# plt.figure(figsize=(10, 8))
# sns.heatmap(avg_attention.cpu().numpy(), xticklabels=tokens, yticklabels=tokens, cmap='Blues', annot=True)
# plt.title('Attention Weights (Average Over All Heads)')
# plt.xlabel('Token')
# plt.ylabel('Token')
# plt.show()
