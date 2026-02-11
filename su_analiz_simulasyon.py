import random

# Normal çalışma aralıkları
NORMAL_BASINC_MIN = 45
NORMAL_BASINC_MAX = 55

NORMAL_AKIS_MIN = 90
NORMAL_AKIS_MAX = 110

def veri_uret():
    """
    Sensörlerden gelen basınç ve akış verisini simüle eder.
    Bazen anormal değer üretir.
    """
    # %10 ihtimalle kaçak simülasyonu
    if random.random() < 0.1:
        basinc = random.randint(20, 35)  # düşük basınç
        akis = random.randint(130, 160)  # anormal yüksek akış
    else:
        basinc = random.randint(NORMAL_BASINC_MIN, NORMAL_BASINC_MAX)
        akis = random.randint(NORMAL_AKIS_MIN, NORMAL_AKIS_MAX)

    return basinc, akis


def anomali_kontrol(basinc, akis):
    """
    Basınç ve akış değerlerini kontrol eder.
    Normal aralık dışındaysa kaçak şüphesi üretir.
    """
    if basinc < NORMAL_BASINC_MIN or akis > NORMAL_AKIS_MAX:
        return True
    return False


def sistem_calistir():
    print("Turkcell Akıllı Su Ağı - Sensör Analiz Simülasyonu Başlatıldı\n")

    for i in range(20):
        basinc, akis = veri_uret()
        print(f"Veri {i+1}: Basınç={basinc} | Akış={akis}")

        if anomali_kontrol(basinc, akis):
            print(">>> KAÇAK ŞÜPHESİ TESPİT EDİLDİ!\n")
        else:
            print("Normal\n")


if __name__ == "__main__":
    sistem_calistir()
