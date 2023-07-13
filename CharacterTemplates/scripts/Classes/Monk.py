from CharacterTemplates.scripts.CharacterItem import ClassItem
from configurator.Entity import Entity


class Monk(Entity, ClassItem):
	def __init__(self):
		Entity.__init__(self)
		ClassItem.__init__(self)
		self._HitDie = '1d8'
		self._name = 'Monk'
		self._description = """
<b>Subset of WikiDot</b> http://dnd5e.wikidot.com
<div class="col-lg-12">
<p>As a monk, you gain the following class features.</p>
<h5 id="toc1"><span>Hit Points</span></h5>
<p><strong>Hit Dice:</strong> 1d8 per monk level<br>
<strong>Hit Points at 1st Level:</strong> 8 + your Constitution modifier<br>
<strong>Hit Points at Higher Levels:</strong> 1d8 (or 5) + your Constitution modifier per monk level after 1st</p>
<h5 id="toc2"><span>Proficiencies</span></h5>
<p><strong>Armor:</strong> None<br>
<strong>Weapons:</strong> Simple weapons, shortswords<br>
<strong>Tools:</strong> Choose one type of artisan's tools or one musical instrument<br>
<strong>Saving Throws:</strong> Strength, Dexterity<br>
<strong>Skills:</strong> Choose two from Acrobatics, Athletics, History, Insight, Religion, and Stealth</p>
<h5 id="toc3"><span>Equipment</span></h5>
<p>You start with the following equipment, in addition to the equipment granted by your background:</p>
<ul>
<li>(a) a shortsword or (b) any simple weapon</li>
<li>(a) a dungeoneer's pack or (b) an explorer's pack</li>
<li>10 darts</li>
</ul>
<h3 id="toc4"><span>Unarmored Defense</span></h3>
<p>Beginning at 1st level, while you are wearing no armor and not wielding a shield, your AC equals 10 + your Dexterity modifier + your Wisdom modifier.</p>
<h3 id="toc5"><span>Martial Arts</span></h3>
<p>At 1st level, your practice of martial arts gives you mastery of combat styles that use unarmed strikes and monk weapons, which are shortswords and any simple melee weapons that don't have the two-handed or heavy property.</p>
<p>You gain the following benefits while you are unarmed or wielding only monk weapons and you aren't wearing armor or wielding a shield:</p>
<ul>
<li>You can use Dexterity instead of Strength for the attack and damage rolls of your unarmed strikes and monk weapons.</li>
</ul>
<ul>
<li>You can roll a d4 in place of the normal damage of your unarmed strike or monk weapon. This die changes as you gain monk levels, as shown in the Martial Arts column of the Monk table.</li>
</ul>
<ul>
<li>When you use the Attack action with an unarmed strike or a monk weapon on your turn, you can make one unarmed strike as a bonus action. For example, if you take the Attack action and attack with a quarterstaff, you can also make an unarmed strike as a bonus action, assuming you haven't already taken a bonus action this turn.</li>
</ul>
<p>Certain monasteries use specialized forms of the monk weapons. For example, you might use a club that is two lengths of wood connected by a short chain (called a nunchaku) or a sickle with a shorter, straighter blade (called a kama). Whatever name you use for a monk weapon, you can use the game statistics provided for the weapon on the <a href="http://dnd5e.wikidot.com/weapons">Weapons</a> page.</p>
<h3 id="toc6"><span>Ki</span></h3>
<p>Starting at 2nd level, your training allows you to harness the mystic energy of ki. Your access to this energy is represented by a number of ki points. Your monk level determines the number of points you have, as shown in the Ki Points column of the Monk table.</p>
<p>You can spend these points to fuel various ki features. You start knowing three such features: Flurry of Blows, Patient Defense, and Step of the Wind. You learn more ki features as you gain levels in this class.</p>
<p>When you spend a ki point, it is unavailable until you finish a short or long rest, at the end of which you draw all of your expended ki back into yourself. You must spend at least 30 minutes of the rest meditating to regain your ki points.</p>
<p>Some of your ki features require your target to make a saving throw to resist the feature's effects. The saving throw DC is calculated as follows:</p>
<p><strong>Ki save DC</strong> = 8 + your proficiency bonus + your Wisdom modifier</p>
<ul>
<li><strong>Flurry of Blows.</strong> Immediately after you take the Attack action on your turn, you can spend 1 ki point to make two unarmed strikes as a bonus action.</li>
</ul>
<ul>
<li><strong>Patient Defense.</strong> You can spend 1 ki point to take the Dodge action as a bonus action on your turn.</li>
</ul>
<ul>
<li><strong>Step of the Wind.</strong> You can spend 1 ki point to take the Disengage or Dash action as a bonus action on your turn, and your jump distance is doubled for the turn.</li>
</ul>
<h3 id="toc7"><span>Unarmored Movement</span></h3>
<p>Starting at 2nd level, your speed increases by 10 feet while you are not wearing armor or wielding a shield. This bonus increases when you reach certain monk levels, as shown in the Monk table.</p>
<p>At 9th level, you gain the ability to move along vertical surfaces and across liquids on your turn without falling during the move.</p>
<h3 id="toc8"><span>Dedicated Weapon (Optional)</span></h3>
<p>Also at 2nd level, you train yourself to use a variety of weapons as monk weapons, not just simple melee weapons and shortswords. Whenever you finish a short or long rest, you can touch one weapon, focus your ki on it, and then count that weapon as a monk weapon until you use this feature again.</p>
<p>The chosen weapon must meet these criteria:</p>
<ul>
<li>The weapon must be a simple or martial weapon.</li>
</ul>
<ul>
<li>You must be proficient with it.</li>
</ul>
<ul>
<li>It must lack the heavy and special properties.</li>
</ul>
</div>
"""

	def register(self):
		super().register()

	def update(self):
		super().update()
