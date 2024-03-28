from project import choose_word, display_word, check_guess
import random

def choose_word():
    words = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "strawberry", "pineapple", "blueberry", "apricot", "avocado", "blackberry", "cranberry", "grapefruit", "guava", "lemon", "lime", "lychee", "papaya", "peach", "pear", "plum", "raspberry", "watermelon"]
    return random.choice(words)


def test_choose_word():
    words = set()
    for _ in range(100):
        word = choose_word()
        assert word in ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "strawberry", "pineapple", "blueberry", "apricot", "avocado", "blackberry", "cranberry", "grapefruit", "guava", "lemon", "lime", "lychee", "papaya", "peach", "pear", "plum", "raspberry", "watermelon"]
        words.add(word)
    assert len(words) == 25  # Ensure all words are chosen at least once

def test_display_word():
    assert display_word("apple", {"a", "p", "l"}) == "appl_"
    assert display_word("banana", {"a", "n", "b"}) == "banana"

def test_check_guess():
    assert check_guess("apple", {"a", "p"}, "l") == True
    assert check_guess("banana", {"a", "n", "b"}, "c") == False

