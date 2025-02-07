# Fauna dictionaries
herpetofauna = {"Chameleon", "Tortoise", "Cobra", "Gecko", "Iguana", "Alligator", "Anaconda", "Newt", "Frog", "Axolotl"}
mammalia = {"Tiger", "Elephant", "Bison", "Lynx", "Giraffe", "Cheetah", "Wolf", "Horse", "Deer", "Badger"}
ichthyofauna = {"Dolphin", "Orca", "Seal", "Electric Eel", "Manta Ray", "Sea Turtle", "Shark", "Jellyfish", "Octopus", "Whale"}
avifauna = {"Eagle", "Albatross", "Crow", "Raven", "Heron", "Toucan", "Parrot", "Penguin", "Swan", "Falcon"}

# Fauna to element mapping
fauna_elements = {
    "Ichthyofauna": "Water",
    "Avifauna": "Air",
    "Mammalia": "Earth",
    "Herpetofauna": "Fire"
}

mythical_creatures_elements = {
    "Thunderbird": ["Air", "Water", "Fire", "Earth"],
    "Zephyr": ["Air", "Water", "Earth", "Fire"],
    "Griffin": ["Air", "Fire", "Earth", "Water"],
    "Phoenix": ["Air", "Fire", "Water", "Earth"],
    "Sphinx": ["Air", "Earth", "Water", "Fire"],
    "Pegasus": ["Air", "Earth", "Fire", "Water"],
    "Mermaid": ["Water", "Air", "Fire", "Earth"],
    "Naiad": ["Water", "Air", "Earth", "Fire"],
    "Siren": ["Water", "Fire", "Air", "Earth"],
    "Leviathan": ["Water", "Fire", "Earth", "Air"],
    "Kelpie": ["Water", "Earth", "Air", "Fire"],
    "Hydra": ["Water", "Earth", "Fire", "Air"],
    "Djinn": ["Fire", "Air", "Water", "Earth"],
    "Dragon": ["Fire", "Air", "Earth", "Water"],
    "Ifrit": ["Fire", "Water", "Air", "Earth"],
    "Chimera": ["Fire", "Water", "Earth", "Air"],
    "Fire Giant": ["Fire", "Earth", "Air", "Water"],
    "Hellhound": ["Fire", "Earth", "Water", "Air"],
    "Nymph": ["Earth", "Air", "Water", "Fire"],
    "Gargoyle": ["Earth", "Air", "Fire", "Water"],
    "Dryad": ["Earth", "Water", "Air", "Fire"],
    "Basilisk": ["Earth", "Water", "Fire", "Air"],
    "Minotaur": ["Earth", "Fire", "Water", "Air"],
    "Centaur": ["Earth", "Fire", "Air", "Water"]
}

mythical_creature_descriptions = {
    "Thunderbird": "A mighty creature of the skies, symbolizing power, freedom, and transformation.\n"
                   "The Thunderbird's presence commands respect and awe, embodying the strength of storms.\n"
                   "It represents a force of nature, unyielding and majestic.\n",

    "Zephyr": "The gentle spirit of the wind, embodying grace, speed, and adaptability.\n"
              "Zephyr moves swiftly and effortlessly, bringing change and renewal wherever it goes.\n"
              "It symbolizes the balance between subtlety and power.\n",

    "Griffin": "A noble creature with the strength of a lion and the agility of an eagle.\n"
               "Griffins guard treasures and secrets, embodying courage, guardianship, and wisdom.\n"
               "Their dual nature reflects harmony between strength and intellect.\n",

    "Phoenix": "The eternal symbol of rebirth, rising from its ashes to live anew.\n"
               "The Phoenix represents resilience, immortality, and the power of transformation.\n"
               "Its flames inspire hope and the ability to overcome any challenge.\n",

    "Sphinx": "A creature of mystery and wisdom, known for its riddles and profound knowledge.\n"
              "The Sphinx embodies intellect, curiosity, and the pursuit of truth.\n"
              "It guards ancient secrets, challenging seekers to prove their worth.\n",

    "Pegasus": "A winged horse that represents freedom, inspiration, and transcendence.\n"
               "Pegasus soars to great heights, embodying the power of imagination and dreams.\n"
               "It inspires those who seek to rise above the ordinary.\n",

    "Mermaid": "A mystical being of the sea, symbolizing beauty, mystery, and emotional depth.\n"
               "Mermaids are known for their alluring voices and connection to the ocean's wisdom.\n"
               "They represent the duality of human nature, balancing allure and danger.\n",

    "Naiad": "A freshwater nymph that embodies grace, serenity, and the life-giving essence of water.\n"
             "Naiads guard rivers and springs, symbolizing purity, renewal, and quiet strength.\n"
             "Their presence brings healing and harmony to their surroundings.\n",

    "Siren": "A captivating creature with a voice that lures sailors to their fate.\n"
             "The Siren symbolizes temptation, mystery, and the power of the unknown.\n"
             "It represents both the allure and peril of unchecked desires.\n",

    "Leviathan": "A massive sea creature that embodies chaos, strength, and the untamed power of the deep.\n"
                 "The Leviathan represents overwhelming force and the mysteries of the ocean.\n"
                 "It serves as a reminder of nature's awe-inspiring and uncontrollable might.\n",

    "Kelpie": "A shape-shifting water spirit known for its cunning and power.\n"
              "The Kelpie symbolizes transformation, mystery, and the dual nature of water as life-giving and destructive.\n"
              "It serves as a cautionary tale about the hidden dangers beneath beauty.\n",

    "Hydra": "A multi-headed serpent representing resilience and the challenges of persistence.\n"
             "For every head cut off, the Hydra grows two more, symbolizing adaptability and growth through adversity.\n"
             "It embodies the idea that challenges can strengthen and multiply one's resolve.\n",

    "Djinn": "A fiery spirit with immense power and the ability to grant wishes, often with a twist.\n"
             "The Djinn represents the dual nature of desire and the consequences of one's choices.\n"
             "It embodies cunning, freedom, and the untamed power of fire.\n",

    "Dragon": "A legendary beast symbolizing wisdom, strength, and boundless potential.\n"
              "Dragons guard great treasures and ancient secrets, representing both greed and enlightenment.\n"
              "They embody the balance between destruction and creation.\n",

    "Ifrit": "A powerful being of fire, known for its strength, independence, and unpredictable nature.\n"
             "The Ifrit symbolizes passion, transformation, and the fiery spirit of rebellion.\n"
             "It serves as a reminder of the power and danger of unbridled ambition.\n",

    "Chimera": "A fearsome creature with the parts of a lion, goat, and serpent, symbolizing complexity and unpredictability.\n"
               "The Chimera represents challenges that are multifaceted and require ingenuity to overcome.\n"
               "It embodies the power of diversity and the need to face fears head-on.\n",

    "Fire Giant": "A towering being of flame and strength, representing raw power and the force of nature.\n"
                  "The Fire Giant embodies endurance, resilience, and the fiery passion to achieve great feats.\n"
                  "It serves as a symbol of transformation through trials and challenges.\n",

    "Hellhound": "A spectral guardian of the underworld, representing loyalty, vigilance, and the boundaries between worlds.\n"
                 "The Hellhound symbolizes protection and the courage to face the unknown.\n"
                 "It serves as a reminder of the importance of loyalty and fearlessness.\n",

    "Nymph": "A spirit of nature, representing beauty, vitality, and harmony with the earth.\n"
             "Nymphs embody the gentle, nurturing aspects of nature and its ability to inspire.\n"
             "They symbolize the balance between humanity and the natural world.\n",

    "Gargoyle": "A stone guardian that wards off evil, representing protection, endurance, and strength.\n"
                "Gargoyles symbolize the blending of artistry and utility, standing watch over sacred spaces.\n"
                "They remind us of the importance of vigilance and resilience.\n",

    "Dryad": "A tree spirit embodying the life and wisdom of the forest.\n"
             "Dryads symbolize growth, patience, and the interconnectedness of all living things.\n"
             "They serve as guardians of nature, reminding us to live in harmony with the earth.\n",

    "Basilisk": "A deadly serpent whose gaze can turn creatures to stone, symbolizing fear and the power of perception.\n"
                "The Basilisk embodies the dual nature of beauty and danger.\n"
                "It serves as a reminder of the importance of facing fears with courage.\n",

    "Minotaur": "A powerful half-man, half-bull creature, representing strength, determination, and inner conflict.\n"
                "The Minotaur symbolizes the struggle between primal instincts and rational thought.\n"
                "It serves as a guide to overcoming inner challenges and finding balance.\n",

    "Centaur": "A being with the body of a horse and the torso of a man, symbolizing duality and the balance between intellect and instinct.\n"
               "Centaurs embody freedom, exploration, and the connection between humanity and nature.\n"
               "They inspire those who seek adventure and wisdom.\n"
}

