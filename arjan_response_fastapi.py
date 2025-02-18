import requests

print("Adicionando um item...")
print(requests.post(url="http://localhost:5000/item", json=dict(name="Tool 2", price=9.99, count=8, id=4)).json())

print("\nExibindo os itens após adicionar novo item...")
print(requests.get(url="http://localhost:5000/items").json())

print("\nExibindo um item n.º 1...")
print(requests.get(url="http://localhost:5000/item/1").json())

print("\nExibindo um item n.º 5...")
print(requests.get(url="http://localhost:5000/item/5").json())

print("\nDeletando um item n.º 2...")
print(requests.delete(url="http://localhost:5000/item/2").json())

print("\nExibindo os itens após deletar um item...")
print(requests.get(url="http://localhost:5000/items").json())

print("\nDeletando um item n.º 5...")
print(requests.delete(url="http://localhost:5000/item/5").json())

print("\nAtualizando um item n.º 1...")
print(requests.put("http://localhost:5000/item/1?count=10").json())

print("\nExibindo os itens após atualizar item 1...")
print(requests.get(url="http://localhost:5000/items").json())

print("\nAtualizando um item n.º 1...")
print(requests.put("http://localhost:5000/item/1?price=-1").json())

print("\nAtualizando um item n.º 1...")
print(requests.put("http://localhost:5000/item/1").json())

print("\nAtualizando um item n.º 1...")
print(requests.put("http://localhost:5000/item/1?name=SuperDuperHammer").json())

print("\nExibindo um item a pesquisar com count=20...")
print(requests.get("http://localhost:5000/item?count=20").json())

print("\nExibindo um item a pesquisar com category=tools...")
print(requests.get("http://localhost:5000/item?category=tools").json())

print("\nExibindo um item a pesquisar com category=ingredient...")
print(requests.get("http://localhost:5000/item?category=ingredient").json())

print("\nExibindo um item a pesquisar com count=Hello...")
print(requests.get("http://localhost:5000/item/?count=Hello").json())
