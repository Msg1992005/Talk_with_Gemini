# the instruction given to user
instruction_for_chat = """
        Hello there Type your prompt here and for exit just type exit on your prompt.
        Please 1st provide your Gemini API befor start chating.
        to clear history type clear_history
        """
# configuration of the gemini ai
generation_config = {
          "temperature": 0.6,
          "top_p": 1,
          "top_k": 1,
          "max_output_tokens": 2050,
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
default_clearing_size = 10 # in mb
# The text file where the text are gonna store
default_file = "Previous_chat_histories.txt"
# a function to save data on a file
def save_chat(file,data):
    with open(file,"a") as user_chat:
        user_chat.write(data)
def clear_storage():
        import os 
        if os.path.getsize(default_file)>= default_clearing_size*(1024**2):
                 with open(default_file,"w") as f:
                    f.write("")
        else:
            print(f"Your history size :  {os.path.getsize(default_file)} byte or {os.path.getsize(default_file)/1024} kb")
# a function to chat with gemini
def chat_command():
    # change saving to False to Not save the Chat history to
    _saving = True
    _instruction =instruction_for_chat
    _config = generation_config
    _setting = safety_settings
    _gemini = True
    _User_api = " "
    print(_instruction)
    while _gemini:
        prompt = input("Gemini # ")  
        # checking the prompts from user to find exeptional command
        match(prompt):
            # command to stop_saving
            case"stop_saving":
                    saving = False
        # command to clear history file
            case"clear_history":
                with open(default_file,"w") as f:
                    f.write("cleared")
        # command to exit the terminal
            case"exit":
                gc.collect()
                _gemini = False
                del genai
        # command to clear the terminal while chating with gemini
            case"clear":
              from os import system
              try:
                      system("cls")  # this is for window 
              except:
                      system("clear")
              del system
        # main chating place where you chat with gemini
            case _:
                if  _User_api == " ":
                        print("Please enter API key 1st")
                        _User_api = input("ENTER your api key")
                else:
                        try:
                                # importing gemini module , sorry i dont use request may be that saves more memory
                                import google.generativeai as genai
                        except:
                                from os import system
                                system("pip install google-generativeai")
                                import google.generativeai as genai
                        genai.configure(api_key=_User_api)  # setup the api with model
                        model = genai.GenerativeModel('gemini-pro',generation_config=_config,safety_settings=_setting)  # setup the model type
                        response = model.generate_content(f"{prompt}",) # the response from gemini
                        print(response.text.replace('•', '  *'))  # printing the response (i dont use for loop to print chunks of the chats so user now have to wait for long time
                        if _saving == True:
                                save_chat(default_file,"me-> \t"+prompt+": \t \n response -> \t"+response.text+"/n")
                        else:
                            pass  
if(__name__=="__main__"):
        try:
                chat_command()
        except:
                print("Error occure may be you type some inappropriate thing LOL,change the safty setting")
                print("Or else You provides wrong API")
                print("make sure to replace the _User_API variable with your api instand of manually giving api every time.")
        finally:
            clear_storage()  # to clear the history
exit()
