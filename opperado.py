import random
import os

import hikari


opperado = hikari.GatewayBot(os.environ["FICHA_DE_OPPERADO"])
contador_de_mensagens_do_tutu = 0


@opperado.listen(hikari.MessageCreateEvent)
async def xingamento_de_tutu(evento):
	xingamentos = ["Bobo.", "Burro.", "Seboso.", "Chatão, mané.", "Boca de sebo."]
	if evento.content.lower() == "o tutu é":
		await evento.message.respond(random.choice(xingamentos))


@opperado.listen(hikari.MessageCreateEvent)
async def cala_a_boca(evento):
	calabocamentos = ["Quem chamou o Tutu?", "Ninguém gosta do Tutu, fica quieto!", "Cala a boca, Tutu"]
	global contador_de_mensagens_do_tutu
	if evento.message.author.id == os.environ.get("ID_DO_TUTU", 624365838610202624):
		contador_de_mensagens_do_tutu += 1
	if contador_de_mensagens_do_tutu == 30:
		contador_de_mensagens_do_tutu = 0
		await evento.message.respond(random.choice(calabocamentos))


opperado.run()
