from tkinter import OptionMenu, StringVar, Tk, Label, Text, Button, filedialog, messagebox
from gtts import gTTS 
import pyttsx3
import PyPDF2
import os

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
    
    try:
    
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
    except Exception as e:
        messagebox.howerror("Error", f"Speech failes: {e}")

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
    
    try:
            

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
    except Exception as e:
        messagebox.showerroe("Error", f"Failed to save audio: {e}")

def upload_file():
    file_path = filedialog.askopenfilename(filetype=[("Text Files", "*.txt"), ("PDF files", "*.pdf")])
    if not file_path:
        return
    
    text_box.delete("1.0", "end")

    try:
        if file_path.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                text_box.insert("1.0", content)

        elif file_path.endswith(".pdf"):
            with open(file_path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                content = ""
                for page in reader.pages:
                    content += page.extract_text() + "\n"
                text_box.insert("1.0", content)

    except Exception as e:
        messagebox.showerror("Error", f"Failed to load file: {e}")
        
# ==========    Logic    ==========
# ==========    Logic    ==========
# ==========    Logic    ==========

# create the window
root = Tk()
root.title("Text To Speech App")  #the title of the window
root.geometry("500x500")        # width and height is the window in pixels

# Adding a label
label = Label (root, text="Enter your text below:")
label.pack()

# Adding a multi-line text box
text_box = Text (root, wrap="word", height=10, width=50)
text_box.pack(pady=10)

# Dropdowns for voice options
voice_var = StringVar(value="default")
Label(root, text="Voice (for WAV):").pack()
voice_menu = OptionMenu(root, voice_var, "default", "male", "female").pack()

# Dropdown for language options
lang_var = StringVar(value="en")
Label(root, text="Language (for MP3):").pack()
lang_menu = OptionMenu(root, lang_var, "en", "es", "fr", "de", "hi").pack()

# ==========    Buttons    ==========
# ==========    Buttons    ==========
# ==========    Buttons    ==========

# Adding a button to speak text
button = Button (root, text="🔊 Speak Text", command=speak_text).pack(pady=5)
# Adding a utton ti chose a file
button = Button(root, text="📂 Upload TxT / PDF Files", command=open_file).pack(pady=5)
# Adding a button to save audio
button = Button(root, text="💾 Save as MP3/Wav", command=save_audio).pack(pady=5)

# Starts the app's loop
root.mainloop()


