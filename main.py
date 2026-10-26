#comment :p
from pyscript import display, document


def countries_capital(e):
    document.getElementById("result").innerHTML = " "
    user_input = document.getElementById("input1").value.title().strip()
    countries = {
    'Madagascar': 'Antananarivo',
    'Mongolia': 'Ulaanbaatar',
    'Egypt': 'Cairo',
    'Philippines': 'Manila',
    'USA': 'Washington D.C.',
    'Denmark': 'Copenhagen',
    'Chile': 'Santiago'
    }
    country_checker = user_input in countries

    message_display  = (f"COUNTRY {user_input} UNIDENTIFIED")
    display(message_display[country_checker], target="result")
    