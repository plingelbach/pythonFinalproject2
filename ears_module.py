# ears_module.py

def cat_ears(num_cats: int) -> int:
    """Calculate the total number of cat ears."""
    if num_cats == 0:
        return 0
    else:
        return 2 + cat_ears(num_cats - 1)


def alien_ears(num_aliens: int) -> int:
    """Calculate the total number of alien ears."""
    if num_aliens == 1:
        return 3
    elif num_aliens == 2:
        return 5
    elif num_aliens % 2 == 1:
        return 3 + alien_ears(num_aliens - 1)
    else:
        return 2 + alien_ears(num_aliens - 1)
