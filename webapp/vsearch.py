def search4vowels(phrase:str) -> set:
	"""인자로 받은 문자의 모음을 찾아 리턴"""
	vowels = set('aeiou')
	return vowels.intersection(set(phrase))


def search4letters(phrase:str, letters:str='aeiou') -> set:
        """phrase 안의 letters를 찾아 리턴"""
        return set(letters).intersection(set(phrase))
