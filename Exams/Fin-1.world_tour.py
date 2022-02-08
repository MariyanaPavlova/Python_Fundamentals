ext = input()

while True:
    tour = input()
    if tour == "Travel":
        break

    tour_s = tour.split(":")
    command = tour_s[0]

    if command.startswith("Add"):
        index = int(tour_s[1])
        destin = tour_s[2]

        if 0 <= index < len(text):
            beg = text[:index]
            end = text[index:]
            text = beg + destin + end
        print(text)

    elif command == "Remove Stop":
        start_i = int(tour_s[1])
        end_i = int(tour_s[2])

        if 0 <= start_i < len(text) and 0 <= end_i < len(text):
            text = text[:start_i]+text[end_i+1:]

            #text = text.replace(text[start_i:end_i], "", 1)
        print(text)

    elif command == "Switch":
        old = tour_s[1]
        new = tour_s[2]

        if old in text:
            text = text.replace(old, new)
        print(text)

print(f"Ready for world tour! Planned stops: {text}")
