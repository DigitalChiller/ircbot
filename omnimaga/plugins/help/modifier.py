## LICENSE
#    This file is part of nBot.
#
#    nBot is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    nBot is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with nBot.  If not, see <http://www.gnu.org/licenses/>.
#

def sendSyntax(self, cmd, plugin=None):
	if cmd in self.cmds:
		if len(self.cmds[cmd]) == 0:
			self.feedback("no plugin featuring this command")
		else:
			if len(self.cmds[cmd]) > 1 and plugin == None:
				self.feedback("these plugins are featuring the command, please be more specific: " + ", ".join(self.cmds[cmd]))
			elif len(self.cmds[cmd]) == 1:
				plugin = self.cmds[cmd]

			for l in self.plVars[plugin].help[cmd]:
				self.feedback(l)
