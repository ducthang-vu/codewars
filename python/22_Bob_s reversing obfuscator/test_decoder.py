import unittest
from .decoder import decoder


class SequenceTest(unittest.TestCase):
    def test_string1(self):
        self.assertEqual(decoder("Lor-.tile gnicsipida rutetcesnoc ,tema tis rolod muspi me", '-'), "Lorem ipsum "
                                                                                                    "dolor sit amet, "
                                                                                                    "consectetur "
                                                                                                    "adipiscing elit.")

    def test_string2(self):
        self.assertEqual(decoder("q.tile gnicsipida rutetcesnoc ,tema tis rolod muspi meroL", 'q'), "Lorem ipsum "
                                                                                                    "dolor sit amet, "
                                                                                                    "consectetur "
                                                                                                    "adipiscing elit.")

    def test_string3(self):
        self.assertEqual(decoder("Proinq.tile sitrobol rotittrop ,non muspi siu dnefiele ,sutcel neipas ", 'q'),
                         "Proin sapien lectus, eleifend uis ipsum non, porttitor lobortis elit.")

    def test_string4(self):
        self.assertEqual(decoder("q.qSusqsitanenev cen lsin sillom subinif ecsuF .itnetop essidnep", 'q'),
                         "Suspendisse potenti. Fusce finibus mollis nisl nec venenatis.")

    def test_string5(self):
        self.assertEqual(decoder("Dq.silucaiqonec mollq odommoc qis ipsum qlsin lev", 'q'),
                         "Donec mollis ipsum vel nisl commodo iaculis.")

    def test_string6(self):
        self.assertEqual(decoder("qqqqAqq.qqliuaqqsutcqqm nulla dolor, varius eget aliuam sed, venenatis eu le", 'qq'),
                         "Aliuam nulla dolor, varius eget aliuam sed, venenatis eu lectus.")

    def test_string7(self):
        self.assertEqual(decoder("Uqq.siruam qqt rutrum,qqtaptulov qq enim at qqmine mau qqsodales tqqsuirav "
                                 "ceqqincidunt,qqn ,sucal qq est sem qqatrop", 'qq'),
                         "Ut rutrum, enim at sodales tincidunt, est sem porta lacus, nec varius uam enim volutpat "
                         "mauris.")

    def test_string8(self):
        self.assertEqual(decoder("Vizq.anrzqvazqu sillavnoc ,ni eugua tnudicnit ,sillom tare eativ sum", 'zq'),
                         "Vivamus vitae erat mollis, tincidunt augue in, convallis urna.")
