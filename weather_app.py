import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests

# 🔑 Replace this with your OpenWeatherMap API key
API_KEY = "51f96dc7615f4af945ec7ff3b326e5e5"

def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] == "404":
            messagebox.showerror("Error", "City not found.")
            return

        weather = data["weather"][0]["description"].title()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        result_text = (
            f"Weather: {weather}\n"
            f"Temperature: {temp}°C\n"
            f"💧 Humidity: {humidity}%\n"
            f"🍃 Wind Speed: {wind} m/s"
        )
        result_label.config(text=result_text)

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

# 🌈 GUI Setup
root = tk.Tk()
root.title("🌤️ Weather App")
root.geometry("450x400")
root.resizable(False, False)

# 📷 Load and set background image
bg_img = Image.open("background_bg.jpg").resize((450, 400))
bg_photo = ImageTk.PhotoImage(bg_img)
tk.Label(root, image=bg_photo).place(x=0, y=0, relwidth=1, relheight=1)

# 🔲 Overlay frame to place widgets on top
overlay = tk.Frame(root, bg="#ffffff", bd=0)
overlay.place(relx=0.5, rely=0.5, anchor="center")

# 📝 Title
tk.Label(overlay, text="Live Weather App", font=("Helvetica", 18, "bold"), bg="#ffffff", fg="#0077b6").pack(pady=10)

# 🌆 City Input
tk.Label(overlay, text="Enter City:", font=("Arial", 12), bg="#ffffff").pack()
city_entry = tk.Entry(overlay, font=("Arial", 14), width=15, justify="center", bd=2, relief="solid")
city_entry.pack(pady=5)

# 🔍 Get Weather Button
tk.Button(
    overlay, text="Get Weather", command=get_weather,
    bg="#0077b6", fg="white", font=("Arial", 12, "bold"),
    padx=10, pady=5
).pack(pady=10)

# 📋 Result Display
result_label = tk.Label(overlay, text="", font=("Arial", 12), bg="#ffffff", fg="#023047", justify="center")
result_label.pack(pady=10)

# 🔚 Footer
tk.Label(root, text="Powered by OpenWeatherMap", font=("Arial", 9), bg="#ffffff", fg="gray").pack(side="bottom", pady=8)

root.mainloop()
