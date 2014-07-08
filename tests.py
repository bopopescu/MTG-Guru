from django.test import TestCase
from mtg_project.models import *

class MTG_TEST(TestCase) :

    """
    Tests for MagicCard class
    """

    def test_MagicCard_1(self) :
        card_dict = {"card_ID" : 378490,
            "card_name" : 'Charging Badger',
            "card_setID" : 'BNG',
            "card_type" : 'Creature',
            "card_subtype" : 'Badger',
            "card_mana_cost" : '{G}',
            "card_converted_cost" : 1,
            "card_loyalty" : 'NULL',
            "card_rarity" : 'C',
            "card_text" : 'Trample',
            "card_flavor_text" : '#_"If the hierarchies of nature were determined by ferocity alone, the badger would be lord of the beasts."_#£#_—Anthousa of Setessa_#',
            "card_power" : 1.0,
            "card_toughness" : 1.0,
            "card_price" : 0.14}

        MagicCard.objects.create(**card_dict)
        card_object = MagicCard.objects.get(card_dict["card_ID"])

        self.assertEqual(card_object.card_ID, 378490)
        self.assertEqual(card_object.card_name, 'Charging Badger')
        self.assertEqual(card_object.card_setID, 'BNG')
        self.assertEqual(card_object.card_type, 'Creature')

    def test_MagicCard_2(self) :
        card_dict = {"card_ID" : 373500,
            "card_name" : 'Ashiok, Nightmare Weaver',
            "card_setID" : 'THS',
            "card_type" : 'Planeswalker',
            "card_subtype" : 'Ashiok',
            "card_mana_cost" : '{1}{U}{B}',
            "card_converted_cost" : 3,
            "card_loyalty" : 3,
            "card_rarity" : 'M',
            "card_text" : "+2: Exile the top three cards of target opponent''s library.£-X: Put a creature card with converted mana cost X exiled with Ashiok, Nightmare Weaver onto the battlefield under your control. That creature is a Nightmare in addition to its other types.£-10: Exile all cards from all opponents'' hands and graveyards.",
            "card_flavor_text" : '',
            "card_power" : 0,
            "card_toughness" : 0,
            "card_price" : 8.14}

        MagicCard.objects.create(**card_dict)
        card_object = MagicCard.objects.get(card_dict["card_ID"])

        self.assertEqual(card_object.card_ID, 373500)
        self.assertEqual(card_object.card_mana_cost, '{1}{U}{B}')
        self.assertEqual(card_object.card_flavor_text, '')
        self.assertEqual(card_object.card_loyalty, 3)

    def test_MagicCard_3(self) :
        card_dict = {"card_ID" : 136142,
            "card_name" : 'Tarmogoyf',
            "card_setID" : 'FUT',
            "card_type" : 'Creature',
            "card_subtype" : 'Lhurgoyf',
            "card_mana_cost" : '{1}{G}',
            "card_converted_cost" : 2,
            "card_loyalty" : 'NULL',
            "card_rarity" : 'R',
            "card_text" : "Tarmogoyf''s power is equal to the number of card types among cards in all graveyards and its toughness is equal to that number plus 1.",
            "card_flavor_text" : '',
            "card_power" : -1,
            "card_toughness" : -2,
            "card_price" : 190.38}

        MagicCard.objects.create(**card_dict)
        card_object = MagicCard.objects.get(card_dict["card_ID"])

        self.assertEqual(card_object.card_text, "Tarmogoyf''s power is equal to the number of card types among cards in all graveyards and its toughness is equal to that number plus 1.")
        self.assertEqual(card_object.card_power, -1)
        self.assertEqual(card_object.card_toughness, -2)
        self.assertEqual(card_object.card_price, 190.38)

    """
    Tests for MagicSet class
    """

    def test_MagicSet_1(self) :
        set_dict = {"set_ID" : 'BNG',
                "set_name" : 'Born of the Gods',
                "set_symbol" : 'NULL',
                "set_release_date" :'02/2014',
                "set_num_cards" : 165,
                "set_cards" : [378373, 378402, 378459, 378374, 378375, 378403, 378460, 378376, 378488, 378430, 378404, 378431, 378489, 378432, 378529, 378433, 378434, 378461, 378377, 378435, 378490, 378405, 378516, 378436, 378491, 378406, 378492, 378462, 378378, 378407, 378408, 378437, 378438, 378379, 378380, 378517, 378518, 378381, 378463, 378409, 378410, 378464, 378382, 378439, 378465, 378519, 378440, 378466, 378411, 378493, 378383, 378441, 378467, 378442, 378468, 378469, 378412, 378413, 378470, 378443, 378444, 378384, 378445, 378385, 378386, 378530, 378494, 378387, 378388, 378446, 378447, 378389, 378495, 378531, 378390, 378496, 378471, 378520, 378497, 378521, 378522, 378472, 378414, 378473, 378391, 378448, 378415, 378416, 378498, 378523, 378392, 378499, 378449, 378500, 378501, 378502, 378417, 378450, 378474, 378393, 378418, 378503, 378451, 378475, 378419, 378394, 378395, 378452, 378504, 378420, 378476, 378524, 378505, 378506, 378532, 378477, 378396, 378525, 378507, 378526, 378478, 378421, 378397, 378479, 378453, 378480, 378481, 378508, 378509, 378482, 378483, 378454, 378510, 378511, 378455, 378398, 378422, 378527, 378533, 378512, 378513, 378423, 378399, 378456, 378534, 378484, 378424, 378425, 378400, 378514, 378535, 378536, 378537, 378426, 378485, 378486, 378427, 378515, 378401, 378428, 378457, 378458, 378429, 378487, 378528]}
        
        MagicSet.objects.create(**set_dict)
        set_object = MagicSet.objects.get(set_dict["set_ID"])

        self.assertEqual(set_object.set_ID, 'BNG')
        self.assertEqual(set_object.set_symbol, 'NULL')

    def test_MagicSet_2(self) :
        set_dict = {"set_ID" : 'BNG',
                "set_name" : 'Born of the Gods',
                "set_symbol" : 'NULL',
                "set_release_date" :'02/2014',
                "set_num_cards" : 165,
                "set_cards" : [378373, 378402, 378459, 378374, 378375, 378403, 378460, 378376, 378488, 378430, 378404, 378431, 378489, 378432, 378529, 378433, 378434, 378461, 378377, 378435, 378490, 378405, 378516, 378436, 378491, 378406, 378492, 378462, 378378, 378407, 378408, 378437, 378438, 378379, 378380, 378517, 378518, 378381, 378463, 378409, 378410, 378464, 378382, 378439, 378465, 378519, 378440, 378466, 378411, 378493, 378383, 378441, 378467, 378442, 378468, 378469, 378412, 378413, 378470, 378443, 378444, 378384, 378445, 378385, 378386, 378530, 378494, 378387, 378388, 378446, 378447, 378389, 378495, 378531, 378390, 378496, 378471, 378520, 378497, 378521, 378522, 378472, 378414, 378473, 378391, 378448, 378415, 378416, 378498, 378523, 378392, 378499, 378449, 378500, 378501, 378502, 378417, 378450, 378474, 378393, 378418, 378503, 378451, 378475, 378419, 378394, 378395, 378452, 378504, 378420, 378476, 378524, 378505, 378506, 378532, 378477, 378396, 378525, 378507, 378526, 378478, 378421, 378397, 378479, 378453, 378480, 378481, 378508, 378509, 378482, 378483, 378454, 378510, 378511, 378455, 378398, 378422, 378527, 378533, 378512, 378513, 378423, 378399, 378456, 378534, 378484, 378424, 378425, 378400, 378514, 378535, 378536, 378537, 378426, 378485, 378486, 378427, 378515, 378401, 378428, 378457, 378458, 378429, 378487, 378528]}
        
        MagicSet.objects.create(**set_dict)
        set_object = MagicSet.objects.get(set_dict["set_ID"])

        self.assertEqual(set_object.set_name, 'Born of the Gods')
        self.assertEqual(set_object.set_num_cards, 165)

    def test_MagicSet_3(self) :
        set_dict = {"set_ID" : 'UNH',
            "set_name" : 'Unhinged',
            "set_symbol" : 'NULL',
            "set_release_date" : '11/2004',
            "set_num_cards" : 140,
            "set_cards" : [73935, 74252, 74284, 74317, 74356, 74329, 74251, 73937, 74254, 74231, 74350, 73938, 74227, 73979, 73939, 73977, 74249, 74289, 74244, 74236, 74220, 74306, 73940, 74327, 74354, 74303, 73956, 74359, 74262, 74325, 73943, 74287, 73961, 73944, 74312, 74275, 73936, 73966, 74300, 74348, 74224, 74261, 74330, 73946, 74318, 74301, 74218, 73950, 73941, 73947, 74298, 74221, 74314, 74295, 74281, 74328, 74296, 74307, 73981, 73951, 74271, 73971, 74322, 74260, 74259, 74293, 74232, 74360, 73964, 74256, 74268, 74266, 73955, 74347, 74304, 74255, 74233, 73957, 74292, 73958, 73949, 74323, 73945, 74286, 74326, 73959, 74337, 74235, 73960, 74237, 74238, 73962, 73963, 74263, 74248, 74333, 74294, 73967, 73968, 74267, 74310, 74250, 74324, 74344, 73942, 74242, 74277, 74332, 73948, 73934, 74270, 74339, 74343, 74276, 74246, 74346, 74272, 74315, 73973, 74265, 73974, 74288, 74342, 73985, 74321, 74349, 74234, 73976, 74345, 74319, 73953, 74219, 74274, 74358, 73972, 74241, 74334, 74331, 74290, 74336]}

        MagicSet.objects.create(**set_dict)
        set_object = MagicSet.objects.get(set_dict["set_ID"])

        self.assertEqual(set_object.set_release_date, '11/2004')
        self.assertEqual(set_object.set_cards, [73935, 74252, 74284, 74317, 74356, 74329, 74251, 73937, 74254, 74231, 74350, 73938, 74227, 73979, 73939, 73977, 74249, 74289, 74244, 74236, 74220, 74306, 73940, 74327, 74354, 74303, 73956, 74359, 74262, 74325, 73943, 74287, 73961, 73944, 74312, 74275, 73936, 73966, 74300, 74348, 74224, 74261, 74330, 73946, 74318, 74301, 74218, 73950, 73941, 73947, 74298, 74221, 74314, 74295, 74281, 74328, 74296, 74307, 73981, 73951, 74271, 73971, 74322, 74260, 74259, 74293, 74232, 74360, 73964, 74256, 74268, 74266, 73955, 74347, 74304, 74255, 74233, 73957, 74292, 73958, 73949, 74323, 73945, 74286, 74326, 73959, 74337, 74235, 73960, 74237, 74238, 73962, 73963, 74263, 74248, 74333, 74294, 73967, 73968, 74267, 74310, 74250, 74324, 74344, 73942, 74242, 74277, 74332, 73948, 73934, 74270, 74339, 74343, 74276, 74246, 74346, 74272, 74315, 73973, 74265, 73974, 74288, 74342, 73985, 74321, 74349, 74234, 73976, 74345, 74319, 73953, 74219, 74274, 74358, 73972, 74241, 74334, 74331, 74290, 74336])

    """
    Tests for MagicType class
    """

    def test_MagicType_1(self) :
        type_dict = {"type_name" : 'Enchant Creature',
            "type_description" : 'Enchantment creatures were introduced on a futureshifted card in Future Sight: Lucent Liminid. They later reappeared as a fullfledged mechanic in the Theros set, where they represent the gods themselves , and their emissaries (creatures with bestow). The enchantment creatures were highlighted in the following set, which was named after them: Born of the Gods. These had all global enchantment effects.',
            "type_subtype" : ['Sheep', 'Elk', 'Giant', 'Lamia', 'Siren', 'Elemental', 'Hag', 'Satyr', 'Crab', 'Merfolk', 'Horror', 'Centaur', 'Beast', 'Insect', 'Snake', 'Nymph', 'Manticore', 'Spirit', 'Zombie', 'Human Soldier', 'Gorgon', 'Unicorn', 'Cat', 'Boar', 'Cyclops', 'Ox', 'Nautilus', 'Human Wizard', 'Human Cleric', 'Demon', 'Spider', 'Nymph Dryad', 'Chimera', 'Human Warrior', 'Wolf', 'Hound', 'Archon', 'Minotaur']}

        MagicType.objects.create(**type_dict)
        type_object = MagicType.objects.get(type_dict["type_name"])

        self.assertEqual(type_object.type_name, 'Enchant Creature')
        self.assertEqual(type_object.type_description, 'Enchantment creatures were introduced on a futureshifted card in Future Sight: Lucent Liminid. They later reappeared as a fullfledged mechanic in the Theros set, where they represent the gods themselves , and their emissaries (creatures with bestow). The enchantment creatures were highlighted in the following set, which was named after them: Born of the Gods. These had all global enchantment effects.')
        self.assertEqual(type_object.type_subtype, ['Sheep', 'Elk', 'Giant', 'Lamia', 'Siren', 'Elemental', 'Hag', 'Satyr', 'Crab', 'Merfolk', 'Horror', 'Centaur', 'Beast', 'Insect', 'Snake', 'Nymph', 'Manticore', 'Spirit', 'Zombie', 'Human Soldier', 'Gorgon', 'Unicorn', 'Cat', 'Boar', 'Cyclops', 'Ox', 'Nautilus', 'Human Wizard', 'Human Cleric', 'Demon', 'Spider', 'Nymph Dryad', 'Chimera', 'Human Warrior', 'Wolf', 'Hound', 'Archon', 'Minotaur'])

    def test_MagicType_2(self) :
        type_dict = {"type_name" : 'Interrupts',
            "type_description" : 'Interrupt is an obsolete card type. It has not been supported by the game since Sixth Edition. Under the original rules, an interrupt was a spell that would resolve before the rest of the Batch. Some examples of interrupts include Counterspell, Red Elemental Blast and Dark Ritual. All Interrupt cards have received errata to make them instants, and all references to Interrupts have been given errata to reference instants.',
            "type_subtype" : []}

        MagicType.objects.create(**type_dict)
        type_object = MagicType.objects.get(type_dict["type_name"])

        self.assertEqual(type_object.type_name, 'Interrupts')
        self.assertEqual(type_object.type_description, 'Interrupt is an obsolete card type. It has not been supported by the game since Sixth Edition. Under the original rules, an interrupt was a spell that would resolve before the rest of the Batch. Some examples of interrupts include Counterspell, Red Elemental Blast and Dark Ritual. All Interrupt cards have received errata to make them instants, and all references to Interrupts have been given errata to reference instants.')
        self.assertEqual(type_object.type_subtype, [])

    def test_MagicType_3(self) :
        type_dict = {"type_name" : 'Basic Land',
            "type_description" : 'These lands are unlike nonbasic lands in that any number may be included in a deck. There are basic lands for each color — Plains, Island, Swamp, Mountain, and Forest for white, blue, black, red, and green, respectively. Each basic land has the basic land type of the same name; e.g., Plains have the Plains land type. Basic lands are thought of as the cornerstones of Magic design, and no lands should be printed if they are strictly better than basic lands, with the sole exception to this rule being the dual lands from Alpha/Beta/Unlimited/Revised. Consequently, other, nonbasic lands feature drawbacks, in addition to the fact that no more than four copies of nonbasic lands may be played in a deck.',
            "type_subtype" : ['Plains', 'Island', 'Swamp', 'Forest', 'Mountain']}

        MagicType.objects.create(**type_dict)
        type_object = MagicType.objects.get(type_dict["type_name"])

        self.assertEqual(type_object.type_name, 'Basic Land')
        self.assertEqual(type_object.type_description, 'These lands are unlike nonbasic lands in that any number may be included in a deck. There are basic lands for each color — Plains, Island, Swamp, Mountain, and Forest for white, blue, black, red, and green, respectively. Each basic land has the basic land type of the same name; e.g., Plains have the Plains land type. Basic lands are thought of as the cornerstones of Magic design, and no lands should be printed if they are strictly better than basic lands, with the sole exception to this rule being the dual lands from Alpha/Beta/Unlimited/Revised. Consequently, other, nonbasic lands feature drawbacks, in addition to the fact that no more than four copies of nonbasic lands may be played in a deck.')
        self.assertEqual(type_object.type_subtype, ['Plains', 'Island', 'Swamp', 'Forest', 'Mountain'])

    """
    Tests for MagicSubtype class
    """

    def test_MagicSubtype_1(self) :
        subtype_dict = {"subtype_name" : 'Beast',
            "subtype_supertype" : ['Artifact Creature', 'Creature', 'Enchantment Creature', 'Summon']}

        MagicSubtype.objects.create(**subtype_dict)
        subtype_object = MagicSubtype.objects.get(subtype_dict["subtype_name"])

        self.assertEqual(subtype_object.subtype_name, 'Beast')
        self.assertEqual(subtype_object.subtype_supertype, ['Artifact Creature', 'Creature', 'Enchantment Creature', 'Summon'])

    def test_MagicSubtype_2(self) :
        subtype_dict = {"subtype_name" : 'Hound Construct',
            "subtype_supertype" : ['Artifact Creature']}

        MagicSubtype.objects.create(**subtype_dict)
        subtype_object = MagicSubtype.objects.get(subtype_dict["subtype_name"])

        self.assertEqual(subtype_object.subtype_name, 'Hound Construct')
        self.assertEqual(subtype_object.subtype_supertype, ['Artifact Creature'])

    def test_MagicSubtype_3(self) :
        subtype_dict = {"subtype_name" : 'Angel',
            "subtype_supertype" : ['Creature', 'Legendary Creature', 'Snow Creature']}

        MagicSubtype.objects.create(**subtype_dict)
        subtype_object = MagicSubtype.objects.get(subtype_dict["subtype_name"])

        self.assertEqual(subtype_object.subtype_name, 'Angel')
        self.assertEqual(subtype_object.subtype_supertype, ['Creature', 'Legendary Creature', 'Snow Creature'])


print("tests.py")
print("Done.")

