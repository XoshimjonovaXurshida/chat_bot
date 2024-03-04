import g4f

content="takrorlanuvchi sikllar haqida ma'lumot ber, o'zbek tilida"
def chat_bot(content):
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": content}],
        #stream=True,
        )
    return response



def savol(savol, mavzu=""):
    if mavzu=="tibbiyot":
        content=f"savolim tibbiyot bilan bog'liq. {savol}ga tibbiyot yo'nalishida javob ber"
    elif mavzu=="dasturlash":
        content=f"savolim dasturlash bilan bog'liq. {savol}ga dasturlash yo'nalishida javob ber"
    else:
        content=f"Ushbu savolga o'zbek tilida javob ber, Savol - {savol}"
    javob=chat_bot(content)
    return javob




print(savol("dasturlash tili"))
print(32*"*")
print(savol("sikl","tibbiyot"))
print(32*"*")
print(savol("sikl","dasturlash"))

#for message in response:
#    print(message, flush=True, end='')