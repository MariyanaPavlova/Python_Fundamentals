data = input()

exam_results = {}
submissions = {}

while not data == "exam finished":
    data = data.split("-")
    if len(data) > 2:
        username = data[0]
        lang = data[1]
        points = int(data[-1])

        if username not in exam_results:
            exam_results[username] = points
        else:
            if exam_results[username] < points:
                exam_results[username] = points

        if lang not in submissions:
            submissions[lang] = 1
        else:
            submissions[lang] += 1

    else:
        username = data[0]
        banned = data[1]
        del exam_results[username]

    data = input()

exam_results_sorted = sorted(exam_results.items(), key=lambda x: (-x[1], x[0]))
print('Results:')
for key, value in exam_results_sorted:
    print(f'{key} | {value}')

submissions_sorted = sorted(submissions.items(), key=lambda x: (-x[1], x[0]))
print("Submissions:")
for key, value in submissions_sorted:
    print(f'{key} - {value}')