animal_descriptions = {
    # Herpetofauna
    "Chameleon": "The Chameleon represents adaptability and keen observation.\n"
                 "It thrives by blending into its surroundings, embodying change and versatility.\n"
                 "Chameleons remind us of the importance of patience and strategic adjustment.\n",
    "Tortoise": "The Tortoise symbolizes endurance, wisdom, and stability.\n"
                "Its slow and steady pace reflects the value of persistence and long-term vision.\n"
                "Tortoises remind us that consistency leads to success.\n",
    "Cobra": "The Cobra represents power, protection, and mysticism.\n"
             "It is both revered and feared, embodying transformation and heightened awareness.\n"
             "Cobras remind us to respect and harness our inner strength.\n",
    "Gecko": "The Gecko symbolizes agility, resilience, and resourcefulness.\n"
             "Its ability to navigate tricky environments reflects adaptability and quick thinking.\n"
             "Geckos teach us to find solutions in unexpected ways.\n",
    "Iguana": "The Iguana embodies calmness, balance, and a connection to nature.\n"
              "It thrives in diverse environments, reminding us of the power of inner peace and harmony.\n"
              "Iguanas encourage patience and adaptability.\n",
    "Alligator": "The Alligator represents primal power, patience, and ancient wisdom.\n"
                 "It navigates between water and land, symbolizing adaptability and stealth.\n"
                 "Alligators teach us to strike with precision when the time is right.\n",
    "Anaconda": "The Anaconda symbolizes strength, mystery, and transformation.\n"
                "Its ability to constrict reflects the importance of focus and perseverance.\n"
                "Anacondas remind us to channel our power effectively.\n",
    "Newt": "The Newt represents regeneration, resilience, and change.\n"
            "Its ability to heal and adapt to its environment symbolizes hope and transformation.\n"
            "Newts teach us that growth comes from embracing change.\n",
    "Frog": "The Frog embodies renewal, transformation, and adaptability.\n"
            "Its life cycle reflects the power of growth and the courage to evolve.\n"
            "Frogs remind us to leap forward with confidence.\n",
    "Axolotl": "The Axolotl symbolizes regeneration, resilience, and youthfulness.\n"
               "Its ability to heal and adapt embodies hope and the potential for renewal.\n"
               "Axolotls teach us the value of staying curious and open to change.\n",

    # Mammalia
    "Tiger": "The Tiger represents courage, strength, and independence.\n"
             "Its fierce and majestic presence symbolizes raw power and focus.\n"
             "Tigers remind us to be bold and fearless in pursuit of our goals.\n",
    "Elephant": "The Elephant embodies wisdom, loyalty, and gentle strength.\n"
                "It represents deep emotional connections and the importance of family and community.\n"
                "Elephants remind us to move through life with purpose and empathy.\n",
    "Bison": "The Bison symbolizes endurance, abundance, and grounded strength.\n"
             "It thrives on the plains, representing resilience and the power of collective effort.\n"
             "Bison teach us to honor tradition and embrace steady progress.\n",
    "Lynx": "The Lynx represents intuition, secrecy, and mystery.\n"
            "Its keen senses and elusive nature embody insight and self-awareness.\n"
            "Lynxes teach us the value of observation and discretion.\n",
    "Giraffe": "The Giraffe symbolizes perspective, grace, and vision.\n"
               "Its ability to see far ahead represents foresight and awareness.\n"
               "Giraffes remind us to aim high while staying grounded.\n",
    "Cheetah": "The Cheetah embodies speed, focus, and precision.\n"
               "Its swift movements reflect the power of determination and clear goals.\n"
               "Cheetahs remind us to act swiftly and with purpose.\n",
    "Wolf": "The Wolf symbolizes loyalty, instinct, and teamwork.\n"
            "It thrives in packs, representing the balance between independence and collaboration.\n"
            "Wolves teach us to trust our instincts and value community.\n",
    "Horse": "The Horse represents freedom, strength, and endurance.\n"
             "Its unbridled spirit symbolizes adventure and personal growth.\n"
             "Horses remind us to pursue our passions with unwavering energy.\n",
    "Deer": "The Deer embodies gentleness, grace, and intuition.\n"
            "Its peaceful presence reflects sensitivity and a connection to nature.\n"
            "Deer teach us to approach life with kindness and compassion.\n",
    "Badger": "The Badger symbolizes determination, resourcefulness, and tenacity.\n"
              "Its fearless nature reflects courage and the power of persistence.\n"
              "Badgers remind us to stand firm and fight for what matters.\n",

    # Ichthyofauna
    "Dolphin": "The Dolphin represents intelligence, joy, and community.\n"
               "Its playful nature embodies harmony and connection with others.\n"
               "Dolphins remind us of the importance of communication and curiosity.\n",
    "Orca": "The Orca symbolizes strength, unity, and deep emotional bonds.\n"
            "It thrives in close-knit pods, reflecting loyalty and family ties.\n"
            "Orcas teach us the power of collaboration and mutual support.\n",
    "Seal": "The Seal embodies adaptability, playfulness, and emotional depth.\n"
            "Its dual life in water and on land symbolizes balance and flexibility.\n"
            "Seals remind us to embrace change with a light heart.\n",
    "Electric Eel": "The Electric Eel represents innovation, resilience, and hidden power.\n"
                    "Its ability to generate electricity symbolizes unique talents and creative problem-solving.\n"
                    "Electric Eels teach us to harness our inner energy effectively.\n",
    "Manta Ray": "The Manta Ray symbolizes grace, intuition, and the mysteries of the sea.\n"
                 "Its gentle movements reflect harmony and emotional balance.\n"
                 "Manta Rays remind us to trust our instincts and flow with life.\n",
    "Sea Turtle": "The Sea Turtle embodies patience, longevity, and a connection to the earth and sea.\n"
                  "It represents the balance between steady progress and adaptability.\n"
                  "Sea Turtles teach us to journey through life with persistence and calm.\n",
    "Shark": "The Shark represents focus, power, and determination.\n"
             "Its apex predator status reflects resilience and adaptability.\n"
             "Sharks remind us to move forward with confidence and precision.\n",
    "Jellyfish": "The Jellyfish symbolizes simplicity, flow, and resilience.\n"
                 "Its gentle movements reflect harmony with the natural world.\n"
                 "Jellyfish teach us the value of going with the flow while staying resilient.\n",
    "Octopus": "The Octopus embodies intelligence, adaptability, and creativity.\n"
               "Its ability to camouflage and solve problems symbolizes resourcefulness and flexibility.\n"
               "Octopuses teach us to think outside the box and embrace transformation.\n",
    "Whale": "The Whale symbolizes depth, wisdom, and a profound connection to the world.\n"
             "Its song and presence reflect communication and emotional intelligence.\n"
             "Whales remind us to explore the depths of our emotions and connections.\n",

    # Avifauna
    "Eagle": "The Eagle represents vision, strength, and independence.\n"
             "Its ability to soar high reflects ambition and clear perspective.\n"
             "Eagles teach us to rise above challenges and see the bigger picture.\n",
    "Albatross": "The Albatross symbolizes endurance, freedom, and a deep connection to the sea.\n"
                 "Its long journeys reflect resilience and exploration.\n"
                 "Albatrosses remind us to embrace life's vast opportunities.\n",
    "Crow": "The Crow represents intelligence, transformation, and mystery.\n"
            "Its adaptability reflects resourcefulness and insight.\n"
            "Crows teach us to see beyond the surface and embrace change.\n",
    "Raven": "The Raven embodies wisdom, prophecy, and adaptability.\n"
             "Its mysterious nature symbolizes transformation and guidance.\n"
             "Ravens remind us to embrace life's mysteries and seek knowledge.\n",
    "Heron": "The Heron symbolizes patience, elegance, and self-reflection.\n"
             "Its stillness reflects the value of introspection and balance.\n"
             "Herons teach us to move through life with grace and mindfulness.\n",
    "Toucan": "The Toucan represents expression, vibrancy, and individuality.\n"
              "Its colorful presence symbolizes joy and creativity.\n"
              "Toucans remind us to embrace our unique qualities and stand out.\n",
    "Parrot": "The Parrot embodies communication, intelligence, and playfulness.\n"
              "Its mimicry reflects the power of connection and learning.\n"
              "Parrots teach us to express ourselves and share our voice.\n",
    "Penguin": "The Penguin symbolizes unity, resilience, and adaptability.\n"
               "Its life in harsh climates reflects teamwork and determination.\n"
               "Penguins remind us of the strength found in community.\n",
    "Swan": "The Swan represents beauty, grace, and transformation.\n"
            "Its serene presence reflects inner peace and spiritual growth.\n"
            "Swans teach us the value of finding harmony within ourselves.\n",
    "Falcon": "The Falcon symbolizes speed, precision, and vision.\n"
              "Its focused hunting style reflects determination and clarity.\n"
              "Falcons remind us to act swiftly and with purpose.\n"
}

# Personality metrics dictionaries
social_orientation = {"Social", "Harmonious", "Assertive", "Reserved"}
emotional_cognitive_flexibility = {"Curious", "Stable", "Introspective", "Optimistic"}
self_expression_purpose = {"Innovative", "Pragmatic", "Compassionate", "Expressive"}
values_integrity = {"Ethical", "Flexible", "Realistic", "Contemplative"}
resilience_adaptation = {"Composed", "Resourceful", "Progressive", "Supportive"}

