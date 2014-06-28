import unittest
from hashmap import Hashmap


class HashmapTest(unittest.TestCase):
    
    def setUp(self):
        self.hashmap = Hashmap()
        self.sayings = {
            'Lannister' : 'A Lannister always pays his debts',
            'Baratheon' : 'Ours is the Fury',
            'Greyjoy' : 'We Do Dot Sow',
            'Tyrell' : 'Growing Strong',
            'Stark' : 'Winter is Coming',
            'Tully' : 'Unbowed, Unbent, Unbroken',
            'Bolton' : 'Our Blades are Sharp',
            'Karstark': 'The Sun of Winter',
        }

    def fill_sayings(self):
        for house, saying in self.sayings.items():
            self.hashmap[house] = saying
    
    def test_setting_getting(self):
        self.assertEqual(self.hashmap['Lannister'], Hashmap.absent)
        self.assertEqual(self.hashmap['Baratheon'], Hashmap.absent)

        self.hashmap['Lannister'] = self.sayings['Lannister']
        self.assertEqual(self.hashmap['Lannister'], self.sayings['Lannister'])
        self.assertEqual(self.hashmap['Baratheon'], Hashmap.absent)

        self.hashmap['Baratheon'] = self.sayings['Baratheon']
        self.assertEqual(self.hashmap['Lannister'], self.sayings['Lannister'])
        self.assertEqual(self.hashmap['Baratheon'], self.sayings['Baratheon'])

    def test_resizing_set(self):
        sayings = list(self.sayings.items())
        for house, saying in sayings[:5]:
            self.hashmap[house] = saying
            self.assertEqual(self.hashmap[house], saying)    
            self.assertEqual(len(self.hashmap._backing), 8)

        for house, saying in sayings[5:]:
            self.hashmap[house] = saying
            self.assertEqual(self.hashmap[house], saying)    
            self.assertEqual(len(self.hashmap._backing), 16)

    def test_resizing_del(self):
        self.fill_sayings()

        houses = list(self.sayings.keys())
        for house in houses[:5]:
            del self.hashmap[house]
            self.assertEqual(len(self.hashmap._backing), 16)

        for house in houses[5:]:
            del self.hashmap[house]
            self.assertEqual(len(self.hashmap._backing), 8)

    def test_replacing(self):
        self.hashmap['Lannister'] = self.sayings['Lannister']
        self.assertEqual(self.hashmap['Lannister'], self.sayings['Lannister'])

        self.hashmap['Lannister'] = 'Hear Me Roar!'
        self.assertEqual(self.hashmap['Lannister'], 'Hear Me Roar!')

    def test_deleting(self):
        self.hashmap['Baratheon'] = self.sayings['Baratheon']

        del self.hashmap['Baratheon']
        self.assertEqual(self.hashmap['Baratheon'], Hashmap.absent)

        self.hashmap['Baratheon'] = self.sayings['Lannister']
        self.assertEqual(self.hashmap['Baratheon'], self.sayings['Lannister'])

    def test_deleting_non_existant(self):
        with self.assertRaises(KeyError):
            del self.hashmap['Baratheon']

    def test_containing(self):
        self.assertTrue('Lannister' not in self.hashmap)

        self.hashmap['Lannister'] = self.sayings['Lannister']
        self.assertTrue('Lannister' in self.hashmap)

        del self.hashmap['Lannister']
        self.assertTrue('Lannister' not in self.hashmap)

    def test_len(self):
        count = 0
        for house, saying in self.sayings.items():
            self.hashmap[house] = saying
            count += 1
            self.assertEqual(len(self.hashmap), count)

        for house in self.sayings.keys():
            del self.hashmap[house]
            count -= 1
            self.assertEqual(len(self.hashmap), count)

    def test_iteration(self):
        self.fill_sayings()

        for house, saying in self.hashmap:
            self.assertEqual(self.sayings[house], saying)

if __name__ == '__main__':
    unittest.main()
