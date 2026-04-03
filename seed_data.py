import os
import django

# Setup environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tk2_pkpl.settings')
django.setup()

from biodata.models import Member

def seed_members():
    Member.objects.all().delete()

    data_anggota = [
        {
            "name": "Alya Nabilla Khamil",
            "npm": "2406358094",
            "prodi": "Ilmu Komputer",
            "bio": "Naturally funny",
            "photo": "photos/alya.JPG"
        },
        {
            "name": "Keisha Vania Laurent",
            "npm": "2406437331",
            "prodi": "Ilmu Komputer",
            "bio": "Roger sumatra",
            "photo": "photos/keisha.jpg"
        },
        {
            "name": "Saffana Firsta Aqila",
            "npm": "2406440023",
            "prodi": "Ilmu Komputer",
            "bio": "Aku suka pink",
            "photo": "photos/saffana.jpg"
        },
        {
            "name": "Nadia Aisyah Fazila",
            "npm": "2406495584",
            "prodi": "Ilmu Komputer",
            "bio": "Every skibidi will become a sigma someday",
            "photo": "photos/nadia.jpg"
        },
        {
            "name": "Sahila Khairatul Athia",
            "npm": "2406495716",
            "prodi": "Ilmu Komputer",
            "bio": "Air susu dibalas air jordan",
            "photo": "photos/sahila.jpg"
        },
    ]

    for data in data_anggota:
        Member.objects.create(**data)
        print(f"Berhasil membuat data untuk: {data['name']}")

    print("Semua data member berhasil di-seed!")

if __name__ == '__main__':
    seed_members()