# Archetypes with their specific traits
archetypes = {
    "The Vanguard": {
    "traits": ["Assertive", "Curious", "Innovative", "Realistic", "Progressive"],
    "fauna": ["Anaconda", "Tiger"],
    "description": "Vanguards are bold leaders who embrace curiosity and innovation to drive meaningful change.\n"
    "They approach challenges with realism and a progressive mindset, always pushing boundaries.\n"
    "Their assertiveness and strategic thinking make them natural pioneers in any endeavor.\n"
    },
    "The Mediator": {
        "traits": ["Social", "Introspective", "Compassionate", "Contemplative", "Supportive"],
        "fauna": ["Seal", "Frog"],
        "description": "Mediators are compassionate individuals who excel at fostering understanding and harmony.\n"
        "Their introspective nature allows them to navigate complex emotions with care and thoughtfulness.\n"
        "Supportive and contemplative, they build bridges between people, promoting lasting connections.\n"
    },
    "The Strategist": {
        "traits": ["Harmonious", "Stable", "Innovative", "Contemplative", "Supportive"],
        "fauna": ["Lynx", "Raven"],
        "description": "Strategists are thoughtful planners who combine stability with innovative thinking.\n"
        "They approach problems with a harmonious mindset, ensuring well-rounded and supportive solutions.\n"
        "Their contemplative nature helps them see the bigger picture while maintaining attention to detail.\n"
    },
    "The Advocate": {
        "traits": ["Reserved", "Curious", "Compassionate", "Ethical", "Progressive"],
        "fauna": ["Badger", "Dolphin"],
        "description": "Advocates are driven by a strong ethical compass and a desire to bring about positive change.\n"
        "They balance their reserved nature with compassionate action, standing up for what they believe in.\n"
        "Their progressive mindset and curiosity fuel their passion for justice and equality.\n"
    },
    "The Achiever": {
        "traits": ["Assertive", "Optimistic", "Innovative", "Flexible", "Supportive"],
        "fauna": ["Cobra", "Falcon"],
        "description": "Achievers are dynamic and optimistic individuals who thrive on reaching new heights.\n"
        "Their innovative spirit and flexibility allow them to adapt to any challenge with confidence.\n"
        "Supportive of others, they inspire those around them with their assertiveness and determination.\n"
    },
    "The Diplomat": {
    "traits": ["Social", "Curious", "Pragmatic", "Realistic", "Supportive"],
    "fauna": ["Elephant", "Penguin"],
    "description": "Diplomats are natural connectors who balance curiosity with pragmatic problem-solving.\n"
    "Their realistic approach helps them navigate complex social dynamics with ease.\n"
    "Supportive and adaptable, they build strong relationships rooted in mutual respect.\n"
    },
    "The Analyst": {
        "traits": ["Harmonious", "Curious", "Pragmatic", "Contemplative", "Resourceful"],
        "fauna": ["Gecko", "Giraffe"],
        "description": "Analysts are insightful thinkers who approach problems with curiosity and pragmatism.\n"
        "They value harmony and contemplation.\nThis allows them to uncover hidden solutions.\n"
        "Resourceful and thoughtful, they excel at analyzing complex situations with clarity.\n"
    },
    "The Performer": {
        "traits": ["Assertive", "Stable", "Expressive", "Realistic", "Composed"],
        "fauna": ["Toucan", "Chameleon"],
        "description": "Performers are confident and expressive individuals who captivate those around them.\n"
        "Their stable and realistic nature grounds their creative energy.\nThis makes them reliable leaders.\n"
        "With a composed demeanor, they inspire others through both action and presence.\n"
    },
    "The Free Spirit": {
        "traits": ["Social", "Curious", "Expressive", "Flexible", "Progressive"],
        "fauna": ["Horse", "Parrot"],
        "description": "Free Spirits are adventurous souls who thrive on social connection and self-expression.\n"
        "Their curiosity and flexibility allow them to adapt to new experiences with ease.\n"
        "Progressive and open-minded, they inspire others to embrace authenticity and growth.\n"
    },
    "The Visionary": {
        "traits": ["Reserved", "Optimistic", "Innovative", "Realistic", "Resourceful"],
        "fauna": ["Cheetah", "Newt"],
        "description": "Visionaries are forward-thinking individuals who blend optimism with innovation.\n"
        "Their realistic mindset ensures practical solutions to complex challenges.\n"
        "Resourceful and driven, they inspire others to imagine and build a better future.\n"
    },
    "The Builder": {
    "traits": ["Social", "Stable", "Pragmatic", "Flexible", "Resourceful"],
    "fauna": ["Bison", "Orca"],
    "description": "Builders are dependable individuals who create lasting foundations through practical solutions.\n"
    "They combine stability with flexibility, adapting to challenges with ease.\n"
    "Resourceful and social, they excel in collaborative environments where steady progress is key.\n"
    },
    "The Dreamer": {
        "traits": ["Harmonious", "Optimistic", "Expressive", "Ethical", "Supportive"],
        "fauna": ["Jellyfish", "Iguana"],
        "description": "Dreamers are imaginative souls who see the world through a lens of optimism and creativity.\n"
        "Their expressive nature and strong ethical values inspire those around them.\n"
        "Supportive and harmonious, they encourage others to pursue their dreams with confidence.\n"
    },
    "The Guardian": {
        "traits": ["Assertive", "Stable", "Compassionate", "Flexible", "Progressive"],
        "fauna": ["Wolf", "Whale"],
        "description": "Guardians are strong protectors who balance assertiveness with compassion.\n"
        "Their stable and flexible nature allows them to support others through change.\n"
        "Progressive and caring, they lead by example, fostering growth and security.\n"
    },
    "The Sage": {
        "traits": ["Harmonious", "Introspective", "Compassionate", "Contemplative", "Composed"],
        "fauna": ["Tortoise", "Heron"],
        "description": "Sages are wise and introspective individuals who bring harmony and understanding to their environment.\n"
        "They approach life with compassion and a contemplative mindset.\n"
        "Composed and thoughtful, they guide others through reflection and calm presence.\n"
    },
    "The Creator": {
        "traits": ["Reserved", "Introspective", "Innovative", "Ethical", "Composed"],
        "fauna": ["Axolotl", "Manta Ray"],
        "description": "Creators are inventive thinkers who merge introspection with innovation.\n"
        "Their ethical values guide their creative pursuits, ensuring meaningful impact.\n"
        "Composed and reserved, they bring thoughtful solutions to life through careful design.\n"
    },
    "The Philosopher": {
    "traits": ["Reserved", "Optimistic", "Expressive", "Contemplative", "Resourceful"],
    "fauna": ["Crow", "Octopus"],
    "description": "Philosophers are deep thinkers who blend optimism with thoughtful reflection.\n"
    "Their expressive nature allows them to share profound insights with the world.\n"
    "Resourceful and reserved, they seek meaning and clarity in all aspects of life.\n"
    },
    "The Explorer": {
        "traits": ["Social", "Introspective", "Expressive", "Flexible", "Composed"],
        "fauna": ["Albatross", "Sea Turtle"],
        "description": "Explorers are adventurous souls who thrive on discovering new experiences and perspectives.\n"
        "Their introspective and expressive nature helps them connect deeply with others and themselves.\n"
        "Flexible and composed, they navigate life’s journeys with confidence and grace.\n"
    },
    "The Investigator": {
        "traits": ["Reserved", "Stable", "Compassionate", "Realistic", "Composed"],
        "fauna": ["Electric Eel", "Alligator"],
        "description": "Investigators are meticulous and compassionate individuals who seek to uncover hidden truths.\n"
        "Their stable and realistic mindset grounds their explorations in practical outcomes.\n"
        "Reserved yet composed, they approach every challenge with thoughtful precision.\n"
    },
    "The Nurturer": {
        "traits": ["Assertive", "Introspective", "Pragmatic", "Ethical", "Resourceful"],
        "fauna": ["Swan", "Deer"],
        "description": "Nurturers are caring and assertive individuals who balance introspection with practical support.\n"
        "Their strong ethical foundation guides their compassionate actions.\n"
        "Resourceful and pragmatic, they help others grow and thrive in meaningful ways.\n"
    },
    "The Pioneer": {
        "traits": ["Harmonious", "Optimistic", "Pragmatic", "Ethical", "Progressive"],
        "fauna": ["Shark", "Eagle"],
        "description": "Pioneers are trailblazers driven by harmony and optimism as they forge new paths.\n"
        "Their pragmatic and ethical approach ensures lasting, positive impact.\n"
        "Progressive and fearless, they inspire others to embrace change and innovation.\n"
    }
}

# Animal traits assignment
animal_traits = {
    #Mammalifauna
    "Tiger": {"primary_trait": "Innovative", "secondary_trait": "Progressive"},
    "Cheetah": {"primary_trait": "Innovative", "secondary_trait": "Resourceful"},
    "Horse": {"primary_trait": "Progressive", "secondary_trait": "Expressive"},
    "Lynx": {"primary_trait": "Innovative", "secondary_trait": "Contemplative"},
    "Giraffe": {"primary_trait": "Resourceful", "secondary_trait": "Contemplative"},
    "Badger": {"primary_trait": "Ethical", "secondary_trait": "Compassionate"},
    "Wolf": {"primary_trait": "Flexible", "secondary_trait": "Stable"},
    "Deer": {"primary_trait": "Resourceful", "secondary_trait": "Ethical"},
    "Elephant": {"primary_trait": "Supportive", "secondary_trait": "Realistic"},
    "Bison": {"primary_trait": "Resourceful", "secondary_trait": "Social"},

    #Avifauna
    "Falcon": {"primary_trait": "Assertive", "secondary_trait": "Supportive"},
    "Raven": {"primary_trait": "Stable", "secondary_trait": "Supportive"},
    "Penguin": {"primary_trait": "Social", "secondary_trait": "Pragmatic"},
    "Eagle": {"primary_trait": "Pragmatic", "secondary_trait": "Progressive"},
    "Heron": {"primary_trait": "Compassionate", "secondary_trait": "Harmonious"},
    "Toucan": {"primary_trait": "Composed", "secondary_trait": "Stable"},
    "Swan": {"primary_trait": "Assertive", "secondary_trait": "Pragmatic"},
    "Crow": {"primary_trait": "Optimistic", "secondary_trait": "Contemplative"},
    "Parrot": {"primary_trait": "Flexible", "secondary_trait": "Curious"},
    "Albatross": {"primary_trait": "Introspective", "secondary_trait": "Composed"},

    #Ichtyofauna
    "Dolphin": {"primary_trait": "Reserved", "secondary_trait": "Curious"},
    "Orca": {"primary_trait": "Stable", "secondary_trait": "Pragmatic"},
    "Jellyfish": {"primary_trait": "Harmonious", "secondary_trait": "Supportive"},
    "Manta Ray": {"primary_trait": "Reserved", "secondary_trait": "Composed"},
    "Whale": {"primary_trait": "Compassionate", "secondary_trait": "Assertive"},
    "Seal": {"primary_trait": "Compassionate", "secondary_trait": "Introspective"},
    "Octopus": {"primary_trait": "Reserved", "secondary_trait": "Expressive"},
    "Shark": {"primary_trait": "Optimistic", "secondary_trait": "Ethical"},
    "Sea Turtle": {"primary_trait": "Expressive", "secondary_trait": "Social"},
    "Electric Eel": {"primary_trait": "Composed", "secondary_trait": "Realistic"},

    #Herpetofauna
    "Frog": {"primary_trait": "Supportive", "secondary_trait": "Contemplative"},
    "Axolotl": {"primary_trait": "Innovative", "secondary_trait": "Ethical"},
    "Newt": {"primary_trait": "Realistic", "secondary_trait": "Reserved"},
    "Tortoise": {"primary_trait": "Contemplative", "secondary_trait": "Composed"},
    "Chameleon": {"primary_trait": "Assertive", "secondary_trait": "Realistic"},
    "Alligator": {"primary_trait": "Compassionate", "secondary_trait": "Reserved"},
    "Anaconda": {"primary_trait": "Curious", "secondary_trait": "Assertive"},
    "Cobra": {"primary_trait": "Flexible", "secondary_trait": "Innovative"},
    "Gecko": {"primary_trait": "Harmonious", "secondary_trait": "Pragmatic"},
    "Iguana": {"primary_trait": "Ethical", "secondary_trait": "Expressive"},
}

