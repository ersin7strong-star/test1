import subprocess

def ping_google():
    host = "google.com"

    print(f"{host} сайтына пинг жасалуда...\n")

    # Windows: ping -n 4
    # Linux/Mac: ping -c 4
    command = ["ping", "-c", "4", host]

    try:
        result = subprocess.run(command, capture_output=True, text=True)
        output = result.stdout

        print("Пинг нәтижесі:")
        print(output)

        # Қол жетімді екенін тексеру
        if "0% packet loss" in output or "0.0% packet loss" in output:
            print("\nСервер қолжетімді ✅")
        else:
            print("\nСервер қолжетімсіз ❌")

    except Exception as e:
        print(f"Қате пайда болды: {e}")

ping_google()
