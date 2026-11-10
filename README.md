# python-django-demo

TurkHosting Python Hosting testleri için Django uygulaması.

## Ayarlar (ortam değişkenleri)
| Değişken | Anlamı |
|---|---|
| `DJANGO_SECRET_KEY` | Gizli anahtar (üretimde mutlaka değiştirin) |
| `DJANGO_DEBUG` | `1` ise DEBUG açık, varsayılan kapalı |
| `DJANGO_ALLOWED_HOSTS` | Virgülle ayrılmış alan adları, varsayılan `*` |
| `DB_ENGINE` | `postgres` ise PostgreSQL, boşsa SQLite |
| `DB_NAME`, `DB_USER`, `DB_PASSWORD` | PostgreSQL bilgileri |
| `DB_HOST`, `DB_PORT` | Varsayılan `127.0.0.1` ve `5433` |

## Plesk'e yükleme
1. Dosyaları `httpdocs` içine yükleyin (`static` klasörü ile birlikte; Scan belge kökünü buna ayarlar).
2. Python sayfasında **Scan**, **Enable Python**, **Create Virtual Environment**, **Install Dependencies**, sayfayı yenileyin.
3. SSH ile: `.venv/bin/python manage.py migrate` ve `.venv/bin/python manage.py collectstatic --noinput`.
4. Yönetici: `.venv/bin/python manage.py createsuperuser`.

## Statik dosyalar
`STATIC_ROOT = BASE_DIR / "static" / "static"`. Belge kökü `/httpdocs/static` olduğu için `BASE_DIR / "static"` yazılırsa dosyalar `/static/...` yerine `/admin/...` adresinden sunulur ve 404 alınır.