# Dictionary for questions related to "Social Orientation"
social_orientation_questions = [
    {
        "question": "What role do you take at parties?",
        "answers": [
            "I enjoy meeting new people.",  # Social
            "I ensure everyone feels comfortable.",  # Harmonious
            "I try to make something happen.",  # Assertive
            "I prefer to observe."  # Reserved
        ],
        "traits": ["Social", "Harmonious", "Assertive", "Reserved"],
        "elements": ["Air", "Water", "Fire", "Earth"]  # Corresponding elemental scores
    },
    {
        "question": "What role do you best play in group projects?",
        "answers": [
            "The connector. I like to facilitate communication between team members.",  # Social
            "The teammate. I like to find where I can be most useful.",  # Harmonious
            "The leader. I like to direct the action.",  # Assertive
            "The independent worker. I like to work alone and offer my expertise when needed."  # Reserved
        ],
        "traits": ["Social", "Harmonious", "Assertive", "Reserved"],
        "elements": ["Air", "Water", "Fire", "Earth"]  # Corresponding elemental scores
    },
    {
        "question": "How do you converse with strangers?",
        "answers": [
            "Openly and joyous.",  # Social
            "I follow their lead.",  # Harmonious
            "I take the lead.",  # Assertive
            "I don't."  # Reserved
        ],
        "traits": ["Social", "Harmonious", "Assertive", "Reserved"],
        "elements": ["Air", "Water", "Fire", "Earth"]  # Corresponding elemental scores
    },
    {
        "question": "What role do you most often take in your friend groups?",
        "answers": [
            "I’m the connector who brings more people together.",  # Social
            "I’m the peacekeeper, ensuring everyone gets along.",  # Harmonious
            "I'm the planner, I make sure we follow through with plans.",  # Assertive
            "I’m the quiet supporter, always there when needed."  # Reserved
        ],
        "traits": ["Social", "Harmonious", "Assertive", "Reserved"],
        "elements": ["Air", "Water", "Fire", "Earth"]  # Corresponding elemental scores
    },
    {
        "question": "How do you approach tough conversations?",
        "answers": [
            "I openly communicate and encourage dialogue to find solutions.",  # Social
            "I prioritize maintaining balance and avoid exacerbating the situation.",  # Harmonious
            "I start them.",  # Assertive
            "I carefully consider my words and only speak when necessary."  # Reserved
        ],
        "traits": ["Social", "Harmonious", "Assertive", "Reserved"],
        "elements": ["Air", "Water", "Fire", "Earth"]  # Corresponding elemental scores
    },
    {
        "question": "How do you approach minor disagreements with your loved ones?",
        "answers": [
            "I listen openly and carefully consider their position.",  # Social
            "I try to compromise as fairly as possible.",  # Harmonious
            "I state my position.",  # Assertive
            "I analyze the facts."  # Reserved
        ],
        "traits": ["Social", "Harmonious", "Assertive", "Reserved"],
        "elements": ["Air", "Water", "Fire", "Earth"]  # Corresponding elemental scores
    },
    {
        "question": "How do you communicate in romantic relationships?",
        "answers": [
            "I communicate with an open mind.",  # Social
            "I focus on creating mutual understanding.",  # Harmonious
            "I’m very expressive.",  # Assertive
            "I prefer to listen and share my thoughts when necessary."  # Reserved
        ],
        "traits": ["Social", "Harmonious", "Assertive", "Reserved"],
        "elements": ["Air", "Water", "Fire", "Earth"]  # Corresponding elemental scores
    },
    {
        "question": "When moving to a new area, how do you make friends?",
        "answers": [
            "I attend events and actively seek out connections.",  # Social
            "I connect to those closest to me.",  # Harmonious
            "I try to make a splash.",  # Assertive
            "I let relationships form naturally over time."  # Reserved
        ],
        "traits": ["Social", "Harmonious", "Assertive", "Reserved"],
        "elements": ["Air", "Water", "Fire", "Earth"]  # Corresponding elemental scores
    },
    {
        "question": "How do you respond to a person who talks too much?",
        "answers": [
            "I redirect the conversation to engage others in the group.",  # Social
            "I patiently listen and encourage them to feel heard.",  # Harmonious
            "I try to steer the discussion.",  # Assertive
            "I quietly endure it but avoid engaging further."  # Reserved
        ],
        "traits": ["Social", "Harmonious", "Assertive", "Reserved"],
        "elements": ["Air", "Water", "Fire", "Earth"]  # Corresponding elemental scores
    },
    {
        "question": "How do you ask someone if they have a problem with you?",
        "answers": [
            "I ask others if they think someone has a problem with me.",  # Social
            "I gently ask in a way that minimizes tension.",  # Harmonious
            "I directly inquire about the issue.",  # Assertive
            "I don't."  # Reserved
        ],
        "traits": ["Social", "Harmonious", "Assertive", "Reserved"],
        "elements": ["Air", "Water", "Fire", "Earth"]  # Corresponding elemental scores
    },
    {
        "question": "How do you show friendship?",
        "answers": [
            "I plan activities.",  # Social
            "I offer emotional support.",  # Harmonious
            "I express all of my appreciation for them.",  # Assertive
            "Through quality time."  # Reserved
        ],
        "traits": ["Social", "Harmonious", "Assertive", "Reserved"],
        "elements": ["Air", "Water", "Fire", "Earth"]  # Corresponding elemental scores
    },
    {
        "question": "How long can you isolate?",
        "answers": [
            "I can't do it at all.",  # Social
            "I can manage for a while if I feel emotionally connected to others.",  # Harmonious
            "I’m fine with short periods but prefer staying active and productive.",  # Assertive
            "I’m comfortable with extended solitude and enjoy the time alone."  # Reserved
        ],
        "traits": ["Social", "Harmonious", "Assertive", "Reserved"],
        "elements": ["Air", "Water", "Fire", "Earth"]  # Corresponding elemental scores
    }
]

# Dictionary for questions related to "Emotional and Cognitive Flexibility"
emotional_cognitive_flexibility_questions = [ #these are graded on a spectrum of emotional - cognitive with respect to optimistic, introspective, curious, stable
    {
        "question": "What do you do when you disagree with someone that you have to coexist with?",
        "answers": [
            "I would try to understand their position.",  # Curious
            "I would try to keep my composure and minimize interaction.",  # Stable
            "I would try to consider my positon more deeply.",  # Introspective
            "I would hope for them to change.",  # Optimistic
        ],
        "traits": ["Curious", "Stable", "Introspective", "Optimistic"],
        "elements": ["Air", "Earth", "Water", "Fire"]  # Corresponding elemental scores
    },
    {
        "question": "What are your thoughts on uncertainty?",
        "answers": [
            "I find it to be a thrilling opportunity for learning something new.",  # Curious
            "Uncertainty is a state of being that can be unraveled with careful observation.",  # Stable
            "I see it as an opportunity for growth.",  # Introspective
            "I anticipate a positive resolution.",  # Optimistic
        ],
        "traits": ["Curious", "Stable", "Introspective", "Optimistic"],
        "elements": ["Air", "Earth", "Water", "Fire"]  # Corresponding elemental scores
    },
    {
        "question": "How would you say you compartmentalize trauma?",
        "answers": [
            "I find new things to spend my time focusing on until it's minimized and can be safely healed.",  # Curious
            "I slowly and steadily process it piece-by-piece.",  # Stable
            "I reflect on how it's affected me and backtrack the path its led me on to re-situate myself from where I left off.",  # Introspective
            "I sooth the storm in my heart with affirmations and love.",  # Optimistic
        ],
        "traits": ["Curious", "Stable", "Introspective", "Optimistic"],
        "elements": ["Air", "Earth", "Water", "Fire"]  # Corresponding elemental scores
    },
    {
        "question": "What theme best fits your approach to life?",
        "answers": [
            "Exploration and continuous learning.",  # Curious
            "If it ain't broke don't fix it.",  # Stable
            "Deep self-reflection and understanding.",  # Introspective
            "I hope for the best outcomes.",  # Optimistic
        ],
        "traits": ["Curious", "Stable", "Introspective", "Optimistic"],
        "elements": ["Air", "Earth", "Water", "Fire"]  # Corresponding elemental scores
    },
    {
        "question": "What do you think of musicals?",
        "answers": [
            "They're not typically what I'm drawn to, but I like some and think there's lots of potential for them.",  # Curious
            "I never really cared for them.",  # Stable
            "They speak deeply to me.",  # Introspective
            "I LOVE THEM SO MUCH. The meaning, the exilharating passion, all of it consumes me.",  # Optimistic
        ],
        "traits": ["Curious", "Stable", "Introspective", "Optimistic"],
        "elements": ["Air", "Earth", "Water", "Fire"]  # Corresponding elemental scores
    },
    {
        "question": "What's your take on moving forward?",
        "answers": [
            "I go where the wind takes me",  # Curious
            "I follow the map.",  # Stable
            "I follow my whims",  # Introspective
            "I go with my gut.",  # Optimistic
        ],
        "traits": ["Curious", "Stable", "Introspective", "Optimistic"],
        "elements": ["Air", "Earth", "Water", "Fire"]  # Corresponding elemental scores
    },
    {
        "question": "How do you work on yourself?",
        "answers": [
            "I tighten screws as they come loose",  # Curious
            "I maintain a strict daily routine.",  # Stable
            "I show myself patience.",  # Introspective
            "I do what feels right.",  # Optimistic
        ],
        "traits": ["Curious", "Stable", "Introspective", "Optimistic"],
        "elements": ["Air", "Earth", "Water", "Fire"]  # Corresponding elemental scores
    },
    {
        "question": "What draws you to art museums?",
        "answers": [
            "I love to see all the different styles and forms of expression.",  # Curious
            "Nothing.",  # Stable
            "I always get something novel out of every experience.",  # Introspective
            "I want to read the stories behind the art, the meaning.",  # Optimistic
        ],
        "traits": ["Curious", "Stable", "Introspective", "Optimistic"],
        "elements": ["Air", "Earth", "Water", "Fire"]  # Corresponding elemental scores
    },
    {
        "question": "Cognitively, how do you think you're most effective in a leadership role?",
        "answers": [
            "I request input from the rest of the team.",  # Curious
            "I provide steady guidance and ensure clear organization.",  # Stable
            "I encourage creativity and openness to new ideas.",  # Introspective
            "I motivate others to achieve their best.",  # Optimistic
        ],
        "traits": ["Curious", "Stable", "Introspective", "Optimistic"],
        "elements": ["Air", "Earth", "Water", "Fire"]  # Corresponding elemental scores
    },
    {
        "question": "What do you do when a loved one accuses you of wrongdoing?",
        "answers": [
            "I deeply consider if I did something wrong.",  # Curious
            "I try to convince them it's a misunderstanding.",  # Stable
            "I apologize.",  # Introspective
            "I make an accusation myself.",  # Optimistic
        ],
        "traits": ["Curious", "Stable", "Introspective", "Optimistic"],
        "elements": ["Air", "Earth", "Water", "Fire"]  # Corresponding elemental scores
    },
    {
        "question": "What is your reason of being?",
        "answers": [
            "To see the world and its people.",  # Curious
            "To stay grounded through hardship and succeed.",  # Stable
            "To know true peace.",  # Introspective
            "To be self-actualized.",  # Optimistic
        ],
        "traits": ["Curious", "Stable", "Introspective", "Optimistic"],
        "elements": ["Air", "Earth", "Water", "Fire"]  # Corresponding elemental scores
    },
    {
        "question": "How do you respond to complex problems?",
        "answers": [
            "I explore alternative solutions or methods to approach it.",  # Curious
            "I break the problem into smaller, manageable tasks.",  # Stable
            "I consider how I work best in different situations to take the approach that I know will be best for me.",  # Introspective
            "I remind myself of past successes and trust I’ll get through it.",  # Optimistic
        ],
        "traits": ["Curious", "Stable", "Introspective", "Optimistic"],
        "elements": ["Air", "Earth", "Water", "Fire"]  # Corresponding elemental scores
    }
]

