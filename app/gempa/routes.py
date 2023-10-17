from app.gempa import gempaBp
import csv
import os
from app.models.gempaTerkini import GempaTerkini
from app.models.gempaDirasakan import GempaDirasakan
from app.extension import db


# Tanggal,Jam,DateTime,Coordinates,Lintang,Bujur,Magnitude,Kedalaman,Wilayah,Potensi,Kategori,Dirasakan
# def insert_data_from_csv(file_path):
#     with open(file_path, mode='r', newline='') as file:
#         reader = csv.reader(file)
#         next(reader)  # Skip the header row if it exists
#         for row in reader:
#             gempa = GempaTerkini(
#                 tanggal=row[0],
#                 jam=row[1],
#                 dateTime=row[2],
#                 coordinates=row[3],
#                 lintang=row[4],
#                 bujur=row[5],
#                 magnitude=float(row[6]),  # Convert magnitude to float
#                 kedalaman=row[7],
#                 wilayah=row[8],
#                 potensi=row[9],
#             )
#             db.session.add(gempa)
#     db.session.commit()


# # masukan data ke database



# @gempaBp.route("", strict_slashes=False)
# def index():
#     gempa_terkini = GempaTerkini.query.all()
#     gempa_dirasakan = GempaDirasakan.query.all()