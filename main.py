"""Talent Team test assignment

Parse HTML and extract First, Last and Middle names from a certain tag.
"""
import sys
from bs4 import BeautifulSoup


def get_fullname(data: str, *, tag: str, cls: str) -> str:
    """Extract First, Last and Middle names from a certain tag.

    Parameters
    ----------
    data: str
        Parsing text data
    tag: str
        The desired tag, which contains Name and Surname, is unique.
    cls: str
        The only attribute of the tag

    Returns
    -------
    text: str or None
        Returns full name, or None if unsuccessful
    """
    soup = BeautifulSoup(data, 'lxml')
    username = soup.find(tag, class_=cls)
    return username.text if username else None


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as html_file:
        content = html_file.read()
        text = get_fullname(content, tag='p', cls='full_name')
        if text:
            words = text.split()
            word_count = len(words)
            if word_count == 3:
                print(f'Ура! Мы нашли фамилию: {words[0]}, имя: {words[1]}, отчество: {words[2]}!')
            elif word_count == 2:
                print(f'Ура! Мы нашли фамилию: {words[0]}, имя: {words[1]}!')
            elif word_count == 1:
                print(f'Ура! Мы нашли имя: {words[0]}!')
            else:
                print('Упс! Кажется, что-то слишком сложное :( ')
        else:
            print('Не удалось найти имя.')