# Dictionary for questions related to "Self-Expression and Purpose"
self_expression_purpose_questions = [
    {
        "question": "What type of art do/would you make?",
        "answers": [
            "My art makes a statement and challenges the status quo.",  # Innovative
            "My art reflects reality in its rawest form.",  # Pragmatic
            "My art embodies the human condition.",  # Compassionate
            "My art bears my heart to the world and leaves nothing to speculation.",  # Expressive
        ],
        "traits": ["Innovative", "Pragmatic", "Compassionate", "Expressive"],
        "elements": ["Air", "Earth", "Water", "Fire"]  # Corresponding elemental scores
    },
    {
        "question": "What's your reason for getting out of bed in the morning?",
        "answers": [
            "I'm ready to pursue my projects and learn.",  # Innovative
            "Well I can't stay in bed, I have things to do.",  # Pragmatic
            "I'm ready to get out to the world and connect with my community.",  # Compassionate
            "I'm excited to take the day head-on and achieve my daily tasks.",  # Expressive
        ],
        "traits": ["Innovative", "Pragmatic", "Compassionate", "Expressive"],
        "elements": ["Air", "Earth", "Water", "Fire"]  # Corresponding elemental scores
    },
    {
        "question": "How do you communicate in the heat of an argument?",
        "answers": [
            "I come up with creative analogies to get my point across.",  # Innovative
            "I stick to the facts and tackle the matter at hand.",  # Pragmatic
            "I navigate their feelings, prioritizing their stability because I know I'm grounded enough to handle it",  # Compassionate
            "I display all my thoughts and emotions, holding nothing back so they know my exact position.",  # Expressive
        ],
        "traits": ["Innovative", "Pragmatic", "Compassionate", "Expressive"],
        "elements": ["Air", "Earth", "Water", "Fire"]  # Corresponding elemental scores
    },
    {
        "question": "How do you show passion for the person you love most?",
        "answers": [
            "I come up with creative dates and games to keep them thrilled and curious.",  # Innovative
            "I tend to their needs and ensure their baseline is provided for.",  # Pragmatic
            "I pay close attention to them as a person and acknowledge their specific desires.",  # Compassionate
            "I make grand displays of affection to really wow them!",  # Expressive
        ],
        "traits": ["Innovative", "Pragmatic", "Compassionate", "Expressive"],
        "elements": ["Air", "Earth", "Water", "Fire"]  # Corresponding elemental scores
    },
    {
        "question": "What's an exciting date in your eyes?",
        "answers": [
            "Something creative like an escape room.",  # Innovative
            "9/11",  # Pragmatic
            "A heartfelt picnic, followed by a walk and finally a romantic evening indoors watching movies.",  # Compassionate
            "I want to do something thrilling, like skydiving, parasailing, or exploring nature.",  # Expressive
        ],
        "traits": ["Innovative", "Pragmatic", "Compassionate", "Expressive"],
        "elements": ["Air", "Earth", "Water", "Fire"]  # Corresponding elemental scores
    },
    {
        "question": "How do you react to being betrayed?",
        "answers": [
            "I restructure the part of my life that they occupied after removing them.",  # Innovative
            "I simply lose trust for them. There's no purpose they serve in my life anymore.",  # Pragmatic
            "I forgive them and allow for redemption.",  # Compassionate
            "I show my hurt and disappointment to process it, leaning on my better friends for support.",  # Expressive
        ],
        "traits": ["Innovative", "Pragmatic", "Compassionate", "Expressive"],
        "elements": ["Air", "Earth", "Water", "Fire"]  # Corresponding elemental scores
    },
    {
        "question": "What purpose do you make for yourself in this life?",
        "answers": [
            "I want to create new things and change the world.",  # Innovative
            "I want to adapt to the world and create a stable life.",  # Pragmatic
            "I want to help uplift and heal others so that the world is a better place for everyone.",  # Compassionate
            "I want to experience life to the fullest and get the most that the world has to offer.",  # Expressive
        ],
        "traits": ["Innovative", "Pragmatic", "Compassionate", "Expressive"],
        "elements": ["Air", "Earth", "Water", "Fire"]  # Corresponding elemental scores
    },
    {
        "question": "What kind of person are you in your friend group?",
        "answers": [
            "I make plans and organize social gatherings.",  # Innovative
            "I make sure the details of our plans are accounted for so that we have need for nothing.",  # Pragmatic
            "I focus on everyone's feelings so that no one feels alone.",  # Compassionate
            "I emphasize the joy of friendship and togetherness when we're all having a good time.",  # Expressive
        ],
        "traits": ["Innovative", "Pragmatic", "Compassionate", "Expressive"],
        "elements": ["Air", "Earth", "Water", "Fire"]  # Corresponding elemental scores
    },
    {
        "question": "How would you describe your heart?",
        "answers": [
            "It thrives off of curiosity and the pursuit of knowledge.",  # Innovative
            "It is a vessel containing four chambers that pumps blood throughout the body.",  # Pragmatic
            "It is a giving fountain of love and affection.",  # Compassionate
            "It is a passionate source of connection to the world around me.",  # Expressive
        ],
        "traits": ["Innovative", "Pragmatic", "Compassionate", "Expressive"],
        "elements": ["Air", "Earth", "Water", "Fire"]  # Corresponding elemental scores
    },
    {
        "question": "How would you describe your mind?",
        "answers": [
            "It is a chamber of imagination and experimentation used for demystifying (or mystifying) the world.",  # Innovative
            "It is one of the most complex biological structures in all of known existence.",  # Pragmatic
            "It is good for making decisions but it cannot lead the heart.",  # Compassionate
            "I'm glad to have it but I find it gets in the way sometimes.",  # Expressive
        ],
        "traits": ["Innovative", "Pragmatic", "Compassionate", "Expressive"],
        "elements": ["Air", "Earth", "Water", "Fire"]  # Corresponding elemental scores
    },
    {
        "question": "How would you describe your spirit?",
        "answers": [
            "I have a spirit of creation and wonder.",  # Innovative
            "I don't know about all of that.",  # Pragmatic
            "The spirit is the root of the universe that connects all things.",  # Compassionate
            "My spirit comes bursting from within to heal myself and others in this tragic world.",  # Expressive
        ],
        "traits": ["Innovative", "Pragmatic", "Compassionate", "Expressive"],
        "elements": ["Air", "Earth", "Water", "Fire"]  # Corresponding elemental scores
    },
    {
        "question": "How do you spend your free time?",
        "answers": [
            "I create something new to hone my skills on whatever I'm trying to master.",  # Innovative
            "I set up the systems in my life to make me well-prepped for the long-term.",  # Pragmatic
            "I try to help the people around me by supporting my community.",  # Compassionate
            "I make vibrant works of art that reflect my internal state of being.",  # Expressive
        ],
        "traits": ["Innovative", "Pragmatic", "Compassionate", "Expressive"],
        "elements": ["Air", "Earth", "Water", "Fire"]  # Corresponding elemental scores
    }
]

# Dictionary for questions related to "Values and Integrity"
values_integrity_questions = [
    {
        "question": "What matters most in friendship?",
        "answers": [
            "Being honest and dependable.",  # Ethical
            "Allowing free space for us to be ourselves, different and similar.",  # Flexible
            "Likability between persons.",  # Realistic
            "It really depends. Friendship is so vast and varied.",  # Contemplative
        ],
        "traits": ["Ethical", "Flexible", "Realistic", "Contemplative"],
        "elements": ["Air", "Water", "Earth", "Fire"]  # Corresponding elemental scores
    },
    {
        "question": "What matters most with a life partner?",
        "answers": [
            "Always respecting each other's boundaries.",  # Ethical
            "The ability to adapt and grow together.",  # Flexible
            "Reliability and consistent support through challenges.",  # Realistic
            "A deep emotional and intellectual connection.",  # Contemplative
        ],
        "traits": ["Ethical", "Flexible", "Realistic", "Contemplative"],
        "elements": ["Air", "Water", "Earth", "Fire"]  # Corresponding elemental scores
    },
    {
        "question": "What matters most in the workplace?",
        "answers": [
            "Upholding fairness and integrity in all interactions.",  # Ethical
            "The ability to adapt to changing circumstances.",  # Flexible
            "Practical results and meeting objectives.",  # Realistic
            "Aligning work with personal values.",  # Contemplative
        ],
        "traits": ["Ethical", "Flexible", "Realistic", "Contemplative"],
        "elements": ["Air", "Water", "Earth", "Fire"]  # Corresponding elemental scores
    },
    {
        "question": "What standard do you hold yourself to with your loved ones?",
        "answers": [
            "Being truthful and maintaining integrity.",  # Ethical
            "Adjusting to their needs while staying true to myself.",  # Flexible
            "Being a reliable and dependable presence.",  # Realistic
            "Deeply honoring our bond.",  # Contemplative
        ],
        "traits": ["Ethical", "Flexible", "Realistic", "Contemplative"],
        "elements": ["Air", "Water", "Earth", "Fire"]  # Corresponding elemental scores
    },
    {
        "question": "What values would you prioritize as a company leader?",
        "answers": [
            "Upholding the highest standard of respect on all parts.",  # Ethical
            "Fostering a dynamic culture that can accompany everyone's needs.",  # Flexible
            "Following the most logical and calculated paths of risk for company growth.",  # Realistic
            "Creating an environment where many diverse perspectives can contribute.",  # Contemplative
        ],
        "traits": ["Ethical", "Flexible", "Realistic", "Contemplative"],
        "elements": ["Air", "Water", "Earth", "Fire"]  # Corresponding elemental scores
    },
    {
        "question": "What best fits your thoughts on human nature?",
        "answers": [
            "Human nature is inherently good but thrives on ethical guidance.",  # Ethical
            "Human nature is adaptable and resilient.",  # Flexible
            "Human nature is practical and survival-focused.",  # Realistic
            "Human nature is a complex philosophical subject worth deep discussion.",  # Contemplative
        ],
        "traits": ["Ethical", "Flexible", "Realistic", "Contemplative"],
        "elements": ["Air", "Water", "Earth", "Fire"]  # Corresponding elemental scores
    },
    {
        "question": "How do you deal with having a bad boss?",
        "answers": [
            "I maintain professionalism and do what’s right despite the challenges.",  # Ethical
            "I adapt to the situation and focus on the brighter side.",  # Flexible
            "I focus on my work.",  # Realistic
            "I reflect on the nature of my work and find a balance.",  # Contemplative
        ],
        "traits": ["Ethical", "Flexible", "Realistic", "Contemplative"],
        "elements": ["Air", "Water", "Earth", "Fire"]  # Corresponding elemental scores
    },
    {
        "question": "How do you keep a secret?",
        "answers": [
            "I keep it to myself no matter the person.",  # Ethical
            "I keep it to myself if they're my friend, but if I don't like them, I'll tell some people.",  # Flexible
            "I might forget it if it's innocuous enough but I'll tell people if it's dire.",  # Realistic
            "I consider the importance of the secret and weigh its confidentiality against my values.",  # Contemplative
        ],
        "traits": ["Ethical", "Flexible", "Realistic", "Contemplative"],
        "elements": ["Air", "Water", "Earth", "Fire"]  # Corresponding elemental scores
    },
    {
        "question": "How do you work with bad coworkers?",
        "answers": [
            "I maintain respectful and professional relations.",  # Ethical
            "I compromise to make things easier.",  # Flexible
            "I stay professional but try to keep my distance and set boundaries.",  # Realistic
            "I strategize the best approach depending on the situation, which sometimes can mean confrontation.",  # Contemplative
        ],
        "traits": ["Ethical", "Flexible", "Realistic", "Contemplative"],
        "elements": ["Air", "Water", "Earth", "Fire"]  # Corresponding elemental scores
    },
    {
        "question": "How do you value integrity?",
        "answers": [
            "Integrity is the root of living a valuable life, regardless of who you maintain it for.",  # Ethical
            "I value integrity as far as I value the person to whom I'm being integrous.",  # Flexible
            "Sometimes I'll deceive and lie to people if it's the safest option or if I truly don't respect them.",  # Realistic
            "I am stuck between regarding integrity highly and wondering if it's worth the trade off of all that comes from sacrificing it.",  # Contemplative
        ],
        "traits": ["Ethical", "Flexible", "Realistic", "Contemplative"],
        "elements": ["Air", "Water", "Earth", "Fire"]  # Corresponding elemental scores
    },
    {
        "question": "What do you believe of truth from a cosmic perspective?",
        "answers": [
            "There is a grand universal truth of goodness underlying all things which must be upheld and respected.",  # Ethical
            "Truth is fluid and depends on perspective and context.",  # Flexible
            "There is an objective reasoning of cause and effect behind everything which births truth from fact, no matter how big or small.",  # Realistic
            "Truth is subjective no matter the scale.",  # Contemplative
        ],
        "traits": ["Ethical", "Flexible", "Realistic", "Contemplative"],
        "elements": ["Air", "Water", "Earth", "Fire"]  # Corresponding elemental scores
    },
    {
        "question": "What is your value of loyalty?",
        "answers": [
            "Loyalty only works insofar as it does not jeopardize the wellbeing of the innocent.",  # Ethical
            "Loyalty is something I can selectively give for my optimized benefit.",  # Flexible
            "Loyalty is only as valuable as the perosn for whom I'm holding it.",  # Realistic
            "Loyalty has a definition that changes on the context.",  # Contemplative
        ],
        "traits": ["Ethical", "Flexible", "Realistic", "Contemplative"],
        "elements": ["Air", "Water", "Earth", "Fire"]  # Corresponding elemental scores
    }
]

