## variables
# msg = message dict
# args = list of args
# nickHgl = is bot addressed? (bot: <message>)
# target = channel or private chat
# fromOwner = author is owner
# 
## functions
# self.feedback(msg)
#  use this to send something back
# bot.botdo(action, *args, **kwargs)
#  use this to tell the bot to do something

if nickHgl:
	if fromOwner or auth(uperms, plName, msg["cmd"]):
		if msg["cmd"] == "join":
			if len(args) == 1:
				bot.botdo("join", msg["args"])
			else:
				self.handleError("syntax")

		elif msg["cmd"] == "part":
			if len(args) == 0:
				bot.botdo("part", target)
			elif len(args) == 1:
				bot.botdo("part", msg["args"])

		elif msg["cmd"] == "nick":
			if len(args) == 1:
				bot.botdo("nick", args[0])
			else:
				self.handleError("syntax")

		elif msg["cmd"] == "exit":
			self.feedback("not implemented")

		elif msg["cmd"] == "privmsg":
			if len(args) > 1:
				bot.botdo("privmsg", args[0], " ".join(args[1:]))
			else:
				self.handleError("syntax")

		elif msg["cmd"] == "sendraw":
			if len(args) > 1:
				bot.botdo("raw", msg["args"])
			else:
				self.handleError("syntax")

		elif msg["cmd"] == "botdo":
			if len(args) > 1:
				bot.botdo(args[0], msg["args"].split("|"))
			else:
				self.handleError("syntax")

		elif msg["cmd"] == "refreshconfig":
			bot.configFile.read()
			bot.config = bot.configFile.data
			self.feedback("success")
