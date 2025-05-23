from gtts import gTTS # type: ignore
import pyttsx3
from tkinter import OptionMenu, StringVar, Tk, Label, Text, Button, filedialog, messagebox
import PyPDF2

# ==========    Functions    ==========
# ==========    Functions    ==========
# ==========    Functions    ==========

#   speaking txet
def speak_text():
    text = text_box.get("1.0", "end").strip()
    # if text:
    #     engine.say(text)
    #     engine.runAndWait()

    if not text:
        messagebox.showwarning("Empty Text", "Please enter or upload some text first.")
        return
    
    engine = pyttsx3.init()

    selected_voice = voice_var.get()
    voices = engine.getProperty("voices")

    for v in voices:
        if selected_voice == "male" and "male" in v.name.lower():
            engine.setProperty("voice", v.id)
            break
        elif selected_voice == "female" and "female" in v.name.lower():
            engine.setProperty("voice", v.id)
            break
        elif selected_voice == "default":
            break

    engine.say(text)
    engine.runAndWait()



#   prints text from textbox to the terminal
def show_text():
    user_input = text_box.get("1.0", "end") #reads the test box
    print("You typed:", user_input)


#   allows user to upload files from computer
def open_file() :
    file_path = filedialog.askopenfilename(filetypes= [("Text or PDF files", "*.txt *pdf")])
    if not file_path:
        return 
    
    if file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    elif file_path.endswith("pdf"):
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            content = "\n".join([page.extract_text() for page in reader.pages if page.extraxt_text()])
    else:
        content = "Unsupported file type."  

    text_box.delete("1.0", "end")
    text_box.insert("1.0", content)

engin = pyttsx3.init()


#   allows user to save speech files

def save_audio():
    text = text_box.get("1.0", "end").strip()
    
    if not text:
        messagebox.showwarning("Empty Text", "Please enter or upload some text first.")
        return
    
    file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3"), ("WAV files", "*.wav")])
    
    if not file_path:
        return
    
    if file_path.endswith(".mp3"):
        # tts = gTTS(text=text)
        # tts.save(file_path)

        selected_lang = lang_var.get()
        tts = gTTS(text=text, lang=selected_lang)
        tts.save(file_path)
        messagebox.showinfo("Success", "MP3 files saved successfully")

    elif file_path.endswith(".wav"):
        engine = pyttsx3.init()
        engine.save_to_file(text, file_path)
        engine.runAndWait()
        messagebox.showinfo("Success", "WAV files saved successfully")
        




# ==========    Logic    ==========
# ==========    Logic    ==========
# ==========    Logic    ==========


# create the window

root = Tk()
root.title("My First TTS App")  #the title of the window
root.geometry("500x500")        # width and height is the window in pixels

# Adding a label
label = Label (root, text="Enter your text below:")
label.pack()

# Adding a multi-line text box
text_box = Text (root, height=10, width=50)
text_box.pack()


# Dropdowns at the top of your GUI setup (before buttons)
voice_var = StringVar(value="default")
lang_var = StringVar(value="en")

Label(root, text="Voice (pyttsx3):").pack()
voice_menu = OptionMenu(root, voice_var, "default", "male", "female")
voice_menu.pack()

Label(root, text="Language (gTTS):").pack()
lang_menu = OptionMenu(root, lang_var, "en", "es", "fr", "de", "hi")
lang_menu.pack()




# ==========    Buttons    ==========
# ==========    Buttons    ==========
# ==========    Buttons    ==========

# Adding a button to print in the terminal 

button = Button (root, text="Print Text", command=show_text)
button.pack()

# Adding a button to speak text
button = Button (root, text="🔊 Speak Text", command=speak_text)
button.pack()
button = Button(root, text="📂 Upload TxT / PDF Files", command=open_file).pack()


# Adding a button to save audio
button = Button(root, text="💾 Save as MP3/Wav", command=save_audio).pack()








# Starts the app's loop
root.mainloop()


