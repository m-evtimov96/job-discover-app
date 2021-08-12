from django.core.exceptions import ValidationError
from django.test import TestCase

from JobDiscover.core.validators import validate_start_with_capital, validate_correct_bulstat, validate_image_file_size


class ValidateStartWithCapitalTests(TestCase):
    def test_startsWithLower_expectToRaise(self):
        value = 'sample'
        with self.assertRaises(ValidationError) as context:
            validate_start_with_capital(value)

        self.assertIsNotNone(context.exception)

    def test_startsWithCapitalAndHaveMoreCapitalAfter_expectToRais(self):
        value = 'SamPle'
        with self.assertRaises(ValidationError) as context:
            validate_start_with_capital(value)

        self.assertIsNotNone(context.exception)

    def test_startsWithCapital_expectToDoNothing(self):
        value = 'Sample'
        validate_start_with_capital(value)


class ValidateCorrectBulstatTests(TestCase):
    def test_lenIs9OnlyDigits_expectToDoNothing(self):
        value = '012345678'
        validate_correct_bulstat(value)

    def test_lenIs13OnlyDigits_expectToDoNothing(self):
        value = '0123456789012'
        validate_correct_bulstat(value)

    def test_lenIs9WithChars_expectToRaise(self):
        value = '12345678a'
        with self.assertRaises(ValidationError) as context:
            validate_correct_bulstat(value)

        self.assertIsNotNone(context.exception)

    def test_lenIs13WithChars_expectToRaise(self):
        value = '1234567890asd'
        with self.assertRaises(ValidationError) as context:
            validate_correct_bulstat(value)

        self.assertIsNotNone(context.exception)

    def test_lenIs10WithChars_expectToRaise(self):
        value = '123456789a'
        with self.assertRaises(ValidationError) as context:
            validate_correct_bulstat(value)

        self.assertIsNotNone(context.exception)

    def test_lenIs10OnlDigits_expectToRaise(self):
        value = '1234567890'
        with self.assertRaises(ValidationError) as context:
            validate_correct_bulstat(value)

        self.assertIsNotNone(context.exception)


# class ValidateImageFileSizeTests(TestCase):
#     def test_sizeIsBiggerThan2Mb_expectToRaise(self):
#         value = (2 * 1024 * 1024) + 1
#         with self.assertRaises(ValidationError) as context:
#             validate_image_file_size(value)
#
#         self.assertIsNotNone(context.exception)
#
#     def test_sizeIs2Mb_expectToDoNothing(self):
#         value = 2 * 1024 * 1024
#         validate_image_file_size(value)
#
#     def test_sizeIsLessThan2Mb_expectToDoNothing(self):
#         value = (2 * 1024 * 1024) - 1
#         validate_image_file_size(value)

# Find a way to Mock image size