import pytest
from unittest import mock
from brute import Brute

todo = pytest.mark.skip(reason='todo: pending spec')

def describe_Brute():

    @pytest.fixture
    def cracker():
        return Brute("TDD")
    
    @pytest.fixture
    def cracker_mock_brute_hash(mocker):
        return mocker.patch.object(Brute, 'hash', return_value='TDD')
    
    @pytest.fixture
    def cracker_mock_brute_randomGuess(mocker):
        return mocker.patch.object(Brute, 'randomGuess', return_value='TDD')
    
    @pytest.fixture
    def mock_brute_hash(mocker):
        return mocker.patch.object(Brute, 'hash', return_value='test')
    
    @pytest.fixture
    def mock_brute_randomGuess(mocker):
        return mocker.patch.object(Brute, 'randomGuess', return_value='test')
    

    def describe_bruteOnce():
        # write your test cases here
        def it_tests_bruteOnce():
            b = Brute("test")
            assert b.bruteOnce("test") == True

        def it_tests_bruteOnce_with_mismatch():
            b = Brute("test")
            assert b.bruteOnce("test2") == False

        def it_tests_bruteOnce_with_longer_string():
            b = Brute("testingThisLongString")
            assert b.bruteOnce("testingThisLongString") == True

        def it_tests_brute_init_with_digits():
            with pytest.raises(TypeError):
                b = Brute(1234)

        def it_tests_brute_with_float():
            with pytest.raises(TypeError):
                b = Brute(3.14)

        def it_tests_brute_init_with_dictionary():
            with pytest.raises(TypeError):
                b = Brute({'test': 1})

        def it_tests_brute_init_with_list():
            with pytest.raises(TypeError):
                b = Brute([1, 2, 3])

        def it_tests_brute_with_type_none():
            with pytest.raises(TypeError):
                b = Brute(None)

        def it_tests_bruteOnce_with_special_characters():
            b = Brute('!@#$%^&*()')
            assert b.bruteOnce('!@#$%^&*()') == True

    def describe_bruteMany():
        # write your test cases here
        def it_tests_bruteMany(mocker, mock_brute_hash, mock_brute_randomGuess):
            b = Brute("test")
            b.bruteMany()
            mock_brute_hash.assert_called()
            mock_brute_randomGuess.assert_called()

        def it_tests_bruteMany_with_mismatch(mocker, mock_brute_hash, mock_brute_randomGuess):
            b = Brute("test")
            b.bruteMany()
            mock_brute_hash.assert_called()
            mock_brute_randomGuess.assert_called()

        def it_tests_bruteMany_with_longer_string(mocker, mock_brute_hash, mock_brute_randomGuess):
            b = Brute("testingThisLongString")
            b.bruteMany()
            mock_brute_hash.assert_called()
            mock_brute_randomGuess.assert_called()



