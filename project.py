

import csv
from datetime import datetime
import os
from collections import defaultdict

file = "my_money_goes_brrr.csv"

def hi_again():
    print("\nyo yo yo it's your broke homie")
    print("let me see how much you cried since last time\n")

def find_the_receipts():
    if not os.path.exists(file):
        print("first time getting cooked? welcome to the club")
        return []

    stuff = []
    try:
        with open(file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for thing in reader:
                try:
                    thing["Amount"] = float(thing["Amount"])
                    stuff.append(thing)
                except:
                    pass
        print(f"damn... found {len(stuff)} things that hurt to remember")
    except:
        print("file ghosted me, we starting over ig")
        stuff = []
    return stuff

def dont_let_it_disappear(stuff):
    with open(file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Date","Category","Amount","Description"])
        writer.writeheader()
        writer.writerows(stuff)
    print("\nsaved. your trauma is now eternal")

def oof_another_one(stuff):
    print("\nalright what did you do now")
    print("-" * 48)

    when = input(f"\nwhen did this happen (just enter for today → {datetime.now().strftime('%Y-%m-%d')}): ").strip()
    if not when:
        when = datetime.now().strftime("%Y-%m-%d")
        print("   today it is then... rough day huh")

    while True:
        money = input("\nhow much did we lose this time? $").strip().replace("$","").replace(",","")
        try:
            amount = float(money)
            if amount <= 0:
                print("   FREE?? bro stop the cap")
                continue
            break
        except:
            print("   numbers only you gremlin")

    print("\nwhat kinda L was this")
    print("food • coffee • rent • ubereats • skins • booze • therapy • groceries • idk")
    kind = input("\ncategory: ").strip().title()
    if not kind:
        kind = "Why Did I Do This"
        print("   → 'Why Did I Do This' perfect")

    what = input("\nspill the tea, what was it really: ").strip()
    if not what:
        what = "i don't wanna talk about it"

    stuff.append({
        "Date": when,
        "Category": kind,
        "Amount": amount,
        "Description": what
    })

    print(f"\n+${amount:.2f} → {kind}")
    print(f"   \"{what}\"")
    print("you're really out here collecting Ls like pokemon cards")

def show_the_whole_L(stuff):
    if not stuff:
        print("\nnothing yet... either you're rich or in denial")
        return

    print(f"\nfull list of your bad decisions ({len(stuff)} and counting)")
    print("═" * 95)
    for s in sorted(stuff, key=lambda x: x["Date"], reverse=True):
        print(f"{s['Date']} | {s['Category']:<15} | ${s['Amount']:>9,.2f} | {s['Description']}")
    print("═" * 95)

def the_cold_hard_truth(stuff):
    if not stuff:
        print("\nno pain no gain (literally)")
        return

    total = sum(x["Amount"] for x in stuff)
    cats = defaultdict(float)
    for x in stuff:
        cats[x["Category"]] += x["Amount"]

    print(f"\ncongrats you spent")
    print(f"                    ${total:,.2f}")
    print("\nhere's where your life went")

    for cat, amt in sorted(cats.items(), key=lambda x: x[1], reverse=True):
        pct = amt / total * 100
        bar = "█" * int(pct // 2)
        print(f"  {cat:<15} ${amt:>9,.2f}  {pct:>5.1f}% {bar}")

    print("\nkeep going king")
    print("at least you're aware now")

def run():
    print("expense tracker")
    print("for people who are tired of being surprised by their bank account\n")

    hi_again()
    my_mistakes = find_the_receipts()

    while True:
        print("\nwhat we doing boss")
        print("   1 → just spent money (again)")
        print("   2 → show me the receipts")
        print("   3 → how cooked am i")
        print("   4 → save and run away")

        pick = input("\n> ").strip()

        if pick == "1":
            oof_another_one(my_mistakes)
        elif pick == "2":
            show_the_whole_L(my_mistakes)
        elif pick == "3":
            the_cold_hard_truth(my_mistakes)
        elif pick == "4":
            dont_let_it_disappear(my_mistakes)
            print("\nsaved. go touch grass")
            print("see ya when you spend again (soon)")
            break
        else:
            print("bruh... 1 2 3 or 4")
            print("that's the entire vibe")

if __name__ == "__main__":
    run()
     
