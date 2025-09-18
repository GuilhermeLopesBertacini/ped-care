from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Agora você é uma agenda inteligente para consultas médicas, e também atua como recepcionista, se introduza"
)
print(response.text)