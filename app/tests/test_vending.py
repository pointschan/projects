__author__ = 'pointschan'

import unittest
import sys
from control.vending import vend_pop
from StringIO import StringIO

class test_vending(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # ###########################################################
    # Test purchase with amount in Number - different scenario
    # ###########################################################
    def test_purchase_cool_cola_with_exact_amount_in_number(self):
        sys.stdout = StringIO()
        amount_returned = vend_pop('Cool Cola', 3.59)
        result_string = sys.stdout.getvalue().strip()
        self.assertEqual("Here's some pop: Cool Cola", result_string)
        self.assertEqual(0.0, amount_returned)

    def test_purchase_mighty_mist_with_exact_amount_in_number(self):
        sys.stdout = StringIO()
        amount_returned = vend_pop('Mighty Mist', 4.27)
        result_string = sys.stdout.getvalue().strip()
        self.assertEqual("Here's some pop: Mighty Mist", result_string)
        self.assertEqual(0.0, amount_returned)

    def test_purchase_butter_beer_with_exact_amount_in_number(self):
        sys.stdout = StringIO()
        amount_returned = vend_pop('Butter Beer', 5.99)
        result_string = sys.stdout.getvalue().strip()
        self.assertEqual("Here's some pop: Butter Beer", result_string)
        self.assertEqual(0.0, amount_returned)

    def test_purchase_cool_cola_with_exact_amount_in_number_6_decimal(self):
        sys.stdout = StringIO()
        amount_returned = vend_pop('Cool Cola', 3.590000)
        result_string = sys.stdout.getvalue().strip()
        self.assertEqual("Here's some pop: Cool Cola", result_string)
        self.assertEqual(0.0, amount_returned)

    def test_purchase_cool_cola_with_exact_amount_in_number_with_leading_zero(self):
        sys.stdout = StringIO()
        amount_returned = vend_pop('Cool Cola', 003.59)
        result_string = sys.stdout.getvalue().strip()
        self.assertEqual("Here's some pop: Cool Cola", result_string)
        self.assertEqual(0.0, amount_returned)

    # ##########################################################
    # Test purchase with amount in string
    # ##########################################################
    def test_purchase_cool_cola_with_exact_amount_in_string(self):
        sys.stdout = StringIO()
        amount_returned = vend_pop('Cool Cola', '3.59')
        result_string = sys.stdout.getvalue().strip()
        self.assertEqual("Here's some pop: Cool Cola", result_string)
        self.assertEqual(0.0, amount_returned)

    def test_purchase_mighty_mist_with_exact_amount_in_string(self):
        sys.stdout = StringIO()
        amount_returned = vend_pop('Mighty Mist', '4.27')
        result_string = sys.stdout.getvalue().strip()
        self.assertEqual("Here's some pop: Mighty Mist", result_string)
        self.assertEqual(0.0, amount_returned)

    def test_purchase_butter_beer_with_exact_amount_in_string(self):
        sys.stdout = StringIO()
        amount_returned = vend_pop('Butter Beer', '5.99')
        result_string = sys.stdout.getvalue().strip()
        self.assertEqual("Here's some pop: Butter Beer", result_string)
        self.assertEqual(0.0, amount_returned)

    def test_purchase_cool_cola_with_exact_amount_in_string_with_6_decimal(self):
        sys.stdout = StringIO()
        amount_returned = vend_pop('Cool Cola', '3.590000')
        result_string = sys.stdout.getvalue().strip()
        self.assertEqual("Here's some pop: Cool Cola", result_string)
        self.assertEqual(0.0, amount_returned)

    # ###########################################################
    # Test purchase with extra amount
    # ############################################################
    def test_purchase_cool_cola_with_extra_amount_in_number_1(self):
        sys.stdout = StringIO()
        amount_returned = vend_pop('Cool Cola', 4.00)
        result_string = sys.stdout.getvalue().strip()
        self.assertEqual("Here's some pop: Cool Cola", result_string)
        self.assertEqual(0.41, amount_returned)

    def test_purchase_cool_cola_with_extra_amount_in_number_2(self):
        sys.stdout = StringIO()
        amount_returned = vend_pop('Cool Cola', 123.00)
        result_string = sys.stdout.getvalue().strip()
        self.assertEqual("Here's some pop: Cool Cola", result_string)
        self.assertEqual(119.41, amount_returned)

    def test_purchase_cool_cola_with_extra_amount_in_integer_4(self):
        sys.stdout = StringIO()
        amount_returned = vend_pop('Cool Cola', 4)
        result_string = sys.stdout.getvalue().strip()
        self.assertEqual("Here's some pop: Cool Cola", result_string)
        self.assertEqual(0.41, amount_returned)

    def test_purchase_cool_cola_with_extra_amount_in_integer_00100(self):
        sys.stdout = StringIO()
        amount_returned = vend_pop('Cool Cola', 00100)
        result_string = sys.stdout.getvalue().strip()
        self.assertEqual("Here's some pop: Cool Cola", result_string)
        self.assertEqual(96.41, amount_returned)

    def test_purchase_cool_cola_with_extra_amount_in_string_with_2_decimal(self):
        sys.stdout = StringIO()
        amount_returned = vend_pop('Cool Cola', '4.00')
        result_string = sys.stdout.getvalue().strip()
        self.assertEqual("Here's some pop: Cool Cola", result_string)
        self.assertEqual(0.41, amount_returned)

    def test_purchase_cool_cola_with_extra_amount_in_string_integer(self):
        sys.stdout = StringIO()
        amount_returned = vend_pop('Cool Cola', '4')
        result_string = sys.stdout.getvalue().strip()
        self.assertEqual("Here's some pop: Cool Cola", result_string)
        self.assertEqual(0.41, amount_returned)

    # ######################################################
    # Test purchase with not enough amount
    # ######################################################
    def test_purchase_cool_cola_with_not_enough_coins_1(self):
        with self.assertRaises(Exception) as context:
            amount_returned = vend_pop('Cool Cola', 3.58)
        self.assertEqual('Not enough coins. Insert 0.01 more!', context.exception.message)

    def test_purchase_cool_cola_with_not_enough_coins_2(self):
        with self.assertRaises(Exception) as context:
            amount_returned = vend_pop('Cool Cola', 3.588888)
        self.assertEqual('Not enough coins. Insert 0.0 more!', context.exception.message)

    def test_purchase_cool_cola_with_not_enough_coins_3(self):
        with self.assertRaises(Exception) as context:
            amount_returned = vend_pop('Cool Cola', 0.01)
        self.assertEqual('Not enough coins. Insert 3.58 more!', context.exception.message)

    def test_purchase_cool_cola_with_not_enough_coins_4(self):
        with self.assertRaises(Exception) as context:
            amount_returned = vend_pop('Cool Cola', 0)
        self.assertEqual('Please insert coins. No freebies!', context.exception.message)

    def test_purchase_cool_cola_with_not_enough_coins_5(self):
        with self.assertRaises(Exception) as context:
            amount_returned = vend_pop('Cool Cola', -0)
        self.assertEqual('Please insert coins. No freebies!', context.exception.message)

    def test_purchase_cool_cola_with_not_enough_coins_6(self):
        with self.assertRaises(Exception) as context:
            amount_returned = vend_pop('Cool Cola', -3.59)
        self.assertEqual('Please insert coins. No freebies!', context.exception.message)

    # ################################################################################
    # Test purchase with invalid amount - these test will fail until we fix the script
    # ################################################################################
    def test_purchase_cool_cola_with_invalid_pay_amount_none(self):
        with self.assertRaises(Exception) as context:
            amount_returned = vend_pop('Cool Cola', None)
        self.assertEqual('Fix this: exception not caught, invalid amount None!', context.exception.message)

    def test_purchase_cool_cola_with_invalid_pay_amount_string(self):
        with self.assertRaises(Exception) as context:
            amount_returned = vend_pop('Cool Cola', 'INVALID')
        self.assertEqual('Fix this: Exception not caught, invalid amount!', context.exception.message)

    # ################################################################################
    # Test purchase 'Cool cola' with leading/trailing spaces
    # ################################################################################
    def test_purchase_cool_cola_with_leading_spaces(self):
        with self.assertRaises(Exception) as context:
            amount_returned = vend_pop('    Cool Cola', 3.59)
        self.assertEqual('Invalid selection:     Cool Cola', context.exception.message)

    def test_purchase_cool_cola_with_trailing_spaces(self):
        with self.assertRaises(Exception) as context:
            amount_returned = vend_pop('Cool Cola      ', 3.59)
        self.assertEqual('Invalid selection: Cool Cola      ', context.exception.message)

    # ################################################################################
    # Test purchase pop with invalid selection
    # ################################################################################
    def test_purchase_pop_with_invalid_selection_None(self):
        with self.assertRaises(Exception) as context:
            amount_returned = vend_pop(None, 3.59)
        self.assertEqual('Invalid selection: None', context.exception.message)

    def test_purchase_pop_with_invalid_selection_Coooool_Cola(self):
        with self.assertRaises(Exception) as context:
            amount_returned = vend_pop('Coooool Cola', 3.59)
        self.assertEqual('Invalid selection: Coooool Cola', context.exception.message)

    def test_purchase_pop_with_invalid_selection_(self):
        with self.assertRaises(Exception) as context:
            amount_returned = vend_pop('Invalid selection', 3.59)
        self.assertEqual('Invalid selection: Invalid selection', context.exception.message)

    def test_purchase_pop_with_numeric_pop_selection(self):
        with self.assertRaises(Exception) as context:
            amount_returned = vend_pop(999, 3.59)
        self.assertEqual('Invalid selection: 999', context.exception.message)

    def test_purchase_pop_with_non_defined_invalid_pop_selection(self):
        with self.assertRaises(Exception) as context:
            amount_returned = vend_pop(pop100, 3.59)
        self.assertEqual('Invalid selection: pop100', context.exception.message)

if __name__ == '__main__':
    unittest.main()
