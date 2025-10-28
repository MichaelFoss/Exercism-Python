"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        if item not in current_cart.keys():
            current_cart[item] = 0
        current_cart[item] += 1
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    cart: dict[str, int] = dict.fromkeys(notes, 1)
    return cart


def update_recipes(ideas: dict[str, dict[str, int]], recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart: dict[str, int]):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    sorted_cart: dict[str, int] = sorted(cart.items())
    return sorted_cart


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    fulfillment_cart: dict[str, tuple[int, str, bool]] = {}
    for item in cart.keys():
        fulfillment_cart[item] = [cart[item]] + aisle_mapping[item]
    reversed_fulfillment_cart: dict[str, tuple[int, str, bool]] = dict(sorted(fulfillment_cart.items(), reverse=True))
    return reversed_fulfillment_cart


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    for item in fulfillment_cart.keys():
        store_inventory[item][0] -= fulfillment_cart[item][0]
        if store_inventory[item][0] == 0:
            store_inventory[item][0] = 'Out of Stock'
    return store_inventory
