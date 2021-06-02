
import random
import pandas

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

student_score = {student: random.randint(50, 100) for student in names}
print(student_score)

passed_students = {student:score for (student, score) in student_score.items() if score >= 60}
print(passed_students)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
word_length = {word: len(word) for word in sentence.split()}
print(word_length)

weather_C = {
    "Monday": 24,
    "Tuesday": 30,
    "Wednesday": 35,
    "Thursday": 28,
    "Friday": 22,
    "Saturday": 30,
    "Sunday": 27
}

weather_F = {day: temp * 9/5 + 32 for (day, temp) in weather_C.items()}
print(weather_F)

student_dict = {
    "students": ["Angela", "James", "Lily"],
    "scores": [56, 78, 83]
}

df = pandas.DataFrame(student_dict)
print(df)
for (index, row) in df.iterrows():
    print(row.students)
    print(row.scores)
    if row.students == "Angela":
        print(row.scores)






