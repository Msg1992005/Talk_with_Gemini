# the instruction given to user
instruction_for_chat = """
        Hello there Type your prompt here and for exit just type exit on your prompt.
        Please 1st provide your Gemini API befor start chating. for more info type help_api on termina
        """

# configuration of the gemini ai
generation_config = {
          "temperature": 0.4,
          "top_p": 1,
          "top_k": 1,
          "max_output_tokens": 1050,
        }
safety_settings = [
          {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_ONLY_HIGH"
          },
          {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_ONLY_HIGH"
          },
          {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_ONLY_HIGH"
          },
          {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_ONLY_HIGH"
          },
        ]
# a constant to deside wether you want to store your chat history or not
saving = True
default_file = "Previous_chat_histories.txt"
def save_chat(file,data):
    with open(file,"a") as user_chat:
        user_chat.write(data)
def chat_command():
    import gc
    gc.enable()
    _instruction =instruction_for_chat
    _config = generation_config
    _setting = safety_settings
    _gemini = True
    print(_instruction)
    while _gemini:
        prompt = input("Gemini # ")
        

        match(prompt):
            case"clear_history":
                with open(default_file,"w") as f:
                    f.write("cleared")
            case"exit":
                gc.collect()
                _gemini = False
                del genai
            case"clear":
              from os import system
              system("cls")
              del system
            
            case _:
                import google.generativeai as genai
                genai.configure(api_key="AIzaSyA7tSOMa-udZVth9yF0L__xlMH4cBXOlqs")
                model = genai.GenerativeModel('gemini-pro',generation_config=_config,safety_settings=_setting)
                response = model.generate_content(f"{prompt}",)
                print(response.text.replace('•', '  *'))
                if saving != False:
                    save_chat(default_file,"me-> \t"+prompt+": \t \n response -> \t"+response.text+"/n")
                else:
                    pass
                
if(__name__=="__main__"):
  chat_command()
