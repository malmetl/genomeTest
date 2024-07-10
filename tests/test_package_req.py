from genomeTest import GenomeHttpclient
from datetime import datetime
import json
import urllib3

client = GenomeHttpclient("https://genomepre.crie.ru",
                          token="")


def test_package():
    data = {
        'username': "crie_kurochkin",
        'password': "2CZSudsG",
    }
    auth_key = client.get_authorization_request(data=data)
    print(auth_key)
    data = {
        "sample_data": {
            "sample_name": "sample_name",
            "sequence_name": "sequence_name",
            "sample_pick_date": "2023-10-09",
            "sample_pick_place": "Россия, г Москва",
            "sample_type": 1,
            "seq_area": 0,
            "author": "Ivanov",
            "comment": "Comment",
            "seq_method": {
                "type": 1,
                "seq_platform_model": 1,
                "assembly_principle": 0,
                "assembly_program": "Название программного обеспечения и версия",
                "completion_degree": 1,
                "avg_depth": "50",
                "pathogen_coverage": "20"
            },
            "disease_source": {
                "type": 0,
                "object": {
                    "born_year": "1987",
                    "age": {
                        "type": 1,
                        "age_years": "42"
                    },
                    "gender": 1,
                    "sick_symptoms": "symptoma",
                    "sick_diagnosis": "ХОНДРОПАТИИ (M91-M94)",
                    "clinical_type": {
                        "type": 3
                    },
                    "foreign": {
                        "type": 2
                    },
                    "sick_date": "2024-01-01",
                    "society_type": 1,
                    "issue": 1,
                    "complications": {
                        "type": 0
                    },
                    "severity": "описание тяжести болезни",
                    "infection_source": {
                        "type": 1,
                        "infection_source_description": "contact info"
                    },
                    "hospitalization": 2,
                    "vaccination_info": {
                        "type": 1,
                        "vaccination_info_name": 7,
                        "vaccination_info_date": "2024-02-01",
                        "vaccination_info_name_2": 9,
                        "vaccination_info_date_2": "2024-02-02",
                        "vaccination_info_name_3": 10,
                        "vaccination_info_date_3": "2024-02-03"
                    }
                }
            }
        },
        "sequence": [
            ">fasta-content-fasta-content-fasta-content-fasta-content-fasta-content-fasta-content-fasta-content-fasta-content"
        ]
    }

    new_package = client.post_package_request(data=data)
    print(new_package.text)