# Dictionary for questions related to "Resilience and Adaptation"
resilience_adaptation_questions = [
    {
        "question": "How do you prepare for setbacks?",
        "answers": [
            "Preparation for hardship comes in self-regulation to face them confidently.",  # Composed
            "As logic would dictate, I save up my resources.",  # Resourceful
            "I remember how time never stops moving forward and align myself with its inevitable continuation for resilience.",  # Progressive
            "I build trust within my support groups so that I know the people I love and trust will be there for me.",  # Supportive
        ],
        "traits": ["Composed", "Resourceful", "Progressive", "Supportive"],
        "elements": ["Earth", "Air", "Fire", "Water"]  # Corresponding elemental scores
    },
    {
        "question": "How do you recover from setbacks?",
        "answers": [
            "I maintain a calm demeanor and take time for a balanced reset.",  # Composed
            "I use my skills to rebuild efficiently.",  # Resourceful
            "I focus on what I’ve learned to improve one step at a time.",  # Progressive
            "I lean on friends and loved ones for support.",  # Supportive
        ],
        "traits": ["Composed", "Resourceful", "Progressive", "Supportive"],
        "elements": ["Earth", "Air", "Fire", "Water"]  # Corresponding elemental scores
    },
    {
        "question": "How do you approach uncertainty?",
        "answers": [
            "I stay calm and grounded, trusting that clarity will come.",  # Composed
            "I look for tools and methods to manage the situation.",  # Resourceful
            "I embrace it confidently as an opportunity for growth and change.",  # Progressive
            "I involve others and seek reassurance to navigate it together.",  # Supportive
        ],
        "traits": ["Composed", "Resourceful", "Progressive", "Supportive"],
        "elements": ["Earth", "Air", "Fire", "Water"]  # Corresponding elemental scores
    },
    {
        "question": "How do you take risks?",
        "answers": [
            "I weigh the options carefully and remain calm under pressure.",  # Composed
            "I make calculated decisions and plan for contingencies.",  # Resourceful
            "I focus on the potential for growth and improvement.",  # Progressive
            "I seek input and support from those I trust before acting.",  # Supportive
        ],
        "traits": ["Composed", "Resourceful", "Progressive", "Supportive"],
        "elements": ["Earth", "Air", "Fire", "Water"]  # Corresponding elemental scores
    },
    {
        "question": "How do you adapt to change?",
        "answers": [
            "I focus on maintaining my inner balance while I slowly and securely adjust.",  # Composed
            "I find practical ways to adjust and make the most of the situation.",  # Resourceful
            "I jump head first into the change and continue pursuing it until I'm fully adapted.",  # Progressive
            "I find a support network that helps me find my place so I can adjust comfortably.",  # Supportive
        ],
        "traits": ["Composed", "Resourceful", "Progressive", "Supportive"],
        "elements": ["Earth", "Air", "Fire", "Water"]  # Corresponding elemental scores
    },
    {
        "question": "What team role do you do best in a team-based competition?",
        "answers": [
            "I keep us focused.",  # Composed
            "I make sure we have all the tools we need.",  # Resourceful
            "I lead the charge forward.",  # Progressive
            "I create a team-friendly environment.",  # Supportive
        ],
        "traits": ["Composed", "Resourceful", "Progressive", "Supportive"],
        "elements": ["Earth", "Air", "Fire", "Water"]  # Corresponding elemental scores
    },
    {
        "question": "How do you fend for yourself?",
        "answers": [
            "I stay focused on meeting my needs.",  # Composed
            "I use my skills and available tools to solve problems.",  # Resourceful
            "I secure my future with forward-thinking.",  # Progressive
            "I build a support network.",  # Supportive
        ],
        "traits": ["Composed", "Resourceful", "Progressive", "Supportive"],
        "elements": ["Earth", "Air", "Fire", "Water"]  # Corresponding elemental scores
    },
    {
        "question": "How do you approach long-term goals?",
        "answers": [
            "I keep my eyes on the end goal and steadily work toward my objectives.",  # Composed
            "I strategize effectively and use my resources efficiently.",  # Resourceful
            "I focus on growth and success.",  # Progressive
            "I involve others and build a support network to stay motivated.",  # Supportive
        ],
        "traits": ["Composed", "Resourceful", "Progressive", "Supportive"],
        "elements": ["Earth", "Air", "Fire", "Water"]  # Corresponding elemental scores
    },
    {
        "question": "What do you do when faced with opposition?",
        "answers": [
            "I remain composed and stay true to my values.",  # Composed
            "I find creative ways to work around or address the issue.",  # Resourceful
            "I approach it as an opportunity to grow stronger and improve.",  # Progressive
            "I seek allies and collaborate to address the opposition.",  # Supportive
        ],
        "traits": ["Composed", "Resourceful", "Progressive", "Supportive"],
        "elements": ["Earth", "Air", "Fire", "Water"]  # Corresponding elemental scores
    },
    {
        "question": "How do you console others in hard times?",
        "answers": [
            "I offer a calm and steady presence to help them feel grounded.",  # Composed
            "I provide practical advice or solutions to ease their burden.",  # Resourceful
            "I encourage them to focus on the positives and what lies ahead.",  # Progressive
            "I listen attentively and let them know they’re not alone.",  # Supportive
        ],
        "traits": ["Composed", "Resourceful", "Progressive", "Supportive"],
        "elements": ["Earth", "Air", "Fire", "Water"]  # Corresponding elemental scores
    },
    {
        "question": "How does your philosophy on survival most closely relate?",
        "answers": [
            "Staying grounded and practical is the key to overcoming challenges.",  # Composed
            "Using available tools and resources ensures survival.",  # Resourceful
            "Every challenge is an opportunity to grow and improve, thus improving survivorship.",  # Progressive
            "Survival is about helping and being helped by others.",  # Supportive
        ],
        "traits": ["Composed", "Resourceful", "Progressive", "Supportive"],
        "elements": ["Earth", "Air", "Fire", "Water"]  # Corresponding elemental scores
    },
    {
        "question": "When do you know to throw in the towel?",
        "answers": [
            "When continuing is no longer productive.",  # Composed
            "When resources are exhausted.",  # Resourceful
            "When ending may open doors to better opportunities.",  # Progressive
            "When my close loved ones grow concerned for my well-being.",  # Supportive
        ],
        "traits": ["Composed", "Resourceful", "Progressive", "Supportive"],
        "elements": ["Earth", "Air", "Fire", "Water"]  # Corresponding elemental scores
    }
]

import os
import random
import matplotlib.pyplot as plt
import numpy as np

# Mock input function for automated testing
def mock_input(lower, upper):
    return random.randint(lower, upper)

