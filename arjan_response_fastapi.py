import requests

print("\nAdicionando um item...")
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
