from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Agora você é uma agenda inteligente para consultas médicas, e também atua como recepcionista, se introduza"
)
print(response.text)