import datetime as dt

import matplotlib.pyplot as plt
from pyscript import display, web, when


web.page["hi"].textContent = "Hello there! Please enter your name and click Go:"
web.page["date"].textContent = dt.date.today().strftime("%A %B %d, %Y")
web.page["pythonStatus"].textContent = "Python tools are ready."
web.page["namebtn"].disabled = False
web.page["interestbtn"].disabled = False


@when("click", "#namebtn")
def greet(_event):
    name = web.page["name"].value.strip()

    if not name:
        web.page["saludo"].textContent = "Please enter your name first."
        return

    web.page["saludo"].textContent = (
        f"Greetings {name}! Nice to have you here. "
        "Are you interested in data visualization?"
    )
    web.page["inputInterest"].style["display"] = "flex"


def show_life_expectancy_chart():
    countries = [
        "Afghanistan", "Argentina", "Australia", "Bolivia", "Brazil", "Canada",
        "Chile", "Colombia", "Haiti", "Japan", "Mexico", "Venezuela",
    ]
    life_expectancy = [65, 77, 83, 72, 76, 82, 80, 77, 64, 85, 75, 72]

    figure, axis = plt.subplots(figsize=(10, 5))
    bars = axis.bar(countries, life_expectancy, color="#7FFFD4")
    axis.set_xlabel("Country")
    axis.set_ylabel("Life expectancy (years)")
    axis.set_title("Life expectancy in selected countries (2020)")
    axis.tick_params(axis="x", labelrotation=35)

    for bar, value in zip(bars, life_expectancy):
        axis.text(
            bar.get_x() + bar.get_width() / 2,
            value,
            str(value),
            ha="center",
            va="bottom",
        )

    figure.tight_layout()
    display(figure, target="graficos", append=False)
    plt.close(figure)

    lowest = min(range(len(life_expectancy)), key=life_expectancy.__getitem__)
    highest = max(range(len(life_expectancy)), key=life_expectancy.__getitem__)
    web.page["grafInsight"].textContent = (
        f"Lowest: {countries[lowest]} ({life_expectancy[lowest]} years). "
        f"Highest: {countries[highest]} ({life_expectancy[highest]} years)."
    )


@when("click", "#interestbtn")
def show_interest_result(_event):
    answer = web.page["interested"].value.strip().casefold()
    interest = web.page["interest"]

    if answer in {"yes", "si"}:
        interest.textContent = (
            "Great! This bar chart uses Matplotlib to compare life expectancy "
            "and highlight the lowest and highest values."
        )
        show_life_expectancy_chart()
    elif answer == "no":
        interest.textContent = "Sorry about that. Maybe next time."
        web.page["graficos"].innerHTML = ""
        web.page["grafInsight"].textContent = ""
    else:
        interest.textContent = "Please answer yes or no."
