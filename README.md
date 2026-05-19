# 8-AMALIY KO'NIKMA - Django Loyiha Hujjati

## 1) Loyiha haqida
Ushbu loyiha Django asosida yaratilgan web-ilova bo'lib, quyidagi asosiy funksiyalar mavjud:
- Login (tizimga kirish)
- Registration (ro'yxatdan o'tish)
- Profilni tahrirlash
- Profil rasmi yuklash
- Navbar ichida foydalanuvchi rasmi, ism-familya va guruh nomini ko'rsatish
- Bosh sahifada maxsus dizayn (`8-AMALIY KO'NIKMA`)

## 2) Ishga tushirish
### Talablar
- Python 3
- Virtual environment (`.venv`)

### Ishga tushirish qadamlari
```bash
source .venv/bin/activate
python manage.py migrate
python manage.py runserver 0.0.0.0:5050
```

Brauzerda ochish:
- `http://127.0.0.1:5050/`

## 3) Qo'shilgan va o'zgartirilgan qismlar
### Model (`user.User`) ga qo'shilgan maydonlar
- `group_name` - guruh nomi
- `address` - manzil
- `birth_date` - tug'ilgan sana
- `image` - profil rasmi

### Form va view yangilanishlari
- Profil formasiga yangi maydonlar qo'shildi.
- Rasm yuklash uchun `multipart/form-data` va `request.FILES` qo'shildi.

### Navbar dizayni
- O'ng tomonda avatar/profil rasmi
- Dropdown (`Profil`, `Chiqish`) + ikonlar
- Minimal/modern dizayn, rounded, shadow, hover, responsive

### Login/Registration dizayni
- Forma markazga joylashtirildi
- Zamonaviy karta uslubi
- Message (alert)lar custom dizaynga o'tkazildi

## 4) Berilgan vazifaga moslik tahlili
Quyida siz bergan topshiriq punktlari bo'yicha holat:

### 1-punkt
**Talab:** Login va parol maydonlari bo'lsin, tugma bo'lsin. To'g'ri bo'lsa 2-forma, noto'g'ri bo'lsa 3-forma.

**Holat:**
- Login/parol maydonlari va tasdiqlash tugmasi **bor**.
- To'g'ri login/parol bo'lsa asosiy sahifaga o'tish **bor**.
- Noto'g'ri login/parolda aynan “3-formaga redirect” qilish hozir **yo'q** (hozir xatolik shu sahifaning o'zida ko'rsatiladi).

### 2-punkt
**Talab:** 2-formada FIO, guruh, manzil, tug'ilgan sana va rasm ko'rsatilishi; orqa fonga rasm.

**Holat:**
- FIO, guruh, manzil, tug'ilgan sana, profil rasmi maydonlari **qo'shilgan**.
- Profilga rasm yuklash **ishlaydi**.
- Navbar’da rasm + ism-familya + guruh ko'rsatish **bor**.
- “2-forma”ni alohida ko'rinishda aynan faqat ko'rsatish (read-only profile page) va “orqa fon rasm” talabi **qisman** bajarilgan (profil form bor, lekin maxsus alohida 2-forma dizayni hali yakunlanmagan).

### 3-punkt
**Talab:** 3-forma avtorizatsiya/ro'yxatdan o'tish oynasi bo'lsin, tugma bosilganda messagebox (xatolik oynasi) chiqsin.

**Holat:**
- Registration form **bor**.
- Tugma **bor**.
- Validation xatoliklari message/alert ko'rinishida chiqadi.
- Ammo alohida “3-forma”ga shartli o'tish va maxsus modal/messagebox oqimi **to'liq ajratib ishlanmagan**.

## 5) Yakuniy xulosa
Loyiha topshiriqning katta qismini qoplaydi (login, registration, profil ma'lumotlari, rasm, UI dizayn).
Lekin topshiriqni **100% mos** deb aytish uchun quyidagi 2 ta qismni yakunlash kerak:
1. Noto'g'ri login/parolda aniq 3-formaga yo'naltirish logikasi.
2. 2-formani alohida “siz haqingizdagi ma'lumotlar” sahifasi sifatida (read-only + fon rasmi) yakuniy ko'rinishga keltirish.

---
Agar xohlasangiz, keyingi qadamda men shu 2 ta bandni ham to'liq qilib, topshiriqni 100% formatga olib beraman.
