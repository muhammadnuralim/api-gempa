from app.extension import db

class GempaDirasakan(db.Model):
    __tablename__ = 'gempa_dirasakan'

    id = db.Column(db.Integer, primary_key=True)
    tanggal = db.Column(db.String)
    jam = db.Column(db.String)
    dateTime = db.Column(db.String)
    coordinates = db.Column(db.String)
    lintang = db.Column(db.String)
    bujur = db.Column(db.String)
    magnitude = db.Column(db.Numeric)  # Menggunakan tipe data Numeric
    kedalaman = db.Column(db.String)
    wilayah = db.Column(db.String)
    dirasakan = db.Column(db.String)

    def __repr__(self):
        return f'<GempaDirasakan(id={self.id}, tanggal={self.tanggal}, wilayah={self.wilayah})>'

    def serialize(self):
        return {
            'id': self.id,
            'tanggal': self.tanggal,
            'jam': self.jam,
            'dateTime': self.dateTime,
            'coordinates': self.coordinates,
            'lintang': self.lintang,
            'bujur': self.bujur,
            'magnitude': float(self.magnitude),  # Convert Numeric to float
            'kedalaman': self.kedalaman,
            'wilayah': self.wilayah,
            'dirasakan': self.dirasakan
        }
