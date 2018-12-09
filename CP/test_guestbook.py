import pytest
import main

def test_guestbook():
  assert main.read('Guest_book.json') == 3