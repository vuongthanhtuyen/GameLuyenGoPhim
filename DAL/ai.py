# import openai

# # Set up your OpenAI API key
# openai.api_key = 'Your_aip'

# def generate_vietnamese_words():
#     # Prompt GPT-4 to generate a list of 100 Vietnamese words
#     prompt = "Hãy tạo ra một danh sách gồm 100 từ tiếng Việt."

#     response = openai.ChatCompletion.create(
#         model="gpt-4",  # or the appropriate model name
#         messages=[
#             {"role": "system", "content": "Bạn là một trợ lý AI."},
#             {"role": "user", "content": prompt}
#         ],
#         max_tokens=300  # Adjust if necessary
#     )

#     words = response.choices[0].message['content'].strip()
#     return words

# # Generate and display the list of 100 Vietnamese words
# vietnamese_words = generate_vietnamese_words()
# print(vietnamese_words)
