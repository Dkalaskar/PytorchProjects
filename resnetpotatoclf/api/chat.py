import openai
import os

openai.api_key = ("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")
# #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
# #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
# #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
# #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 new



# response = openai.Completion.create(
#     engine="davinci",
#     prompt="The quick brown fox jumps over the lazy dog",
#     max_tokens=50,
#     temperature=0.7,
#     top_p=0.9,
#     frequency_penalty=0.5,
#     presence_penalty=0.3,
    
# )

#################################################################################
model_engine = "text-davinci-03"
prompt = "Early Blight"
response = openai.Completion.create(
    engine='text-davinci-003',  # Specify the ChatGPT model
    prompt='Hello, ChatGPT!',
    max_tokens=50,  # Maximum length of the response
    temperature=0.7,  # Controls the randomness of the output (0.0 - deterministic, 1.0 - highly random)
    n = 1,  # Number of responses to generate
    stop=None 
    
)
print(response.choices[0].text.strip())