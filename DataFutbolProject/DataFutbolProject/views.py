from django.shortcuts import render
import openai, os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_KEY", None)

def chatbot(request):
    chatbot_response=None
    if api_key is not None and request.method=="POST":
        openai.api_key=api_key
        role = {"role": "system","content": "Eres un asistente tecnico de futbol, tienes que ayudar a los entrenadores"}
        prompt = [role]
        user_input= request.POST.get('user_input')
        prompt.append({"role": "user", "content": user_input})

        response=openai.Completion.create(
            engine="text-davinci-003",
            prompt = prompt)
        print(response)

        chatbot_response = response["choices"][0]["text"]
    else:
        print("Error with openAi Key")
    return render(request, 'profile.html',{"response":chatbot_response})