from core.base import PaymentMethod
from core.processor import register_plugin

@register_plugin("virtualaccount")
class VirtualAccount(PaymentMethod):
    def __init__(self, saldo: float, expired_in_hours: int = 24) -> None:
        super().__init__(saldo)
        self.expired_in_hours: int = expired_in_hours
        self.status: str = "menunggu"

    def biaya_admin(self, jumlah: float) -> float:
        # Contoh: biaya admin tetap untuk Virtual Account adalah Rp3.000
        return 3000.0

    def proses(self, jumlah: float) -> bool:
        admin: float = self.biaya_admin(jumlah)
        total: float = jumlah + admin

        if self.saldo < total:
            self.status = "gagal"
            print(f"[VirtualAccount] Pembayaran gagal: Saldo tidak cukup untuk jumlah {jumlah} + admin {admin}")
            return False

        self.saldo -= total
        self.status = "berhasil"
        print(f"[VirtualAccount] Pembayaran {jumlah} berhasil (Admin: {admin}, Total: {total}). Status: {self.status}, Batas waktu: {self.expired_in_hours} jam.")
        return True