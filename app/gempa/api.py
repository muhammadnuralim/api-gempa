from flask import jsonify, request
from app.gempa import api_gempa
from flask_restful import Resource
from app.models.gempaTerkini import GempaTerkini
from app.models.gempaDirasakan import GempaDirasakan

class GempaResourceAll(Resource):
    def get(self):
        gempa_terkini = GempaTerkini.query.all()
        gempa_dirasakan = GempaDirasakan.query.all()

        if gempa_terkini and gempa_dirasakan:
            serialize_gempa_terkini = [item.serialize() for item in gempa_terkini]
            serialize_gempa_dirasakan = [item.serialize() for item in gempa_dirasakan]

            response_data = {
                "gempa_terkini": serialize_gempa_terkini,
                "gempa_dirasakan": serialize_gempa_dirasakan,
                "source": "BMKG (Badan Meteorologi, Klimatologi, dan Geofisika)"
            }

            return jsonify(response_data)
        else:
            return {"error": "Invalid data type"}, 400

api_gempa.add_resource(GempaResourceAll, '/gempa/all')


class GempaResourcePaginate(Resource):
    def get(self):
        page = request.args.get('page', type=int, default=1)
        per_page = request.args.get('per_page', type=int, default=10)

        gempa_terkini_paginated = GempaTerkini.query.paginate(page=page, per_page=per_page)
        gempa_dirasakan_paginated = GempaDirasakan.query.paginate(page=page, per_page=per_page)

        gempa_terkini_items = gempa_terkini_paginated.items
        gempa_dirasakan_items = gempa_dirasakan_paginated.items

        serialize_gempa_terkini = [item.serialize() for item in gempa_terkini_items]
        serialize_gempa_dirasakan = [item.serialize() for item in gempa_dirasakan_items]
        total_gempa = gempa_terkini_paginated.total + gempa_dirasakan_paginated.total
        total_pages = (total_gempa + per_page - 1) // per_page
        response_data = {
            "gempa_terkini": serialize_gempa_terkini,
            "gempa_dirasakan": serialize_gempa_dirasakan,
            "source": "BMKG (Badan Meteorologi, Klimatologi, dan Geofisika)",
            "total_pages": total_pages,
            "total_data_gempa": total_gempa,
            "total_gempa_terkini": gempa_terkini_paginated.total,
            "total_gempa_dirasakan": gempa_dirasakan_paginated.total,
            "current_page": gempa_terkini_paginated.page,
            "per_page": gempa_terkini_paginated.per_page
        }

        return jsonify(response_data)

api_gempa.add_resource(GempaResourcePaginate, '/gempa/paginate')
