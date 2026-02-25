from infrastructure.repositories.inmemory.item import InMemoryItemRepository

item_repo = InMemoryItemRepository()

def get_item_repo():
    return item_repo