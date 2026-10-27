import threading
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from core.assistant import Jarvis

class JarvisGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("JARVIS")
        self.root.geometry("820x560")
        self.root.minsize(700, 480)

        self.title = tk.Label(self.root, text="J A R V I S", font=("Segoe UI", 28, "bold"))
        self.title.pack(pady=(18, 4))
        self.status = tk.Label(self.root, text="READY", font=("Segoe UI", 10))
        self.status.pack()

        self.output = ScrolledText(self.root, wrap=tk.WORD, font=("Consolas", 11))
        self.output.pack(fill=tk.BOTH, expand=True, padx=18, pady=18)

        bar = tk.Frame(self.root)
        bar.pack(fill=tk.X, padx=18, pady=(0, 18))
        self.entry = tk.Entry(bar, font=("Segoe UI", 12))
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.entry.bind("<Return>", lambda e: self.send())
        tk.Button(bar, text="SEND", command=self.send, width=10).pack(side=tk.RIGHT)

        self.jarvis = Jarvis()
        self.write("JARVIS: GUI online.")

    def write(self, text):
        self.output.insert(tk.END, text + "\n")
        self.output.see(tk.END)

    def send(self):
        text = self.entry.get().strip()
        if not text:
            return
        self.entry.delete(0, tk.END)
        self.write("YOU: " + text)
        self.status.config(text="THINKING...")
        threading.Thread(target=self._work, args=(text,), daemon=True).start()

    def _work(self, text):
        response = self.jarvis.handle(text)
        self.root.after(0, lambda: self._done(response))

    def _done(self, response):
        self.write("JARVIS: " + response)
        self.status.config(text="READY")
        threading.Thread(target=self.jarvis.speaker.speak, args=(response,), daemon=True).start()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    JarvisGUI().run()
