now = 2021

born = int(input("Podaj rok urodzenia"))

if born > now:
    print("Nie prawidłowy rok urodzenia");
else:
    a = now - born;
    
    if a >= 18:
        print("Jesteś w wieku ", a, "lat - pełnoletni")
    else:
        print("Nie jesteś pełnoletni ! ", a, "lat ")