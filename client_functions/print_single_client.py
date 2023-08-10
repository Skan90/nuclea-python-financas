def print_single_client(client):
    print("[{")
    for key, value in client.items():
        if key == "Endereço":
            print(f"'{key}': {value},")
        else:
            print(f"'{key}': '{value}',")
    print("}]")