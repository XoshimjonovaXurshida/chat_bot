import g4f

content="takrorlanuvchi sikllar haqida ma'lumot ber, o'zbek tilida"

response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": content}],
    stream=True,
)
for message in response:
    print(message, flush=True, end='')