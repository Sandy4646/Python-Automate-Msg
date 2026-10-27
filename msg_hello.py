import pywhatkit
import time

phone_numbers = [
    "+917075748497",
    "+919059938185",
    "+919000247829",
    "+919949311561",
    "+917730976982",
    "+919767072983",
    "+919010948492",
    "+919652193600",
    "+917095149752",
    "+918179895478",
    "+918500128112",
    "+919912564640",
    "+919703349061",
    "+917671869891",
    "+919705428150",
    "+919985983246",
    "+918374234247",
    "+919908077465",
    "+918106269000",
    "+919701194988",
    "+919494521791",
    "+919502470205",
    "+919666319269",
    "+919959266304",
    "+919000029484",
    "+916303311799",
    "+917569822035",
    "+917731825769",
    "+919676672444",

]

message = """
🌿 WORLD PSORIASIS DAY | SPECIAL ANNOUNCEMENT

Dear Sir/Madam,

Sri Bhaskara Ayurvedic Hospital is offering FREE CONSULTATIONS from October 23rd to 31st at our centres in Hyderabad, Vizag, Vijayawada, and Bangalore.

🎥 Watch Our Patient Testimonial Video:
https://vimeo.com/reviews/84de2786-e625-4a86-aa8b-5c9aaf891d2c/videos/1238389291

📅 Offer Valid: October 23–31
📍 Locations: Hyderabad | Vizag | Vijayawada | Bangalore
🎉 Consultation Fee: FREE

📞 Book Your Free Consultation:
7981855536, 9550211483

Warm regards,
Team Sri Bhaskara Ayurvedic Hospital 🌿


""" # your message

for number in phone_numbers:
    pywhatkit.sendwhatmsg_instantly(
        number,
        message,
        wait_time=12,      # seconds to wait for WhatsApp Web to load (default is 15)
        tab_close=True,    # auto-closes the tab after sending
        close_time=3       # seconds to wait before closing
    )
    time.sleep(5)  # small buffer between numbers

