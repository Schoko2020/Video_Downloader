import customtkinter as ctk
import threading
import logic



class VideoDownloaderApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Video Downloader")
        self.geometry("850x650")

        try:
            self.iconbitmap("icon.ico")
        except:
            pass

        self.grid_columnconfigure(0, weight=1)

        self.label_title = ctk.CTkLabel(self, text = "Link eingeben")
        self.label_title.grid(row=0, column=0, pady=20)

        self.entry_link = ctk.CTkEntry(self, width=400)
        self.entry_link.grid(row=1, column=0, pady=20)

        self.button_download = ctk.CTkButton(self, text="Download", command=self.start_download)
        self.button_download.grid(row=2, column=0, pady=20)

        self.label_status = ctk.CTkLabel(self, text="Warte auf Link...")
        self.label_status.grid(row=3, column=0, pady=10)

        self.progress_bar = ctk.CTkProgressBar(self, width=400)
        self.progress_bar.set(0)
        self.progress_bar.grid(row=4, column=0, pady=10)

        self.button_update = ctk.CTkButton(self, text="yt-dlp Update", command=self.start_update, width=100)
        self.button_update.grid(row=5, column=0, pady=600)


    def start_download(self):
        link = self.entry_link.get()

        if link == "":
            print("Kein Link eingegeben")
            return

        worker_thread = threading.Thread(target=self.background_task, args=(link,))

        worker_thread.start()

    def background_task(self, link):
        print("background downloading is starting")
        logic.run_download(link, self.show_progress)
        print("Download fertig!")

    def show_progress(self, stream_data):
        if stream_data['status'] == 'downloading':
            data_str = stream_data.get('_percent_str')
            data_str = data_str.replace("%", "")
            data_float = float(data_str)
            data_float /= 100
            print(f'Lade {data_float}')

            if data_float != 1:
                self.label_status.configure(text=f"{data_str}%")

            if data_float == 1:
                self.label_status.configure(text="Fertig!")

            self.progress_bar.set(data_float)

    def start_update(self):
         self.label_status.configure(text="Suche Updates...")
         update_thread = threading.Thread(target=self.run_update_process)
         update_thread.start()

    def run_update_process(self):
         success = logic.update_yt_dlp()
         if success:
            self.label_status.configure(text="Update fertig! Bitte Neustarten.")
         else:
            self.label_status.configure(text="Update fehlgeschlagen.")


            
    

        #print(f"Der Button wurde geklickt! Link ist: {link}")
