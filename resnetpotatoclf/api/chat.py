import openai
import os

openai.api_key = ("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")
#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
#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
#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
#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 new



response = openai.Completion.create(
    engine="davinci",
    prompt="The quick brown fox jumps over the lazy dog",
    max_tokens=50,
    temperature=0.7,
    top_p=0.9,
    frequency_penalty=0.5,
    presence_penalty=0.3,
    
)