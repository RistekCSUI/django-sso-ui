# django-sso-ui

Sebuah library python untuk memudahkan aplikasi django menggunakan SSO
Universitas Indonesia.

## Instalasi

`pip install django-sso-ui`

## Cara Menggunakan

Pertama import decorator `with_sso_ui`
`from django_sso_ui.decorators import with_sso_ui`

Lalu wrap ke view yang membutuhkan info user sso ui. Jangan lupa tambahkan parameter `sso_profile` pada fungsi view yang di wrap.

```py
@with_sso_ui
def login(request, sso_profile):
    return HttpResponse(json.dumps(sso_profile))
```

Apabila pengguna tidak diharuskan login dengan SSO untuk mengakses view tersebut, tambahkan parameter `force_login=False` pada decorator.

```py
@with_sso_ui(force_login=False)
def login(request, sso_profile):
    return HttpResponse(json.dumps(sso_profile))
```

## Settings

Untuk mengubah endpoint cas yang digunakan, terdapat opsi di tambahkan
line berikut di `settings.py` dengan endpoint yang diinginkan
`SSO_UI_URL="https://sso.ui.ac.id/cas2/"`

Untuk memaksa library untuk menggunakan `https` untuk url callback setelah
login CAS berhasil, tambahkan line berikut di `settings.py`
`SSO_UI_FORCE_SERVICE_HTTPS=True`

## Notes

Informasi tambahan seperti fakultas, study_program hanya bisa didapatkan
apabila menggunakan `https://sso.ui.ac.id/cas2`.
