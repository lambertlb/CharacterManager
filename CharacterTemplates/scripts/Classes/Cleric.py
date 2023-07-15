from CharacterTemplates.scripts.CharacterEntity import CharacterEntity
from CharacterTemplates.scripts.CharacterItem import ClassItem


class Cleric(CharacterEntity, ClassItem):
	def __init__(self):
		CharacterEntity.__init__(self)
		ClassItem.__init__(self)
		self._HitDie = '1d8'
		self._name = 'Cleric'
		self._description = """
<b>Subset of WikiDot</b> http://dnd5e.wikidot.com
<div class="feature">
<div class="row">
<h1 id="toc0"><span>Class Features</span></h1>
<div class="col-lg-12">
<p>As a cleric, you gain the following class features.</p>
<h5 id="toc1"><span>Hit Points</span></h5>
<p><strong>Hit Dice:</strong> 1d8 per cleric level<br>
<strong>Hit Points at 1st Level:</strong> 8 + your Constitution modifier<br>
<strong>Hit Points at Higher Levels:</strong> 1d8 (or 5) + your Constitution modifier per cleric level after 1st</p>
<h5 id="toc2"><span>Proficiencies</span></h5>
<p><strong>Armor:</strong> Light armor, medium armor, shields<br>
<strong>Weapons:</strong> All simple weapons<br>
<strong>Tools:</strong> None<br>
<strong>Saving Throws:</strong> Wisdom, Charisma<br>
<strong>Skills:</strong> Choose two from History, Insight, Medicine, Persuasion, and Religion</p>
<h5 id="toc3"><span>Equipment</span></h5>
<p>You start with the following equipment, in addition to the equipment granted by your background:</p>
<ul>
<li>(a) a mace or (b) a warhammer (if proficient)</li>
<li>(a) scale mail, (b) leather armor, or (c) chain mail (if proficient)</li>
<li>(a) a light crossbow and 20 bolts or (b) any simple weapon</li>
<li>(a) a priest's pack or (b) an explorer's pack</li>
<li>A shield and a holy symbol</li>
</ul>
<h3 id="toc4"><span>Spellcasting</span></h3>
<p>As a conduit for divine power, you can cast cleric spells.</p>
<h5 id="toc5"><span>Cantrips</span></h5>
<p>At 1st level, you know three cantrips of your choice from the <a href="http://dnd5e.wikidot.com/spells:cleric">cleric spell list</a>. You learn additional cleric cantrips of your choice at higher levels, as shown in the Cantrips Known column of the Cleric table.</p>
<h5 id="toc6"><span>Spell Slots</span></h5>
<p>The Cleric table shows how many spell slots you have to cast your cleric spells of 1st level and higher. To cast one of these spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest.</p>
<p>You prepare the list of cleric spells that are available for you to cast, choosing from the cleric spell list. When you do so, choose a number of cleric spells equal to your Wisdom modifier + your cleric level (minimum of one spell). The spells must be of a level for which you have spell slots.</p>
<p>For example, if you are a 3rd-level cleric, you have four 1st-level and two 2nd-level spell slots. With a Wisdom of 16, your list of prepared spells can include six spells of 1st or 2nd level, in any combination. If you prepare the 1st-level spell <a href="http://dnd5e.wikidot.com/spell:cure-wounds">Cure Wounds</a>, you can cast it using a 1st-level or 2nd-level slot. Casting the spell doesn't remove it from your list of prepared spells.</p>
<p>You can change your list of prepared spells when you finish a long rest. Preparing a new list of cleric spells requires time spent in prayer and meditation: at least 1 minute per spell level for each spell on your list.</p>
<h5 id="toc7"><span>Spellcasting Ability</span></h5>
<p>Wisdom is your spellcasting ability for your cleric spells. The power of your spells comes from your devotion to your deity. You use your Wisdom whenever a cleric spell refers to your spellcasting ability. In addition, you use your Wisdom modifier when setting the saving throw DC for a cleric spell you cast and when making an attack roll with one.</p>
<p><strong>Spell save DC</strong> = 8 + your proficiency bonus + your Wisdom modifier</p>
<p><strong>Spell attack modifier</strong> = your proficiency bonus + your Wisdom modifier</p>
<h5 id="toc8"><span>Ritual Casting</span></h5>
<p>You can cast a cleric spell as a ritual if that spell has the ritual tag and you have the spell prepared.</p>
<h5 id="toc9"><span>Spellcasting Focus</span></h5>
<p>You can use a holy symbol as a spellcasting focus for your cleric spells.</p>
<h3 id="toc10"><span>Divine Domain</span></h3>
<p>At 1st level, you choose a domain shaped by your choice of Deity and the gifts they grant you. Your choice grants you domain spells and other features when you choose it at 1st level. It also grants you additional ways to use Channel Divinity when you gain that feature at 2nd level, and additional benefits at 6th, 8th, and 17th levels.</p>
<table class="wiki-content-table">
<tbody><tr>
<th>Domain</th>
<th>Source</th>
</tr>
<tr>
<td><a href="http://dnd5e.wikidot.com/cleric:arcana">Arcana</a></td>
<td>Sword Coast Adventurer's Guide</td>
</tr>
<tr>
<td><a href="http://dnd5e.wikidot.com/cleric:death">Death</a></td>
<td>Dungeon Master's Guide</td>
</tr>
<tr>
<td><a href="http://dnd5e.wikidot.com/cleric:forge">Forge</a></td>
<td>Xanathar's Guide to Everything</td>
</tr>
<tr>
<td><a href="http://dnd5e.wikidot.com/cleric:grave">Grave</a></td>
<td>Xanathar's Guide to Everything</td>
</tr>
<tr>
<td><a href="http://dnd5e.wikidot.com/cleric:knowledge">Knowledge</a></td>
<td>Player's Handbook</td>
</tr>
<tr>
<td><a href="http://dnd5e.wikidot.com/cleric:life">Life</a></td>
<td>Player's Handbook</td>
</tr>
<tr>
<td><a href="http://dnd5e.wikidot.com/cleric:light">Light</a></td>
<td>Player's Handbook</td>
</tr>
<tr>
<td><a href="http://dnd5e.wikidot.com/cleric:nature">Nature</a></td>
<td>Player's Handbook</td>
</tr>
<tr>
<td><a href="http://dnd5e.wikidot.com/cleric:order">Order</a></td>
<td>Guildmaster's Guide to Ravnica<br>
Tasha's Cauldron of Everything</td>
</tr>
<tr>
<td><a href="http://dnd5e.wikidot.com/cleric:peace">Peace</a></td>
<td>Tasha's Cauldron of Everything</td>
</tr>
<tr>
<td><a href="http://dnd5e.wikidot.com/cleric:tempest">Tempest</a></td>
<td>Player's Handbook</td>
</tr>
<tr>
<td><a href="http://dnd5e.wikidot.com/cleric:trickery">Trickery</a></td>
<td>Player's Handbook</td>
</tr>
<tr>
<td><a href="http://dnd5e.wikidot.com/cleric:twilight">Twilight</a></td>
<td>Tasha's Cauldron of Everything</td>
</tr>
<tr>
<td><a href="http://dnd5e.wikidot.com/cleric:war">War</a></td>
<td>Player's Handbook</td>
</tr>
<tr>
<th colspan="2">The following domains are designed for the Amonkhet setting, but may be used elsewhere with DM permission</th>
</tr>
<tr>
<td><a href="http://dnd5e.wikidot.com/cleric:solidarity">Solidarity</a></td>
<td><a href="https://media.wizards.com/2017/downloads/magic/plane-shift_amonkhet.pdf">Amonkhet</a></td>
</tr>
<tr>
<td><a href="http://dnd5e.wikidot.com/cleric:strength">Strength</a></td>
<td><a href="https://media.wizards.com/2017/downloads/magic/plane-shift_amonkhet.pdf">Amonkhet</a></td>
</tr>
<tr>
<td><a href="http://dnd5e.wikidot.com/cleric:ambition">Ambition</a></td>
<td><a href="https://media.wizards.com/2017/downloads/magic/plane-shift_amonkhet.pdf">Amonkhet</a></td>
</tr>
<tr>
<td><a href="http://dnd5e.wikidot.com/cleric:zeal">Zeal</a></td>
<td><a href="https://media.wizards.com/2017/downloads/magic/plane-shift_amonkhet.pdf">Amonkhet</a></td>
</tr>
<tr>
<th colspan="2">The following subclass is unofficial homebrew created by WOTC affiliated DM, Matthew Mercer</th>
</tr>
<tr>
<td><a href="http://dnd5e.wikidot.com/cleric:blood">Blood</a></td>
<td>Tal'Dorei Campaign Guide</td>
</tr>
<tr>
<th colspan="2">The following domains are unofficial content developed by Eberron writer Keith Baker and released on the Dungeon Master's Guild</th>
</tr>
<tr>
<td><a href="http://dnd5e.wikidot.com/cleric:mind">Mind</a></td>
<td>Exploring Eberron</td>
</tr>
<tr>
<th colspan="2">The following domains are unofficial content developed by WotC designers</th>
</tr>
<tr>
<td><a href="http://dnd5e.wikidot.com/cleric:beauty-hb">Beauty</a></td>
<td colspan="2"><a href="https://twitter.com/mikemearls/status/1015752965213204480">Twitter</a></td>
</tr>
<tr>
<th colspan="2">Unearthed Arcana</th>
</tr>
<tr>
<td><a href="http://dnd5e.wikidot.com/cleric:fate-ua">Fate</a></td>
<td><a href="https://media.wizards.com/2022/dnd/downloads/UA2022-WondersoftheMultiverse.pdf">Unearthed Arcana 85 - Wonders of the Multiverse</a></td>
</tr>
<tr>
<th colspan="2">Archived Unearthed Arcana</th>
</tr>
<tr>
<td><a href="http://dnd5e.wikidot.com/cleric:city-ua">City</a></td>
<td><a href="https://media.wizards.com/2015/downloads/dnd/UA_ModernMagic.pdf">Unearthed Arcana 7 - Modern Magic</a></td>
</tr>
<tr>
<td><a href="http://dnd5e.wikidot.com/cleric:protection-ua">Protection</a></td>
<td><a href="https://media.wizards.com/2016/dnd/downloads/UA_Cleric.pdf">Unearthed Arcana 22 - Cleric</a></td>
</tr>
<tr>
<td><a href="http://dnd5e.wikidot.com/cleric:twilight-ua">Twilight</a></td>
<td><a href="https://media.wizards.com/2019/dnd/downloads/UA-TwilightFireNames.pdf">Unearthed Arcana 63 - Cleric, Druid, Wizard</a></td>
</tr>
<tr>
<td><a href="http://dnd5e.wikidot.com/cleric:unity-ua">Unity</a></td>
<td><a href="https://media.wizards.com/2020/dnd/downloads/UA2020_02_06_Subclasses2.pdf">Unearthed Arcana 68 - Subclasses, Part 2</a></td>
</tr>
</tbody></table>
<h5 id="toc11"><span>Domain Spells</span></h5>
<p>Each domain has a list of spells-its domain spells that you gain at the cleric levels noted in the domain description. Once you gain a domain spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day.</p>
<p>If you have a domain spell that doesn't appear on the cleric spell list, the spell is nonetheless a cleric spell for you.</p>
<h3 id="toc12"><span>Channel Divinity</span></h3>
<p>At 2nd level, you gain the ability to channel divine energy directly from your deity, using that energy to fuel magical effects. You start with two such effects: Turn Undead and an effect determined by your domain. Some domains grant you additional effects as you advance in levels, as noted in the domain description.</p>
<p>When you use your Channel Divinity, you choose which effect to create. You must then finish a short or long rest to use your Channel Divinity again.</p>
<p>Some Channel Divinity effects require saving throws. When you use such an effect from this class, the DC equals your cleric spell save DC.</p>
<p>Beginning at 6th level, you can use your Channel Divinity twice between rests, and beginning at 18th level, you can use it three times between rests. When you finish a short or long rest, you regain your expended uses.</p>
<h5 id="toc13"><span>Channel Divinity: Turn Undead</span></h5>
<p>As an action, you present your holy symbol and speak a prayer censuring the undead. Each undead that can see or hear you within 30 feet of you must make a Wisdom saving throw. If the creature fails its saving throw, it is turned for 1 minute or until it takes any damage.</p>
<p>A turned creature must spend its turns trying to move as far away from you as it can, and it can't willingly move to a space within 30 feet of you. It also can't take reactions. For its action, it can use only the Dash action or try to escape from an effect that prevents it from moving. If there's nowhere to move, the creature can use the Dodge action.</p>
<h3 id="toc14"><span>Harness Divine Power (Optional)</span></h3>
<p>At 2nd level, you can expend a use of your Channel Divinity to fuel your spells. As a bonus action, you touch your holy symbol, utter a prayer, and regain one expended spell slot, the level of which can be no higher than half your proficiency bonus (rounded up). The number of times you can use this feature is based on the level you've reached in this class: 2nd level, once; 6th level, twice; and 18th level, thrice. You regain all expended uses when you finish a long rest.</p>
<h3 id="toc15"><span>Ability Score Improvement</span></h3>
<p>When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.</p>
<h3 id="toc16"><span>Cantrip Versatility (Optional)</span></h3>
<p>Whenever you reach a level in this class that grants the Ability Score Improvement feature, you can replace one cantrip you learned from this class's Spellcasting feature with another cantrip from the <a href="http://dnd5e.wikidot.com/spells:cleric">cleric spell list</a>.</p>
<h3 id="toc17"><span>Destroy Undead</span></h3>
<p>Starting at 5th level, when an undead fails its saving throw against your Turn Undead feature, the creature is instantly destroyed if its challenge rating is at or below a certain threshold, as shown in the Cleric table above.</p>
<h3 id="toc18"><span>Blessed Strikes (Optional)</span></h3>
<p><em>Replaces the Divine Strike or Potent Spellcasting feature</em></p>
<p>When you reach 8th level, you are blessed with divine might in battle. When a creature takes damage from one of your cantrips or weapon attacks, you can also deal 1d8 radiant damage to that creature. Once you deal this damage, you can't use this feature again until the start of your next turn.</p>
<h3 id="toc19"><span>Divine Intervention</span></h3>
<p>Beginning at 10th level, you can call on your deity to intervene on your behalf when your need is great.</p>
<p>Imploring your deity's aid requires you to use your action. Describe the assistance you seek, and roll percentile dice. If you roll a number equal to or lower than your cleric level, your deity intervenes. The DM chooses the nature of the intervention; the effect of any cleric spell or cleric domain spell would be appropriate. If your deity intervenes, you can't use this feature again for 7 days. Otherwise, you can use it again after you finish a long rest.</p>
<p>At 20th level, your call for intervention succeeds automatically, no roll required.</p>
</div>
</div>
</div>"""

	def register(self):
		super().register()

	def update(self):
		super().update()
