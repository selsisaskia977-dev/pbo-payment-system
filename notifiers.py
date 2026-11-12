class TelegramNotifier:
    def __init__(self, token_bot: str = "TOKEN-CONTOH"):
        self.token_bot = token_bot
 
    def kirim(self, penerima: str, pesan: str) -> None:
        ...  # TODO: cetak "[TELEGRAM] ke <penerima>: <pesan>"
class ConsoleNotifier:
    def kirim(self, penerima: str, pesan: str) -> None:
        print(f"[CONSOLE] ke {penerima}: {pesan}")

class EmailNotifier:
    def kirim(self, penerima: str, pesan: str) -> None:
        print(f"[EMAIL via smtp.kampus.ac.id] ke {penerima}: {pesan}")

class TelegramNotifier:
    def __init__(self, token_bot: str = "TOKEN-CONTOH"):
        self.token_bot = token_bot

    def kirim(self, penerima: str, pesan: str) -> None:
        print(f"[TELEGRAM] ke {penerima}: {pesan}")