# Function to run the quiz
def run_quiz(input_handler=None):
    """Conducts the quiz, collects user inputs, updates scores, and resolves ties."""
    metrics = {
        "Social Orientation": ["Social", "Harmonious", "Assertive", "Reserved"],
        "Emotional and Cognitive Flexibility": ["Curious", "Stable", "Introspective", "Optimistic"],
        "Self-Expression and Purpose": ["Innovative", "Pragmatic", "Compassionate", "Expressive"],
        "Values and Integrity": ["Ethical", "Flexible", "Realistic", "Contemplative"],
        "Resilience and Adaptation": ["Composed", "Resourceful", "Progressive", "Supportive"]
    }

    # Initialize scores
    metric_scores = {metric: {trait: 0 for trait in traits} for metric, traits in metrics.items()}
    element_scores = {element: 0 for element in ["Air", "Water", "Fire", "Earth"]}
    all_questions = [social_orientation_questions, emotional_cognitive_flexibility_questions, 
                     self_expression_purpose_questions, values_integrity_questions, resilience_adaptation_questions]

    # Shuffle questions in each category
    for question_set in all_questions:
        random.shuffle(question_set)

    question_number = 1  # Track question numbers for clarity
    for i in range(max(len(q) for q in all_questions)):
        for question_set in all_questions:
            if i < len(question_set):
                question = question_set[i]
                print(f"\nQuestion {question_number}: {question['question']}\n")
                for j, answer in enumerate(question["answers"], start=1):
                    print(f"{j}. {answer}\n")

                while True:
                    try:
                        if input_handler:
                            choice = input_handler(1, len(question["answers"])) - 1
                        else:
                            choice = int(input("Choose an option (1-4): ")) - 1

                        if 0 <= choice < len(question["answers"]):
                            break
                        else:
                            print("Invalid choice. Please select a valid number.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                # Update scores
                for metric, traits in metrics.items():
                    if question["traits"][choice] in traits:
                        metric_scores[metric][question["traits"][choice]] += 1
                        break
                element_scores[question["elements"][choice]] += 1
                question_number += 1

    resolve_ties_recursively(metric_scores, element_scores, input_handler)
    combined_trait_scores = {trait: score for category in metric_scores.values() for trait, score in category.items()}
    return combined_trait_scores, element_scores

def get_user_choice(prompt, num_options):
    """
    Prompts the user to select an option from a list of choices.
    
    Args:
        prompt (str): The prompt to display to the user.
        num_options (int): The number of valid options (1 to num_options).
    
    Returns:
        int: The index of the chosen option (0-based).
    """
    while True:
        try:
            choice = int(input(prompt)) - 1  # Convert to 0-based index
            if 0 <= choice < num_options:
                return choice
            else:
                print(f"Invalid choice. Please enter a number between 1 and {num_options}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def resolve_ties_recursively(metric_scores, element_scores, tie_break_input=None):
    """
    Resolves only first-place ties across traits and elements.
    Allows ties in second or third place to remain unresolved.
    Automatically resolves ties using the provided input handler (tie_break_input) during the Test Phase.
    """
    def get_first_place_ties(scores):
        """Identifies only the highest-scoring traits that are tied."""
        max_score = max(scores.values())  # Find highest score in the category
        tied_items = [item for item, score in scores.items() if score == max_score]
        return tied_items if len(tied_items) > 1 else []  # Return list only if there's a tie

    def resolve_tie(scores, category_name, tied_items):
        """Resolves a single tie."""
        print(f"\nThere is a tie for FIRST PLACE in {category_name} between:")
        for i, item in enumerate(tied_items, start=1):
            print(f"{i}. {item}")

        while True:
            if tie_break_input:
                choice = tie_break_input(1, len(tied_items)) - 1  # Automated tie resolution
            else:
                try:
                    choice = int(input(f"Choose the trait that you feel best represents you (enter the number): ")) - 1
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue

            if 0 <= choice < len(tied_items):
                chosen_item = tied_items[choice]
                scores[chosen_item] += 1  # Increase score to break tie
                break
            else:
                print("Invalid choice. Please select a valid number.")

    # **Resolve ties in first-place traits only**
    for metric, scores in metric_scores.items():
        first_place_tied_items = get_first_place_ties(scores)
        if first_place_tied_items:
            resolve_tie(scores, metric, first_place_tied_items)

    # **Resolve ties in first-place elemental alignments only**
    first_place_element_tied_items = get_first_place_ties(element_scores)
    if first_place_element_tied_items:
        resolve_tie(element_scores, "Elements", first_place_element_tied_items)

    print("\nTie resolution complete.")

def calculate_introversion_extroversion(adjusted_scores):
    """
    Calculates introversion and extroversion proportions based on adjusted trait scores.
    """
    extroverted_traits = {
        "Social", "Assertive", "Optimistic", "Curious", "Expressive", "Innovative",
        "Flexible", "Realistic", "Progressive", "Supportive"
    }
    introverted_traits = {
        "Reserved", "Harmonious", "Introspective", "Stable", "Compassionate", "Pragmatic",
        "Ethical", "Contemplative", "Composed", "Resourceful"
    }

    extroverted_score = sum(adjusted_scores[trait] for trait in extroverted_traits if trait in adjusted_scores)
    introverted_score = sum(adjusted_scores[trait] for trait in introverted_traits if trait in adjusted_scores)
    total_score = extroverted_score + introverted_score

    introversion_proportion = introverted_score / total_score if total_score > 0 else 0
    extroversion_proportion = extroverted_score / total_score if total_score > 0 else 0

    return {
        "Introversion": introversion_proportion,
        "Extroversion": extroversion_proportion
    }            

# Function to determine the user's mythical creature
def get_mythical_creature(element_scores):
    sorted_elements = sorted(element_scores, key=element_scores.get, reverse=True)

    for creature, elements in mythical_creatures_elements.items():
        if elements == sorted_elements:
            return creature

    return "Unknown Creature"

def calculate_trait_ranks_with_modifiers(flat_trait_scores):
    """
    Adjusts flat trait scores using rank-based modifiers.
    """
    rank_modifiers = [0.8, 0.6, 0.4, 0.2]
    ranked_traits = sorted(flat_trait_scores.items(), key=lambda x: x[1], reverse=True)

    adjusted_scores = {}
    for rank, (trait, score) in enumerate(ranked_traits):
        if rank < len(rank_modifiers):  # Ensure rank doesn't exceed available modifiers
            adjusted_scores[trait] = score * rank_modifiers[rank]
        else:
            adjusted_scores[trait] = score * 0.2  # Apply the smallest modifier for extra ranks
    return adjusted_scores

def calculate_archetype_scores(metric_scores):
    """
    Calculates archetype scores using rank-based modifiers and adjusted weights.
    Returns a sorted list of tuples.
    """
    adjusted_scores = calculate_trait_ranks_with_modifiers(metric_scores)

    archetype_scores = {}
    for archetype, details in archetypes.items():
        score = 0
        for i, trait in enumerate(details["traits"], start=1):
            weight = (5 - i) / 5 # Weight inversely proportional to rank
            score += adjusted_scores.get(trait, 0) * weight
        archetype_scores[archetype] = score

    # Return a sorted list of tuples
    return sorted(archetype_scores.items(), key=lambda x: x[1], reverse=True)

def calculate_top_animals(archetype_scores, trait_scores):
    """
    Determines the top 2 animals using trait amplification and archetype weighting.
    Ensures all animals across all archetypes are scored.

    Returns:
        tuple: ((primary_animal, primary_score), (secondary_animal, secondary_score), all_animal_scores)
    """
    if not archetype_scores:
        raise ValueError("Archetype scores list is empty.")

    total_archetype_score = sum(score for _, score in archetype_scores)
    
    # **NEW: Assign weights to ALL archetypes, not just the top 3**
    archetype_weights = {
        archetype: score / total_archetype_score for archetype, score in archetype_scores
    }

    # Initialize scores for **ALL animals** across **ALL archetypes**
    all_animal_scores = {animal: 0 for archetype in archetypes for animal in archetypes[archetype]["fauna"]}

    # Compute scores for all animals
    for archetype, weight in archetype_weights.items():
        for animal in archetypes[archetype]["fauna"]:
            primary_trait = animal_traits[animal]["primary_trait"]
            secondary_trait = animal_traits[animal]["secondary_trait"]

            primary_score = trait_scores.get(primary_trait, 0)
            secondary_score = trait_scores.get(secondary_trait, 0)

            min_weight = min(archetype_weights.values())
            max_weight = max(archetype_weights.values())
            normalized_weights = {k: (v - min_weight) / (max_weight - min_weight) + 0.2 for k, v in archetype_weights.items()}
            total_score = ((primary_score * 0.6) + (secondary_score * 0.4)) * normalized_weights[archetype]
            all_animal_scores[animal] += total_score  # Accumulate scores

    # Sort animals by final computed score
    sorted_animals = sorted(all_animal_scores.items(), key=lambda x: x[1], reverse=True)

    # Select primary and secondary animals
    primary_animal, primary_score = sorted_animals[0]
    primary_archetype = next(a for a in archetypes if primary_animal in archetypes[a]["fauna"])

    # Choose the next highest-ranked animal from a different archetype
    secondary_animal, secondary_score = None, None
    for animal, score in sorted_animals[1:]:
        if animal not in archetypes[primary_archetype]["fauna"]:
            secondary_animal, secondary_score = animal, score
            break
    else:
        secondary_animal, secondary_score = sorted_animals[1]  # Fallback

    return (primary_animal, primary_score), (secondary_animal, secondary_score), all_animal_scores

def get_directory(name, is_test_phase):
    """
    Creates and retrieves the appropriate directory for saving files.
    If in test phase, a "mock" subfolder is created within the user's directory.
    """
    base_directory = "C:/Users/johna/OneDrive/Documents/Misc/AnimalTestResults"
    
    # Use "mock" for test phase or user name for person phase
    directory_name = "mock" if is_test_phase else name
    file_directory = os.path.join(base_directory, directory_name)
    
    # Create the directory if it does not exist
    if not os.path.exists(file_directory):
        os.makedirs(file_directory)
    
    return file_directory

def save_raw_data_to_file(name, trait_scores, element_scores, archetype_scores, all_animal_scores, file_directory):
    """
    Saves all raw data and additional information into a separate .txt file.
    Includes detailed archetype and animal scores and descriptive information.

    Parameters:
    - name (str): The user's name for the folder and file.
    - trait_scores (dict): Scores for all traits across categories.
    - element_scores (dict): Scores for elemental alignments.
    - archetype_scores (dict): Scores for all archetypes.
    - animal_scores (list): List of tuples with animal names and scores.
    """
    
    # Filepath for raw data
    file_path = os.path.join(file_directory, f"{name}_RawData.txt")
    
    with open(file_path, "w") as file:
        # Introduction
        file.write("Raw Data Report\n")
        file.write("=" * 50 + "\n")
        file.write(f"This report contains all the raw data and additional information from the quiz.\n")
        file.write(f"User: {name}\n\n")

        # Trait Scores grouped by categories
        file.write("Trait Scores by Categories:\n")
        file.write("-" * 50 + "\n")
        metrics = {
            "Social Orientation": ["Social", "Harmonious", "Assertive", "Reserved"],
            "Emotional and Cognitive Flexibility": ["Curious", "Stable", "Introspective", "Optimistic"],
            "Self-Expression and Purpose": ["Innovative", "Pragmatic", "Compassionate", "Expressive"],
            "Values and Integrity": ["Ethical", "Flexible", "Realistic", "Contemplative"],
            "Resilience and Adaptation": ["Composed", "Resourceful", "Progressive", "Supportive"]
        }

        for category, traits in metrics.items():
            file.write(f"\n{category}:\n")
            for trait in traits:
                file.write(f"  {trait}: {trait_scores.get(trait, 0)}\n")
        file.write("\n")

        # Elemental Scores
        file.write("Elemental Alignment Scores:\n")
        file.write("-" * 50 + "\n")
        for element, score in element_scores.items():
            file.write(f"{element}: {score}\n")
        file.write("\n")

        # Archetype Scores
        file.write("Archetype Scores:\n")
        file.write("-" * 50 + "\n")
        for archetype, score in archetype_scores.items():
            file.write(f"{archetype}: {score:.2f}\n")
        file.write("\n")

        # Animal Scores
        file.write("Animal Scores:\n")
        file.write("-" * 50 + "\n")
        sorted_animals = sorted(all_animal_scores.items(), key=lambda x: x[1], reverse=True)
        for animal, score in sorted_animals:
            file.write(f"{animal}: {score:.2f}\n")
        file.write("\n")

        # Mythical Creatures Information
        file.write("Mythical Creatures Information:\n")
        file.write("-" * 50 + "\n")
        for creature, description in mythical_creature_descriptions.items():
            file.write(f"{creature}:\n{description}\n")
        file.write("\n")

        # Archetypes Information
        file.write("Archetypes Information:\n")
        file.write("-" * 50 + "\n")
        for archetype, details in archetypes.items():
            file.write(f"{archetype}:\n")
            file.write(f"Description: {details['description']}\n")
            file.write(f"Top Traits: {', '.join(details['traits'])}\n\n")

        # Fauna Information
        file.write("Fauna Information:\n")
        file.write("-" * 50 + "\n")
        fauna_groups = {
            "Herpetofauna": herpetofauna,
            "Mammalia": mammalia,
            "Ichthyofauna": ichthyofauna,
            "Avifauna": avifauna,
        }
        for group_name, animals in fauna_groups.items():
            file.write(f"{group_name}:\n")
            for animal in animals:
                file.write(f"{animal}: {animal_descriptions.get(animal, 'No description available')}\n")
            file.write("\n")

    print(f"Raw data saved to {file_path}")

def save_results_to_file(name, trait_scores, element_scores, creature, top_archetypes, top_animals, file_directory):
    """
    Saves the results to a file in a directory named after the user.
    
    Args:
        name (str): The name of the user.
        trait_scores (dict): The trait scores by category.
        element_scores (dict): The elemental alignment scores.
        creature (str): The user's mythical creature.
        top_archetypes (list): The top three archetypes with scores.
        top_animals (list): The top two animals.
    """
    # Define file path for results
    file_path = os.path.join(file_directory, f"{name}_Results.txt")

    # Extract top animals and their names
    primary_animal_name = top_animals[0][0]
    secondary_animal_name = top_animals[1][0]

    # Ensure proper lookup of descriptions
    primary_animal_name = primary_animal_name.strip()
    secondary_animal_name = secondary_animal_name.strip()

    # Retrieve descriptions, ensuring no lookup failures
    primary_animal_description = animal_descriptions.get(primary_animal_name)
    secondary_animal_description = animal_descriptions.get(secondary_animal_name)

    # Debugging statements (Remove in final version)
    if primary_animal_description is None:
        print(f"Warning: No description found for {primary_animal_name}")
    if secondary_animal_description is None:
        print(f"Warning: No description found for {secondary_animal_name}")

    # Fallback message if description is still missing
    primary_animal_description = primary_animal_description if primary_animal_description else "No description available."
    secondary_animal_description = secondary_animal_description if secondary_animal_description else "No description available."

    # Open file and write results
    with open(file_path, "w") as file:
        # Greeting
        file.write("Hello! These are the results from your animal self test.\n\n")

        # Write trait scores organized by metrics
        metrics = {
            "Social Orientation": ["Social", "Harmonious", "Assertive", "Reserved"],
            "Emotional and Cognitive Flexibility": ["Curious", "Stable", "Introspective", "Optimistic"],
            "Self-Expression and Purpose": ["Innovative", "Pragmatic", "Compassionate", "Expressive"],
            "Values and Integrity": ["Ethical", "Flexible", "Realistic", "Contemplative"],
            "Resilience and Adaptation": ["Composed", "Resourceful", "Progressive", "Supportive"]
        }

        # Top traits
        file.write("TOP TRAITS:\n")
        for metric, traits in metrics.items():
            top_trait = max(traits, key=lambda t: trait_scores[t])
            file.write(f"Top in {metric}: {top_trait} ({trait_scores[top_trait]})\n")
        file.write("\n")

        # Elemental alignment details
        file.write("ELEMENTAL ALIGNMENT:\n")
        sorted_elements = sorted(element_scores.items(), key=lambda x: x[1], reverse=True)
        for element, score in sorted_elements:
            file.write(f"{element}: {score}\n")
        file.write(f"Top Element: {sorted_elements[0][0]}\n\n")

        file.write("\nARCHETYPES\n")
        file.write("The top archetype scores indicate you as a whole:\n")
        file.write("Think of your true role as a midpoint between all of them, weighted relative to your score for each.\n")
        
        for archetype, score in top_archetypes:
            file.write(f"{archetype} - Alignment Score: {score:.2f}\n")
            file.write(f"{archetypes[archetype]['description']}\n")
            file.write(f"Top Traits: {', '.join(archetypes[archetype]['traits'])}\n\n")

        # Introversion/Extroversion from traits
        intro_extro_proportions = calculate_introversion_extroversion(trait_scores)
        primary_alignment = "introverted" if intro_extro_proportions["Introversion"] > intro_extro_proportions["Extroversion"] else "extroverted"
        secondary_alignment = "extroverted" if primary_alignment == "introverted" else "introverted"

        file.write("INTROVERSION/EXTROVERSION\n")
        file.write(f"Your introversion proportion is: {intro_extro_proportions['Introversion']:.2f}\n")
        file.write(f"Your extroversion proportion is: {intro_extro_proportions['Extroversion']:.2f}\n\n")

        # Animal descriptions with alignment
        file.write(f"ANIMAL SELF\n")
        file.write(f"The {primary_animal_name} embodies your {primary_alignment} nature.\n")
        file.write(f"{primary_animal_description}\n\n")
        file.write(f"The {secondary_animal_name} embodies your {secondary_alignment} nature.\n")
        file.write(f"{secondary_animal_description}\n\n")

        # Mythical creature
        file.write(f"MYTHICAL CREATURE\nYour mythical creature reflects the core nature of your spiritual energy.\n\n")
        file.write(f"Your Mythical Creature: {creature}\n")
        file.write(f"{mythical_creature_descriptions[creature]}\n")

    print(f"Results saved to {file_path}")

def create_combined_radar_chart(file_directory, trait_scores):
    """
    Creates a single image containing 5 radar charts, one for each personality metric.
    
    Parameters:
        file_directory (str): Directory to save the combined radar chart.
        trait_scores (dict): Scores for each personality trait organized by metrics.
    """
    metrics = {
        "Social Orientation": ["Social", "Harmonious", "Assertive", "Reserved"],
        "Emotional and Cognitive Flexibility": ["Curious", "Stable", "Introspective", "Optimistic"],
        "Self-Expression and Purpose": ["Innovative", "Pragmatic", "Compassionate", "Expressive"],
        "Values and Integrity": ["Ethical", "Flexible", "Realistic", "Contemplative"],
        "Resilience and Adaptation": ["Composed", "Resourceful", "Progressive", "Supportive"]
    }

    # Create a subplot grid
    fig, axes = plt.subplots(2, 3, subplot_kw={'projection': 'polar'}, figsize=(16, 10))
    axes = axes.flatten()  # Flatten the grid for easier indexing

    for i, (metric, traits) in enumerate(metrics.items()):
        if i < len(axes):
            ax = axes[i]
            # Get scores for the current metric's traits
            scores = [trait_scores.get(trait, 0) for trait in traits]
            scores += scores[:1]  # Repeat the first value to close the radar chart
            angles = np.linspace(0, 2 * np.pi, len(traits) + 1, endpoint=True)

            # Create the radar chart
            ax.fill(angles, scores, color='blue', alpha=0.25)
            ax.plot(angles, scores, color='blue', linewidth=2)

            # Add labels and title
            ax.set_xticks(angles[:-1])
            ax.set_xticklabels(traits, fontsize=10)
            ax.set_yticks([])
            ax.set_title(metric, fontsize=14, fontweight='bold', pad=10)

    # Hide any unused subplot axes
    for j in range(len(metrics), len(axes)):
        fig.delaxes(axes[j])

    # Save the combined radar chart
    file_path = os.path.join(file_directory, "Combined_Radar_Charts.png")
    plt.tight_layout()
    plt.savefig(file_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"Combined radar charts saved to {file_directory}.")

def create_archetype_pie_chart(file_directory, archetype_scores):
    """
    Creates a pie chart of all archetype scores and saves it as a .png file.
    
    Args:
        file_directory (str): Directory where the file should be saved.
        archetype_scores (dict): Dictionary containing archetypes and their scores.
    """
    # Extract data for the pie chart
    labels = list(archetype_scores.keys())
    sizes = list(archetype_scores.values())
    
    # Plot the pie chart
    plt.figure(figsize=(10, 8))
    plt.pie(
        sizes, 
        labels=labels, 
        autopct='%1.1f%%', 
        startangle=90, 
        textprops={'fontsize': 10}
    )
    plt.title("Archetype Scores Distribution", fontsize=14)
    
    # Save the chart
    file_path = os.path.join(file_directory, "archetype_scores_pie_chart.png")
    plt.savefig(file_path)
    plt.close()
    print(f"Archetype scores pie chart saved to {file_path}")

def main():
    print("Welcome to the Animal Self Test!")

    print("\nLet's begin the quiz.\n"
          "There are 60 questions. Please answer honestly to discover your top archetypes and animals, as well as your mythical creature.\n"
          "Each question measures different metrics of personality categories. All descriptions will be provided after.\n\n")
    
    print("\nSelect the mode for this session:")
    print("1. Test Phase (automated inputs)")
    print("2. Person Phase (manual inputs)")

    while True:
        try:
            phase_choice = int(input("Enter 1 for Test Phase or 2 for Person Phase: "))
            if phase_choice == 1:
                print("\nRunning in Test Phase: All inputs will be randomly selected by the computer.")
                input_handler = mock_input  # Use the automated mock input function
                is_test_phase = True
                name = "mock"  # Automatically set name to "mock"
                break
            elif phase_choice == 2:
                print("\nRunning in Person Phase: You will manually answer each question.")
                input_handler = None  # Default to manual input
                is_test_phase = False
                while True:
                    name = input("\nPlease enter your name: ").strip()
                    if name:
                        break
                    else:
                        print("Name cannot be empty. Please try again.")
                break
            else:
                print("Invalid choice. Please select 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")

    # Get the directory for saving files
    file_directory = get_directory(name, is_test_phase)

    # Run the quiz
    trait_scores, element_scores = run_quiz(input_handler)

    # Calculate scores for archetypes and animals
    archetype_scores = calculate_archetype_scores(trait_scores)  # Sorted list of tuples
    top_archetypes = archetype_scores[:3]  # Keep top 3 for final selection
    _, _, all_animal_scores = calculate_top_animals(archetype_scores, trait_scores)  
    top_animals = sorted(all_animal_scores.items(), key=lambda x: x[1], reverse=True)[:2]  # Extract top 2 animals

    # Determine the mythical creature
    creature = get_mythical_creature(element_scores)

    # Save the results to files
    save_results_to_file(name, trait_scores, element_scores, creature, top_archetypes, top_animals, file_directory)
    save_raw_data_to_file(name, trait_scores, element_scores, dict(archetype_scores), all_animal_scores, file_directory)

    # Create visualizations
    create_combined_radar_chart(file_directory, trait_scores)
    create_archetype_pie_chart(file_directory, dict(archetype_scores))

    print("\nQuiz Complete! All results have been saved.")
main()
